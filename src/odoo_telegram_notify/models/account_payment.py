import os
import requests
from odoo import models, fields, api
from dotenv import load_dotenv
load_dotenv()

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
            ('state', '=', 'paid'),
            ('send_telegram_payment_invoice', '=', False),
        ])

        error_count = 0

        for invoice in paid_invoice:
            try:
                chat_id = invoice.partner_id.chat_id
                message = (f"💵 To'lov qabul qilindi: {invoice.name}\n\nMijoz: {invoice.partner_id.name}\n"
                           f"To'lov usuli: {invoice.journal_id.name}\nTo'lov turi: {invoice.payment_method_line_id.name} \n❗️ Sana:  {invoice.date}\nTo'langan summa: {invoice.amount}"
                           f"\nIzoh: {invoice.memo}")
                data = {
                    'chat_id': chat_id,
                    'text': message
                }
                response = requests.post(url, data=data)
                result = response.json()
                if result.get('ok'):
                    invoice.send_telegram_payment_invoice = True
            except:
                error_count += 1
        return True
