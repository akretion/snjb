from odoo import api, fields, models


class ProductSupplierinfo(models.Model):
    _inherit = "product.supplierinfo"

    categ_margin = fields.Float(
        "Marge Catégorie (%)", 
        related="product_tmpl_id.categ_id.supplierinfo_margin",
        help="Ce pourcentage de marge est appliqué si la marge au niveau du produit n'est pas remplie"
    )

    def _get_supplierinfo_pricelist_price(self):
        self.ensure_one()
        if self.sale_margin:
            return super()._get_supplierinfo_pricelist_price()
        sale_price = self.price_discounted
        categ_margin = self.product_tmpl_id.categ_id.supplierinfo_margin
        if categ_margin:
            sale_price = (sale_price + (sale_price * (categ_margin / 100))) or 0.0
        return sale_price
