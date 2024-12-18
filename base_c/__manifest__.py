{
    "name": "Base custom",
    "summary": "Base custom: minimal with mainly depends on Odoo core",
    "category": "Misc",
    "author": "Akretion",
    "license": "AGPL-3",
    "version": "18.0.1.0.1",
    "depends": [
        "contacts",
        "l10n_fr",  # better to primarly load this instead of 'account'
        "maintenance",
        "purchase",
        "sale_management",
        "sale_stock",
        "product_second_category",
    ],
    "data": [
        "security/group.xml",
        "views/partner.xml",
        "views/category.xml",
    ],
    "demo": [
        "demo/demo.xml",
    ],
}
