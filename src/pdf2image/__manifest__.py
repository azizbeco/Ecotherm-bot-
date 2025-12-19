# -*- coding: utf-8 -*-
{
    'name': "pdf2image",
    'author': "My Company",
    'version': '0.1',

    'depends': ['sale'],

    'data': [
        # 'security/ir.model.access.csv',
        'data/sale_confirm.xml',
        'data/invoice_confirm.xml',
        'data/payment_invoice.xml',
        'data/picking_type_operations.xml',

        'views/sale_order.xml',
        'views/res_partner.xml',
        'views/sale_send_photo_button.xml',
        'views/account_move.xml',
        'views/account_payment.xml',
        'views/stock_picking.xml',
    ],
    'installable': True,
}

