from odoo import api, fields, models
from odoo.exceptions import UserError


class SaleOrder(models.Model):
    _inherit = "sale.order"

    # easy_paid = fields.Boolean(help="Uncomputed field to ensure only used once")
    easy_payable = fields.Boolean(
        compute="_compute_easy_payable", store=True, help="Authorize quick payment")

    @api.depends("order_line.qty_delivered", "order_line.product_uom_qty", "invoice_status")
    def _compute_easy_payable(self):
        for rec in self:
            easy_payable=False
            if rec.state == "sale" and rec.invoice_status == 'to invoice':
                not_shipped = [x for x in rec.order_line if x.product_uom_qty != x.qty_delivered]
                if not not_shipped:
                    easy_payable=True
            elif rec.invoice_status == "invoiced":
                easy_payable=False
            rec.easy_payable = easy_payable
