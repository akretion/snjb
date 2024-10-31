from odoo import models
import logging


logger = logging.getLogger(__name__)


class DfSource(models.Model):
    _inherit = "df.source"

    def _get_test_file_paths(self):
        res = super()._get_test_file_paths()
        res.update({
            "migr": {
                "xmlid": "migr.contact",
            }
        })
        return res



class DbConfig(models.Model):
    _inherit = "db.config"

    def _filter_df(self, df):
        df = super()._filter_df(df)
        # TODO complete
        return df



class DfProcessWiz(models.TransientModel):
    _inherit = "df.process.wiz"

    def _process_touchy_fields(self, record, rebellious):
        super()._process_touchy_fields(record, rebellious)
        for key in rebellious:
            try:
                record[key] = rebellious[key]
            except Exception:
                # vals = {}
                # self.env["field.log"].create(vals)
                logger.warning(f"\n\n\n\n\nPb here {rebellious[key]}")
                continue


class ModelMap(models.Model):
    _inherit = "model.map"

    def _get_touchy_fields_to_import(self):
        res = super()._get_touchy_fields_to_import()
        res.update({"res.partner": ["vat"]})
        return res
