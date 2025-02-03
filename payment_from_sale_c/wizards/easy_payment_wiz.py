from odoo import _, api, models, fields
from odoo.exceptions import UserError


class EasyPaymentWiz(models.TransientModel):
    _name = "easy.payment.wiz"
    _description = "Easy payment from sale"

    payment_method_line_id = fields.Many2one(
        comodel_name="account.payment.method.line", string="Payment", required=True
    )
    payment_domain = fields.Binary(
        compute="_compute_payment_domain", help="Dynamic domain used for any field"
    )
    company_id = fields.Many2one(comodel_name="res.company", required=True)
    amount = fields.Float(readonly=True)
    currency_id = fields.Many2one(comodel_name="res.currency")
    communication = fields.Char(string="Mémo")
    payment_date = fields.Date(string="Date", default=fields.Date.today())

    @api.depends("company_id")
    def _compute_payment_domain(self):
        for rec in self:
            rec.payment_domain = [
                ("id", "in", self.company_id.quick_payment_method_ids.ids)
            ]

    @api.model
    def default_get(self, fields_list):
        res = super().default_get(fields_list)
        sale = self.env["sale.order"].browse(self._context.get("active_id"))
        res["company_id"] = sale.company_id.id
        res["currency_id"] = sale.currency_id.id
        res["amount"] = sale.amount_total
        return res

    def invoice_and_pay(self):
        self.ensure_one()
        sale = self.env["sale.order"].browse(self._context.get("active_id"))
        so_context = {
            "active_model": "sale.order",
            "active_ids": [sale.id],
            "active_id": sale.id,
            # 'default_journal_id': self.company_id.default_journal_sale.id,
        }
        payment_params = {
            "advance_payment_method": "delivered",
            "amount": self.amount,
        }
        downpayment = (
            self.env["sale.advance.payment.inv"]
            .with_context(so_context)
            .create(payment_params)
        )
        res = downpayment.create_invoices()
        invoice = self.env["account.move"].browse(res.get("res_id"))
        invoice.action_post()
        if invoice.amount_total != self.amount:
            raise UserError(
                f"Montant facturé = {invoice.amount_total} <> "
                + f"montant vendu {self.amount} !\n"
                + "Faites l'opération manuellement et idenitifiez la cause !"
            )
        payment_vals = {
            "journal_id": self.payment_method_line_id.journal_id.id,
            "payment_method_line_id": self.payment_method_line_id.id,
            "payment_date": self.payment_date,
            "group_payment": True,
            "amount": self.amount,
            "currency_id": sale.currency_id.id,
        }
        payments = (
            self.env["account.payment.register"]
            .with_context(active_model="account.move", active_ids=[invoice.id])
            .create(payment_vals)
            ._create_payments()
        )
        assert payments
        payments.message_post(body="Validated")
        sale.message_post(body=_("Payment %s", payments._get_html_link()))
        # action to view invoice
        return res
