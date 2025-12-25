
from odoo import models, fields, api
import requests

class SendConfirmedReport(models.Model):
    _inherit = 'account.move'
    send_telegram_posted_invoice = fields.Boolean(default=False)

    def invoice_confirm(self):
        TOKEN = self.env['ir.config_parameter'].sudo().get_param('TOKEN')
        if not TOKEN:
            raise ValueError("Telegram BOT TOKEN is not configured.")

        url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"


        posted_invoice = self.env['account.move'].search([
            ('state', '=', 'posted'),
            ('move_type', '=', 'out_invoice'),
            ('send_telegram_posted_invoice', '=', False),
        ])

        error_count = 0

        for invoice in posted_invoice:
            try:
                chat_id = invoice.partner_id.chat_id
                message = f"✅ Invoice tasqilandi: {invoice.name}\n\n❗️ Sana:  {invoice.invoice_date_due}\nTo'lanishi kerak bo'lgan summa:  {invoice.amount_total}"

                data = {
                    'chat_id': chat_id,
                    'text': message
                }
                response = requests.post(url, data=data)
                result = response.json()
                if result.get('ok'):
                    invoice.send_telegram_posted_invoice = True

            except:
                error_count += 1

        return True
