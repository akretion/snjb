from odoo import fields, models, api
import logging

logger = logging.getLogger(__name__)


class ResPartner(models.Model):
    _inherit = "res.partner"

    lang = fields.Selection(default="fr_FR")
    invoice_sending_method = fields.Selection(default="email")
    typology_id = fields.Many2one(
        comodel_name="res.partner.category",
        compute="_compute_typology_id",
        store=True,
    )

    @api.depends("category_id")
    def _compute_typology_id(self):
        for rec in self:
            res = []
            if rec.category_id:
                res = [
                    x
                    for x in rec.category_id
                    if x.parent_id in self.env.ref("base_c.client_partner_category")
                ]
                res = res and res[0] or res
            rec.typology_id = res

    def _country_df_sage100_replacement(self):
        # Used by db_process module that is not in dependency of this module
        return {
            "ALLEMAGNE": "Allemagne",
        }
