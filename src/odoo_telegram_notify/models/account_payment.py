import os
import requests
from odoo import models, fields, api

TOKEN = os.environ.get("TOKEN")
CHAT_ID = os.environ.get("CHAT_ID")
url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"

class AccountPaymentRegister(models.Model):
    _inherit = 'account.payment'

    send_telegram_payment_invoice = fields.Boolean(default=False)


    def send_telegram_paid_invoice(self):
        TOKEN = self.env['ir.config_parameter'].sudo().get_param('TOKEN')
        if not TOKEN:
            raise ValueError("Telegram BOT TOKEN is not configured.")

        url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"

        paid_invoice = self.env['account.payment'].search([
            ('state', 'in', ['in_process','paid']),
            ('send_telegram_payment_invoice', '=', False),
        ])
        

        error_count = 0

        for payment in paid_invoice:
            try:
                chat_id = payment.partner_id.chat_id
                residual_amount = payment.reconciled_invoice_ids.amount_residual

                if not chat_id:
                    continue
                if payment.state == 'in_process':
                    message = (f"💵 To'lov qabul qilindi!\n\n"
                           f"Invoice: {payment.name}\n"
                           f"Mijoz: {payment.partner_id.name}\n"
                           f"To'langan summa: {payment.amount} {payment.currency_id.symbol}\n"
                           f"Hozirgi qoldiq: {residual_amount} {payment.currency_id.symbol}\n"
                           f"📅 Sana: {payment.date}\n"
                           f"Izoh: {payment.memo or ''}")
                elif payment.state == 'paid':
                    message = (f"💵 To'lov qabul qilindi!\n\n"
                           f"Invoice: {payment.name}\n"
                           f"Mijoz: {payment.partner_id.name}\n"
                           f"To'langan summa: {payment.amount} {payment.currency_id.symbol}\n"
                           f"Hozirgi qoldiq: {residual_amount} {payment.currency_id.symbol}\n"
                           f"📅 Sana: {payment.date}\n"
                           f"Izoh: {payment.memo or ''}")
                else:
                    continue

                data = {
                    'chat_id': chat_id,
                    'text': message
                }
                response = requests.post(url, data=data)
                result = response.json()
                if result.get('ok'):
                    payment.send_telegram_payment_invoice = True
            except:
                error_count += 1
        return True
