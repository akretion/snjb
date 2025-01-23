from odoo import api, fields, models


class SaleOrder(models.Model):
    _inherit = "sale.order"

    vendor_phone = fields.Char(compute="_compute_vendor_phone")
    picking_ref = fields.Char(compute="_compute_picking_ref")
    shipping_ref_no_picking = fields.Char(compute="_compute_shipping_ref_no_picking")

    def _compute_shipping_ref_no_picking(self):
        for rec in self:
            shipping_ref = False
            if rec.state == 'sale' and not rec.picking_ids:
                not_shipped = [x for x in rec.order_line if x.product_uom_qty > x.qty_delivered]
                if not not_shipped:
                    shipping_ref = rec.name
            rec.shipping_ref_no_picking = shipping_ref

    @api.depends("picking_ids")
    def _compute_picking_ref(self):
        for rec in self:
            pickings = False
            refs = ", ".join(
                rec.picking_ids.filtered(lambda s: s.state == "done").mapped("name")
            )
            if refs:
                pickings = f"Livraison # {refs}"
            rec.picking_ref = pickings

    @api.depends("user_id.mobile", "user_id.phone")
    def _compute_vendor_phone(self):
        for rec in self:
            phone = rec.user_id and rec.user_id.mobile or rec.user_id.phone or ""
            if phone:
                rec.vendor_phone = f" 📞 {phone}"
            else:
                rec.vendor_phone = False
