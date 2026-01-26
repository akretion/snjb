from odoo import fields, models


class ProductPriceCategory(models.Model):
    _inherit = "product.price.category"

    supplierinfo_margin = fields.Float(
        string="Marge sur prix fournisseur (%)",
        digits=(16, 2),
        help="Si la marge du prix fournisseur n'est pas définie,"
        "celle de la catégorie tarifaire sera prise en compte à la place.",
    )
    categ_id = fields.Many2one(comodel="product.category")

    def _compute_display_name(self):
        for rec in self:
            name = rec.name
            if rec.supplierinfo_margin:
                name += f" ({rec.supplierinfo_margin} %)"
            rec.display_name = name
