from odoo import api, fields, models
from odoo.exceptions import UserError


class AccountPaymentMethodLine(models.Model):
    _inherit = "account.payment.method.line"

    @api.depends("name")
    def _compute_display_name(self):
        if self.env.context.get("easy_payment"):
            for rec in self:
                rec.display_name = f"{rec.name} {rec.journal_id} - {rec.code} - {rec.payment_method_id}"
        elif self.env.context.get("easy_payment_config"):
            for rec in self:
                rec.display_name = f"{rec.name} {rec.journal_id} - {rec.code} - {rec.payment_method_id}"
        else:
            super()._compute_display_name()
