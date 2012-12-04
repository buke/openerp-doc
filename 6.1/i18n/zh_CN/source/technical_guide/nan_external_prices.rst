
.. i18n: .. module:: nan_external_prices
.. i18n:     :synopsis: External Prices 
.. i18n:     :noindex:
.. i18n: .. 
..

.. module:: nan_external_prices
    :synopsis: External Prices 
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
.. i18n:     <div class="js-kit-rating" title="" permalink="" standalone="yes" path="/nan_external_prices"></div>
.. i18n:     <script src="http://js-kit.com/ratings.js"></script>
..

.. raw:: html

    <div class="js-kit-rating" title="" permalink="" standalone="yes" path="/nan_external_prices"></div>
    <script src="http://js-kit.com/ratings.js"></script>

.. i18n: External Prices (*nan_external_prices*)
.. i18n: =======================================
.. i18n: :Module: nan_external_prices
.. i18n: :Name: External Prices
.. i18n: :Version: 5.0.1.0
.. i18n: :Author: NaN
.. i18n: :Directory: nan_external_prices
.. i18n: :Web: http://www.NaN-tic.com
.. i18n: :Official module: no
.. i18n: :Quality certified: no
..

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

.. i18n: Description
.. i18n: -----------
..

Description
-----------

.. i18n: ::
.. i18n: 
.. i18n:   This module adds new fields in sale orders and invoice lines to store untaxed and tax amounts as created by an external application or online shop. This avoids rounding differences between both applications.
.. i18n:   
.. i18n:   A flag in both sale orders and invoices allows the user to decide what values to use the one of the external application or the ones calculated by OpenERP.
..

::

  This module adds new fields in sale orders and invoice lines to store untaxed and tax amounts as created by an external application or online shop. This avoids rounding differences between both applications.
  
  A flag in both sale orders and invoices allows the user to decide what values to use the one of the external application or the ones calculated by OpenERP.

.. i18n: Download links
.. i18n: --------------
..

Download links
--------------

.. i18n: You can download this module as a zip file in the following version:
..

You can download this module as a zip file in the following version:

.. i18n: (No download links available)
..

(No download links available)

.. i18n: Dependencies
.. i18n: ------------
..

Dependencies
------------

.. i18n:  * :mod:`sale`
.. i18n:  * :mod:`account`
.. i18n:  * :mod:`account_tax_include`
..

 * :mod:`sale`
 * :mod:`account`
 * :mod:`account_tax_include`

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

.. i18n:  * \* INHERIT account.invoice.form.use_external_prices (form)
.. i18n:  * \* INHERIT account.invoice.line.form.external_prices (form)
.. i18n:  * \* INHERIT sale.order.form.use_external_prices (form)
.. i18n:  * \* INHERIT sale.order.form.external_prices (form)
..

 * \* INHERIT account.invoice.form.use_external_prices (form)
 * \* INHERIT account.invoice.line.form.external_prices (form)
 * \* INHERIT sale.order.form.use_external_prices (form)
 * \* INHERIT sale.order.form.external_prices (form)

.. i18n: Objects
.. i18n: -------
..

Objects
-------

.. i18n: None
..

None
