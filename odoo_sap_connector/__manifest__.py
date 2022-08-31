# -*- coding: utf-8 -*-
# Copyright 2022 Morwi Encoders Consulting SA de CV
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl.html).
{
    'name': 'Odoo - SAP Connector',
    'version': '1.0',
    'summary': 'Odoo <-> SAP Integrations',
    'description': "Odoo <-> SAP Integrations",
    'category': "Hidden",
    'website': 'https://www.morwi.mx',
    'depends': ['sale_stock', 'purchase_stock'],
    'data': [
        'data/ir_cron_data.xml',
        'data/stock_location_data.xml',
        'views/crm_team_views.xml',
        'views/stock_picking_type_views.xml',
        'views/res_config_settings_views.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
}
