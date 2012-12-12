
.. module:: account_voucher
    :synopsis: Accounting Voucher Entries (Official, Quality Certified)
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

    <div class="js-kit-rating" title="" permalink="" standalone="yes" path="/account_voucher"></div>
    <script src="http://js-kit.com/ratings.js"></script>

Accounting Voucher Entries (*account_voucher*)
==============================================
:Module: account_voucher
:Name: Accounting Voucher Entries
:Version: 5.0.1.0
:Author: Tiny & Axelor
:Directory: account_voucher
:Web: http://tinyerp.com
:Official module: yes
:Quality certified: yes

Description
-----------

::

  India Accounting module includes all the basic requirements of 
      Basic Accounting, like
      * Bank Payment, Receipt
      * Cash Payment, Receipt

Download links
--------------

You can download this module as a zip file in the following version:

  * `4.2 <http://www.openerp.com/download/modules/4.2/account_voucher.zip>`_
  * `5.0 <http://www.openerp.com/download/modules/5.0/account_voucher.zip>`_
  * `trunk <http://www.openerp.com/download/modules/trunk/account_voucher.zip>`_


Dependencies
------------

 * :mod:`base`
 * :mod:`account`

Reports
-------

 * Voucher Report (Cr/Dr)

 * Voucher Report

Menus
-------

 * Financial Management/Voucher Entries/Open Vouchers
 * Financial Management/Voucher Entries
 * Financial Management/Voucher Entries/Receipt Vouchers
 * Financial Management/Voucher Entries/Receipt Vouchers/Cash Receipts
 * Financial Management/Voucher Entries/Receipt Vouchers/Cash Receipts/New Cash Receipt
 * Financial Management/Voucher Entries/Receipt Vouchers/Bank Receipts
 * Financial Management/Voucher Entries/Receipt Vouchers/Bank Receipts/New Bank Receipt
 * Financial Management/Voucher Entries/Payment Vouchers
 * Financial Management/Voucher Entries/Payment Vouchers/Cash Payments
 * Financial Management/Voucher Entries/Payment Vouchers/Cash Payments/New Cash Payment
 * Financial Management/Voucher Entries/Payment Vouchers/Bank Payments
 * Financial Management/Voucher Entries/Payment Vouchers/Bank Payments/New Bank Payment
 * Financial Management/Voucher Entries/Other Vouchers
 * Financial Management/Voucher Entries/Other Vouchers/Contra Voucher
 * Financial Management/Voucher Entries/Other Vouchers/Journal Sale Voucher
 * Financial Management/Voucher Entries/Other Vouchers/Journal Purchase Voucher
 * Financial Management/Voucher Entries/Other Vouchers/Journal Voucher

Views
-----

 * account.voucher.tree (tree)
 * account.voucher.form (form)
 * \* INHERIT account.move.type.form.inherit2 (form)
 * \* INHERIT account.form1 (form)
 * \* INHERIT account.form2 (form)
 * \* INHERIT account.tree1 (tree)
 * \* INHERIT account.tree2 (tree)
 * \* INHERIT sub.currency.form (form)


Objects
-------

Object: Accounting Voucher (account.voucher)
############################################



:move_ids: Real Entry, many2many





:type: Type, selection, readonly





:account_id: Account, many2one, required, readonly





:reference: Voucher Reference, char





:amount: Amount, float, readonly





:reference_type: Reference Type, selection, required





:company_id: Company, many2one, required





:number: Number, char, readonly





:currency_id: Currency, many2one, required, readonly





:journal_id: Journal, many2one, required, readonly





:state: State, selection, readonly





:payment_ids: Voucher Lines, one2many





:narration: Narration, text, required, readonly





:date: Date, date, readonly





:period_id: Period, many2one, required





:partner_id: Partner, many2one, readonly





:move_id: Account Entry, many2one





:name: Name, char, required, readonly




Object: Voucher Line (account.voucher.line)
###########################################



:ref: Ref., char





:name: Description, char, required





:partner_id: Partner, many2one





:account_analytic_id: Analytic Account, many2one





:amount: Amount, float





:voucher_id: Voucher, many2one





:type: Type, selection





:account_id: Account, many2one, required


