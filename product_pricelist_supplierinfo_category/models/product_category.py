from odoo import fields, models


class ProductCategory(models.Model):
    _inherit = "product.category"

    supplierinfo_margin = fields.Float(
        string="Marge sur prix fournisseur (%)",
        digits=(16, 2),
        help="Si la marge du prix fournisseur n'est pas définie, celle de la catégorie sera prise en compte à la place."
    )
