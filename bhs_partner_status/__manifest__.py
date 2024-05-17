# -*- encoding: utf-8 -*-
{
    'name': "Partner Status",
    'version': '1.0',
    'summary': 'Partner Status',
    'category': 'Mail',
    'description': """
        A product of Bac Ha Software that allows users to manage contact status and 
        add contacts to a blacklist based on their status.
    """,
    "depends": ['mass_mailing'],
    'external_dependencies': {
    },
    'data': [
        'views/res_partner_views.xml'
    ],
    'images': ['static/description/banner.gif'],
    # Author
    'author': 'Bac Ha Software',
    'website': 'https://bachasoftware.com',
    'maintainer': 'Bac Ha Software',
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3'
}
