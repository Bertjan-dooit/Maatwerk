# -*- coding: utf-8 -*-

{
    'name': 'dooIT Customizations',

    'summary': """
dooIT view and reporting customizations.
    """,

    'description': """
This module adds dooIT specific customizations to the user interface and reports.

Customizations:
- dooIT background for login and home screens
    """,

    'version': '15.0',
    'author': 'dooIT / Bertjan van der Heiden',
    'website': 'http://www.dooit.nl',
    'category': 'Uncategorized',
    'license': 'Other proprietary',

    'depends': [
        'base',
        'web', 
        'web_enterprise',
    ],
    'data': [
        'views/no_tours.xml',
    ],
    'installable': True,
    'auto_install': False,
}
