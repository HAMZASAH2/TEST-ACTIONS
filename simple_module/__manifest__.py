# -*- coding: utf-8 -*-
{
    'name': 'Simple Module',
    'version': '18.0.1.0.0',
    'summary': 'A simple Odoo module for demonstration',
    'author': 'Odoo Community Association (OCA)',
    'license': 'LGPL-3',
    'category': 'Uncategorized',
    'depends': ['base'],
    'data': [
        'views/simple_model_views.xml',
        'security/ir.model.access.csv',
    ],
    'demo': [],
    'installable': True,
    'application': False,
    'auto_install': False,
}
