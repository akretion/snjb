from odoo import api, fields, models
from odoo.osv import expression


class ProductProduct(models.Model):
    _inherit = "product.product"

    @api.model
    def _search_display_name(self, operator, value):
        domain = super()._search_display_name(operator, value)
        # we want to be able to search by supplier code for the product from any place
        # (but mainly sale order). So, systematically search on seller_ids.product_code
        # unless we got partner in context (in that case native Odoo already search
        # for the product_code in combination with the supplier, this should be enough
        if not self.env.context.get('partner_id'):
            domains = [domain]
            is_positive = operator not in expression.NEGATIVE_TERM_OPERATORS
            combine = expression.OR if is_positive else expression.AND
            domains.append([('product_tmpl_id.seller_ids.product_code', operator, value)])
            domain = combine(domains)
        return domain
