from odoo import models, fields


def c_extra(self):
    "Populate extra_data field, i.e. product and partner"
    if self.extra_data:
        extra_data = self.extra_data.split("|")
        self.extra_data = "\n".join(extra_data)
