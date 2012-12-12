
.. module:: account_payment_extension
    :synopsis: Account Payment Extension 
    :noindex:
.. 

.. raw:: html

      <br />
    <link rel="stylesheet" href="../_static/hide_objects_in_sidebar.css" type="text/css" />

.. tip:: This module is part of the OpenERP software, the leading Open Source 
  enterprise management system. If you want to discover OpenERP, check our 
  `screencasts <http://openerp.tv>`_ or download 
  `OpenERP <http://openerp.com>`_ directly.

.. raw:: html

    <div class="js-kit-rating" title="" permalink="" standalone="yes" path="/account_payment_extension"></div>
    <script src="http://js-kit.com/ratings.js"></script>

Account Payment Extension (*account_payment_extension*)
=======================================================
:Module: account_payment_extension
:Name: Account Payment Extension
:Version: 5.0.1.1
:Author: Zikzakmedia SL
:Directory: account_payment_extension
:Web: www.zikzakmedia.com
:Official module: no
:Quality certified: no

Description
-----------

::

  Account payment extension.
  
  This module extends the account_payment module with a lot of features:
      * Extension of payment types: The payment type has a translated name and note that can be shown in the invoices.
      * Two default payment types for partners (client and supplier).
      * Automatic selection of payment type in invoices. Now an invoice can have a payment term (30 days, 30/60 days, ...) and a payment type (cash, bank transfer, ...).
      * A default check field in partner bank accounts. The default partner bank accounts are selected in invoices and payments.
      * New menu/tree/forms to see payments to receive and payments to pay.
      * The payments show tree editable fields: Due date, bank account and a check field (for example to write down if a bank check in paper support has been received).
      * Two types of payment orders: Payable payment orders (from supplier invoices) and receivable payment orders (from client invoices). So we can make payment orders to receive the payments of our client invoices. Each payment order type has its own sequence.
      * The payment orders allow negative payment amounts. So we can have payment orders for supplier invoices (pay money) and refund supplier invoices (return or receive money). Or for client invoices (receive money) and refund client invoices (return or pay money).
      * Payment orders: Selected invoices are filtered by payment type, the second message communication can be set at the same time for several invoices.
  Based on previous work of Pablo Rocandio & Zikzakmedia (version for 4.2).

Download links
--------------

You can download this module as a zip file in the following version:

  * `5.0 <http://www.openerp.com/download/modules/5.0/account_payment_extension.zip>`_
  * `trunk <http://www.openerp.com/download/modules/trunk/account_payment_extension.zip>`_


Dependencies
------------

 * :mod:`base`
 * :mod:`account`
 * :mod:`account_payment`

Reports
-------

None


Menus
-------

 * Financial Management/Configuration/Payment/Payment Type
 * Financial Management/Payment/Payable payment orders
 * Financial Management/Payment/Payable payment orders/Pay. payment order
 * Financial Management/Payment/Payable payment orders/Pay. payment order/Draft pay. payment order
 * Financial Management/Payment/Payable payment orders/Pay. payment order/Pay. payment orders to validate
 * Financial Management/Payment/Payable payment orders/New Pay. payment Order
 * Financial Management/Payment/Receivable payment orders
 * Financial Management/Payment/Receivable payment orders/Rec. payment order
 * Financial Management/Payment/Receivable payment orders/Rec. payment order/Draft rec. payment order
 * Financial Management/Payment/Receivable payment orders/Rec. payment order/Rec. payment orders to validate
 * Financial Management/Payment/Receivable payment orders/New rec. payment order
 * Financial Management/Payment/Invoice payments
 * Financial Management/Payment/Invoice payments/Invoice payments to receive
 * Financial Management/Payment/Invoice payments/All received and to receive invoice payments
 * Financial Management/Payment/Invoice payments/Invoice payments to pay
 * Financial Management/Payment/Invoice payments/All paid and to pay invoice payments
 * Financial Management/Payment/Done payments
 * Financial Management/Payment/Done payments/Done receivable payments unreconciled
 * Financial Management/Payment/Done payments/All done receivable payments
 * Financial Management/Payment/Done payments/Done payable payments unreconciled
 * Financial Management/Payment/Done payments/All done payable payments

Views
-----

 * \* INHERIT  (form)
 * \* INHERIT  (form)
 * \* INHERIT view.partner.form3  (form)
 * \* INHERIT view.partner.bank.tree  (form)
 * \* INHERIT res.partner.form.payment_type1 (form)
 * \* INHERIT res.partner.form.payment_type2 (form)
 * payment.type.tree (tree)
 * \* INHERIT payment.type.form_ext (form)
 * \* INHERIT account.invoice.form3.payment_type (form)
 * \* INHERIT account.invoice.form4.payment_type (form)
 * \* INHERIT account.invoice.supplier.form2 (form)
 * \* INHERIT account.payments.move.line.tree (tree)
 * \* INHERIT account.payments.move.line.form (form)
 * \* INHERIT account.bank.statement.form.ext (form)
 * \* INHERIT payment.order.form.ext1 (form)
 * \* INHERIT payment.order.form.ext2 (form)
 * \* INHERIT payment.line.ext1 (form)
 * Payments (tree)


Objects
-------

None
