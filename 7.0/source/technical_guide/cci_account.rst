
.. module:: cci_account
    :synopsis: CCI Account 
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

    <div class="js-kit-rating" title="" permalink="" standalone="yes" path="/cci_account"></div>
    <script src="http://js-kit.com/ratings.js"></script>

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

Description
-----------

::

  specific module for cci project which will use account module (Reports).

Download links
--------------

You can download this module as a zip file in the following version:

  * `5.0 <http://www.openerp.com/download/modules/5.0/cci_account.zip>`_
  * `trunk <http://www.openerp.com/download/modules/trunk/cci_account.zip>`_


Dependencies
------------

 * :mod:`account_invoice_layout`
 * :mod:`sale`
 * :mod:`account_analytic_plans`
 * :mod:`l10n_be`
 * :mod:`base_vat`
 * :mod:`cci_partner`
 * :mod:`membership`

Reports
-------

 * Draft Invoices

 * Print VCS

Menus
-------

 * Financial Management/Periodical Processing/Use Models

Views
-----

 * \* INHERIT account.invoice.supplier.form.inherit (form)
 * \* INHERIT account.invoice.form.inherit (form)
 * \* INHERIT account.bank.statement.form (form)
 * \* INHERIT account.invoice.supplier.form (form)
 * \* INHERIT account.invoice.form (form)
 * \* INHERIT account.invoice.supplier.form (form)
 * \* INHERIT account.invoice.form (form)
 * \* INHERIT sale.order.form (form)


Objects
-------

None
