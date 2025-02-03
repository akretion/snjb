from odoo import fields, models


class AccountPaymentMethodLine(models.Model):
    _inherit = "account.payment.method.line"

    display_communication_payment = fields.Boolean(
        string="Afficher communicaton de paiement",
        help="Si coché, le bloc sur la communication de paiement sera affiché dans les factures.",
    )
