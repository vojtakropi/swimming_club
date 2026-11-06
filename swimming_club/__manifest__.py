# -*- coding: utf-8 -*-
{
    'name': "Swimming Club",

    'summary': """
        Odoo implementations for swimming club for odoo 20
    """,

    'description': """  
    """,

    'author': "vojtakropi",
    # 'website': "https://www.odoo.com/",
    'category': 'Contacts',
    'version': '0.1',
    'application': True,
    'installable': True,
    'depends': ['base', 'contacts'],

    'data': [
        'security/ir.access.csv',
        'views/res_partner_views.xml',
        'views/swimming_pool_views.xml',
    ],
    'assets': {
        'web.assets_backend': [
            'swimming_club/static/src/js/child_contacts_field.js',
        ],
    },
    'license': 'AGPL-3'
}
