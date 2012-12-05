
.. i18n: .. module:: account_cash_discount
.. i18n:     :synopsis: Payment Term with Cash Discount 
.. i18n:     :noindex:
.. i18n: .. 
..

.. module:: account_cash_discount
    :synopsis: Payment Term with Cash Discount 
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
.. i18n:     <div class="js-kit-rating" title="" permalink="" standalone="yes" path="/account_cash_discount"></div>
.. i18n:     <script src="http://js-kit.com/ratings.js"></script>
..

.. raw:: html

    <div class="js-kit-rating" title="" permalink="" standalone="yes" path="/account_cash_discount"></div>
    <script src="http://js-kit.com/ratings.js"></script>

.. i18n: Payment Term with Cash Discount (*account_cash_discount*)
.. i18n: ==========================================================
.. i18n: :Module: account_cash_discount
.. i18n: :Name: Payment Term with Cash Discount
.. i18n: :Version: 5.0.1.0
.. i18n: :Author: Tiny
.. i18n: :Directory: account_cash_discount
.. i18n: :Web: http://www.openerp.com
.. i18n: :Official module: no
.. i18n: :Quality certified: no
..

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

.. i18n: Description
.. i18n: -----------
..

Description
-----------

.. i18n: ::
.. i18n: 
.. i18n:   This module adds cash discounts on payment terms. Cash discounts
.. i18n:       for a payment term can be configured with:
.. i18n:           * A number of days,
.. i18n:           * A discount (%),
.. i18n:           * A debit and a credit account
..

::

  This module adds cash discounts on payment terms. Cash discounts
      for a payment term can be configured with:
          * A number of days,
          * A discount (%),
          * A debit and a credit account

.. i18n: Download links
.. i18n: --------------
..

Download links
--------------

.. i18n: You can download this module as a zip file in the following version:
..

You can download this module as a zip file in the following version:

.. i18n:   * `4.2 <http://www.openerp.com/download/modules/4.2/account_cash_discount.zip>`_
.. i18n:   * `5.0 <http://www.openerp.com/download/modules/5.0/account_cash_discount.zip>`_
.. i18n:   * `trunk <http://www.openerp.com/download/modules/trunk/account_cash_discount.zip>`_
..

  * `4.2 <http://www.openerp.com/download/modules/4.2/account_cash_discount.zip>`_
  * `5.0 <http://www.openerp.com/download/modules/5.0/account_cash_discount.zip>`_
  * `trunk <http://www.openerp.com/download/modules/trunk/account_cash_discount.zip>`_

.. i18n: Dependencies
.. i18n: ------------
..

Dependencies
------------

.. i18n:  * :mod:`account`
..

 * :mod:`account`

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

.. i18n:  * account.cash.discount.form (form)
.. i18n:  * account.cash.discount.tree (tree)
.. i18n:  * \* INHERIT account.payment.term.form (form)
..

 * account.cash.discount.form (form)
 * account.cash.discount.tree (tree)
 * \* INHERIT account.payment.term.form (form)

.. i18n: Objects
.. i18n: -------
..

Objects
-------

.. i18n: Object: Cash Discount (account.cash.discount)
.. i18n: #############################################
..

Object: Cash Discount (account.cash.discount)
#############################################

.. i18n: :payment_id: Associated Payment Term, many2one
..

:payment_id: Associated Payment Term, many2one

.. i18n: :name: Name, char
..

:name: Name, char

.. i18n: :credit_account_id: Credit Account, many2one
..

:credit_account_id: Credit Account, many2one

.. i18n: :delay: Number of Days, integer, required
..

:delay: Number of Days, integer, required

.. i18n: :discount: Discount (%), float, required
..

:discount: Discount (%), float, required

.. i18n: :debit_account_id: Debit Account, many2one
..

:debit_account_id: Debit Account, many2one
