
.. module:: account_anglo_saxon
    :synopsis: Stock Accounting for Anglo Saxon countries 
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

    <div class="js-kit-rating" title="" permalink="" standalone="yes" path="/account_anglo_saxon"></div>
    <script src="http://js-kit.com/ratings.js"></script>

Stock Accounting for Anglo Saxon countries (*account_anglo_saxon*)
==================================================================
:Module: account_anglo_saxon
:Name: Stock Accounting for Anglo Saxon countries
:Version: 5.0.1.2
:Author: Tiny, Veritos
:Directory: account_anglo_saxon
:Web: http://tinyerp.com - http://veritos.nl
:Official module: no
:Quality certified: no

Description
-----------

::

  This module will support the Anglo-Saxons accounting methodology by 
      changing the accounting logic with stock transactions. The difference between the Anglo-Saxon accounting countries 
      and the Rhine or also called Continental accounting countries is the moment of taking the Cost of Goods Sold versus Cost of Sales. 
      Anglo-Saxons accounting does take the cost when sales invoice is created, Continental accounting will take the cost at he moment the goods are shipped.
      This module will add this functionality by using a interim account, to store the value of shipped goods and will contra book this interim account 
      when the invoice is created to transfer this amount to the debtor or creditor account.
      Secondly, price differences between actual purchase price and fixed product standard price are booked on a separate account

Download links
--------------

You can download this module as a zip file in the following version:

(No download links available)


Dependencies
------------

 * :mod:`product`
 * :mod:`account`
 * :mod:`sale`
 * :mod:`purchase`
 * :mod:`stock`

Reports
-------

None


Menus
-------


None


Views
-----

 * \* INHERIT product.normal.form.inherit.stock (form)
 * \* INHERIT product.template.product.form.inherit (form)
 * \* INHERIT product.category.property.form.inherit.stock (form)


Objects
-------

None
