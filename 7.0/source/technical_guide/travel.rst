
.. module:: travel
    :synopsis: Travel Management 
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

    <div class="js-kit-rating" title="" permalink="" standalone="yes" path="/travel"></div>
    <script src="http://js-kit.com/ratings.js"></script>

Travel Management (*travel*)
============================
:Module: travel
:Name: Travel Management
:Version: 5.0.1.0
:Author: Tiny
:Directory: travel
:Web: 
:Official module: no
:Quality certified: no

Description
-----------

::

  None

Download links
--------------

You can download this module as a zip file in the following version:

  * `5.0 <http://www.openerp.com/download/modules/5.0/travel.zip>`_
  * `trunk <http://www.openerp.com/download/modules/trunk/travel.zip>`_


Dependencies
------------

 * :mod:`base`
 * :mod:`product`

Reports
-------

None


Menus
-------

 * Travel Agency
 * Travel Agency/Hostels
 * Travel Agency/Rooms
 * Travel Agency/Rooms/Single Rooms
 * Travel Agency/Rooms/Double Rooms
 * Travel Agency/Airports
 * Travel Agency/Flights

Views
-----

 * travel.flight (form)
 * travel.room (form)
 * travel.room (tree)
 * travel.hostel (form)


Objects
-------

Object: Partner (travel.hostel)
###############################



:comment: Notes, text





:ean13: EAN13, char





:rooms_id: Rooms, one2many





:active: Active, boolean





:property_product_pricelist: Sale Pricelist, many2one

    *This pricelist will be used, instead of the default one,                     for sales to the current partner*



:quality: Quality, char





:city: City, char





:user_id: Dedicated Salesman, many2one

    *The internal user that is in charge of communicating with this partner if any.*



:title: Title, selection





:parent_id: Main Company, many2one





:supplier: Supplier, boolean

    *Check this box if the partner is a supplier. If unchecked, purchasing staff will not see it when encoding a purchase order.*



:ref: Code, char





:events: Events, one2many





:vat: VAT, char

    *Value Added Tax number. Check the box if the partner is subjected to the VAT. Used by the VAT legal statement.*



:website: Website, char





:lang: Language, selection

    *If the selected language is loaded in the system, all documents related to this partner will be printed in that language. If not, it will be English.*



:bank_ids: Banks, one2many





:child_ids: Partner Ref., one2many





:address: Contacts, one2many





:date: Date, date





:customer: Customer, boolean

    *Check this box if the partner is a customer.*



:credit_limit: Credit Limit, float





:name: Name, char, required





:country: Country, many2one





:category_id: Categories, many2many




Object: travel.airport (travel.airport)
#######################################



:city: City, char





:name: Airport name, char





:country: Country, many2one




Object: Product (travel.room)
#############################



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



:hostel_id: Hostel, many2one





:code: Code, char, readonly





:description_purchase: Purchase Description, text





:default_code: Code, char





:qty_available: Real Stock, float, readonly





:variants: Variants, char





:uos_coeff: UOM -> UOS Coeff, float

    *Coefficient to convert UOM to UOS
    uos = uom * coeff*



:product_tmpl_id: Product Template, many2one, required





:virtual_available: Virtual Stock, float, readonly





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



:outgoing_qty: Outgoing, float, readonly





:procure_method: Procure Method, selection, required

    *'Make to Stock': When needed, take from the stock or wait until re-supplying. 'Make to Order': When needed, purchase or produce for the procurement request.*



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





:beds: Nbr of Beds, integer





:lst_price: List Price, float, readonly





:produce_delay: Manufacturing Lead Time, float

    *Average time to produce this product. This is only for the production order and, if it is a multi-level bill of material, it's only for the level of this product. Different delays will be summed for all levels and purchase orders.*



:seller_ids: Partners, one2many





:view: Room View, selection





:price_margin: Variant Price Margin, float




Object: Product (travel.flight)
###############################



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





:partner_id: Partner, many2one





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


