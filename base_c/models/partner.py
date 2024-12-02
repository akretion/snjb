from odoo import fields, models
import logging

logger = logging.getLogger(__name__)


class ResPartner(models.Model):
    _inherit = "res.partner"

    lang = fields.Selection(default="fr_FR")

    def _country_df_snjb_replacement(self):
        return {
            "ALLEMAGNE": "Allemagne",
            "BELGIQUE": "Belgique",
            "ENGLAND": "Royaume-Uni",
            "ESPAGNE": "Espagne",
            "FR 14 682 030 895": "zzz",
            "FRANCE": "zzz",
            '"FRANCE"': "zzz",
            "france": "zzz",
            "France ": "zzz",
            "LES ULIS": "zzz",
            'France   TEL 0664098015': "zzz",
            "FRANCE   TEL 0664098015": "zzz",
            "FR": "zzz",
            "Tel compta Auxerre : 03 86 94 20 00": "zzz",
            "zzz": "France",
            "ITALIE": "Italie",
            "ITALY": "Italie",
            "REPUBLIQUE TCHEQUE": "République tchèque",
        }
