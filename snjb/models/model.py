from odoo import models, fields


class Partner(models.Model):
    _inherit = "res.partner"

    extra_data = fields.Text(inverse="_inverse_extra_data")

    def _inverse_extra_data(self):
        for rec in self:
            if rec.extra_data:
                extra_data = rec.extra_data.split("|")
                rec.extra_data = "\n".join(extra_data)
