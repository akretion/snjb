{
    "name": "Base custom",
    "summary": "Base custom: minimal with mainly depends on Odoo core",
    "category": "Misc",
    "author": "Akretion",
    "license": "AGPL-3",
    "version": "18.0.1.0.0",
    "depends": [
        "contacts",
        "l10n_fr",  # better to primarly load this instead of 'account'
        "purchase",
        "sale_management",
        "sale_stock",
    ],
    "data": [
        "security/group.xml",
    ],
    "demo": [
        "demo/demo.xml",
    ],
}
