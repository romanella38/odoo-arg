# -*- coding: utf-8 -*-
{
    'name': "correo_crm",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
        prueba conn 5
=======
        prueba conn 6
>>>>>>> 50baaf13e9004ac4a9ae591eb098a3b822874b6c
=======
        prueba conn 7
>>>>>>> 219f8c0d88aa4d99442c3315b1b0ff0eb2dfffc4
=======
        prueba conn 9
>>>>>>> 884440b179dd4adf21f526d02894beace76c3684
    """,

    'author': "Carlos Meilan",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/11.0/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','crm'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
