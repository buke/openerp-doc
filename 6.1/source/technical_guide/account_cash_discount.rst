
.. module:: account_cash_discount
    :synopsis: Payment Term with Cash Discount 
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

    <div class="js-kit-rating" title="" permalink="" standalone="yes" path="/account_cash_discount"></div>
    <script src="http://js-kit.com/ratings.js"></script>

Payment Term with Cash Discount (*account_cash_discount*)
==========================================================
:Module: account_cash_discount
:Name: Payment Term with Cash Discount
:Version: 5.0.1.0
:Author: Tiny
:Directory: account_cash_discount
:Web: http://www.openerp.com
:Official module: no
:Quality certified: no

Description
-----------

::

  This module adds cash discounts on payment terms. Cash discounts
      for a payment term can be configured with:
          * A number of days,
          * A discount (%),
          * A debit and a credit account

Download links
--------------

You can download this module as a zip file in the following version:

  * `4.2 <http://www.openerp.com/download/modules/4.2/account_cash_discount.zip>`_
  * `5.0 <http://www.openerp.com/download/modules/5.0/account_cash_discount.zip>`_
  * `trunk <http://www.openerp.com/download/modules/trunk/account_cash_discount.zip>`_


Dependencies
------------

 * :mod:`account`

Reports
-------

None


Menus
-------


None


Views
-----

 * account.cash.discount.form (form)
 * account.cash.discount.tree (tree)
 * \* INHERIT account.payment.term.form (form)


Objects
-------

Object: Cash Discount (account.cash.discount)
#############################################



:payment_id: Associated Payment Term, many2one





:name: Name, char





:credit_account_id: Credit Account, many2one





:delay: Number of Days, integer, required





:discount: Discount (%), float, required





:debit_account_id: Debit Account, many2one


