# Copyright 2013-15 Agile Business Group sagl (<http://www.agilebg.com>)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import api, models


class SaleOrderLine(models.Model):
    _inherit = "sale.order.line"

    @api.multi
    @api.onchange('product_id')
    def product_id_change(self):
        res = super(SaleOrderLine, self).product_id_change()
        if not self.product_id:  # pragma: no cover
            return res
        if (self.user_has_groups(
                'sale_order_line_descrip_name.'
                'group_use_product_descrip_name_per_so_line') and
                self.product_id.description_sale):
            self.name = '[' + self.product_id.default_code + '] ' + self.product_id.name
        return res