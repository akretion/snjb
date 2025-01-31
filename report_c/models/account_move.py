from odoo import api, fields, models


class AccountMove(models.Model):
    _inherit = "account.move"

    display_communication = fields.Char(compute="_compute_display_communication")

    @api.depends("preferred_payment_method_line_id")
    def _compute_display_communication(self):
        for move in self:
            if not move.preferred_payment_method_line_id or move.display_communication_payment:
                move.display_communication = True
            else:
                move.display_communication = False
        
