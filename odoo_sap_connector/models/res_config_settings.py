# -*- coding: utf-8 -*-
# Copyright 2022 Morwi Encoders Consulting SA de CV
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl.html).

from odoo import fields, models


class ResConfigSettings(models.TransientModel):
    _inherit = "res.config.settings"

    sap_user = fields.Char(
        related="company_id.sap_user",
        readonly=False,
    )
    sap_password = fields.Char(
        related="company_id.sap_password",
        readonly=False,
    )
    sap_stock_levels_url = fields.Char(
        related="company_id.sap_stock_levels_url",
        readonly=False,
    )
