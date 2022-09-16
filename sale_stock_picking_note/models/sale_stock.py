# Copyright 2018 Carlos Dauden - Tecnativa <carlos.dauden@tecnativa.com>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import fields, models


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    picking_note = fields.Text(
        string="Picking Note",
    )


class StockMove(models.Model):
    _inherit = 'stock.move'

    def _get_new_picking_values(self):
        vals = super(StockMove, self)._get_new_picking_values()
        sale_order = self.mapped('procurement_id').mapped('sale_line_id').mapped('order_id')
        if len(sale_order) == 1 and sale_order.picking_note:
            vals['note'] = sale_order.picking_note
        return vals
