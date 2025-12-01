{
    'name': 'Delivery Note Restriction',
    'version': '18.0.1.0',
    'author': 'Eyob',
    'category': 'Uncategorized',
    'summary': 'Restric Printing of Delivery Notes For Specified User Only',
    'description': """ """,
    'license': 'LGPL-3',
    'depends': [
        'stock',
    ],
    'data':[
        'security/store_manager_group_security.xml',
        'views/stock_picking_print_inherit.xml',
        'report/stock_delivery_report_inherit.xml',
    ],
    "installable": True,
    "application": False,
    "auto_install": False,
}
