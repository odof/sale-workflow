# -*- coding: utf-8 -*-
# Copyright 2017 ACSONE SA/NV
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    'name': 'Sale Automatic Workflow Payment Ref',
    'summary': """
        Propagates your payment reference from your sale order to your
        payment""",
    'version': '10.0.1.0.1',
    'license': 'AGPL-3',
    'author': 'ACSONE SA/NV,Odoo Community Association (OCA)',
    'website': 'https://github.com/OCA/sale-workflow',
    'depends': [
        'sale_automatic_workflow_payment_mode',
        'base_transaction_id',
    ],
}
