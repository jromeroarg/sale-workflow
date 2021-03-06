# Copyright 2013-15 Agile Business Group sagl (<http://www.agilebg.com>)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import fields, models


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    group_use_product_ref_name_per_so_line = fields.Boolean(
        "Permitir usar ref+nombre del producto en las linea "
        "de orden de venta", implied_group="sale_order_line_ref_name."
        "group_use_product_ref_name_per_so_line",
        help="Permitir usar ref+nombre del producto en la linea "
        "de orden de venta."
        )
