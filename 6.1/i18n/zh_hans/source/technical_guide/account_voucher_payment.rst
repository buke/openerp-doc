
.. i18n: .. module:: account_voucher_payment
.. i18n:     :synopsis: Invoice Payment/Receipt by Vouchers. 
.. i18n:     :noindex:
.. i18n: .. 
..

.. module:: account_voucher_payment
    :synopsis: Invoice Payment/Receipt by Vouchers. 
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
.. i18n:     <div class="js-kit-rating" title="" permalink="" standalone="yes" path="/account_voucher_payment"></div>
.. i18n:     <script src="http://js-kit.com/ratings.js"></script>
..

.. raw:: html

    <div class="js-kit-rating" title="" permalink="" standalone="yes" path="/account_voucher_payment"></div>
    <script src="http://js-kit.com/ratings.js"></script>

.. i18n: Invoice Payment/Receipt by Vouchers. (*account_voucher_payment*)
.. i18n: ================================================================
.. i18n: :Module: account_voucher_payment
.. i18n: :Name: Invoice Payment/Receipt by Vouchers.
.. i18n: :Version: 5.0.1.0
.. i18n: :Author: Tiny & Axelor
.. i18n: :Directory: account_voucher_payment
.. i18n: :Web: http://tinyerpindia.com
.. i18n: :Official module: no
.. i18n: :Quality certified: no
..

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

.. i18n: Description
.. i18n: -----------
..

Description
-----------

.. i18n: ::
.. i18n: 
.. i18n:   This module includes :
.. i18n:       * It reconcile the invoice (supplier, customer) while paying through Accounting Vouchers
.. i18n:       A Voucher, is defined like some document that involve a banking transaction.
.. i18n:       the Objective, is, one time the credit and collection people load some payment on the system, every voucher
.. i18n:       Loaded on system should be reconcilied with a bank statement by Accounting people.
..

::

  This module includes :
      * It reconcile the invoice (supplier, customer) while paying through Accounting Vouchers
      A Voucher, is defined like some document that involve a banking transaction.
      the Objective, is, one time the credit and collection people load some payment on the system, every voucher
      Loaded on system should be reconcilied with a bank statement by Accounting people.

.. i18n: Download links
.. i18n: --------------
..

Download links
--------------

.. i18n: You can download this module as a zip file in the following version:
..

You can download this module as a zip file in the following version:

.. i18n:   * `5.0 <http://www.openerp.com/download/modules/5.0/account_voucher_payment.zip>`_
.. i18n:   * `trunk <http://www.openerp.com/download/modules/trunk/account_voucher_payment.zip>`_
..

  * `5.0 <http://www.openerp.com/download/modules/5.0/account_voucher_payment.zip>`_
  * `trunk <http://www.openerp.com/download/modules/trunk/account_voucher_payment.zip>`_

.. i18n: Dependencies
.. i18n: ------------
..

Dependencies
------------

.. i18n:  * :mod:`base`
.. i18n:  * :mod:`account`
.. i18n:  * :mod:`account_voucher`
..

 * :mod:`base`
 * :mod:`account`
 * :mod:`account_voucher`

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

.. i18n: None
..

None

.. i18n: Views
.. i18n: -----
..

Views
-----

.. i18n:  * \* INHERIT account.voucher.form.inherit (form)
.. i18n:  * \* INHERIT account.voucher.form.inherit2 (form)
.. i18n:  * \* INHERIT account.move.line.form.inherit (form)
.. i18n:  * \* INHERIT account.move.line.form.inherit (tree)
..

 * \* INHERIT account.voucher.form.inherit (form)
 * \* INHERIT account.voucher.form.inherit2 (form)
 * \* INHERIT account.move.line.form.inherit (form)
 * \* INHERIT account.move.line.form.inherit (tree)

.. i18n: Objects
.. i18n: -------
..

Objects
-------

.. i18n: None
..

None
