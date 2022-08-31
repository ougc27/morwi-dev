# -*- coding: utf-8 -*-
# Copyright 2022 Morwi Encoders Consulting SA de CV
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl.html).

from odoo import fields, models


class StockPickingType(models.Model):
    _inherit = "stock.picking.type"

    sap_id = fields.Integer()

    _sql_constraints = [
        ('sap_id_uniq', 'unique (sap_id)',
            "This ID is already being used in another record"),
    ]
