from odoo import fields, models


class ResPartner(models.Model):
    _inherit = "res.partner"

    # I don't know why it doesn't work
    lang = fields.Selection(default="fr_FR")
