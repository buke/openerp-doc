
.. i18n: .. module:: delivery
.. i18n:     :synopsis: Carriers and deliveries (Official, Quality Certified)
.. i18n:     :noindex:
.. i18n: .. 
..

.. module:: delivery
    :synopsis: Carriers and deliveries (Official, Quality Certified)
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
.. i18n:     <div class="js-kit-rating" title="" permalink="" standalone="yes" path="/delivery"></div>
.. i18n:     <script src="http://js-kit.com/ratings.js"></script>
..

.. raw:: html

    <div class="js-kit-rating" title="" permalink="" standalone="yes" path="/delivery"></div>
    <script src="http://js-kit.com/ratings.js"></script>

.. i18n: Carriers and deliveries (*delivery*)
.. i18n: ====================================
.. i18n: :Module: delivery
.. i18n: :Name: Carriers and deliveries
.. i18n: :Version: 5.0.1.0
.. i18n: :Author: Tiny
.. i18n: :Directory: delivery
.. i18n: :Web: 
.. i18n: :Official module: yes
.. i18n: :Quality certified: yes
..

Carriers and deliveries (*delivery*)
====================================
:Module: delivery
:Name: Carriers and deliveries
:Version: 5.0.1.0
:Author: Tiny
:Directory: delivery
:Web: 
:Official module: yes
:Quality certified: yes

.. i18n: Description
.. i18n: -----------
..

Description
-----------

.. i18n: ::
.. i18n: 
.. i18n:   Allows you to add delivery methods in sales orders and packing. You can define your own carrier and delivery grids for prices. When creating invoices from picking, OpenERP is able to add and compute the shipping line.
..

::

  Allows you to add delivery methods in sales orders and packing. You can define your own carrier and delivery grids for prices. When creating invoices from picking, OpenERP is able to add and compute the shipping line.

.. i18n: Download links
.. i18n: --------------
..

Download links
--------------

.. i18n: You can download this module as a zip file in the following version:
..

You can download this module as a zip file in the following version:

.. i18n:   * `4.2 <http://www.openerp.com/download/modules/4.2/delivery.zip>`_
.. i18n:   * `5.0 <http://www.openerp.com/download/modules/5.0/delivery.zip>`_
.. i18n:   * `trunk <http://www.openerp.com/download/modules/trunk/delivery.zip>`_
..

  * `4.2 <http://www.openerp.com/download/modules/4.2/delivery.zip>`_
  * `5.0 <http://www.openerp.com/download/modules/5.0/delivery.zip>`_
  * `trunk <http://www.openerp.com/download/modules/trunk/delivery.zip>`_

.. i18n: Dependencies
.. i18n: ------------
..

Dependencies
------------

.. i18n:  * :mod:`sale`
.. i18n:  * :mod:`purchase`
.. i18n:  * :mod:`stock`
..

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

.. i18n:  * Stock Management/Configuration/Delivery
.. i18n:  * Stock Management/Configuration/Delivery/Delivery Method
.. i18n:  * Stock Management/Configuration/Delivery/Delivery Pricelist
.. i18n:  * Stock Management/Outgoing Products/Packing to be invoiced
.. i18n:  * Stock Management/Incoming Products/Generate Draft Invoices On Receptions
..

 * Stock Management/Configuration/Delivery
 * Stock Management/Configuration/Delivery/Delivery Method
 * Stock Management/Configuration/Delivery/Delivery Pricelist
 * Stock Management/Outgoing Products/Packing to be invoiced
 * Stock Management/Incoming Products/Generate Draft Invoices On Receptions

.. i18n: Views
.. i18n: -----
..

Views
-----

.. i18n:  * delivery.carrier.tree (tree)
.. i18n:  * delivery.carrier.form (form)
.. i18n:  * delivery.grid.tree (tree)
.. i18n:  * delivery.grid.form (form)
.. i18n:  * delivery.grid.line.form (form)
.. i18n:  * delivery.grid.line.tree (tree)
.. i18n:  * \* INHERIT delivery.sale.order_withcarrier.form.view (form)
.. i18n:  * \* INHERIT delivery.stock.picking_withcarrier.out.form.view (form)
.. i18n:  * \* INHERIT stock.picking_withweight.in.form.view (form)
.. i18n:  * \* INHERIT stock.picking_withweight.internal.form.view (form)
.. i18n:  * \* INHERIT delivery.stock.picking_withcarrier.delivery.form.view (form)
.. i18n:  * \* INHERIT res.partner.carrier.property.form.inherit (form)
..

 * delivery.carrier.tree (tree)
 * delivery.carrier.form (form)
 * delivery.grid.tree (tree)
 * delivery.grid.form (form)
 * delivery.grid.line.form (form)
 * delivery.grid.line.tree (tree)
 * \* INHERIT delivery.sale.order_withcarrier.form.view (form)
 * \* INHERIT delivery.stock.picking_withcarrier.out.form.view (form)
 * \* INHERIT stock.picking_withweight.in.form.view (form)
 * \* INHERIT stock.picking_withweight.internal.form.view (form)
 * \* INHERIT delivery.stock.picking_withcarrier.delivery.form.view (form)
 * \* INHERIT res.partner.carrier.property.form.inherit (form)

.. i18n: Objects
.. i18n: -------
..

Objects
-------

.. i18n: Object: Carrier and delivery grids (delivery.carrier)
.. i18n: #####################################################
..

Object: Carrier and delivery grids (delivery.carrier)
#####################################################

.. i18n: :product_id: Delivery Product, many2one, required
..

:product_id: Delivery Product, many2one, required

.. i18n: :price: Price, float, readonly
..

:price: Price, float, readonly

.. i18n: :grids_id: Delivery Grids, one2many
..

:grids_id: Delivery Grids, one2many

.. i18n: :active: Active, boolean
..

:active: Active, boolean

.. i18n: :partner_id: Carrier Partner, many2one, required
..

:partner_id: Carrier Partner, many2one, required

.. i18n: :name: Carrier, char, required
..

:name: Carrier, char, required

.. i18n: Object: Delivery Grid (delivery.grid)
.. i18n: #####################################
..

Object: Delivery Grid (delivery.grid)
#####################################

.. i18n: :name: Grid Name, char, required
..

:name: Grid Name, char, required

.. i18n: :sequence: Sequence, integer, required
..

:sequence: Sequence, integer, required

.. i18n: :state_ids: States, many2many
..

:state_ids: States, many2many

.. i18n: :country_ids: Countries, many2many
..

:country_ids: Countries, many2many

.. i18n: :carrier_id: Carrier, many2one, required
..

:carrier_id: Carrier, many2one, required

.. i18n: :active: Active, boolean
..

:active: Active, boolean

.. i18n: :zip_from: Start Zip, char
..

:zip_from: Start Zip, char

.. i18n: :line_ids: Grid Line, one2many
..

:line_ids: Grid Line, one2many

.. i18n: :zip_to: To Zip, char
..

:zip_to: To Zip, char

.. i18n: Object: Delivery line of grid (delivery.grid.line)
.. i18n: ##################################################
..

Object: Delivery line of grid (delivery.grid.line)
##################################################

.. i18n: :list_price: Sale Price, float, required
..

:list_price: Sale Price, float, required

.. i18n: :name: Name, char, required
..

:name: Name, char, required

.. i18n: :price_type: Price Type, selection, required
..

:price_type: Price Type, selection, required

.. i18n: :max_value: Maximum Value, float, required
..

:max_value: Maximum Value, float, required

.. i18n: :standard_price: Cost Price, float, required
..

:standard_price: Cost Price, float, required

.. i18n: :grid_id: Grid, many2one, required
..

:grid_id: Grid, many2one, required

.. i18n: :variable_factor: Variable Factor, selection, required
..

:variable_factor: Variable Factor, selection, required

.. i18n: :operator: Operator, selection, required
..

:operator: Operator, selection, required

.. i18n: :type: Variable, selection, required
..

:type: Variable, selection, required
