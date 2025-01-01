from odoo import fields, models


class SaleOrder(models.Model):
    _inherit = "sale.order"

    vendor_phone = fields.Char(compute="_compute_vendor_phone")

    def _compute_vendor_phone(self):
        for rec in self:
            phone = rec.user_id and rec.user_id.mobile or rec.user_id.phone or ""
            if phone:
                rec.vendor_phone = f" 📞 {phone}"
            else:
                rec.vendor_phone = False
