# -*- coding: utf-8 -*-

{
'name':'Uapa Updates',
'version': '1.1',
'author':'OBS',
'category':'Updates',
'description': """
A collection of small updates for the implementation of UAPA.
""",
'depends':['base_setup',
        'hr',
        'stock',
        'hr_expense',
        'hr_contract',
        'hr_payroll',
        'hr_payroll_account',
        'account_voucher',
        'event',
        'account_sequence',
        'account_check_writing',
        'account_asset'
#        'point_of_sale'
],
'data':['stock_location_view.xml',
        'hr_updates_view.xml',
        'employee_number_seq.xml',
        'events_updates_view.xml',
        'res_partner_updates_view.xml',
        #'books_authors.xml',
        'account_asset_move_view.xml',
        'account_asset_update_view.xml',
        #'asset_sequences.xml',
        'account_invoice_view.xml',
        'account_journal_update.xml',
        'account_account_update_view.xml',
        'account_invoice_line_update_view.xml',
        'purchase_order.xml',
        'stock_picking_view.xml',
        'product_normal_form_inherit.xml',
        'purchase_requisition_form_inherit.xml'],
'installable':True,
}
