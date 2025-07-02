# -*- coding: utf-8 -*-
{
    'name': 'Simple Module',
    'version': '1.0',
    'summary': 'A simple Odoo module for demonstration',
    'author': 'Your Company',
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
