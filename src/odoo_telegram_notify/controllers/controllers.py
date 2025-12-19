# -*- coding: utf-8 -*-
# from odoo import http


# class Pdf2image(http.Controller):
#     @http.route('/odoo_telegram_notify/odoo_telegram_notify', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/odoo_telegram_notify/odoo_telegram_notify/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('odoo_telegram_notify.listing', {
#             'root': '/odoo_telegram_notify/odoo_telegram_notify',
#             'objects': http.request.env['odoo_telegram_notify.odoo_telegram_notify'].search([]),
#         })

#     @http.route('/odoo_telegram_notify/odoo_telegram_notify/objects/<model("odoo_telegram_notify.odoo_telegram_notify"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('odoo_telegram_notify.object', {
#             'object': obj
#         })

