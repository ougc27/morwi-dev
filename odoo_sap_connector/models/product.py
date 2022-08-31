# -*- coding: utf-8 -*-
# Copyright 2022 Morwi Encoders Consulting SA de CV
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl.html).

import requests

from odoo import api, fields, models


class ProductProduct(models.Model):
    _inherit = "product.product"

    @api.model
    def sync_sap_stock_levels(self):
        Quant = self.env['stock.quant']
        product_quants = self.env['stock.quant']
        sap_location = self.env.ref('odoo_sap_connector.sap_location')

        company = self.env.company
        service_url = company.sap_stock_levels_url
        user = company.sap_user
        password = company.sap_password

        headers = {
            "Prefer": "odata.maxpagesize=500",
            "Prefer": "odata.track-changes"
        }
        response = requests.get(
            service_url, auth=(user, password), headers=headers)
        response_json = response.json()
        # Loop results
        for item in response_json['d']['results']:
            product = self.search(
                [('default_code', '=', item['CMATERIAL_UUID'])],
                limit=1)
            if not product:
                continue
            # Search Quant
            quant = Quant.search(
                [('product_id', '=', product.id),
                 ('location_id', '=', sap_location.id)],
                limit=1)
            if not quant:
                quant = Quant.create({
                    'product_id': product.id,
                    'location_id': sap_location.id,
                })
            # Update Product quantity
            quant.inventory_quantity = float(item['KCON_HAND_STOCK'])
            product_quants |= quant
        # Post Inventory
        product_quants.action_apply_inventory()
