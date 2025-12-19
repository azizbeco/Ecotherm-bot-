
from odoo import models, fields, api
import requests

class StockPickingType(models.Model):
    _inherit = 'stock.picking'

    is_send = fields.Boolean(default=False)
    def action_send_message_about_picking(self):
        TOKEN = self.env['ir.config_parameter'].sudo().get_param('TOKEN')

        if not TOKEN:
            raise ValueError("Telegram BOT TOKEN is not configured.")

        url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"

        all_orders = self.env['stock.picking'].search([
            ('picking_type_id.sequence_code', 'in', ['PICK','PACK','OUT']),
            ('is_send', '=', False),
        ])

        error_count = 0

        for order in all_orders:
            try:
                chat_id = order.partner_id.chat_id

                if order.picking_type_id.sequence_code == 'PICK':
                    message = f"✅ Order in Picking zone: {order.name}\n\nSource Document: {order.origin}"
                elif order.picking_type_id.sequence_code == 'PACK':
                    message = f"✅ Order in Packing zone: {order.name}\n\nSource Document: {order.origin}"
                elif order.picking_type_id.sequence_code == 'OUT':
                    message = f"✅ Order is Out for Delivery: {order.name}\n\nSource Document: {order.origin}"
                else:
                    continue

                data = {
                    'chat_id': chat_id,
                    'text': message
                }
                response = requests.post(url, data=data,timeout=10)
                result = response.json()
                if result.get('ok'):
                    order.is_send = True
            except:
                error_count += 1
        return True



