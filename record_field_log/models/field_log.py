from odoo import models, fields


class FieldLog(models.Model):
    _name = "field.log"
    _description = "Logs on field records"

    field_id = fields.Many2one(comodel_name="ir.model.fields")
    model_id = fields.Many2one(comodel_name="ir.model", related="field_id.model_id")
    model = fields.Char(related="model_id.name")
    res_id = fields.Integer()
    info = fields.Char()
    kind = fields.Selection(selection=[("import_except", "Import Exception")])
