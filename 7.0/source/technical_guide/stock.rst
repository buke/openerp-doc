
.. module:: stock
    :synopsis: Stock Management (Official, Quality Certified)
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

    <div class="js-kit-rating" title="" permalink="" standalone="yes" path="/stock"></div>
    <script src="http://js-kit.com/ratings.js"></script>

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

Description
-----------

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

Download links
--------------

You can download this module as a zip file in the following version:

  * `4.2 <http://www.openerp.com/download/modules/4.2/stock.zip>`_
  * `5.0 <http://www.openerp.com/download/modules/5.0/stock.zip>`_
  * `trunk <http://www.openerp.com/download/modules/trunk/stock.zip>`_


Dependencies
------------

 * :mod:`product`
 * :mod:`account`

Reports
-------

 * Future Stock Forecast

 * Packing list

 * Print Item Labels

 * Location Overview

 * Lots by location

 * Location Content (With children)

Menus
-------

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

Views
-----

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


Objects
-------

Object: Incoterms (stock.incoterms)
###################################



:active: Active, boolean





:code: Code, char, required





:name: Name, char, required




Object: Location (stock.location)
#################################



:comment: Additional Information, text





:address_id: Location Address, many2one





:stock_virtual_value: Virtual Stock Value, float, readonly





:allocation_method: Allocation Method, selection, required





:location_id: Parent Location, many2one





:chained_location_id: Chained Location If Fixed, many2one





:complete_name: Location Name, char, readonly





:usage: Location Type, selection, required





:stock_real_value: Real Stock Value, float, readonly





:chained_location_type: Chained Location Type, selection, required





:account_id: Inventory Account, many2one





:child_ids: Contains, one2many





:chained_delay: Chained Delay (days), integer





:stock_virtual: Virtual Stock, float, readonly





:posz: Height (Z), integer





:posx: Corridor (X), integer





:posy: Shelves (Y), integer





:active: Active, boolean





:icon: Icon, selection





:parent_right: Right Parent, integer





:name: Location Name, char, required





:chained_auto_packing: Automatic Move, selection, required

    *This is used only if you selected a chained location type.
    The 'Automatic Move' value will create a stock move after the current one that will be validated automatically. With 'Manual Operation', the stock move has to be validated by a worker. With 'Automatic No Step Added', the location is replaced in the original move.*



:parent_left: Left Parent, integer





:stock_real: Real Stock, float, readonly




Object: Stock Tracking Lots (stock.tracking)
############################################



:active: Active, boolean





:move_ids: Moves Tracked, one2many





:serial: Reference, char





:date: Date Created, datetime, required





:name: Tracking, char, required




Object: Packing List (stock.picking)
####################################



:origin: Origin Reference, char





:address_id: Partner, many2one





:type: Shipping Type, selection, required





:move_lines: Move lines, one2many





:date_done: Date Done, datetime





:name: Reference, char





:move_type: Delivery Method, selection, required





:invoice_state: Invoice Status, selection, required, readonly





:min_date: Planned Date, datetime





:note: Notes, text





:date: Date Order, datetime





:state: Status, selection, readonly





:location_dest_id: Dest. Location, many2one





:max_date: Max. Planned Date, datetime





:auto_picking: Auto-Packing, boolean





:active: Active, boolean





:location_id: Location, many2one





:backorder_id: Back Order, many2one




Object: Production lot (stock.production.lot)
#############################################



:stock_available: Available, float, readonly





:product_id: Product, many2one, required





:date: Created Date, datetime, required





:revisions: Revisions, one2many





:ref: Internal Ref, char





:name: Serial, char, required




Object: Production lot revisions (stock.production.lot.revision)
################################################################



:indice: Revision, char





:name: Revision Name, char, required





:date: Revision Date, date





:lot_id: Production lot, many2one





:author_id: Author, many2one





:description: Description, text




Object: Stock Move (stock.move)
###############################



:product_uos_qty: Quantity (UOS), float





:address_id: Dest. Address, many2one





:product_uom: Product UOM, many2one, required





:price_unit: Unit Price, float





:product_qty: Quantity, float, required





:product_uos: Product UOS, many2one





:location_id: Source Location, many2one, required





:priority: Priority, selection





:auto_validate: Auto Validate, boolean





:note: Notes, text





:state: Status, selection, readonly





:product_packaging: Packaging, many2one





:move_history_ids: Move History, many2many





:prodlot_id: Production Lot, many2one

    *Production lot is used to put a serial number on the production*



:move_dest_id: Dest. Move, many2one





:date: Date Created, datetime





:product_id: Product, many2one, required





:move_history_ids2: Move History, many2many





:name: Name, char, required





:date_planned: Date, datetime, required

    *Scheduled date for the movement of the products or real date if the move is done.*



:location_dest_id: Dest. Location, many2one, required





:tracking_id: Tracking Lot, many2one

    *Tracking lot is the code that will be put on the logistical unit/pallet*



:picking_id: Packing List, many2one




Object: Inventory (stock.inventory)
###################################



:name: Inventory, char, required, readonly





:date_done: Date done, datetime





:move_ids: Created Moves, many2many





:state: Status, selection, readonly





:date: Date create, datetime, required, readonly





:inventory_line_id: Inventories, one2many, readonly




Object: Inventory line (stock.inventory.line)
#############################################



:inventory_id: Inventory, many2one





:location_id: Location, many2one, required





:product_id: Product, many2one, required





:product_uom: Product UOM, many2one, required





:product_qty: Quantity, float




Object: Warehouse (stock.warehouse)
###################################



:lot_input_id: Location Input, many2one, required





:partner_address_id: Owner Address, many2one





:lot_output_id: Location Output, many2one, required





:name: Name, char, required





:lot_stock_id: Location Stock, many2one, required




Object: stock.picking.move.wizard (stock.picking.move.wizard)
#############################################################



:move_ids: Move lines, many2many, required





:address_id: Dest. Address, many2one





:name: Name, char





:picking_id: Packing list, many2one




Object: Dates of Inventories (report.stock.lines.date)
######################################################



:create_date: Latest Date of Inventory, datetime





:id: Inventory Line Id, integer, readonly





:product_id: Product Id, integer, readonly




Object: Stock report by production lots (stock.report.prodlots)
###############################################################



:prodlot_id: Production lot, many2one, readonly





:location_id: Location, many2one, readonly





:name: Quantity, float, readonly





:product_id: Product, many2one, readonly


