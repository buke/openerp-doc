
.. i18n: .. module:: account_payment_extension
.. i18n:     :synopsis: Account Payment Extension 
.. i18n:     :noindex:
.. i18n: .. 
..

.. module:: account_payment_extension
    :synopsis: Account Payment Extension 
    :noindex:
.. 

.. i18n: .. raw:: html
.. i18n: 
.. i18n:       <br />
.. i18n:     <link rel="stylesheet" href="../_static/hide_objects_in_sidebar.css" type="text/css" />
..

.. raw:: html

      <br />
    <link rel="stylesheet" href="../_static/hide_objects_in_sidebar.css" type="text/css" />

.. i18n: .. tip:: This module is part of the OpenERP software, the leading Open Source 
.. i18n:   enterprise management system. If you want to discover OpenERP, check our 
.. i18n:   `screencasts <http://openerp.tv>`_ or download 
.. i18n:   `OpenERP <http://openerp.com>`_ directly.
..

.. tip:: This module is part of the OpenERP software, the leading Open Source 
  enterprise management system. If you want to discover OpenERP, check our 
  `screencasts <http://openerp.tv>`_ or download 
  `OpenERP <http://openerp.com>`_ directly.

.. i18n: .. raw:: html
.. i18n: 
.. i18n:     <div class="js-kit-rating" title="" permalink="" standalone="yes" path="/account_payment_extension"></div>
.. i18n:     <script src="http://js-kit.com/ratings.js"></script>
..

.. raw:: html

    <div class="js-kit-rating" title="" permalink="" standalone="yes" path="/account_payment_extension"></div>
    <script src="http://js-kit.com/ratings.js"></script>

.. i18n: Account Payment Extension (*account_payment_extension*)
.. i18n: =======================================================
.. i18n: :Module: account_payment_extension
.. i18n: :Name: Account Payment Extension
.. i18n: :Version: 5.0.1.1
.. i18n: :Author: Zikzakmedia SL
.. i18n: :Directory: account_payment_extension
.. i18n: :Web: www.zikzakmedia.com
.. i18n: :Official module: no
.. i18n: :Quality certified: no
..

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

.. i18n: Description
.. i18n: -----------
..

Description
-----------

.. i18n: ::
.. i18n: 
.. i18n:   Account payment extension.
.. i18n:   
.. i18n:   This module extends the account_payment module with a lot of features:
.. i18n:       * Extension of payment types: The payment type has a translated name and note that can be shown in the invoices.
.. i18n:       * Two default payment types for partners (client and supplier).
.. i18n:       * Automatic selection of payment type in invoices. Now an invoice can have a payment term (30 days, 30/60 days, ...) and a payment type (cash, bank transfer, ...).
.. i18n:       * A default check field in partner bank accounts. The default partner bank accounts are selected in invoices and payments.
.. i18n:       * New menu/tree/forms to see payments to receive and payments to pay.
.. i18n:       * The payments show tree editable fields: Due date, bank account and a check field (for example to write down if a bank check in paper support has been received).
.. i18n:       * Two types of payment orders: Payable payment orders (from supplier invoices) and receivable payment orders (from client invoices). So we can make payment orders to receive the payments of our client invoices. Each payment order type has its own sequence.
.. i18n:       * The payment orders allow negative payment amounts. So we can have payment orders for supplier invoices (pay money) and refund supplier invoices (return or receive money). Or for client invoices (receive money) and refund client invoices (return or pay money).
.. i18n:       * Payment orders: Selected invoices are filtered by payment type, the second message communication can be set at the same time for several invoices.
.. i18n:   Based on previous work of Pablo Rocandio & Zikzakmedia (version for 4.2).
..

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

.. i18n: Download links
.. i18n: --------------
..

Download links
--------------

.. i18n: You can download this module as a zip file in the following version:
..

You can download this module as a zip file in the following version:

.. i18n:   * `5.0 <http://www.openerp.com/download/modules/5.0/account_payment_extension.zip>`_
.. i18n:   * `trunk <http://www.openerp.com/download/modules/trunk/account_payment_extension.zip>`_
..

  * `5.0 <http://www.openerp.com/download/modules/5.0/account_payment_extension.zip>`_
  * `trunk <http://www.openerp.com/download/modules/trunk/account_payment_extension.zip>`_

.. i18n: Dependencies
.. i18n: ------------
..

Dependencies
------------

.. i18n:  * :mod:`base`
.. i18n:  * :mod:`account`
.. i18n:  * :mod:`account_payment`
..

 * :mod:`base`
 * :mod:`account`
 * :mod:`account_payment`

.. i18n: Reports
.. i18n: -------
..

Reports
-------

.. i18n: None
..

None

.. i18n: Menus
.. i18n: -------
..

Menus
-------

.. i18n:  * Financial Management/Configuration/Payment/Payment Type
.. i18n:  * Financial Management/Payment/Payable payment orders
.. i18n:  * Financial Management/Payment/Payable payment orders/Pay. payment order
.. i18n:  * Financial Management/Payment/Payable payment orders/Pay. payment order/Draft pay. payment order
.. i18n:  * Financial Management/Payment/Payable payment orders/Pay. payment order/Pay. payment orders to validate
.. i18n:  * Financial Management/Payment/Payable payment orders/New Pay. payment Order
.. i18n:  * Financial Management/Payment/Receivable payment orders
.. i18n:  * Financial Management/Payment/Receivable payment orders/Rec. payment order
.. i18n:  * Financial Management/Payment/Receivable payment orders/Rec. payment order/Draft rec. payment order
.. i18n:  * Financial Management/Payment/Receivable payment orders/Rec. payment order/Rec. payment orders to validate
.. i18n:  * Financial Management/Payment/Receivable payment orders/New rec. payment order
.. i18n:  * Financial Management/Payment/Invoice payments
.. i18n:  * Financial Management/Payment/Invoice payments/Invoice payments to receive
.. i18n:  * Financial Management/Payment/Invoice payments/All received and to receive invoice payments
.. i18n:  * Financial Management/Payment/Invoice payments/Invoice payments to pay
.. i18n:  * Financial Management/Payment/Invoice payments/All paid and to pay invoice payments
.. i18n:  * Financial Management/Payment/Done payments
.. i18n:  * Financial Management/Payment/Done payments/Done receivable payments unreconciled
.. i18n:  * Financial Management/Payment/Done payments/All done receivable payments
.. i18n:  * Financial Management/Payment/Done payments/Done payable payments unreconciled
.. i18n:  * Financial Management/Payment/Done payments/All done payable payments
..

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

.. i18n: Views
.. i18n: -----
..

Views
-----

.. i18n:  * \* INHERIT  (form)
.. i18n:  * \* INHERIT  (form)
.. i18n:  * \* INHERIT view.partner.form3  (form)
.. i18n:  * \* INHERIT view.partner.bank.tree  (form)
.. i18n:  * \* INHERIT res.partner.form.payment_type1 (form)
.. i18n:  * \* INHERIT res.partner.form.payment_type2 (form)
.. i18n:  * payment.type.tree (tree)
.. i18n:  * \* INHERIT payment.type.form_ext (form)
.. i18n:  * \* INHERIT account.invoice.form3.payment_type (form)
.. i18n:  * \* INHERIT account.invoice.form4.payment_type (form)
.. i18n:  * \* INHERIT account.invoice.supplier.form2 (form)
.. i18n:  * \* INHERIT account.payments.move.line.tree (tree)
.. i18n:  * \* INHERIT account.payments.move.line.form (form)
.. i18n:  * \* INHERIT account.bank.statement.form.ext (form)
.. i18n:  * \* INHERIT payment.order.form.ext1 (form)
.. i18n:  * \* INHERIT payment.order.form.ext2 (form)
.. i18n:  * \* INHERIT payment.line.ext1 (form)
.. i18n:  * Payments (tree)
..

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

.. i18n: Objects
.. i18n: -------
..

Objects
-------

.. i18n: None
..

None
