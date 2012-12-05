
.. i18n: .. module:: hotel_restaurant
.. i18n:     :synopsis: Hotel Restaurant Management 
.. i18n:     :noindex:
.. i18n: .. 
..

.. module:: hotel_restaurant
    :synopsis: Hotel Restaurant Management 
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
.. i18n:     <div class="js-kit-rating" title="" permalink="" standalone="yes" path="/hotel_restaurant"></div>
.. i18n:     <script src="http://js-kit.com/ratings.js"></script>
..

.. raw:: html

    <div class="js-kit-rating" title="" permalink="" standalone="yes" path="/hotel_restaurant"></div>
    <script src="http://js-kit.com/ratings.js"></script>

.. i18n: Hotel Restaurant Management (*hotel_restaurant*)
.. i18n: ================================================
.. i18n: :Module: hotel_restaurant
.. i18n: :Name: Hotel Restaurant Management
.. i18n: :Version: 5.0.1.0
.. i18n: :Author: Tiny
.. i18n: :Directory: hotel_restaurant
.. i18n: :Web: 
.. i18n: :Official module: no
.. i18n: :Quality certified: no
..

Hotel Restaurant Management (*hotel_restaurant*)
================================================
:Module: hotel_restaurant
:Name: Hotel Restaurant Management
:Version: 5.0.1.0
:Author: Tiny
:Directory: hotel_restaurant
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
.. i18n:   Module for Hotel/Resort/Restaurant management. You can manage:
.. i18n:       * Configure Property
.. i18n:       * Restaurant Configuration
.. i18n:       * table reservation
.. i18n:       * Generate and process Kitchen Order ticket,
.. i18n:       * Payment
.. i18n:   
.. i18n:       Different reports are also provided, mainly for Restaurant.
..

::

  Module for Hotel/Resort/Restaurant management. You can manage:
      * Configure Property
      * Restaurant Configuration
      * table reservation
      * Generate and process Kitchen Order ticket,
      * Payment
  
      Different reports are also provided, mainly for Restaurant.

.. i18n: Download links
.. i18n: --------------
..

Download links
--------------

.. i18n: You can download this module as a zip file in the following version:
..

You can download this module as a zip file in the following version:

.. i18n:   * `5.0 <http://www.openerp.com/download/modules/5.0/hotel_restaurant.zip>`_
.. i18n:   * `trunk <http://www.openerp.com/download/modules/trunk/hotel_restaurant.zip>`_
..

  * `5.0 <http://www.openerp.com/download/modules/5.0/hotel_restaurant.zip>`_
  * `trunk <http://www.openerp.com/download/modules/trunk/hotel_restaurant.zip>`_

.. i18n: Dependencies
.. i18n: ------------
..

Dependencies
------------

.. i18n:  * :mod:`base`
.. i18n:  * :mod:`hotel`
..

 * :mod:`base`
 * :mod:`hotel`

.. i18n: Reports
.. i18n: -------
..

Reports
-------

.. i18n:  * Kitchen Order Tickets
.. i18n: 
.. i18n:  * Customer Bill
.. i18n: 
.. i18n:  * Table Reservation List
..

 * Kitchen Order Tickets

 * Customer Bill

 * Table Reservation List

.. i18n: Menus
.. i18n: -------
..

Menus
-------

.. i18n:  * Hotel Management/Restaurant
.. i18n:  * Hotel Management/Configuration/Tables
.. i18n:  * Hotel Management/Restaurant/Table Booking
.. i18n:  * Hotel Management/Restaurant/Orders
.. i18n:  * Hotel Management/Restaurant/Table Order
.. i18n:  * Hotel Management/Restaurant/KOT
.. i18n:  * Hotel Management/Configuration/FoodItem Types
.. i18n:  * Hotel Management/Configuration/FoodItem Types/Food Items
.. i18n:  * Hotel Management/Reports/Table Reservation List
..

 * Hotel Management/Restaurant
 * Hotel Management/Configuration/Tables
 * Hotel Management/Restaurant/Table Booking
 * Hotel Management/Restaurant/Orders
 * Hotel Management/Restaurant/Table Order
 * Hotel Management/Restaurant/KOT
 * Hotel Management/Configuration/FoodItem Types
 * Hotel Management/Configuration/FoodItem Types/Food Items
 * Hotel Management/Reports/Table Reservation List

.. i18n: Views
.. i18n: -----
..

Views
-----

.. i18n:  * hotel_restaurant_tables.form (form)
.. i18n:  * hotel_restaurant_tables.tree (tree)
.. i18n:  * hotel_restaurant_reservation.form (form)
.. i18n:  * hotel_restaurant_reservation.tree (tree)
.. i18n:  * hotel_reservation_order.form (form)
.. i18n:  * hotel_reservation_order.tree (tree)
.. i18n:  * hotel_restaurant_order.form (form)
.. i18n:  * hotel_restaurant_order.tree (tree)
.. i18n:  * hotel_restaurant_kitchen_order_tickets.form (form)
.. i18n:  * hotel_restaurant_kitchen_order_tickets.tree (tree)
.. i18n:  * hotel_menucard_type_form (form)
.. i18n:  * hotel_menucard_type_list (tree)
.. i18n:  * hotel.menucard.form (form)
.. i18n:  * hotel.menucard.tree (tree)
..

 * hotel_restaurant_tables.form (form)
 * hotel_restaurant_tables.tree (tree)
 * hotel_restaurant_reservation.form (form)
 * hotel_restaurant_reservation.tree (tree)
 * hotel_reservation_order.form (form)
 * hotel_reservation_order.tree (tree)
 * hotel_restaurant_order.form (form)
 * hotel_restaurant_order.tree (tree)
 * hotel_restaurant_kitchen_order_tickets.form (form)
 * hotel_restaurant_kitchen_order_tickets.tree (tree)
 * hotel_menucard_type_form (form)
 * hotel_menucard_type_list (tree)
 * hotel.menucard.form (form)
 * hotel.menucard.tree (tree)

.. i18n: Objects
.. i18n: -------
..

Objects
-------

.. i18n: Object: amenities Type (hotel.menucard.type)
.. i18n: ############################################
..

Object: amenities Type (hotel.menucard.type)
############################################

.. i18n: :menu_id: category, many2one, required
..

:menu_id: category, many2one, required

.. i18n: :property_account_expense_categ: Expense Account, many2one
..

:property_account_expense_categ: Expense Account, many2one

.. i18n:     *This account will be used to value outgoing stock for the current product category*
..

    *This account will be used to value outgoing stock for the current product category*

.. i18n: :property_stock_journal: Stock journal, many2one
..

:property_stock_journal: Stock journal, many2one

.. i18n:     *This journal will be used for the accounting move generated by stock move*
..

    *This journal will be used for the accounting move generated by stock move*

.. i18n: :isroomtype: Is Room Type, boolean
..

:isroomtype: Is Room Type, boolean

.. i18n: :name: Name, char, required
..

:name: Name, char, required

.. i18n: :ismenutype: Is Menu Type, boolean
..

:ismenutype: Is Menu Type, boolean

.. i18n: :sequence: Sequence, integer
..

:sequence: Sequence, integer

.. i18n: :isservicetype: Is Service Type, boolean
..

:isservicetype: Is Service Type, boolean

.. i18n: :property_stock_account_input_categ: Stock Input Account, many2one
..

:property_stock_account_input_categ: Stock Input Account, many2one

.. i18n:     *This account will be used to value the input stock*
..

    *This account will be used to value the input stock*

.. i18n: :parent_id: Parent Category, many2one
..

:parent_id: Parent Category, many2one

.. i18n: :complete_name: Name, char, readonly
..

:complete_name: Name, char, readonly

.. i18n: :property_account_income_categ: Income Account, many2one
..

:property_account_income_categ: Income Account, many2one

.. i18n:     *This account will be used to value incoming stock for the current product category*
..

    *This account will be used to value incoming stock for the current product category*

.. i18n: :child_id: Child Categories, one2many
..

:child_id: Child Categories, one2many

.. i18n: :isamenitype: Is amenities Type, boolean
..

:isamenitype: Is amenities Type, boolean

.. i18n: :property_stock_account_output_categ: Stock Output Account, many2one
..

:property_stock_account_output_categ: Stock Output Account, many2one

.. i18n:     *This account will be used to value the output stock*
..

    *This account will be used to value the output stock*

.. i18n: Object: Hotel Menucard (hotel.menucard)
.. i18n: #######################################
..

Object: Hotel Menucard (hotel.menucard)
#######################################

.. i18n: :warranty: Warranty (months), float
..

:warranty: Warranty (months), float

.. i18n: :property_stock_procurement: Procurement Location, many2one
..

:property_stock_procurement: Procurement Location, many2one

.. i18n:     *For the current product (template), this stock location will be used, instead of the default one, as the source location for stock moves generated by procurements*
..

    *For the current product (template), this stock location will be used, instead of the default one, as the source location for stock moves generated by procurements*

.. i18n: :uos_id: Unit of Sale, many2one
..

:uos_id: Unit of Sale, many2one

.. i18n:     *Used by companies that manages two unit of measure: invoicing and stock management. For example, in food industries, you will manage a stock of ham but invoice in Kg. Keep empty to use the default UOM.*
..

    *Used by companies that manages two unit of measure: invoicing and stock management. For example, in food industries, you will manage a stock of ham but invoice in Kg. Keep empty to use the default UOM.*

.. i18n: :list_price: Sale Price, float
..

:list_price: Sale Price, float

.. i18n:     *Base price for computing the customer price. Sometimes called the catalog price.*
..

    *Base price for computing the customer price. Sometimes called the catalog price.*

.. i18n: :ean13: EAN13, char
..

:ean13: EAN13, char

.. i18n: :incoming_qty: Incoming, float, readonly
..

:incoming_qty: Incoming, float, readonly

.. i18n:     *Quantities of products that are planned to arrive in selected locations or all internal if none have been selected.*
..

    *Quantities of products that are planned to arrive in selected locations or all internal if none have been selected.*

.. i18n: :standard_price: Cost Price, float, required
..

:standard_price: Cost Price, float, required

.. i18n:     *The cost of the product for accounting stock valuation. It can serves as a base price for supplier price.*
..

    *The cost of the product for accounting stock valuation. It can serves as a base price for supplier price.*

.. i18n: :mes_type: Measure Type, selection, required
..

:mes_type: Measure Type, selection, required

.. i18n: :code: Code, char, readonly
..

:code: Code, char, readonly

.. i18n: :property_account_income: Income Account, many2one
..

:property_account_income: Income Account, many2one

.. i18n:     *This account will be used instead of the default one to value incoming stock for the current product*
..

    *This account will be used instead of the default one to value incoming stock for the current product*

.. i18n: :qty_available: Real Stock, float, readonly
..

:qty_available: Real Stock, float, readonly

.. i18n:     *Current quantities of products in selected locations or all internal if none have been selected.*
..

    *Current quantities of products in selected locations or all internal if none have been selected.*

.. i18n: :cost_method: Costing Method, selection, required
..

:cost_method: Costing Method, selection, required

.. i18n:     *Standard Price: the cost price is fixed and recomputed periodically (usually at the end of the year), Average Price: the cost price is recomputed at each reception of products.*
..

    *Standard Price: the cost price is fixed and recomputed periodically (usually at the end of the year), Average Price: the cost price is recomputed at each reception of products.*

.. i18n: :uos_coeff: UOM -> UOS Coeff, float
..

:uos_coeff: UOM -> UOS Coeff, float

.. i18n:     *Coefficient to convert UOM to UOS
.. i18n:     uos = uom * coeff*
..

    *Coefficient to convert UOM to UOS
    uos = uom * coeff*

.. i18n: :seller_delay: Supplier Lead Time, integer, readonly
..

:seller_delay: Supplier Lead Time, integer, readonly

.. i18n:     *This is the average delay in days between the purchase order confirmation and the reception of goods for this product and for the default supplier. It is used by the scheduler to order requests based on reordering delays.*
..

    *This is the average delay in days between the purchase order confirmation and the reception of goods for this product and for the default supplier. It is used by the scheduler to order requests based on reordering delays.*

.. i18n: :purchase_ok: Can be Purchased, boolean
..

:purchase_ok: Can be Purchased, boolean

.. i18n:     *Determine if the product is visible in the list of products within a selection from a purchase order line.*
..

    *Determine if the product is visible in the list of products within a selection from a purchase order line.*

.. i18n: :product_manager: Product Manager, many2one
..

:product_manager: Product Manager, many2one

.. i18n: :company_id: Company, many2one
..

:company_id: Company, many2one

.. i18n: :loc_rack: Rack, char
..

:loc_rack: Rack, char

.. i18n: :pricelist_sale: Sale Pricelists, text, readonly
..

:pricelist_sale: Sale Pricelists, text, readonly

.. i18n: :ismenucard: Is Room, boolean
..

:ismenucard: Is Room, boolean

.. i18n: :type: Product Type, selection, required
..

:type: Product Type, selection, required

.. i18n:     *Will change the way procurements are processed. Consumables are stockable products with infinite stock, or for use when you have no stock management in the system.*
..

    *Will change the way procurements are processed. Consumables are stockable products with infinite stock, or for use when you have no stock management in the system.*

.. i18n: :property_stock_account_input: Stock Input Account, many2one
..

:property_stock_account_input: Stock Input Account, many2one

.. i18n:     *This account will be used, instead of the default one, to value input stock*
..

    *This account will be used, instead of the default one, to value input stock*

.. i18n: :track_incoming: Track Incoming Lots, boolean
..

:track_incoming: Track Incoming Lots, boolean

.. i18n:     *Force to use a Production Lot during receptions*
..

    *Force to use a Production Lot during receptions*

.. i18n: :property_stock_production: Production Location, many2one
..

:property_stock_production: Production Location, many2one

.. i18n:     *For the current product (template), this stock location will be used, instead of the default one, as the source location for stock moves generated by production orders*
..

    *For the current product (template), this stock location will be used, instead of the default one, as the source location for stock moves generated by production orders*

.. i18n: :supplier_taxes_id: Supplier Taxes, many2many
..

:supplier_taxes_id: Supplier Taxes, many2many

.. i18n: :volume: Volume, float
..

:volume: Volume, float

.. i18n:     *The volume in m3.*
..

    *The volume in m3.*

.. i18n: :outgoing_qty: Outgoing, float, readonly
..

:outgoing_qty: Outgoing, float, readonly

.. i18n:     *Quantities of products that are planned to leave in selected locations or all internal if none have been selected.*
..

    *Quantities of products that are planned to leave in selected locations or all internal if none have been selected.*

.. i18n: :procure_method: Procure Method, selection, required
..

:procure_method: Procure Method, selection, required

.. i18n:     *'Make to Stock': When needed, take from the stock or wait until re-supplying. 'Make to Order': When needed, purchase or produce for the procurement request.*
..

    *'Make to Stock': When needed, take from the stock or wait until re-supplying. 'Make to Order': When needed, purchase or produce for the procurement request.*

.. i18n: :property_stock_inventory: Inventory Location, many2one
..

:property_stock_inventory: Inventory Location, many2one

.. i18n:     *For the current product (template), this stock location will be used, instead of the default one, as the source location for stock moves generated when you do an inventory*
..

    *For the current product (template), this stock location will be used, instead of the default one, as the source location for stock moves generated when you do an inventory*

.. i18n: :variants: Variants, char
..

:variants: Variants, char

.. i18n: :partner_ref: Customer ref, char, readonly
..

:partner_ref: Customer ref, char, readonly

.. i18n: :rental: Rentable Product, boolean
..

:rental: Rentable Product, boolean

.. i18n: :product_id: Product_id, many2one
..

:product_id: Product_id, many2one

.. i18n: :packaging: Logistical Units, one2many
..

:packaging: Logistical Units, one2many

.. i18n:     *Gives the different ways to package the same product. This has no impact on the packing order and is mainly used if you use the EDI module.*
..

    *Gives the different ways to package the same product. This has no impact on the packing order and is mainly used if you use the EDI module.*

.. i18n: :sale_delay: Customer Lead Time, float
..

:sale_delay: Customer Lead Time, float

.. i18n:     *This is the average time between the confirmation of the customer order and the delivery of the finished products. It's the time you promise to your customers.*
..

    *This is the average time between the confirmation of the customer order and the delivery of the finished products. It's the time you promise to your customers.*

.. i18n: :pricelist_purchase: Purchase Pricelists, text, readonly
..

:pricelist_purchase: Purchase Pricelists, text, readonly

.. i18n: :name: Name, char, required
..

:name: Name, char, required

.. i18n: :description_sale: Sale Description, text
..

:description_sale: Sale Description, text

.. i18n: :property_stock_account_output: Stock Output Account, many2one
..

:property_stock_account_output: Stock Output Account, many2one

.. i18n:     *This account will be used, instead of the default one, to value output stock*
..

    *This account will be used, instead of the default one, to value output stock*

.. i18n: :seller_ids: Partners, one2many
..

:seller_ids: Partners, one2many

.. i18n: :isroom: Is Room, boolean
..

:isroom: Is Room, boolean

.. i18n: :isservice: Is Service id, boolean
..

:isservice: Is Service id, boolean

.. i18n: :track_production: Track Production Lots, boolean
..

:track_production: Track Production Lots, boolean

.. i18n:     *Force to use a Production Lot during production order*
..

    *Force to use a Production Lot during production order*

.. i18n: :supply_method: Supply method, selection, required
..

:supply_method: Supply method, selection, required

.. i18n:     *Produce will generate production order or tasks, according to the product type. Purchase will trigger purchase orders when requested.*
..

    *Produce will generate production order or tasks, according to the product type. Purchase will trigger purchase orders when requested.*

.. i18n: :weight: Gross weight, float
..

:weight: Gross weight, float

.. i18n:     *The gross weight in Kg.*
..

    *The gross weight in Kg.*

.. i18n: :price_extra: Variant Price Extra, float
..

:price_extra: Variant Price Extra, float

.. i18n: :uom_id: Default UoM, many2one, required
..

:uom_id: Default UoM, many2one, required

.. i18n:     *Default Unit of Measure used for all stock operation.*
..

    *Default Unit of Measure used for all stock operation.*

.. i18n: :description_purchase: Purchase Description, text
..

:description_purchase: Purchase Description, text

.. i18n: :default_code: Code, char
..

:default_code: Code, char

.. i18n: :iscategid: Is categ id, boolean
..

:iscategid: Is categ id, boolean

.. i18n: :virtual_available: Virtual Stock, float, readonly
..

:virtual_available: Virtual Stock, float, readonly

.. i18n:     *Future stock for this product according to the selected location or all internal if none have been selected. Computed as: Real Stock - Outgoing + Incoming.*
..

    *Future stock for this product according to the selected location or all internal if none have been selected. Computed as: Real Stock - Outgoing + Incoming.*

.. i18n: :track_outgoing: Track Outgoing Lots, boolean
..

:track_outgoing: Track Outgoing Lots, boolean

.. i18n:     *Force to use a Production Lot during deliveries*
..

    *Force to use a Production Lot during deliveries*

.. i18n: :product_tmpl_id: Product Template, many2one, required
..

:product_tmpl_id: Product Template, many2one, required

.. i18n: :state: Status, selection
..

:state: Status, selection

.. i18n:     *Tells the user if he can use the product or not.*
..

    *Tells the user if he can use the product or not.*

.. i18n: :uom_po_id: Purchase UoM, many2one, required
..

:uom_po_id: Purchase UoM, many2one, required

.. i18n:     *Default Unit of Measure used for purchase orders. It must be in the same category as the default unit of measure.*
..

    *Default Unit of Measure used for purchase orders. It must be in the same category as the default unit of measure.*

.. i18n: :weight_net: Net weight, float
..

:weight_net: Net weight, float

.. i18n:     *The net weight in Kg.*
..

    *The net weight in Kg.*

.. i18n: :description: Description, text
..

:description: Description, text

.. i18n: :price: Customer Price, float, readonly
..

:price: Customer Price, float, readonly

.. i18n: :active: Active, boolean
..

:active: Active, boolean

.. i18n: :loc_row: Row, char
..

:loc_row: Row, char

.. i18n: :sale_ok: Can be sold, boolean
..

:sale_ok: Can be sold, boolean

.. i18n:     *Determine if the product can be visible in the list of product within a selection from a sale order line.*
..

    *Determine if the product can be visible in the list of product within a selection from a sale order line.*

.. i18n: :loc_case: Case, char
..

:loc_case: Case, char

.. i18n: :produce_delay: Manufacturing Lead Time, float
..

:produce_delay: Manufacturing Lead Time, float

.. i18n:     *Average time to produce this product. This is only for the production order and, if it is a multi-level bill of material, it's only for the level of this product. Different delays will be summed for all levels and purchase orders.*
..

    *Average time to produce this product. This is only for the production order and, if it is a multi-level bill of material, it's only for the level of this product. Different delays will be summed for all levels and purchase orders.*

.. i18n: :property_account_expense: Expense Account, many2one
..

:property_account_expense: Expense Account, many2one

.. i18n:     *This account will be used instead of the default one to value outgoing stock for the current product*
..

    *This account will be used instead of the default one to value outgoing stock for the current product*

.. i18n: :categ_id: Category, many2one, required
..

:categ_id: Category, many2one, required

.. i18n: :lst_price: List Price, float, readonly
..

:lst_price: List Price, float, readonly

.. i18n: :taxes_id: Customer Taxes, many2many
..

:taxes_id: Customer Taxes, many2many

.. i18n: :price_margin: Variant Price Margin, float
..

:price_margin: Variant Price Margin, float

.. i18n: Object: Includes Hotel Restaurant Table (hotel.restaurant.tables)
.. i18n: #################################################################
..

Object: Includes Hotel Restaurant Table (hotel.restaurant.tables)
#################################################################

.. i18n: :capacity: Capacity, integer
..

:capacity: Capacity, integer

.. i18n: :name: Table number, char, required
..

:name: Table number, char, required

.. i18n: Object: Includes Hotel Restaurant Reservation (hotel.restaurant.reservation)
.. i18n: ############################################################################
..

Object: Includes Hotel Restaurant Reservation (hotel.restaurant.reservation)
############################################################################

.. i18n: :room_no: Room No, many2one
..

:room_no: Room No, many2one

.. i18n: :end_date: End Date, datetime, required
..

:end_date: End Date, datetime, required

.. i18n: :tableno: Table number, many2many
..

:tableno: Table number, many2many

.. i18n: :partner_address_id: Address, many2one
..

:partner_address_id: Address, many2one

.. i18n: :state: state, selection, required, readonly
..

:state: state, selection, required, readonly

.. i18n: :cname: Customer Name, many2one, required
..

:cname: Customer Name, many2one, required

.. i18n: :reservation_id: Reservation No, char, required
..

:reservation_id: Reservation No, char, required

.. i18n: :start_date: Start Date, datetime, required
..

:start_date: Start Date, datetime, required

.. i18n: Object: Includes Hotel Restaurant Order (hotel.restaurant.kitchen.order.tickets)
.. i18n: ################################################################################
..

Object: Includes Hotel Restaurant Order (hotel.restaurant.kitchen.order.tickets)
################################################################################

.. i18n: :tableno: Table number, many2many
..

:tableno: Table number, many2many

.. i18n: :room_no: Room No, char, readonly
..

:room_no: Room No, char, readonly

.. i18n: :w_name: Waiter Name, char, readonly
..

:w_name: Waiter Name, char, readonly

.. i18n: :kot_date: Date, datetime
..

:kot_date: Date, datetime

.. i18n: :orderno: Order Number, char, readonly
..

:orderno: Order Number, char, readonly

.. i18n: :resno: Reservation Number, char
..

:resno: Reservation Number, char

.. i18n: :kot_list: Order List, one2many
..

:kot_list: Order List, one2many

.. i18n: Object: Includes Hotel Restaurant Order (hotel.restaurant.order)
.. i18n: ################################################################
..

Object: Includes Hotel Restaurant Order (hotel.restaurant.order)
################################################################

.. i18n: :order_no: Order Number, char, required
..

:order_no: Order Number, char, required

.. i18n: :room_no: Room No, many2one
..

:room_no: Room No, many2one

.. i18n: :tax: Tax (%) , float
..

:tax: Tax (%) , float

.. i18n: :table_no: Table number, many2many
..

:table_no: Table number, many2many

.. i18n: :amount_subtotal: Subtotal, float, readonly
..

:amount_subtotal: Subtotal, float, readonly

.. i18n: :o_date: Date, datetime, required
..

:o_date: Date, datetime, required

.. i18n: :order_list: Order List, one2many
..

:order_list: Order List, one2many

.. i18n: :amount_total: Total, float, readonly
..

:amount_total: Total, float, readonly

.. i18n: :waiter_name: Waiter Name, many2one, required
..

:waiter_name: Waiter Name, many2one, required

.. i18n: Object: Reservation Order (hotel.reservation.order)
.. i18n: ###################################################
..

Object: Reservation Order (hotel.reservation.order)
###################################################

.. i18n: :date1: Date, datetime, required
..

:date1: Date, datetime, required

.. i18n: :waitername: Waiter Name, many2one
..

:waitername: Waiter Name, many2one

.. i18n: :amount_subtotal: Subtotal, float, readonly
..

:amount_subtotal: Subtotal, float, readonly

.. i18n: :reservationno: Reservation No, char
..

:reservationno: Reservation No, char

.. i18n: :tax: Tax (%) , float
..

:tax: Tax (%) , float

.. i18n: :order_list: Order List, one2many
..

:order_list: Order List, one2many

.. i18n: :order_number: Order No, char
..

:order_number: Order No, char

.. i18n: :table_no: Table number, many2many
..

:table_no: Table number, many2many

.. i18n: :amount_total: Total, float, readonly
..

:amount_total: Total, float, readonly

.. i18n: Object: Includes Hotel Restaurant Order (hotel.restaurant.order.list)
.. i18n: #####################################################################
..

Object: Includes Hotel Restaurant Order (hotel.restaurant.order.list)
#####################################################################

.. i18n: :o_list: unknown, many2one
..

:o_list: unknown, many2one

.. i18n: :item_qty: Qty, char, required
..

:item_qty: Qty, char, required

.. i18n: :name: Item Name, many2one, required
..

:name: Item Name, many2one, required

.. i18n: :kot_order_list: unknown, many2one
..

:kot_order_list: unknown, many2one

.. i18n: :price_subtotal: Subtotal, float, readonly
..

:price_subtotal: Subtotal, float, readonly

.. i18n: :o_l: unknown, many2one
..

:o_l: unknown, many2one

.. i18n: :item_rate: Rate, float
..

:item_rate: Rate, float
