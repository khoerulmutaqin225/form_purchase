# -*- coding: utf-8 -*-
{
    'name': "form_purchase",
    

    'summary': "Short (1 phrase/line) summary of the module's purpose",

    'description': """
Long description of module's purpose
    """,

    'author': "KHOERUL MUTAQIN",
    'website': "https://github.com/khoerulmutaqin225/form_purchase",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/khoerulmutaqin225/form_purchase
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'point_of_sale' ],

    # always loaded
    'data': [
        'data/email_template.xml',
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'views/point_of_sale.xml',
    ],
    'assets': {
        'point_of_sale.assets': [
            'form_purchase/static/src/js/pos_inherit.js',
            'form_purchase/static/src/js/chat_inherit.js',
        ],
    },
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'qweb': [
        'static/src/xml/NumpadWidget.xml',
        'static/src/xml/PaymentScreen.xml',
    ],    
}

