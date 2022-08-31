# -*- coding: utf-8 -*-
# Copyright 2022 Morwi Encoders Consulting SA de CV
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl.html).

from odoo import fields, models


class ResCompany(models.Model):
    _inherit = "res.company"

    sap_user = fields.Char(
        default="ODATAUSER",
    )
    sap_password = fields.Char(
        default="Dintec_2022*",
    )
    sap_stock_levels_url = fields.Char(
        default="https://my360737.sapbydesign.com/sap/byd/odata/scm_internallogistics_analytics.svc/RPSCMINVV02_Q0001QueryResults?$select=CCO_UUID,CMATERIAL_UUID,CSITE_UUID,CON_HAND_STOCK_UOM,TON_HAND_STOCK_UOM,KCON_HAND_STOCK&$filter=(CCO_UUID%20eq%20%27MX%27)%20and%20(CSITE_UUID%20eq%20%27MXO%27)&$format=json",
    )
