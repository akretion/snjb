from odoo import fields, models
from .model import c_extra
import logging

logger = logging.getLogger(__name__)


class ProductProduct(models.Model):
    _inherit = "product.product"

    extra_data = fields.Text(inverse="_inverse_extra_data")

    def _inverse_extra_data(self):
        for rec in self:
            c_extra(rec)
