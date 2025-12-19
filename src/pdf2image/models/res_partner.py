from odoo import models, fields, api


class ResPartner(models.Model):
    _inherit = 'res.partner'

    chat_id = fields.Char(string="Telegram Chat ID", help="Telegram Group Chat ID for sending messages.")
