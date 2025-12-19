# -*- coding: utf-8 -*-
# from odoo import http


# class SendPhotoButtonForSaleorder(http.Controller):
#     @http.route('/send_photo_button_for_saleorder/send_photo_button_for_saleorder', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/send_photo_button_for_saleorder/send_photo_button_for_saleorder/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('send_photo_button_for_saleorder.listing', {
#             'root': '/send_photo_button_for_saleorder/send_photo_button_for_saleorder',
#             'objects': http.request.env['send_photo_button_for_saleorder.send_photo_button_for_saleorder'].search([]),
#         })

#     @http.route('/send_photo_button_for_saleorder/send_photo_button_for_saleorder/objects/<model("send_photo_button_for_saleorder.send_photo_button_for_saleorder"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('send_photo_button_for_saleorder.object', {
#             'object': obj
#         })

