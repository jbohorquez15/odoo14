# -*- coding: utf-8 -*-
{
    'name': "Biblioteca",

    'summary': """
        Modulo que Permite la Gestion de clientes y Libros 
        """,

    'description': """
        El objetivo de este modulo es Controlar los Clientes y que Libros se  les asigno 
    """,

    'author': "Callphone S.A",
    'website': "http://www.callphoneecuador.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Administration',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],
    
    # only loaded in demonstration mode
    'demo': [
        'demo/biblioteca_demos.xml',
    ],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'views/libros_views.xml',
    ],
    
}
