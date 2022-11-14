# -*- coding: utf-8 -*-
{
    'name': "Library Management",
    'summary': "Manage library catalog and book lending.",
    'author': "Diki Hamdnai",
    "license": "AGPL-3",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Services/Library',
    'version': '15.0.1.0.0',

    # any module necessary for this one to work correctly
    'depends': ['base'],
    'application': True,

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'security/library_security.xml',

        'views/views.xml',
        'views/templates.xml',
        'views/library_menu.xml',
        'views/book_view.xml',
        'views/template/book_list_template.xml',
    ],
    # only loaded in demonstration mode
    # 'demo': [
    #     'demo/demo.xml',
    # ],
}
