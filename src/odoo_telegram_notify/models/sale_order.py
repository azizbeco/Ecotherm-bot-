from odoo import models, fields, api
from pdf2image import convert_from_bytes
import requests
import os
import tempfile
from dotenv import load_dotenv
load_dotenv()


# TOKEN = os.environ.get('TOKEN')
# CHAT_ID = os.environ.get('CHAT_ID')


class PDF2ImageConfig(models.Model):
    _inherit = "sale.order"

    sent_qoute = fields.Boolean(default=False)

    def sale_confirm(self):
        quotes = self.env['sale.order'].search([
            ('state', '=', 'sale'),
            ('sent_qoute', '=', False),
        ])
        TOKEN = self.env['ir.config_parameter'].sudo().get_param('TOKEN')

        if not TOKEN:
            raise ValueError("Telegram BOT TOKEN is not configured.")

        for order in quotes:
            chat_id = order.partner_id.chat_id
            message = f'Sale Quote Tasdiqlandi: {order.name}'

            pdf_content = self.env['ir.actions.report']._render_qweb_pdf(
                report_ref='sale.action_report_saleorder',
                res_ids=order.id
            )[0]
            order.pdf2image(pdf_content, caption=message, token=TOKEN, chat_id=chat_id)
            order.sent_qoute = True










    def pdf2image(self,pdf_content, caption=None,token=None, chat_id=None):
        image = convert_from_bytes(pdf_content, dpi=200)

        with tempfile.TemporaryDirectory() as temp_dir:
            image_paths = []
            for i, img in enumerate(image):
                image_path = os.path.join(temp_dir, f'page_{i}.png')
                img.save(image_path, 'PNG')
                image_paths.append(image_path)
            self.send_image_to_telegram(image_paths, caption=caption, token=token, chat_id=chat_id)

    def send_quote_to_telegram(self, caption=None):
        self.ensure_one()
        TOKEN = self.env['ir.config_parameter'].sudo().get_param('TOKEN')
        pdf_content = self.env['ir.actions.report']._render_qweb_pdf(
            report_ref='sale.action_report_saleorder',
            res_ids=self.ids
        )[0]
        for record in self:
            chat_id = record.partner_id.chat_id


        self.pdf2image(pdf_content, caption=caption,token=TOKEN, chat_id=chat_id)


    def send_image_to_telegram(self,image_path, caption=None,token=None, chat_id=None):
        telegram_api = f'https://api.telegram.org/bot{token}/sendPhoto'

        for image_path in image_path:
            with open(image_path, 'rb') as photo:
                files = {'photo': photo}
                data = {
                    'chat_id': chat_id,
                    'caption': caption or f'Quote: {self.name}'
                }
                response = requests.post(telegram_api, data=data, files=files)

                if response.status_code != 200:
                    raise Exception(f"Failed to send image to Telegram: {response.text}")






