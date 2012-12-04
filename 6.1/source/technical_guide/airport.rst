
.. module:: airport
    :synopsis: Airport 
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

    <div class="js-kit-rating" title="" permalink="" standalone="yes" path="/airport"></div>
    <script src="http://js-kit.com/ratings.js"></script>

Airport (*airport*)
===================
:Module: airport
:Name: Airport
:Version: 5.0.1.0
:Author: Tiny
:Directory: airport
:Web: 
:Official module: no
:Quality certified: no

Description
-----------

::

  Sample module to manage airport, flights and hostels

Download links
--------------

You can download this module as a zip file in the following version:

  * `5.0 <http://www.openerp.com/download/modules/5.0/airport.zip>`_
  * `trunk <http://www.openerp.com/download/modules/trunk/airport.zip>`_


Dependencies
------------

 * :mod:`base`
 * :mod:`product`

Reports
-------

None


Menus
-------

 * Airports
 * Airports/Configuration
 * Airports/Configuration/Airport
 * Airports/Air Lines
 * Airports/Configuration/Flights

Views
-----

 * airport.airport (tree)
 * airport.airport (form)
 * airport.flight (form)


Objects
-------

Object: airport.airport (airport.airport)
#########################################



:city: City, char





:country_id: Country, many2one





:lines: Flight lines, many2many





:name: Airport name, char




Object: Product (airport.flight)
################################



:warranty: Warranty (months), float





:ean13: EAN13, char





:supply_method: Supply method, selection, required

    *Produce will generate production order or tasks, according to the product type. Purchase will trigger purchase orders when requested.*



:uos_id: Unit of Sale, many2one

    *Used by companies that manages two unit of measure: invoicing and stock management. For example, in food industries, you will manage a stock of ham but invoice in Kg. Keep empty to use the default UOM.*



:list_price: Sale Price, float

    *Base price for computing the customer price. Sometimes called the catalog price.*



:weight: Gross weight, float

    *The gross weight in Kg.*



:incoming_qty: Incoming, float, readonly





:standard_price: Cost Price, float, required

    *The cost of the product for accounting stock valuation. It can serves as a base price for supplier price.*



:price_extra: Variant Price Extra, float





:mes_type: Measure Type, selection, required





:uom_id: Default UoM, many2one, required

    *Default Unit of Measure used for all stock operation.*



:code: Code, char, readonly





:description_purchase: Purchase Description, text





:default_code: Code, char





:qty_available: Real Stock, float, readonly





:partner_id: Customer, many2one





:variants: Variants, char





:uos_coeff: UOM -> UOS Coeff, float

    *Coefficient to convert UOM to UOS
    uos = uom * coeff*



:product_tmpl_id: Product Template, many2one, required





:date: Departure Date, datetime





:seller_delay: Supplier Lead Time, integer, readonly

    *This is the average delay in days between the purchase order confirmation and the reception of goods for this product and for the default supplier. It is used by the scheduler to order requests based on reordering delays.*



:purchase_ok: Can be Purchased, boolean

    *Determine if the product is visible in the list of products within a selection from a purchase order line.*



:product_manager: Product Manager, many2one





:company_id: Company, many2one





:name: Name, char, required





:active: Active, boolean





:state: Status, selection

    *Tells the user if he can use the product or not.*



:loc_rack: Rack, char





:uom_po_id: Purchase UoM, many2one, required

    *Default Unit of Measure used for purchase orders. It must be in the same category as the default unit of measure.*



:type: Product Type, selection, required

    *Will change the way procurements are processed. Consumables are stockable products with infinite stock, or for use when you have no stock management in the system.*



:price: Customer Price, float, readonly





:description: Description, text





:weight_net: Net weight, float

    *The net weight in Kg.*



:volume: Volume, float

    *The volume in m3.*



:airport_from: Airport Departure, many2one





:outgoing_qty: Outgoing, float, readonly





:procure_method: Procure Method, selection, required

    *'Make to Stock': When needed, take from the stock or wait until re-supplying. 'Make to Order': When needed, purchase or produce for the procurement request.*



:virtual_available: Virtual Stock, float, readonly





:cost_method: Costing Method, selection, required

    *Standard Price: the cost price is fixed and recomputed periodically (usually at the end of the year), Average Price: the cost price is recomputed at each reception of products.*



:partner_ref: Customer ref, char, readonly





:loc_row: Row, char





:sale_ok: Can be sold, boolean

    *Determine if the product can be visible in the list of product within a selection from a sale order line.*



:rental: Rentable Product, boolean





:packaging: Logistical Units, one2many

    *Gives the different ways to package the same product. This has no impact on the packing order and is mainly used if you use the EDI module.*



:sale_delay: Customer Lead Time, float

    *This is the average time between the confirmation of the customer order and the delivery of the finished products. It's the time you promise to your customers.*



:loc_case: Case, char





:description_sale: Sale Description, text





:categ_id: Category, many2one, required





:lst_price: List Price, float, readonly





:produce_delay: Manufacturing Lead Time, float

    *Average time to produce this product. This is only for the production order and, if it is a multi-level bill of material, it's only for the level of this product. Different delays will be summed for all levels and purchase orders.*



:seller_ids: Partners, one2many





:airport_to: Airport Arrival, many2one





:price_margin: Variant Price Margin, float


