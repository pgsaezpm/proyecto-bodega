# -*- coding: utf-8 -*-
{
    'name': "Gimnasio",

    'summary': "Módulo para la gestión del gimnasio.",

    'description': """
: En este módulo guardaremos la información necesaria para la gestión del gimnasio.
    """,

    'author': "Pablo García Sáez",
    'website': "https://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',
    'application': 'True',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/suscripcion.xml',
        'views/entrenador.xml',
        'views/clase.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}

