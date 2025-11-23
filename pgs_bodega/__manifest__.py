# -*- coding: utf-8 -*-
{
    'name': "Gestión Bodegas Emilio Moro",

    'summary': "Modulo de gestíon para bodegas Emilio Moro",

    'description': """
Este módulo gestionara los proveedores y la uva de la bodega
    """,

    'author': "Pablo García Sáez",
    'website': "https://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',
    'application': True,

    # any module necessary for this one to work correctly
    'depends': ['base','product'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'views/proveedor_viticultor.xml',
        'views/variedad_uva.xml',
        'views/denominacion_origen.xml',
        'views/producto_uva.xml',
        'views/parcela.xml',
        'views/registro_albaran.xml',
        'data/localidades_espana.csv',
        'views/deposito.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}

