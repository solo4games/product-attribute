# -*- coding: utf-8 -*-
# Copyright 2017 LasLabs Inc.
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl.html).

{
    'name': 'Product UoM - Technology',
    'summary': 'Adds technology related units of measure, such as '
               'informational units like gigabyte.',
    'version': '10.0.1.0.0',
    'category': 'Extra Tools',
    'website': 'https://laslabs.com/',
    'author': 'LasLabs, Odoo Community Association (OCA)',
    'license': 'LGPL-3',
    'application': False,
    'installable': True,
    'depends': [
        'base_external_system',
    ],
    'data': [
        'security/ir.model.access.csv',
        'wizards/wizard_address_validate_view.xml',
    ],
}
