
.. i18n: .. module:: stock
.. i18n:     :synopsis: Stock Management (Official, Quality Certified)
.. i18n:     :noindex:
.. i18n: .. 
..

.. module:: stock
    :synopsis: Stock Management (Official, Quality Certified)
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
.. i18n:     <div class="js-kit-rating" title="" permalink="" standalone="yes" path="/stock"></div>
.. i18n:     <script src="http://js-kit.com/ratings.js"></script>
..

.. raw:: html

    <div class="js-kit-rating" title="" permalink="" standalone="yes" path="/stock"></div>
    <script src="http://js-kit.com/ratings.js"></script>

.. i18n: Stock Management (*stock*)
.. i18n: ==========================
.. i18n: :Module: stock
.. i18n: :Name: Stock Management
.. i18n: :Version: 5.0.1.1
.. i18n: :Author: Tiny
.. i18n: :Directory: stock
.. i18n: :Web: http://www.openerp.com
.. i18n: :Official module: yes
.. i18n: :Quality certified: yes
..

Stock Management (*stock*)
==========================
:Module: stock
:Name: Stock Management
:Version: 5.0.1.1
:Author: Tiny
:Directory: stock
:Web: http://www.openerp.com
:Official module: yes
:Quality certified: yes

.. i18n: Description
.. i18n: -----------
..

Description
-----------

.. i18n: ::
.. i18n: 
.. i18n:   OpenERP Stock Management module can manage multi-warehouses, multi and structured stock locations.
.. i18n:   Thanks to the double entry management, the inventory controlling is powerful and flexible:
.. i18n:   * Moves history and planning,
.. i18n:   * Different inventory methods (FIFO, LIFO, ...)
.. i18n:   * Stock valuation (standard or average price, ...)
.. i18n:   * Robustness faced with Inventory differences
.. i18n:   * Automatic reordering rules (stock level, JIT, ...)
.. i18n:   * Bar code supported
.. i18n:   * Rapid detection of mistakes through double entry system
.. i18n:   * Traceability (upstream/downstream, production lots, serial number, ...)
..

::

  OpenERP Stock Management module can manage multi-warehouses, multi and structured stock locations.
  Thanks to the double entry management, the inventory controlling is powerful and flexible:
  * Moves history and planning,
  * Different inventory methods (FIFO, LIFO, ...)
  * Stock valuation (standard or average price, ...)
  * Robustness faced with Inventory differences
  * Automatic reordering rules (stock level, JIT, ...)
  * Bar code supported
  * Rapid detection of mistakes through double entry system
  * Traceability (upstream/downstream, production lots, serial number, ...)

.. i18n: Download links
.. i18n: --------------
..

Download links
--------------

.. i18n: You can download this module as a zip file in the following version:
..

You can download this module as a zip file in the following version:

.. i18n:   * `4.2 <http://www.openerp.com/download/modules/4.2/stock.zip>`_
.. i18n:   * `5.0 <http://www.openerp.com/download/modules/5.0/stock.zip>`_
.. i18n:   * `trunk <http://www.openerp.com/download/modules/trunk/stock.zip>`_
..

  * `4.2 <http://www.openerp.com/download/modules/4.2/stock.zip>`_
  * `5.0 <http://www.openerp.com/download/modules/5.0/stock.zip>`_
  * `trunk <http://www.openerp.com/download/modules/trunk/stock.zip>`_

.. i18n: Dependencies
.. i18n: ------------
..

Dependencies
------------

.. i18n:  * :mod:`product`
.. i18n:  * :mod:`account`
..

 * :mod:`product`
 * :mod:`account`

.. i18n: Reports
.. i18n: -------
..

Reports
-------

.. i18n:  * Future Stock Forecast
.. i18n: 
.. i18n:  * Packing list
.. i18n: 
.. i18n:  * Print Item Labels
.. i18n: 
.. i18n:  * Location Overview
.. i18n: 
.. i18n:  * Lots by location
.. i18n: 
.. i18n:  * Location Content (With children)
..

 * Future Stock Forecast

 * Packing list

 * Print Item Labels

 * Location Overview

 * Lots by location

 * Location Content (With children)

.. i18n: Menus
.. i18n: -------
..

Menus
-------

.. i18n:  * Stock Management
.. i18n:  * Stock Management/Configuration
.. i18n:  * Stock Management/Periodical Inventory
.. i18n:  * Stock Management/Periodical Inventory/Draft Periodical Inventories
.. i18n:  * Stock Management/Periodical Inventory/New Periodical Inventory
.. i18n:  * Stock Management/Traceability
.. i18n:  * Stock Management/Traceability/Tracking Lots
.. i18n:  * Stock Management/Traceability/Production Lots
.. i18n:  * Stock Management/Configuration/Locations
.. i18n:  * Stock Management/Stock Locations Structure
.. i18n:  * Stock Management/Configuration/Warehouses
.. i18n:  * Stock Management/Delivery Orders
.. i18n:  * Stock Management/Delivery Orders/Delivery Orders to Process
.. i18n:  * Stock Management/Delivery Orders/Future Delivery Orders
.. i18n:  * Stock Management/Delivery Orders/Calendar of Deliveries
.. i18n:  * Stock Management/Outgoing Products
.. i18n:  * Stock Management/Outgoing Products/Available Packing
.. i18n:  * Stock Management/Outgoing Products/Confirmed Packing Waiting Availability
.. i18n:  * Stock Management/Incoming Products
.. i18n:  * Stock Management/Incoming Products/Packing to Process
.. i18n:  * Stock Management/Incoming Products/New Reception Packing
.. i18n:  * Stock Management/Internal Moves
.. i18n:  * Stock Management/Internal Moves/Available Packing
.. i18n:  * Stock Management/Internal Moves/Confirmed Packing Waiting Availability
.. i18n:  * Stock Management/Internal Moves/New Internal Packing
.. i18n:  * Stock Management/Traceability/Low Level
.. i18n:  * Stock Management/Traceability/Low Level/Stock Moves
.. i18n:  * Stock Management/Traceability/Low Level/Stock Moves/Draft Moves
.. i18n:  * Stock Management/Traceability/Low Level/Stock Moves/Available Moves
.. i18n:  * Stock Management/Traceability/Low Level/Packing
.. i18n:  * Stock Management/Configuration/Incoterms
.. i18n:  * Stock Management/Reporting
.. i18n:  * Stock Management/Reporting/Traceability
.. i18n:  * Stock Management/Reporting/Traceability/Stock by Lots
.. i18n:  * Stock Management/Reporting/Dates of Inventories
.. i18n:  * Stock Management/Reporting/Locations' Values
..

 * Stock Management
 * Stock Management/Configuration
 * Stock Management/Periodical Inventory
 * Stock Management/Periodical Inventory/Draft Periodical Inventories
 * Stock Management/Periodical Inventory/New Periodical Inventory
 * Stock Management/Traceability
 * Stock Management/Traceability/Tracking Lots
 * Stock Management/Traceability/Production Lots
 * Stock Management/Configuration/Locations
 * Stock Management/Stock Locations Structure
 * Stock Management/Configuration/Warehouses
 * Stock Management/Delivery Orders
 * Stock Management/Delivery Orders/Delivery Orders to Process
 * Stock Management/Delivery Orders/Future Delivery Orders
 * Stock Management/Delivery Orders/Calendar of Deliveries
 * Stock Management/Outgoing Products
 * Stock Management/Outgoing Products/Available Packing
 * Stock Management/Outgoing Products/Confirmed Packing Waiting Availability
 * Stock Management/Incoming Products
 * Stock Management/Incoming Products/Packing to Process
 * Stock Management/Incoming Products/New Reception Packing
 * Stock Management/Internal Moves
 * Stock Management/Internal Moves/Available Packing
 * Stock Management/Internal Moves/Confirmed Packing Waiting Availability
 * Stock Management/Internal Moves/New Internal Packing
 * Stock Management/Traceability/Low Level
 * Stock Management/Traceability/Low Level/Stock Moves
 * Stock Management/Traceability/Low Level/Stock Moves/Draft Moves
 * Stock Management/Traceability/Low Level/Stock Moves/Available Moves
 * Stock Management/Traceability/Low Level/Packing
 * Stock Management/Configuration/Incoterms
 * Stock Management/Reporting
 * Stock Management/Reporting/Traceability
 * Stock Management/Reporting/Traceability/Stock by Lots
 * Stock Management/Reporting/Dates of Inventories
 * Stock Management/Reporting/Locations' Values

.. i18n: Views
.. i18n: -----
..

Views
-----

.. i18n:  * stock.inventory.line.tree (tree)
.. i18n:  * stock.inventory.line.form (form)
.. i18n:  * stock.inventory.tree (tree)
.. i18n:  * stock.inventory.form (form)
.. i18n:  * stock.tracking.form (form)
.. i18n:  * stock.tracking.tree (tree)
.. i18n:  * stock.tracking.tree (tree)
.. i18n:  * stock.production.lot.revision.form (form)
.. i18n:  * stock.production.lot.revision.tree (tree)
.. i18n:  * stock.production.lot.form (form)
.. i18n:  * stock.production.lot.tree (tree)
.. i18n:  * Stock Moves (tree)
.. i18n:  * Stock Moves (tree)
.. i18n:  * stock.location.form (form)
.. i18n:  * stock.location.tree (tree)
.. i18n:  * stock.location.tree (tree)
.. i18n:  * stock.warehouse (form)
.. i18n:  * stock.warehouse.tree (tree)
.. i18n:  * stock.picking.move.wizard.form (form)
.. i18n:  * stock.picking.calendar (calendar)
.. i18n:  * stock.picking.tree (tree)
.. i18n:  * stock.picking.form (form)
.. i18n:  * stock.picking.delivery.tree (tree)
.. i18n:  * stock.picking.delivery.form (form)
.. i18n:  * stock.picking.out.tree (tree)
.. i18n:  * stock.picking.out.form (form)
.. i18n:  * stock.picking.in.tree (tree)
.. i18n:  * stock.picking.in.form (form)
.. i18n:  * stock.move.tree (tree)
.. i18n:  * stock.move.form (form)
.. i18n:  * stock.incoterms.tree (tree)
.. i18n:  * stock.incoterms.form (form)
.. i18n:  * \* INHERIT product.category.stock.property.form.inherit (form)
.. i18n:  * \* INHERIT product.template.stock.property.form.inherit (form)
.. i18n:  * \* INHERIT product.normal.stock.acc.property.form.inherit (form)
.. i18n:  * \* INHERIT product.normal.stock.form.inherit (form)
.. i18n:  * \* INHERIT product.normal.stock.property.form.inherit (form)
.. i18n:  * \* INHERIT res.partner.stock.property.form.inherit (form)
.. i18n:  * stock.report.prodlots.view (tree)
.. i18n:  * report.stock.lines.date.tree (tree)
.. i18n:  * report.stock.lines.date.form (form)
.. i18n:  * stock.location.tree (tree)
..

 * stock.inventory.line.tree (tree)
 * stock.inventory.line.form (form)
 * stock.inventory.tree (tree)
 * stock.inventory.form (form)
 * stock.tracking.form (form)
 * stock.tracking.tree (tree)
 * stock.tracking.tree (tree)
 * stock.production.lot.revision.form (form)
 * stock.production.lot.revision.tree (tree)
 * stock.production.lot.form (form)
 * stock.production.lot.tree (tree)
 * Stock Moves (tree)
 * Stock Moves (tree)
 * stock.location.form (form)
 * stock.location.tree (tree)
 * stock.location.tree (tree)
 * stock.warehouse (form)
 * stock.warehouse.tree (tree)
 * stock.picking.move.wizard.form (form)
 * stock.picking.calendar (calendar)
 * stock.picking.tree (tree)
 * stock.picking.form (form)
 * stock.picking.delivery.tree (tree)
 * stock.picking.delivery.form (form)
 * stock.picking.out.tree (tree)
 * stock.picking.out.form (form)
 * stock.picking.in.tree (tree)
 * stock.picking.in.form (form)
 * stock.move.tree (tree)
 * stock.move.form (form)
 * stock.incoterms.tree (tree)
 * stock.incoterms.form (form)
 * \* INHERIT product.category.stock.property.form.inherit (form)
 * \* INHERIT product.template.stock.property.form.inherit (form)
 * \* INHERIT product.normal.stock.acc.property.form.inherit (form)
 * \* INHERIT product.normal.stock.form.inherit (form)
 * \* INHERIT product.normal.stock.property.form.inherit (form)
 * \* INHERIT res.partner.stock.property.form.inherit (form)
 * stock.report.prodlots.view (tree)
 * report.stock.lines.date.tree (tree)
 * report.stock.lines.date.form (form)
 * stock.location.tree (tree)

.. i18n: Objects
.. i18n: -------
..

Objects
-------

.. i18n: Object: Incoterms (stock.incoterms)
.. i18n: ###################################
..

Object: Incoterms (stock.incoterms)
###################################

.. i18n: :active: Active, boolean
..

:active: Active, boolean

.. i18n: :code: Code, char, required
..

:code: Code, char, required

.. i18n: :name: Name, char, required
..

:name: Name, char, required

.. i18n: Object: Location (stock.location)
.. i18n: #################################
..

Object: Location (stock.location)
#################################

.. i18n: :comment: Additional Information, text
..

:comment: Additional Information, text

.. i18n: :address_id: Location Address, many2one
..

:address_id: Location Address, many2one

.. i18n: :stock_virtual_value: Virtual Stock Value, float, readonly
..

:stock_virtual_value: Virtual Stock Value, float, readonly

.. i18n: :allocation_method: Allocation Method, selection, required
..

:allocation_method: Allocation Method, selection, required

.. i18n: :location_id: Parent Location, many2one
..

:location_id: Parent Location, many2one

.. i18n: :chained_location_id: Chained Location If Fixed, many2one
..

:chained_location_id: Chained Location If Fixed, many2one

.. i18n: :complete_name: Location Name, char, readonly
..

:complete_name: Location Name, char, readonly

.. i18n: :usage: Location Type, selection, required
..

:usage: Location Type, selection, required

.. i18n: :stock_real_value: Real Stock Value, float, readonly
..

:stock_real_value: Real Stock Value, float, readonly

.. i18n: :chained_location_type: Chained Location Type, selection, required
..

:chained_location_type: Chained Location Type, selection, required

.. i18n: :account_id: Inventory Account, many2one
..

:account_id: Inventory Account, many2one

.. i18n: :child_ids: Contains, one2many
..

:child_ids: Contains, one2many

.. i18n: :chained_delay: Chained Delay (days), integer
..

:chained_delay: Chained Delay (days), integer

.. i18n: :stock_virtual: Virtual Stock, float, readonly
..

:stock_virtual: Virtual Stock, float, readonly

.. i18n: :posz: Height (Z), integer
..

:posz: Height (Z), integer

.. i18n: :posx: Corridor (X), integer
..

:posx: Corridor (X), integer

.. i18n: :posy: Shelves (Y), integer
..

:posy: Shelves (Y), integer

.. i18n: :active: Active, boolean
..

:active: Active, boolean

.. i18n: :icon: Icon, selection
..

:icon: Icon, selection

.. i18n: :parent_right: Right Parent, integer
..

:parent_right: Right Parent, integer

.. i18n: :name: Location Name, char, required
..

:name: Location Name, char, required

.. i18n: :chained_auto_packing: Automatic Move, selection, required
..

:chained_auto_packing: Automatic Move, selection, required

.. i18n:     *This is used only if you selected a chained location type.
.. i18n:     The 'Automatic Move' value will create a stock move after the current one that will be validated automatically. With 'Manual Operation', the stock move has to be validated by a worker. With 'Automatic No Step Added', the location is replaced in the original move.*
..

    *This is used only if you selected a chained location type.
    The 'Automatic Move' value will create a stock move after the current one that will be validated automatically. With 'Manual Operation', the stock move has to be validated by a worker. With 'Automatic No Step Added', the location is replaced in the original move.*

.. i18n: :parent_left: Left Parent, integer
..

:parent_left: Left Parent, integer

.. i18n: :stock_real: Real Stock, float, readonly
..

:stock_real: Real Stock, float, readonly

.. i18n: Object: Stock Tracking Lots (stock.tracking)
.. i18n: ############################################
..

Object: Stock Tracking Lots (stock.tracking)
############################################

.. i18n: :active: Active, boolean
..

:active: Active, boolean

.. i18n: :move_ids: Moves Tracked, one2many
..

:move_ids: Moves Tracked, one2many

.. i18n: :serial: Reference, char
..

:serial: Reference, char

.. i18n: :date: Date Created, datetime, required
..

:date: Date Created, datetime, required

.. i18n: :name: Tracking, char, required
..

:name: Tracking, char, required

.. i18n: Object: Packing List (stock.picking)
.. i18n: ####################################
..

Object: Packing List (stock.picking)
####################################

.. i18n: :origin: Origin Reference, char
..

:origin: Origin Reference, char

.. i18n: :address_id: Partner, many2one
..

:address_id: Partner, many2one

.. i18n: :type: Shipping Type, selection, required
..

:type: Shipping Type, selection, required

.. i18n: :move_lines: Move lines, one2many
..

:move_lines: Move lines, one2many

.. i18n: :date_done: Date Done, datetime
..

:date_done: Date Done, datetime

.. i18n: :name: Reference, char
..

:name: Reference, char

.. i18n: :move_type: Delivery Method, selection, required
..

:move_type: Delivery Method, selection, required

.. i18n: :invoice_state: Invoice Status, selection, required, readonly
..

:invoice_state: Invoice Status, selection, required, readonly

.. i18n: :min_date: Planned Date, datetime
..

:min_date: Planned Date, datetime

.. i18n: :note: Notes, text
..

:note: Notes, text

.. i18n: :date: Date Order, datetime
..

:date: Date Order, datetime

.. i18n: :state: Status, selection, readonly
..

:state: Status, selection, readonly

.. i18n: :location_dest_id: Dest. Location, many2one
..

:location_dest_id: Dest. Location, many2one

.. i18n: :max_date: Max. Planned Date, datetime
..

:max_date: Max. Planned Date, datetime

.. i18n: :auto_picking: Auto-Packing, boolean
..

:auto_picking: Auto-Packing, boolean

.. i18n: :active: Active, boolean
..

:active: Active, boolean

.. i18n: :location_id: Location, many2one
..

:location_id: Location, many2one

.. i18n: :backorder_id: Back Order, many2one
..

:backorder_id: Back Order, many2one

.. i18n: Object: Production lot (stock.production.lot)
.. i18n: #############################################
..

Object: Production lot (stock.production.lot)
#############################################

.. i18n: :stock_available: Available, float, readonly
..

:stock_available: Available, float, readonly

.. i18n: :product_id: Product, many2one, required
..

:product_id: Product, many2one, required

.. i18n: :date: Created Date, datetime, required
..

:date: Created Date, datetime, required

.. i18n: :revisions: Revisions, one2many
..

:revisions: Revisions, one2many

.. i18n: :ref: Internal Ref, char
..

:ref: Internal Ref, char

.. i18n: :name: Serial, char, required
..

:name: Serial, char, required

.. i18n: Object: Production lot revisions (stock.production.lot.revision)
.. i18n: ################################################################
..

Object: Production lot revisions (stock.production.lot.revision)
################################################################

.. i18n: :indice: Revision, char
..

:indice: Revision, char

.. i18n: :name: Revision Name, char, required
..

:name: Revision Name, char, required

.. i18n: :date: Revision Date, date
..

:date: Revision Date, date

.. i18n: :lot_id: Production lot, many2one
..

:lot_id: Production lot, many2one

.. i18n: :author_id: Author, many2one
..

:author_id: Author, many2one

.. i18n: :description: Description, text
..

:description: Description, text

.. i18n: Object: Stock Move (stock.move)
.. i18n: ###############################
..

Object: Stock Move (stock.move)
###############################

.. i18n: :product_uos_qty: Quantity (UOS), float
..

:product_uos_qty: Quantity (UOS), float

.. i18n: :address_id: Dest. Address, many2one
..

:address_id: Dest. Address, many2one

.. i18n: :product_uom: Product UOM, many2one, required
..

:product_uom: Product UOM, many2one, required

.. i18n: :price_unit: Unit Price, float
..

:price_unit: Unit Price, float

.. i18n: :product_qty: Quantity, float, required
..

:product_qty: Quantity, float, required

.. i18n: :product_uos: Product UOS, many2one
..

:product_uos: Product UOS, many2one

.. i18n: :location_id: Source Location, many2one, required
..

:location_id: Source Location, many2one, required

.. i18n: :priority: Priority, selection
..

:priority: Priority, selection

.. i18n: :auto_validate: Auto Validate, boolean
..

:auto_validate: Auto Validate, boolean

.. i18n: :note: Notes, text
..

:note: Notes, text

.. i18n: :state: Status, selection, readonly
..

:state: Status, selection, readonly

.. i18n: :product_packaging: Packaging, many2one
..

:product_packaging: Packaging, many2one

.. i18n: :move_history_ids: Move History, many2many
..

:move_history_ids: Move History, many2many

.. i18n: :prodlot_id: Production Lot, many2one
..

:prodlot_id: Production Lot, many2one

.. i18n:     *Production lot is used to put a serial number on the production*
..

    *Production lot is used to put a serial number on the production*

.. i18n: :move_dest_id: Dest. Move, many2one
..

:move_dest_id: Dest. Move, many2one

.. i18n: :date: Date Created, datetime
..

:date: Date Created, datetime

.. i18n: :product_id: Product, many2one, required
..

:product_id: Product, many2one, required

.. i18n: :move_history_ids2: Move History, many2many
..

:move_history_ids2: Move History, many2many

.. i18n: :name: Name, char, required
..

:name: Name, char, required

.. i18n: :date_planned: Date, datetime, required
..

:date_planned: Date, datetime, required

.. i18n:     *Scheduled date for the movement of the products or real date if the move is done.*
..

    *Scheduled date for the movement of the products or real date if the move is done.*

.. i18n: :location_dest_id: Dest. Location, many2one, required
..

:location_dest_id: Dest. Location, many2one, required

.. i18n: :tracking_id: Tracking Lot, many2one
..

:tracking_id: Tracking Lot, many2one

.. i18n:     *Tracking lot is the code that will be put on the logistical unit/pallet*
..

    *Tracking lot is the code that will be put on the logistical unit/pallet*

.. i18n: :picking_id: Packing List, many2one
..

:picking_id: Packing List, many2one

.. i18n: Object: Inventory (stock.inventory)
.. i18n: ###################################
..

Object: Inventory (stock.inventory)
###################################

.. i18n: :name: Inventory, char, required, readonly
..

:name: Inventory, char, required, readonly

.. i18n: :date_done: Date done, datetime
..

:date_done: Date done, datetime

.. i18n: :move_ids: Created Moves, many2many
..

:move_ids: Created Moves, many2many

.. i18n: :state: Status, selection, readonly
..

:state: Status, selection, readonly

.. i18n: :date: Date create, datetime, required, readonly
..

:date: Date create, datetime, required, readonly

.. i18n: :inventory_line_id: Inventories, one2many, readonly
..

:inventory_line_id: Inventories, one2many, readonly

.. i18n: Object: Inventory line (stock.inventory.line)
.. i18n: #############################################
..

Object: Inventory line (stock.inventory.line)
#############################################

.. i18n: :inventory_id: Inventory, many2one
..

:inventory_id: Inventory, many2one

.. i18n: :location_id: Location, many2one, required
..

:location_id: Location, many2one, required

.. i18n: :product_id: Product, many2one, required
..

:product_id: Product, many2one, required

.. i18n: :product_uom: Product UOM, many2one, required
..

:product_uom: Product UOM, many2one, required

.. i18n: :product_qty: Quantity, float
..

:product_qty: Quantity, float

.. i18n: Object: Warehouse (stock.warehouse)
.. i18n: ###################################
..

Object: Warehouse (stock.warehouse)
###################################

.. i18n: :lot_input_id: Location Input, many2one, required
..

:lot_input_id: Location Input, many2one, required

.. i18n: :partner_address_id: Owner Address, many2one
..

:partner_address_id: Owner Address, many2one

.. i18n: :lot_output_id: Location Output, many2one, required
..

:lot_output_id: Location Output, many2one, required

.. i18n: :name: Name, char, required
..

:name: Name, char, required

.. i18n: :lot_stock_id: Location Stock, many2one, required
..

:lot_stock_id: Location Stock, many2one, required

.. i18n: Object: stock.picking.move.wizard (stock.picking.move.wizard)
.. i18n: #############################################################
..

Object: stock.picking.move.wizard (stock.picking.move.wizard)
#############################################################

.. i18n: :move_ids: Move lines, many2many, required
..

:move_ids: Move lines, many2many, required

.. i18n: :address_id: Dest. Address, many2one
..

:address_id: Dest. Address, many2one

.. i18n: :name: Name, char
..

:name: Name, char

.. i18n: :picking_id: Packing list, many2one
..

:picking_id: Packing list, many2one

.. i18n: Object: Dates of Inventories (report.stock.lines.date)
.. i18n: ######################################################
..

Object: Dates of Inventories (report.stock.lines.date)
######################################################

.. i18n: :create_date: Latest Date of Inventory, datetime
..

:create_date: Latest Date of Inventory, datetime

.. i18n: :id: Inventory Line Id, integer, readonly
..

:id: Inventory Line Id, integer, readonly

.. i18n: :product_id: Product Id, integer, readonly
..

:product_id: Product Id, integer, readonly

.. i18n: Object: Stock report by production lots (stock.report.prodlots)
.. i18n: ###############################################################
..

Object: Stock report by production lots (stock.report.prodlots)
###############################################################

.. i18n: :prodlot_id: Production lot, many2one, readonly
..

:prodlot_id: Production lot, many2one, readonly

.. i18n: :location_id: Location, many2one, readonly
..

:location_id: Location, many2one, readonly

.. i18n: :name: Quantity, float, readonly
..

:name: Quantity, float, readonly

.. i18n: :product_id: Product, many2one, readonly
..

:product_id: Product, many2one, readonly
