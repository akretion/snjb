from odoo import models, fields


def c_extra(self):
    if self.extra_data:
        extra_data = self.extra_data.split("|")
        self.extra_data = "\n".join(extra_data)


class Partner(models.Model):
    _inherit = "res.partner"

    extra_data = fields.Text(inverse="_inverse_extra_data")

    def _inverse_extra_data(self):
        for rec in self:
            c_extra(rec)


class Product(models.Model):
    _inherit = "product.product"

    extra_data = fields.Text(inverse="_inverse_extra_data")

    def _inverse_extra_data(self):
        for rec in self:
            c_extra(rec)
