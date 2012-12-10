
.. i18n: .. module:: point_of_sale_extension
.. i18n:     :synopsis: Point Of Sale Extension 
.. i18n:     :noindex:
.. i18n: .. 
..

.. module:: point_of_sale_extension
    :synopsis: Point Of Sale Extension 
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
.. i18n:     <div class="js-kit-rating" title="" permalink="" standalone="yes" path="/point_of_sale_extension"></div>
.. i18n:     <script src="http://js-kit.com/ratings.js"></script>
..

.. raw:: html

    <div class="js-kit-rating" title="" permalink="" standalone="yes" path="/point_of_sale_extension"></div>
    <script src="http://js-kit.com/ratings.js"></script>

.. i18n: Point Of Sale Extension (*point_of_sale_extension*)
.. i18n: ===================================================
.. i18n: :Module: point_of_sale_extension
.. i18n: :Name: Point Of Sale Extension
.. i18n: :Version: 5.0.1.0
.. i18n: :Author: Zikzakmedia SL
.. i18n: :Directory: point_of_sale_extension
.. i18n: :Web: http://www.zikzakmedia.com
.. i18n: :Official module: no
.. i18n: :Quality certified: no
..

Point Of Sale Extension (*point_of_sale_extension*)
===================================================
:Module: point_of_sale_extension
:Name: Point Of Sale Extension
:Version: 5.0.1.0
:Author: Zikzakmedia SL
:Directory: point_of_sale_extension
:Web: http://www.zikzakmedia.com
:Official module: no
:Quality certified: no

.. i18n: Description
.. i18n: -----------
..

Description
-----------

.. i18n: ::
.. i18n: 
.. i18n:   * Only it allows delete draft or cancelled POS orders and POS order lines.
.. i18n:   * If POS order has a partner, the partner is stored in:
.. i18n:       - The stock.picking created by the pos order.
.. i18n:       - The account.move.line created by the pos order.
.. i18n:   * POS orders with amount_total==0 no creates account moves (it gives error).
.. i18n:   * Shows the payment type (journal) in the payments list in the second tab of the POS.
.. i18n:   * The journals used to pay with the POS can be chosen (in the configuration tab of the company: Administration / Users / Companies).
.. i18n:   * Product prices with or without taxes included (select in the configuration tab of the company).
.. i18n:   * Shows a warning in the payment wizard (but you can continue) if:
.. i18n:       - A product added in the POS order has already been requested by the partner (the partner has a sale order with this product), so the user can decide if is better to do a POS order from a sale order.
.. i18n:       - There is not enough virtual stock in any of the products.
.. i18n:     These two warnings can be activated/deactivated (in the configuration tab of the company).
.. i18n:   * List and search POS order lines by number of order, partner and state.
.. i18n:   * If product_visible_discount module is installed and visible discount field in price list is checked, computes discounts in point of sale order lines.
..

::

  * Only it allows delete draft or cancelled POS orders and POS order lines.
  * If POS order has a partner, the partner is stored in:
      - The stock.picking created by the pos order.
      - The account.move.line created by the pos order.
  * POS orders with amount_total==0 no creates account moves (it gives error).
  * Shows the payment type (journal) in the payments list in the second tab of the POS.
  * The journals used to pay with the POS can be chosen (in the configuration tab of the company: Administration / Users / Companies).
  * Product prices with or without taxes included (select in the configuration tab of the company).
  * Shows a warning in the payment wizard (but you can continue) if:
      - A product added in the POS order has already been requested by the partner (the partner has a sale order with this product), so the user can decide if is better to do a POS order from a sale order.
      - There is not enough virtual stock in any of the products.
    These two warnings can be activated/deactivated (in the configuration tab of the company).
  * List and search POS order lines by number of order, partner and state.
  * If product_visible_discount module is installed and visible discount field in price list is checked, computes discounts in point of sale order lines.

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

.. i18n:  * :mod:`point_of_sale`
..

 * :mod:`point_of_sale`

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

.. i18n:  * \* INHERIT res.company.pos.config (form)
.. i18n:  * \* INHERIT pos.order.form.ext1 (form)
.. i18n:  * \* INHERIT pos.order.form.ext2 (form)
.. i18n:  * \* INHERIT pos.order.form.ext3 (form)
.. i18n:  * \* INHERIT pos.order.form.ext4 (form)
.. i18n:  * \* INHERIT pos.order.form.ext5 (form)
.. i18n:  * \* INHERIT pos.order.form.ext6 (form)
.. i18n:  * \* INHERIT pos.order.form.ext7 (form)
.. i18n:  * \* INHERIT pos.order.form.ext8 (form)
.. i18n:  * \* INHERIT Sales ext1 (tree)
.. i18n:  * \* INHERIT Sale lines ext1 (tree)
.. i18n:  * \* INHERIT Sale lines ext2 (tree)
.. i18n:  * \* INHERIT Sale lines ext3 (tree)
..

 * \* INHERIT res.company.pos.config (form)
 * \* INHERIT pos.order.form.ext1 (form)
 * \* INHERIT pos.order.form.ext2 (form)
 * \* INHERIT pos.order.form.ext3 (form)
 * \* INHERIT pos.order.form.ext4 (form)
 * \* INHERIT pos.order.form.ext5 (form)
 * \* INHERIT pos.order.form.ext6 (form)
 * \* INHERIT pos.order.form.ext7 (form)
 * \* INHERIT pos.order.form.ext8 (form)
 * \* INHERIT Sales ext1 (tree)
 * \* INHERIT Sale lines ext1 (tree)
 * \* INHERIT Sale lines ext2 (tree)
 * \* INHERIT Sale lines ext3 (tree)

.. i18n: Objects
.. i18n: -------
..

Objects
-------

.. i18n: Object: Change path to rml file to get a better POS receipt (pos.report.change)
.. i18n: ###############################################################################
..

Object: Change path to rml file to get a better POS receipt (pos.report.change)
###############################################################################
