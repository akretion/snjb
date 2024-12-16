{
    "name": "Product Pricelist Supplierinfo Category",
    "summary": "Allow to configure a margin for supplierinfo prices on category in case it is not set on product",
    "category": "Misc",
    "author": "Akretion",
    "license": "AGPL-3",
    "version": "18.0.1.0.1",
    # TODO we did fork and change the name of the OCA module product_pricelist_supplierinfo_discount
    # because it is not stable yet and we want to avoid unexpected change
    # Once merged in OCA we should go back on it. (and OCA module needs to manage the
    # price_discounted)
    "depends": [
        "product_pricelist_supplierinfo_discount",
        "sale",
    ],
    "data": [
        "views/product_category.xml",
    ],
    "demo": [
    ],
}
