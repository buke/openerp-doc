
.. i18n: .. module:: product_visible_discount
.. i18n:     :synopsis: Visible Discount 
.. i18n:     :noindex:
.. i18n: .. 
..

.. module:: product_visible_discount
    :synopsis: Visible Discount 
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
.. i18n:     <div class="js-kit-rating" title="" permalink="" standalone="yes" path="/product_visible_discount"></div>
.. i18n:     <script src="http://js-kit.com/ratings.js"></script>
..

.. raw:: html

    <div class="js-kit-rating" title="" permalink="" standalone="yes" path="/product_visible_discount"></div>
    <script src="http://js-kit.com/ratings.js"></script>

.. i18n: Visible Discount (*product_visible_discount*)
.. i18n: =============================================
.. i18n: :Module: product_visible_discount
.. i18n: :Name: Visible Discount
.. i18n: :Version: 5.0.1.0
.. i18n: :Author: Tiny
.. i18n: :Directory: product_visible_discount
.. i18n: :Web: 
.. i18n: :Official module: no
.. i18n: :Quality certified: no
..

Visible Discount (*product_visible_discount*)
=============================================
:Module: product_visible_discount
:Name: Visible Discount
:Version: 5.0.1.0
:Author: Tiny
:Directory: product_visible_discount
:Web: 
:Official module: no
:Quality certified: no

.. i18n: Description
.. i18n: -----------
..

Description
-----------

.. i18n: ::
.. i18n: 
.. i18n:   This module lets you calculate discounts on Sale Order lines and Invoice lines base on the partner's pricelist.
.. i18n:       To this end, a new check box named "Visible Discount" is added to the pricelist form.
.. i18n:       Example:
.. i18n:           For the product PC1 and the partner "Asustek": if listprice=450, and the price calculated using Asustek's pricelist is 225
.. i18n:           If the check box is checked, we will have on the sale order line: Unit price=450, Discount=50,00, Net price=225
.. i18n:           If the check box is unchecked, we will have on Sale Order and Invoice lines: Unit price=225, Discount=0,00, Net price=225
..

::

  This module lets you calculate discounts on Sale Order lines and Invoice lines base on the partner's pricelist.
      To this end, a new check box named "Visible Discount" is added to the pricelist form.
      Example:
          For the product PC1 and the partner "Asustek": if listprice=450, and the price calculated using Asustek's pricelist is 225
          If the check box is checked, we will have on the sale order line: Unit price=450, Discount=50,00, Net price=225
          If the check box is unchecked, we will have on Sale Order and Invoice lines: Unit price=225, Discount=0,00, Net price=225

.. i18n: Download links
.. i18n: --------------
..

Download links
--------------

.. i18n: You can download this module as a zip file in the following version:
..

You can download this module as a zip file in the following version:

.. i18n:   * `5.0 <http://www.openerp.com/download/modules/5.0/product_visible_discount.zip>`_
.. i18n:   * `trunk <http://www.openerp.com/download/modules/trunk/product_visible_discount.zip>`_
..

  * `5.0 <http://www.openerp.com/download/modules/5.0/product_visible_discount.zip>`_
  * `trunk <http://www.openerp.com/download/modules/trunk/product_visible_discount.zip>`_

.. i18n: Dependencies
.. i18n: ------------
..

Dependencies
------------

.. i18n:  * :mod:`base`
.. i18n:  * :mod:`product`
.. i18n:  * :mod:`account`
.. i18n:  * :mod:`sale`
..

 * :mod:`base`
 * :mod:`product`
 * :mod:`account`
 * :mod:`sale`

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

.. i18n:  * \* INHERIT product.pricelist.tree (form)
.. i18n:  * \* INHERIT product.pricelist.form (form)
..

 * \* INHERIT product.pricelist.tree (form)
 * \* INHERIT product.pricelist.form (form)

.. i18n: Objects
.. i18n: -------
..

Objects
-------

.. i18n: None
..

None
