
.. i18n: .. module:: mrp
.. i18n:     :synopsis: Manufacturing Resource Planning (Official, Quality Certified)
.. i18n:     :noindex:
.. i18n: .. 
..

.. module:: mrp
    :synopsis: Manufacturing Resource Planning (Official, Quality Certified)
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
.. i18n:     <div class="js-kit-rating" title="" permalink="" standalone="yes" path="/mrp"></div>
.. i18n:     <script src="http://js-kit.com/ratings.js"></script>
..

.. raw:: html

    <div class="js-kit-rating" title="" permalink="" standalone="yes" path="/mrp"></div>
    <script src="http://js-kit.com/ratings.js"></script>

.. i18n: Manufacturing Resource Planning (*mrp*)
.. i18n: =======================================
.. i18n: :Module: mrp
.. i18n: :Name: Manufacturing Resource Planning
.. i18n: :Version: 5.0.1.1
.. i18n: :Author: Tiny
.. i18n: :Directory: mrp
.. i18n: :Web: http://www.openerp.com
.. i18n: :Official module: yes
.. i18n: :Quality certified: yes
..

Manufacturing Resource Planning (*mrp*)
=======================================
:Module: mrp
:Name: Manufacturing Resource Planning
:Version: 5.0.1.1
:Author: Tiny
:Directory: mrp
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
.. i18n:   This is the base module to manage the manufacturing process in OpenERP.
.. i18n:   
.. i18n:       Features:
.. i18n:       * Make to Stock / Make to Order (by line)
.. i18n:       * Multi-level BoMs, no limit
.. i18n:       * Multi-level routing, no limit
.. i18n:       * Routing and workcenter integrated with analytic accounting
.. i18n:       * Scheduler computation periodically / Just In Time module
.. i18n:       * Multi-pos, multi-warehouse
.. i18n:       * Different reordering policies
.. i18n:       * Cost method by product: standard price, average price
.. i18n:       * Easy analysis of troubles or needs
.. i18n:       * Very flexible
.. i18n:       * Allows to browse Bill of Materials in complete structure
.. i18n:           that include child and phantom BoMs
.. i18n:       It supports complete integration and planning of stockable goods,
.. i18n:       consumable of services. Services are completely integrated with the rest
.. i18n:       of the software. For instance, you can set up a sub-contracting service
.. i18n:       in a BoM to automatically purchase on order the assembly of your production.
.. i18n:   
.. i18n:       Reports provided by this module:
.. i18n:       * Bill of Material structure and components
.. i18n:       * Load forecast on workcenters
.. i18n:       * Print a production order
.. i18n:       * Stock forecasts
..

::

  This is the base module to manage the manufacturing process in OpenERP.
  
      Features:
      * Make to Stock / Make to Order (by line)
      * Multi-level BoMs, no limit
      * Multi-level routing, no limit
      * Routing and workcenter integrated with analytic accounting
      * Scheduler computation periodically / Just In Time module
      * Multi-pos, multi-warehouse
      * Different reordering policies
      * Cost method by product: standard price, average price
      * Easy analysis of troubles or needs
      * Very flexible
      * Allows to browse Bill of Materials in complete structure
          that include child and phantom BoMs
      It supports complete integration and planning of stockable goods,
      consumable of services. Services are completely integrated with the rest
      of the software. For instance, you can set up a sub-contracting service
      in a BoM to automatically purchase on order the assembly of your production.
  
      Reports provided by this module:
      * Bill of Material structure and components
      * Load forecast on workcenters
      * Print a production order
      * Stock forecasts

.. i18n: Download links
.. i18n: --------------
..

Download links
--------------

.. i18n: You can download this module as a zip file in the following version:
..

You can download this module as a zip file in the following version:

.. i18n:   * `4.2 <http://www.openerp.com/download/modules/4.2/mrp.zip>`_
.. i18n:   * `5.0 <http://www.openerp.com/download/modules/5.0/mrp.zip>`_
.. i18n:   * `trunk <http://www.openerp.com/download/modules/trunk/mrp.zip>`_
..

  * `4.2 <http://www.openerp.com/download/modules/4.2/mrp.zip>`_
  * `5.0 <http://www.openerp.com/download/modules/5.0/mrp.zip>`_
  * `trunk <http://www.openerp.com/download/modules/trunk/mrp.zip>`_

.. i18n: Dependencies
.. i18n: ------------
..

Dependencies
------------

.. i18n:  * :mod:`stock`
.. i18n:  * :mod:`hr`
.. i18n:  * :mod:`purchase`
.. i18n:  * :mod:`product`
.. i18n:  * :mod:`process`
..

 * :mod:`stock`
 * :mod:`hr`
 * :mod:`purchase`
 * :mod:`product`
 * :mod:`process`

.. i18n: Reports
.. i18n: -------
..

Reports
-------

.. i18n:  * BOM Structure
.. i18n: 
.. i18n:  * Production Order
..

 * BOM Structure

 * Production Order

.. i18n: Menus
.. i18n: -------
..

Menus
-------

.. i18n:  * Manufacturing/Compute All Schedulers
.. i18n:  * Manufacturing
.. i18n:  * Stock Management/Automatic Procurements
.. i18n:  * Manufacturing/Configuration
.. i18n:  * Manufacturing/Configuration/Properties
.. i18n:  * Manufacturing/Configuration/Properties/Property Categories
.. i18n:  * Manufacturing/Configuration/Properties/Properties
.. i18n:  * Manufacturing/Configuration/Workcenters
.. i18n:  * Manufacturing/Configuration/Routings
.. i18n:  * Manufacturing/Configuration/Bill of Materials
.. i18n:  * Manufacturing/Configuration/Bill of Materials/Bill of Material Structure
.. i18n:  * Manufacturing/Configuration/Bill of Materials/New Bill of Materials
.. i18n:  * Manufacturing/Configuration/Bill of Materials Components
.. i18n:  * Manufacturing/Production Orders
.. i18n:  * Manufacturing/Production Orders/Production Orders Planning
.. i18n:  * Manufacturing/Production Orders/Production Orders To Start
.. i18n:  * Manufacturing/Production Orders/Production Orders in Progress
.. i18n:  * Manufacturing/Production Orders/Production Orders Waiting Products
.. i18n:  * Manufacturing/Production Orders/New Production Order
.. i18n:  * Manufacturing/Procurement Orders
.. i18n:  * Manufacturing/Procurement Orders/Unscheduled procurements
.. i18n:  * Stock Management/Automatic Procurements/Exceptions Procurements
.. i18n:  * Stock Management/Automatic Procurements/Exceptions Procurements/Exceptions Procurements to Fix
.. i18n:  * Stock Management/Automatic Procurements/Exceptions Procurements/Temporary Procurement Exceptions
.. i18n:  * Manufacturing/Procurement Orders/New Procurement
.. i18n:  * Stock Management/Automatic Procurements/Minimum Stock Rules
.. i18n:  * Manufacturing/Compute All Schedulers/Compute Procurements Only
.. i18n:  * Manufacturing/Compute All Schedulers/Compute Stock Minimum Rules Only
..

 * Manufacturing/Compute All Schedulers
 * Manufacturing
 * Stock Management/Automatic Procurements
 * Manufacturing/Configuration
 * Manufacturing/Configuration/Properties
 * Manufacturing/Configuration/Properties/Property Categories
 * Manufacturing/Configuration/Properties/Properties
 * Manufacturing/Configuration/Workcenters
 * Manufacturing/Configuration/Routings
 * Manufacturing/Configuration/Bill of Materials
 * Manufacturing/Configuration/Bill of Materials/Bill of Material Structure
 * Manufacturing/Configuration/Bill of Materials/New Bill of Materials
 * Manufacturing/Configuration/Bill of Materials Components
 * Manufacturing/Production Orders
 * Manufacturing/Production Orders/Production Orders Planning
 * Manufacturing/Production Orders/Production Orders To Start
 * Manufacturing/Production Orders/Production Orders in Progress
 * Manufacturing/Production Orders/Production Orders Waiting Products
 * Manufacturing/Production Orders/New Production Order
 * Manufacturing/Procurement Orders
 * Manufacturing/Procurement Orders/Unscheduled procurements
 * Stock Management/Automatic Procurements/Exceptions Procurements
 * Stock Management/Automatic Procurements/Exceptions Procurements/Exceptions Procurements to Fix
 * Stock Management/Automatic Procurements/Exceptions Procurements/Temporary Procurement Exceptions
 * Manufacturing/Procurement Orders/New Procurement
 * Stock Management/Automatic Procurements/Minimum Stock Rules
 * Manufacturing/Compute All Schedulers/Compute Procurements Only
 * Manufacturing/Compute All Schedulers/Compute Stock Minimum Rules Only

.. i18n: Views
.. i18n: -----
..

Views
-----

.. i18n:  * mrp.property.group.form (form)
.. i18n:  * mrp.property.tree (tree)
.. i18n:  * mrp.property.form (form)
.. i18n:  * mrp.workcenter.tree (tree)
.. i18n:  * mrp.workcenter.form (form)
.. i18n:  * mrp.routing.workcenter.tree (tree)
.. i18n:  * mrp.routing.workcenter.form (form)
.. i18n:  * mrp.routing.form (form)
.. i18n:  * mrp.routing.tree (tree)
.. i18n:  * mrp.bom.form (form)
.. i18n:  * mrp.bom.tree (tree)
.. i18n:  * mrp.bom.revision (tree)
.. i18n:  * mrp.bom.revision (form)
.. i18n:  * mrp.production.tree (tree)
.. i18n:  * mrp.production.calendar (calendar)
.. i18n:  * mrp.production.gantt (gantt)
.. i18n:  * mrp.production.graph (graph)
.. i18n:  * mrp.production.form (form)
.. i18n:  * mrp.production.lot.line.form (form)
.. i18n:  * mrp.production.lot.line.tree (tree)
.. i18n:  * mrp.production.product.line.form (form)
.. i18n:  * mrp.production.product.line.tree (tree)
.. i18n:  * mrp.procurement.tree (tree)
.. i18n:  * mrp.procurement.form (form)
.. i18n:  * stock.warehouse.orderpoint.tree (tree)
.. i18n:  * stock.warehouse.orderpoint.form (form)
.. i18n:  * \* INHERIT res.company.mrp.config (form)
..

 * mrp.property.group.form (form)
 * mrp.property.tree (tree)
 * mrp.property.form (form)
 * mrp.workcenter.tree (tree)
 * mrp.workcenter.form (form)
 * mrp.routing.workcenter.tree (tree)
 * mrp.routing.workcenter.form (form)
 * mrp.routing.form (form)
 * mrp.routing.tree (tree)
 * mrp.bom.form (form)
 * mrp.bom.tree (tree)
 * mrp.bom.revision (tree)
 * mrp.bom.revision (form)
 * mrp.production.tree (tree)
 * mrp.production.calendar (calendar)
 * mrp.production.gantt (gantt)
 * mrp.production.graph (graph)
 * mrp.production.form (form)
 * mrp.production.lot.line.form (form)
 * mrp.production.lot.line.tree (tree)
 * mrp.production.product.line.form (form)
 * mrp.production.product.line.tree (tree)
 * mrp.procurement.tree (tree)
 * mrp.procurement.form (form)
 * stock.warehouse.orderpoint.tree (tree)
 * stock.warehouse.orderpoint.form (form)
 * \* INHERIT res.company.mrp.config (form)

.. i18n: Objects
.. i18n: -------
..

Objects
-------

.. i18n: Object: Workcenter (mrp.workcenter)
.. i18n: ###################################
..

Object: Workcenter (mrp.workcenter)
###################################

.. i18n: :costs_cycle_account_id: Cycle Account, many2one
..

:costs_cycle_account_id: Cycle Account, many2one

.. i18n:     *Complete this only if you want automatic analytic accounting entries on production orders.*
..

    *Complete this only if you want automatic analytic accounting entries on production orders.*

.. i18n: :time_efficiency: Time Efficiency, float
..

:time_efficiency: Time Efficiency, float

.. i18n:     *Factor that multiplies all times expressed in the workcenter.*
..

    *Factor that multiplies all times expressed in the workcenter.*

.. i18n: :code: Code, char
..

:code: Code, char

.. i18n: :time_start: Time before prod., float
..

:time_start: Time before prod., float

.. i18n:     *Time in hours for the setup.*
..

    *Time in hours for the setup.*

.. i18n: :name: Workcenter Name, char, required
..

:name: Workcenter Name, char, required

.. i18n: :time_stop: Time after prod., float
..

:time_stop: Time after prod., float

.. i18n:     *Time in hours for the cleaning.*
..

    *Time in hours for the cleaning.*

.. i18n: :capacity_per_cycle: Capacity per Cycle, float
..

:capacity_per_cycle: Capacity per Cycle, float

.. i18n:     *Number of operation this workcenter can do in parallel. If this workcenter represent a team of 5 workers, the capacity per cycle is 5.*
..

    *Number of operation this workcenter can do in parallel. If this workcenter represent a team of 5 workers, the capacity per cycle is 5.*

.. i18n: :type: Type, selection, required
..

:type: Type, selection, required

.. i18n: :costs_journal_id: Analytic Journal, many2one
..

:costs_journal_id: Analytic Journal, many2one

.. i18n: :note: Description, text
..

:note: Description, text

.. i18n:     *Description of the workcenter. Explain here what's a cycle according to this workcenter.*
..

    *Description of the workcenter. Explain here what's a cycle according to this workcenter.*

.. i18n: :costs_hour: Cost per hour, float
..

:costs_hour: Cost per hour, float

.. i18n: :costs_hour_account_id: Hour Account, many2one
..

:costs_hour_account_id: Hour Account, many2one

.. i18n:     *Complete this only if you want automatic analytic accounting entries on production orders.*
..

    *Complete this only if you want automatic analytic accounting entries on production orders.*

.. i18n: :costs_cycle: Cost per cycle, float
..

:costs_cycle: Cost per cycle, float

.. i18n: :timesheet_id: Working Time, many2one
..

:timesheet_id: Working Time, many2one

.. i18n:     *The normal working time of the workcenter.*
..

    *The normal working time of the workcenter.*

.. i18n: :active: Active, boolean
..

:active: Active, boolean

.. i18n: :costs_general_account_id: General Account, many2one
..

:costs_general_account_id: General Account, many2one

.. i18n: :time_cycle: Time for 1 cycle (hour), float
..

:time_cycle: Time for 1 cycle (hour), float

.. i18n:     *Time in hours for doing one cycle.*
..

    *Time in hours for doing one cycle.*

.. i18n: Object: Property Group (mrp.property.group)
.. i18n: ###########################################
..

Object: Property Group (mrp.property.group)
###########################################

.. i18n: :name: Property Group, char, required
..

:name: Property Group, char, required

.. i18n: :description: Description, text
..

:description: Description, text

.. i18n: Object: Property (mrp.property)
.. i18n: ###############################
..

Object: Property (mrp.property)
###############################

.. i18n: :group_id: Property Group, many2one, required
..

:group_id: Property Group, many2one, required

.. i18n: :composition: Properties composition, selection, required
..

:composition: Properties composition, selection, required

.. i18n:     *Not used in computations, for information purpose only.*
..

    *Not used in computations, for information purpose only.*

.. i18n: :name: Name, char, required
..

:name: Name, char, required

.. i18n: :description: Description, text
..

:description: Description, text

.. i18n: Object: Routing (mrp.routing)
.. i18n: #############################
..

Object: Routing (mrp.routing)
#############################

.. i18n: :workcenter_lines: Workcenters, one2many
..

:workcenter_lines: Workcenters, one2many

.. i18n: :code: Code, char
..

:code: Code, char

.. i18n: :name: Name, char, required
..

:name: Name, char, required

.. i18n: :note: Description, text
..

:note: Description, text

.. i18n: :active: Active, boolean
..

:active: Active, boolean

.. i18n: :location_id: Production Location, many2one
..

:location_id: Production Location, many2one

.. i18n:     *Keep empty if you produce at the location where the finished products are needed. Set a location if you produce at a fixed location. This can be a partner location if you subcontract the manufacturing operations.*
..

    *Keep empty if you produce at the location where the finished products are needed. Set a location if you produce at a fixed location. This can be a partner location if you subcontract the manufacturing operations.*

.. i18n: Object: Routing workcenter usage (mrp.routing.workcenter)
.. i18n: #########################################################
..

Object: Routing workcenter usage (mrp.routing.workcenter)
#########################################################

.. i18n: :cycle_nbr: Number of Cycle, float, required
..

:cycle_nbr: Number of Cycle, float, required

.. i18n:     *A cycle is defined in the workcenter definition.*
..

    *A cycle is defined in the workcenter definition.*

.. i18n: :name: Name, char, required
..

:name: Name, char, required

.. i18n: :sequence: Sequence, integer
..

:sequence: Sequence, integer

.. i18n: :note: Description, text
..

:note: Description, text

.. i18n: :routing_id: Parent Routing, many2one
..

:routing_id: Parent Routing, many2one

.. i18n: :workcenter_id: Workcenter, many2one, required
..

:workcenter_id: Workcenter, many2one, required

.. i18n: :hour_nbr: Number of Hours, float, required
..

:hour_nbr: Number of Hours, float, required

.. i18n: Object: Bill of Material (mrp.bom)
.. i18n: ##################################
..

Object: Bill of Material (mrp.bom)
##################################

.. i18n: :property_ids: Properties, many2many
..

:property_ids: Properties, many2many

.. i18n: :product_uos_qty: Product UOS Qty, float
..

:product_uos_qty: Product UOS Qty, float

.. i18n: :date_stop: Valid Until, date
..

:date_stop: Valid Until, date

.. i18n:     *Validity of this BoM or component. Keep empty if it's always valid.*
..

    *Validity of this BoM or component. Keep empty if it's always valid.*

.. i18n: :code: Code, char
..

:code: Code, char

.. i18n: :product_uom: Product UOM, many2one, required
..

:product_uom: Product UOM, many2one, required

.. i18n: :sequence: Sequence, integer
..

:sequence: Sequence, integer

.. i18n: :child_complete_ids: BoM Hierarchy, many2many, readonly
..

:child_complete_ids: BoM Hierarchy, many2many, readonly

.. i18n: :product_qty: Product Qty, float, required
..

:product_qty: Product Qty, float, required

.. i18n: :product_uos: Product UOS, many2one
..

:product_uos: Product UOS, many2one

.. i18n: :date_start: Valid From, date
..

:date_start: Valid From, date

.. i18n:     *Validity of this BoM or component. Keep empty if it's always valid.*
..

    *Validity of this BoM or component. Keep empty if it's always valid.*

.. i18n: :routing_id: Routing, many2one
..

:routing_id: Routing, many2one

.. i18n:     *The list of operations (list of workcenters) to produce the finished product. The routing is mainly used to compute workcenter costs during operations and to plan future loads on workcenters based on production planning.*
..

    *The list of operations (list of workcenters) to produce the finished product. The routing is mainly used to compute workcenter costs during operations and to plan future loads on workcenters based on production planning.*

.. i18n: :bom_lines: BoM Lines, one2many
..

:bom_lines: BoM Lines, one2many

.. i18n: :type: BoM Type, selection, required
..

:type: BoM Type, selection, required

.. i18n:     *Use a phantom bill of material in raw materials lines that have to be automatically computed in on eproduction order and not one per level. If you put "Phantom/Set" at the root level of a bill of material it is considered as a set or pack: the products are replaced by the components between the sale order to the picking without going through the production order. The normal BoM will generate one production order per BoM level.*
..

    *Use a phantom bill of material in raw materials lines that have to be automatically computed in on eproduction order and not one per level. If you put "Phantom/Set" at the root level of a bill of material it is considered as a set or pack: the products are replaced by the components between the sale order to the picking without going through the production order. The normal BoM will generate one production order per BoM level.*

.. i18n: :method: Method, selection, readonly
..

:method: Method, selection, readonly

.. i18n: :child_ids: BoM Hierarchy, many2many, readonly
..

:child_ids: BoM Hierarchy, many2many, readonly

.. i18n: :bom_id: Parent BoM, many2one
..

:bom_id: Parent BoM, many2one

.. i18n: :revision_type: indice type, selection
..

:revision_type: indice type, selection

.. i18n: :active: Active, boolean
..

:active: Active, boolean

.. i18n: :product_efficiency: Product Efficiency, float, required
..

:product_efficiency: Product Efficiency, float, required

.. i18n:     *Efficiency on the production. A factor of 0.9 means a loss of 10% in the production.*
..

    *Efficiency on the production. A factor of 0.9 means a loss of 10% in the production.*

.. i18n: :product_id: Product, many2one, required
..

:product_id: Product, many2one, required

.. i18n: :product_rounding: Product Rounding, float
..

:product_rounding: Product Rounding, float

.. i18n:     *Rounding applied on the product quantity. For integer only values, put 1.0*
..

    *Rounding applied on the product quantity. For integer only values, put 1.0*

.. i18n: :name: Name, char, required
..

:name: Name, char, required

.. i18n: :revision_ids: BoM Revisions, one2many
..

:revision_ids: BoM Revisions, one2many

.. i18n: :position: Internal Ref., char
..

:position: Internal Ref., char

.. i18n:     *Reference to a position in an external plan.*
..

    *Reference to a position in an external plan.*

.. i18n: Object: Bill of material revisions (mrp.bom.revision)
.. i18n: #####################################################
..

Object: Bill of material revisions (mrp.bom.revision)
#####################################################

.. i18n: :indice: Revision, char
..

:indice: Revision, char

.. i18n: :name: Modification name, char, required
..

:name: Modification name, char, required

.. i18n: :bom_id: BoM, many2one
..

:bom_id: BoM, many2one

.. i18n: :last_indice: last indice, char
..

:last_indice: last indice, char

.. i18n: :date: Modification Date, date
..

:date: Modification Date, date

.. i18n: :author_id: Author, many2one
..

:author_id: Author, many2one

.. i18n: :description: Description, text
..

:description: Description, text

.. i18n: Object: Production (mrp.production)
.. i18n: ###################################
..

Object: Production (mrp.production)
###################################

.. i18n: :origin: Origin, char
..

:origin: Origin, char

.. i18n: :product_uos_qty: Product UoS Qty, float, readonly
..

:product_uos_qty: Product UoS Qty, float, readonly

.. i18n: :product_uom: Product UOM, many2one, required, readonly
..

:product_uom: Product UOM, many2one, required, readonly

.. i18n: :sale_ref: Sale Ref, char, readonly
..

:sale_ref: Sale Ref, char, readonly

.. i18n: :product_qty: Product Qty, float, required, readonly
..

:product_qty: Product Qty, float, required, readonly

.. i18n: :product_uos: Product UoS, many2one, readonly
..

:product_uos: Product UoS, many2one, readonly

.. i18n: :date_planned_date: Scheduled Date, date, readonly
..

:date_planned_date: Scheduled Date, date, readonly

.. i18n: :sale_name: Sale Name, char, readonly
..

:sale_name: Sale Name, char, readonly

.. i18n: :location_src_id: Raw Materials Location, many2one, required
..

:location_src_id: Raw Materials Location, many2one, required

.. i18n:     *Location where the system will look for products used in raw materials.*
..

    *Location where the system will look for products used in raw materials.*

.. i18n: :cycle_total: Total Cycles, float, readonly
..

:cycle_total: Total Cycles, float, readonly

.. i18n: :date_start: Start Date, datetime
..

:date_start: Start Date, datetime

.. i18n: :priority: Priority, selection
..

:priority: Priority, selection

.. i18n: :state: Status, selection, readonly
..

:state: Status, selection, readonly

.. i18n: :product_lines: Scheduled goods, one2many
..

:product_lines: Scheduled goods, one2many

.. i18n: :bom_id: Bill of Material, many2one
..

:bom_id: Bill of Material, many2one

.. i18n: :move_lines: Products Consumed, many2many
..

:move_lines: Products Consumed, many2many

.. i18n: :date_planned_end: Scheduled End, date, readonly
..

:date_planned_end: Scheduled End, date, readonly

.. i18n: :routing_id: Routing, many2one
..

:routing_id: Routing, many2one

.. i18n: :date_finished: End Date, datetime
..

:date_finished: End Date, datetime

.. i18n: :move_created_ids: Moves Created, one2many
..

:move_created_ids: Moves Created, one2many

.. i18n: :product_id: Product, many2one, required
..

:product_id: Product, many2one, required

.. i18n: :workcenter_lines: Workcenters Utilisation, one2many
..

:workcenter_lines: Workcenters Utilisation, one2many

.. i18n: :name: Reference, char, required
..

:name: Reference, char, required

.. i18n: :move_prod_id: Move product, many2one, readonly
..

:move_prod_id: Move product, many2one, readonly

.. i18n: :date_planned: Scheduled date, datetime, required
..

:date_planned: Scheduled date, datetime, required

.. i18n: :hour_total: Total Hours, float, readonly
..

:hour_total: Total Hours, float, readonly

.. i18n: :location_dest_id: Finished Products Location, many2one, required
..

:location_dest_id: Finished Products Location, many2one, required

.. i18n:     *Location where the system will stock the finished products.*
..

    *Location where the system will stock the finished products.*

.. i18n: :picking_id: Packing list, many2one, readonly
..

:picking_id: Packing list, many2one, readonly

.. i18n:     *This is the internal picking list take bring the raw materials to the production plan.*
..

    *This is the internal picking list take bring the raw materials to the production plan.*

.. i18n: Object: Work Orders (mrp.production.workcenter.line)
.. i18n: ####################################################
..

Object: Work Orders (mrp.production.workcenter.line)
####################################################

.. i18n: :name: Work Order, char, required
..

:name: Work Order, char, required

.. i18n: :hour: Nbr of hour, float
..

:hour: Nbr of hour, float

.. i18n: :sequence: Sequence, integer, required
..

:sequence: Sequence, integer, required

.. i18n: :production_id: Production Order, many2one
..

:production_id: Production Order, many2one

.. i18n: :workcenter_id: Workcenter, many2one, required
..

:workcenter_id: Workcenter, many2one, required

.. i18n: :cycle: Nbr of cycle, float
..

:cycle: Nbr of cycle, float

.. i18n: Object: Production scheduled products (mrp.production.product.line)
.. i18n: ###################################################################
..

Object: Production scheduled products (mrp.production.product.line)
###################################################################

.. i18n: :product_uos_qty: Product UOS Qty, float
..

:product_uos_qty: Product UOS Qty, float

.. i18n: :name: Name, char, required
..

:name: Name, char, required

.. i18n: :product_uom: Product UOM, many2one, required
..

:product_uom: Product UOM, many2one, required

.. i18n: :production_id: Production Order, many2one
..

:production_id: Production Order, many2one

.. i18n: :product_qty: Product Qty, float, required
..

:product_qty: Product Qty, float, required

.. i18n: :product_uos: Product UOS, many2one
..

:product_uos: Product UOS, many2one

.. i18n: :product_id: Product, many2one, required
..

:product_id: Product, many2one, required

.. i18n: Object: Procurement (mrp.procurement)
.. i18n: #####################################
..

Object: Procurement (mrp.procurement)
#####################################

.. i18n: :origin: Origin, char
..

:origin: Origin, char

.. i18n:     *Reference of the document that created this procurement.
.. i18n:     This is automatically completed by OpenERP.*
..

    *Reference of the document that created this procurement.
    This is automatically completed by OpenERP.*

.. i18n: :product_uos_qty: UoS Quantity, float, readonly
..

:product_uos_qty: UoS Quantity, float, readonly

.. i18n: :purchase_id: Purchase Order, many2one
..

:purchase_id: Purchase Order, many2one

.. i18n: :product_id: Product, many2one, required
..

:product_id: Product, many2one, required

.. i18n: :product_uom: Product UoM, many2one, required, readonly
..

:product_uom: Product UoM, many2one, required, readonly

.. i18n: :date_planned: Scheduled date, datetime, required
..

:date_planned: Scheduled date, datetime, required

.. i18n: :close_move: Close Move at end, boolean, required
..

:close_move: Close Move at end, boolean, required

.. i18n: :priority: Priority, selection, required
..

:priority: Priority, selection, required

.. i18n: :property_ids: Properties, many2many
..

:property_ids: Properties, many2many

.. i18n: :date_close: Date Closed, datetime
..

:date_close: Date Closed, datetime

.. i18n: :note: Note, text
..

:note: Note, text

.. i18n: :procure_method: Procurement Method, selection, required, readonly
..

:procure_method: Procurement Method, selection, required, readonly

.. i18n:     *If you encode manually a procurement, you probably want to use a make to order method.*
..

    *If you encode manually a procurement, you probably want to use a make to order method.*

.. i18n: :state: Status, selection, required
..

:state: Status, selection, required

.. i18n: :product_qty: Quantity, float, required, readonly
..

:product_qty: Quantity, float, required, readonly

.. i18n: :product_uos: Product UoS, many2one, readonly
..

:product_uos: Product UoS, many2one, readonly

.. i18n: :message: Latest error, char
..

:message: Latest error, char

.. i18n: :location_id: Location, many2one, required
..

:location_id: Location, many2one, required

.. i18n: :bom_id: BoM, many2one
..

:bom_id: BoM, many2one

.. i18n: :move_id: Reservation, many2one
..

:move_id: Reservation, many2one

.. i18n: :name: Name, char, required
..

:name: Name, char, required

.. i18n: Object: Orderpoint minimum rule (stock.warehouse.orderpoint)
.. i18n: ############################################################
..

Object: Orderpoint minimum rule (stock.warehouse.orderpoint)
############################################################

.. i18n: :product_max_qty: Max Quantity, float, required
..

:product_max_qty: Max Quantity, float, required

.. i18n:     *When the virtual stock goes belong the Min Quantity, OpenERP generates a procurement to bring the virtual stock to the Max Quantity.*
..

    *When the virtual stock goes belong the Min Quantity, OpenERP generates a procurement to bring the virtual stock to the Max Quantity.*

.. i18n: :product_min_qty: Min Quantity, float, required
..

:product_min_qty: Min Quantity, float, required

.. i18n:     *When the virtual stock goes belong the Min Quantity, OpenERP generates a procurement to bring the virtual stock to the Max Quantity.*
..

    *When the virtual stock goes belong the Min Quantity, OpenERP generates a procurement to bring the virtual stock to the Max Quantity.*

.. i18n: :qty_multiple: Qty Multiple, integer, required
..

:qty_multiple: Qty Multiple, integer, required

.. i18n:     *The procurement quantity will by rounded up to this multiple.*
..

    *The procurement quantity will by rounded up to this multiple.*

.. i18n: :procurement_id: Purchase Order, many2one
..

:procurement_id: Purchase Order, many2one

.. i18n: :name: Name, char, required
..

:name: Name, char, required

.. i18n: :product_uom: Product UOM, many2one, required
..

:product_uom: Product UOM, many2one, required

.. i18n: :warehouse_id: Warehouse, many2one, required
..

:warehouse_id: Warehouse, many2one, required

.. i18n: :logic: Reordering Mode, selection, required
..

:logic: Reordering Mode, selection, required

.. i18n: :active: Active, boolean
..

:active: Active, boolean

.. i18n: :location_id: Location, many2one, required
..

:location_id: Location, many2one, required

.. i18n: :product_id: Product, many2one, required
..

:product_id: Product, many2one, required
