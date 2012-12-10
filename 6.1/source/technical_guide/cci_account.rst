
.. i18n: .. module:: cci_account
.. i18n:     :synopsis: CCI Account 
.. i18n:     :noindex:
.. i18n: .. 
..

.. module:: cci_account
    :synopsis: CCI Account 
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
.. i18n:     <div class="js-kit-rating" title="" permalink="" standalone="yes" path="/cci_account"></div>
.. i18n:     <script src="http://js-kit.com/ratings.js"></script>
..

.. raw:: html

    <div class="js-kit-rating" title="" permalink="" standalone="yes" path="/cci_account"></div>
    <script src="http://js-kit.com/ratings.js"></script>

.. i18n: CCI Account (*cci_account*)
.. i18n: ===========================
.. i18n: :Module: cci_account
.. i18n: :Name: CCI Account
.. i18n: :Version: 5.0.1.0
.. i18n: :Author: Tiny
.. i18n: :Directory: cci_account
.. i18n: :Web: http://www.openerp.com
.. i18n: :Official module: no
.. i18n: :Quality certified: no
..

CCI Account (*cci_account*)
===========================
:Module: cci_account
:Name: CCI Account
:Version: 5.0.1.0
:Author: Tiny
:Directory: cci_account
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
.. i18n:   specific module for cci project which will use account module (Reports).
..

::

  specific module for cci project which will use account module (Reports).

.. i18n: Download links
.. i18n: --------------
..

Download links
--------------

.. i18n: You can download this module as a zip file in the following version:
..

You can download this module as a zip file in the following version:

.. i18n:   * `5.0 <http://www.openerp.com/download/modules/5.0/cci_account.zip>`_
.. i18n:   * `trunk <http://www.openerp.com/download/modules/trunk/cci_account.zip>`_
..

  * `5.0 <http://www.openerp.com/download/modules/5.0/cci_account.zip>`_
  * `trunk <http://www.openerp.com/download/modules/trunk/cci_account.zip>`_

.. i18n: Dependencies
.. i18n: ------------
..

Dependencies
------------

.. i18n:  * :mod:`account_invoice_layout`
.. i18n:  * :mod:`sale`
.. i18n:  * :mod:`account_analytic_plans`
.. i18n:  * :mod:`l10n_be`
.. i18n:  * :mod:`base_vat`
.. i18n:  * :mod:`cci_partner`
.. i18n:  * :mod:`membership`
..

 * :mod:`account_invoice_layout`
 * :mod:`sale`
 * :mod:`account_analytic_plans`
 * :mod:`l10n_be`
 * :mod:`base_vat`
 * :mod:`cci_partner`
 * :mod:`membership`

.. i18n: Reports
.. i18n: -------
..

Reports
-------

.. i18n:  * Draft Invoices
.. i18n: 
.. i18n:  * Print VCS
..

 * Draft Invoices

 * Print VCS

.. i18n: Menus
.. i18n: -------
..

Menus
-------

.. i18n:  * Financial Management/Periodical Processing/Use Models
..

 * Financial Management/Periodical Processing/Use Models

.. i18n: Views
.. i18n: -----
..

Views
-----

.. i18n:  * \* INHERIT account.invoice.supplier.form.inherit (form)
.. i18n:  * \* INHERIT account.invoice.form.inherit (form)
.. i18n:  * \* INHERIT account.bank.statement.form (form)
.. i18n:  * \* INHERIT account.invoice.supplier.form (form)
.. i18n:  * \* INHERIT account.invoice.form (form)
.. i18n:  * \* INHERIT account.invoice.supplier.form (form)
.. i18n:  * \* INHERIT account.invoice.form (form)
.. i18n:  * \* INHERIT sale.order.form (form)
..

 * \* INHERIT account.invoice.supplier.form.inherit (form)
 * \* INHERIT account.invoice.form.inherit (form)
 * \* INHERIT account.bank.statement.form (form)
 * \* INHERIT account.invoice.supplier.form (form)
 * \* INHERIT account.invoice.form (form)
 * \* INHERIT account.invoice.supplier.form (form)
 * \* INHERIT account.invoice.form (form)
 * \* INHERIT sale.order.form (form)

.. i18n: Objects
.. i18n: -------
..

Objects
-------

.. i18n: None
..

None
