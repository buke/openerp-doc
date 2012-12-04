
.. module:: nan_external_prices
    :synopsis: External Prices 
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

    <div class="js-kit-rating" title="" permalink="" standalone="yes" path="/nan_external_prices"></div>
    <script src="http://js-kit.com/ratings.js"></script>

External Prices (*nan_external_prices*)
=======================================
:Module: nan_external_prices
:Name: External Prices
:Version: 5.0.1.0
:Author: NaN
:Directory: nan_external_prices
:Web: http://www.NaN-tic.com
:Official module: no
:Quality certified: no

Description
-----------

::

  This module adds new fields in sale orders and invoice lines to store untaxed and tax amounts as created by an external application or online shop. This avoids rounding differences between both applications.
  
  A flag in both sale orders and invoices allows the user to decide what values to use the one of the external application or the ones calculated by OpenERP.

Download links
--------------

You can download this module as a zip file in the following version:

(No download links available)


Dependencies
------------

 * :mod:`sale`
 * :mod:`account`
 * :mod:`account_tax_include`

Reports
-------

None


Menus
-------


None


Views
-----

 * \* INHERIT account.invoice.form.use_external_prices (form)
 * \* INHERIT account.invoice.line.form.external_prices (form)
 * \* INHERIT sale.order.form.use_external_prices (form)
 * \* INHERIT sale.order.form.external_prices (form)


Objects
-------

None
