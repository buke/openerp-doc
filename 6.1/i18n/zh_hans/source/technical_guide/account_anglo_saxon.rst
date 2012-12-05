
.. i18n: .. module:: account_anglo_saxon
.. i18n:     :synopsis: Stock Accounting for Anglo Saxon countries 
.. i18n:     :noindex:
.. i18n: .. 
..

.. module:: account_anglo_saxon
    :synopsis: Stock Accounting for Anglo Saxon countries 
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
.. i18n:     <div class="js-kit-rating" title="" permalink="" standalone="yes" path="/account_anglo_saxon"></div>
.. i18n:     <script src="http://js-kit.com/ratings.js"></script>
..

.. raw:: html

    <div class="js-kit-rating" title="" permalink="" standalone="yes" path="/account_anglo_saxon"></div>
    <script src="http://js-kit.com/ratings.js"></script>

.. i18n: Stock Accounting for Anglo Saxon countries (*account_anglo_saxon*)
.. i18n: ==================================================================
.. i18n: :Module: account_anglo_saxon
.. i18n: :Name: Stock Accounting for Anglo Saxon countries
.. i18n: :Version: 5.0.1.2
.. i18n: :Author: Tiny, Veritos
.. i18n: :Directory: account_anglo_saxon
.. i18n: :Web: http://tinyerp.com - http://veritos.nl
.. i18n: :Official module: no
.. i18n: :Quality certified: no
..

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

.. i18n: Description
.. i18n: -----------
..

Description
-----------

.. i18n: ::
.. i18n: 
.. i18n:   This module will support the Anglo-Saxons accounting methodology by 
.. i18n:       changing the accounting logic with stock transactions. The difference between the Anglo-Saxon accounting countries 
.. i18n:       and the Rhine or also called Continental accounting countries is the moment of taking the Cost of Goods Sold versus Cost of Sales. 
.. i18n:       Anglo-Saxons accounting does take the cost when sales invoice is created, Continental accounting will take the cost at he moment the goods are shipped.
.. i18n:       This module will add this functionality by using a interim account, to store the value of shipped goods and will contra book this interim account 
.. i18n:       when the invoice is created to transfer this amount to the debtor or creditor account.
.. i18n:       Secondly, price differences between actual purchase price and fixed product standard price are booked on a separate account
..

::

  This module will support the Anglo-Saxons accounting methodology by 
      changing the accounting logic with stock transactions. The difference between the Anglo-Saxon accounting countries 
      and the Rhine or also called Continental accounting countries is the moment of taking the Cost of Goods Sold versus Cost of Sales. 
      Anglo-Saxons accounting does take the cost when sales invoice is created, Continental accounting will take the cost at he moment the goods are shipped.
      This module will add this functionality by using a interim account, to store the value of shipped goods and will contra book this interim account 
      when the invoice is created to transfer this amount to the debtor or creditor account.
      Secondly, price differences between actual purchase price and fixed product standard price are booked on a separate account

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

.. i18n:  * :mod:`product`
.. i18n:  * :mod:`account`
.. i18n:  * :mod:`sale`
.. i18n:  * :mod:`purchase`
.. i18n:  * :mod:`stock`
..

 * :mod:`product`
 * :mod:`account`
 * :mod:`sale`
 * :mod:`purchase`
 * :mod:`stock`

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

.. i18n:  * \* INHERIT product.normal.form.inherit.stock (form)
.. i18n:  * \* INHERIT product.template.product.form.inherit (form)
.. i18n:  * \* INHERIT product.category.property.form.inherit.stock (form)
..

 * \* INHERIT product.normal.form.inherit.stock (form)
 * \* INHERIT product.template.product.form.inherit (form)
 * \* INHERIT product.category.property.form.inherit.stock (form)

.. i18n: Objects
.. i18n: -------
..

Objects
-------

.. i18n: None
..

None
