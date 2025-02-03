from odoo import api, fields, models


class AccountMove(models.Model):
    _inherit = "account.move"

    display_communication = fields.Boolean(
        compute="_compute_display_communication", store=True
    )
    toto = fields.Boolean()

    @api.depends("preferred_payment_method_line_id")
    def _compute_display_communication(self):
        for move in self:
            if (
                not move.preferred_payment_method_line_id
                or move.preferred_payment_method_line_id.display_communication_payment
            ):
                move.display_communication = True
            else:
                move.display_communication = False
