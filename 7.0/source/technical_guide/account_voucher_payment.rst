
.. module:: account_voucher_payment
    :synopsis: Invoice Payment/Receipt by Vouchers. 
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

    <div class="js-kit-rating" title="" permalink="" standalone="yes" path="/account_voucher_payment"></div>
    <script src="http://js-kit.com/ratings.js"></script>

Invoice Payment/Receipt by Vouchers. (*account_voucher_payment*)
================================================================
:Module: account_voucher_payment
:Name: Invoice Payment/Receipt by Vouchers.
:Version: 5.0.1.0
:Author: Tiny & Axelor
:Directory: account_voucher_payment
:Web: http://tinyerpindia.com
:Official module: no
:Quality certified: no

Description
-----------

::

  This module includes :
      * It reconcile the invoice (supplier, customer) while paying through Accounting Vouchers
      A Voucher, is defined like some document that involve a banking transaction.
      the Objective, is, one time the credit and collection people load some payment on the system, every voucher
      Loaded on system should be reconcilied with a bank statement by Accounting people.

Download links
--------------

You can download this module as a zip file in the following version:

  * `5.0 <http://www.openerp.com/download/modules/5.0/account_voucher_payment.zip>`_
  * `trunk <http://www.openerp.com/download/modules/trunk/account_voucher_payment.zip>`_


Dependencies
------------

 * :mod:`base`
 * :mod:`account`
 * :mod:`account_voucher`

Reports
-------

None


Menus
-------


None


Views
-----

 * \* INHERIT account.voucher.form.inherit (form)
 * \* INHERIT account.voucher.form.inherit2 (form)
 * \* INHERIT account.move.line.form.inherit (form)
 * \* INHERIT account.move.line.form.inherit (tree)


Objects
-------

None
