from odoo import fields, models


class ProductSupplierinfo(models.Model):
    _inherit = "product.supplierinfo"

    def _get_supplierinfo_pricelist_price(self):
        self.ensure_one()
        if self.sale_margin:
            return super()._get_supplierinfo_pricelist_price()
        sale_price = self.price
        categ_margin = self.product_tmpl_id.categ_id.supplierinfo_margin
        if categ_margin:
            sale_price = (self.price + (self.price * (categ_margin / 100))) or 0.0
        return sale_price
