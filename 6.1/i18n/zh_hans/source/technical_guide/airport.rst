
.. i18n: .. module:: airport
.. i18n:     :synopsis: Airport 
.. i18n:     :noindex:
.. i18n: .. 
..

.. module:: airport
    :synopsis: Airport 
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
.. i18n:     <div class="js-kit-rating" title="" permalink="" standalone="yes" path="/airport"></div>
.. i18n:     <script src="http://js-kit.com/ratings.js"></script>
..

.. raw:: html

    <div class="js-kit-rating" title="" permalink="" standalone="yes" path="/airport"></div>
    <script src="http://js-kit.com/ratings.js"></script>

.. i18n: Airport (*airport*)
.. i18n: ===================
.. i18n: :Module: airport
.. i18n: :Name: Airport
.. i18n: :Version: 5.0.1.0
.. i18n: :Author: Tiny
.. i18n: :Directory: airport
.. i18n: :Web: 
.. i18n: :Official module: no
.. i18n: :Quality certified: no
..

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

.. i18n: Description
.. i18n: -----------
..

Description
-----------

.. i18n: ::
.. i18n: 
.. i18n:   Sample module to manage airport, flights and hostels
..

::

  Sample module to manage airport, flights and hostels

.. i18n: Download links
.. i18n: --------------
..

Download links
--------------

.. i18n: You can download this module as a zip file in the following version:
..

You can download this module as a zip file in the following version:

.. i18n:   * `5.0 <http://www.openerp.com/download/modules/5.0/airport.zip>`_
.. i18n:   * `trunk <http://www.openerp.com/download/modules/trunk/airport.zip>`_
..

  * `5.0 <http://www.openerp.com/download/modules/5.0/airport.zip>`_
  * `trunk <http://www.openerp.com/download/modules/trunk/airport.zip>`_

.. i18n: Dependencies
.. i18n: ------------
..

Dependencies
------------

.. i18n:  * :mod:`base`
.. i18n:  * :mod:`product`
..

 * :mod:`base`
 * :mod:`product`

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

.. i18n:  * Airports
.. i18n:  * Airports/Configuration
.. i18n:  * Airports/Configuration/Airport
.. i18n:  * Airports/Air Lines
.. i18n:  * Airports/Configuration/Flights
..

 * Airports
 * Airports/Configuration
 * Airports/Configuration/Airport
 * Airports/Air Lines
 * Airports/Configuration/Flights

.. i18n: Views
.. i18n: -----
..

Views
-----

.. i18n:  * airport.airport (tree)
.. i18n:  * airport.airport (form)
.. i18n:  * airport.flight (form)
..

 * airport.airport (tree)
 * airport.airport (form)
 * airport.flight (form)

.. i18n: Objects
.. i18n: -------
..

Objects
-------

.. i18n: Object: airport.airport (airport.airport)
.. i18n: #########################################
..

Object: airport.airport (airport.airport)
#########################################

.. i18n: :city: City, char
..

:city: City, char

.. i18n: :country_id: Country, many2one
..

:country_id: Country, many2one

.. i18n: :lines: Flight lines, many2many
..

:lines: Flight lines, many2many

.. i18n: :name: Airport name, char
..

:name: Airport name, char

.. i18n: Object: Product (airport.flight)
.. i18n: ################################
..

Object: Product (airport.flight)
################################

.. i18n: :warranty: Warranty (months), float
..

:warranty: Warranty (months), float

.. i18n: :ean13: EAN13, char
..

:ean13: EAN13, char

.. i18n: :supply_method: Supply method, selection, required
..

:supply_method: Supply method, selection, required

.. i18n:     *Produce will generate production order or tasks, according to the product type. Purchase will trigger purchase orders when requested.*
..

    *Produce will generate production order or tasks, according to the product type. Purchase will trigger purchase orders when requested.*

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

.. i18n: :weight: Gross weight, float
..

:weight: Gross weight, float

.. i18n:     *The gross weight in Kg.*
..

    *The gross weight in Kg.*

.. i18n: :incoming_qty: Incoming, float, readonly
..

:incoming_qty: Incoming, float, readonly

.. i18n: :standard_price: Cost Price, float, required
..

:standard_price: Cost Price, float, required

.. i18n:     *The cost of the product for accounting stock valuation. It can serves as a base price for supplier price.*
..

    *The cost of the product for accounting stock valuation. It can serves as a base price for supplier price.*

.. i18n: :price_extra: Variant Price Extra, float
..

:price_extra: Variant Price Extra, float

.. i18n: :mes_type: Measure Type, selection, required
..

:mes_type: Measure Type, selection, required

.. i18n: :uom_id: Default UoM, many2one, required
..

:uom_id: Default UoM, many2one, required

.. i18n:     *Default Unit of Measure used for all stock operation.*
..

    *Default Unit of Measure used for all stock operation.*

.. i18n: :code: Code, char, readonly
..

:code: Code, char, readonly

.. i18n: :description_purchase: Purchase Description, text
..

:description_purchase: Purchase Description, text

.. i18n: :default_code: Code, char
..

:default_code: Code, char

.. i18n: :qty_available: Real Stock, float, readonly
..

:qty_available: Real Stock, float, readonly

.. i18n: :partner_id: Customer, many2one
..

:partner_id: Customer, many2one

.. i18n: :variants: Variants, char
..

:variants: Variants, char

.. i18n: :uos_coeff: UOM -> UOS Coeff, float
..

:uos_coeff: UOM -> UOS Coeff, float

.. i18n:     *Coefficient to convert UOM to UOS
.. i18n:     uos = uom * coeff*
..

    *Coefficient to convert UOM to UOS
    uos = uom * coeff*

.. i18n: :product_tmpl_id: Product Template, many2one, required
..

:product_tmpl_id: Product Template, many2one, required

.. i18n: :date: Departure Date, datetime
..

:date: Departure Date, datetime

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

.. i18n: :name: Name, char, required
..

:name: Name, char, required

.. i18n: :active: Active, boolean
..

:active: Active, boolean

.. i18n: :state: Status, selection
..

:state: Status, selection

.. i18n:     *Tells the user if he can use the product or not.*
..

    *Tells the user if he can use the product or not.*

.. i18n: :loc_rack: Rack, char
..

:loc_rack: Rack, char

.. i18n: :uom_po_id: Purchase UoM, many2one, required
..

:uom_po_id: Purchase UoM, many2one, required

.. i18n:     *Default Unit of Measure used for purchase orders. It must be in the same category as the default unit of measure.*
..

    *Default Unit of Measure used for purchase orders. It must be in the same category as the default unit of measure.*

.. i18n: :type: Product Type, selection, required
..

:type: Product Type, selection, required

.. i18n:     *Will change the way procurements are processed. Consumables are stockable products with infinite stock, or for use when you have no stock management in the system.*
..

    *Will change the way procurements are processed. Consumables are stockable products with infinite stock, or for use when you have no stock management in the system.*

.. i18n: :price: Customer Price, float, readonly
..

:price: Customer Price, float, readonly

.. i18n: :description: Description, text
..

:description: Description, text

.. i18n: :weight_net: Net weight, float
..

:weight_net: Net weight, float

.. i18n:     *The net weight in Kg.*
..

    *The net weight in Kg.*

.. i18n: :volume: Volume, float
..

:volume: Volume, float

.. i18n:     *The volume in m3.*
..

    *The volume in m3.*

.. i18n: :airport_from: Airport Departure, many2one
..

:airport_from: Airport Departure, many2one

.. i18n: :outgoing_qty: Outgoing, float, readonly
..

:outgoing_qty: Outgoing, float, readonly

.. i18n: :procure_method: Procure Method, selection, required
..

:procure_method: Procure Method, selection, required

.. i18n:     *'Make to Stock': When needed, take from the stock or wait until re-supplying. 'Make to Order': When needed, purchase or produce for the procurement request.*
..

    *'Make to Stock': When needed, take from the stock or wait until re-supplying. 'Make to Order': When needed, purchase or produce for the procurement request.*

.. i18n: :virtual_available: Virtual Stock, float, readonly
..

:virtual_available: Virtual Stock, float, readonly

.. i18n: :cost_method: Costing Method, selection, required
..

:cost_method: Costing Method, selection, required

.. i18n:     *Standard Price: the cost price is fixed and recomputed periodically (usually at the end of the year), Average Price: the cost price is recomputed at each reception of products.*
..

    *Standard Price: the cost price is fixed and recomputed periodically (usually at the end of the year), Average Price: the cost price is recomputed at each reception of products.*

.. i18n: :partner_ref: Customer ref, char, readonly
..

:partner_ref: Customer ref, char, readonly

.. i18n: :loc_row: Row, char
..

:loc_row: Row, char

.. i18n: :sale_ok: Can be sold, boolean
..

:sale_ok: Can be sold, boolean

.. i18n:     *Determine if the product can be visible in the list of product within a selection from a sale order line.*
..

    *Determine if the product can be visible in the list of product within a selection from a sale order line.*

.. i18n: :rental: Rentable Product, boolean
..

:rental: Rentable Product, boolean

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

.. i18n: :loc_case: Case, char
..

:loc_case: Case, char

.. i18n: :description_sale: Sale Description, text
..

:description_sale: Sale Description, text

.. i18n: :categ_id: Category, many2one, required
..

:categ_id: Category, many2one, required

.. i18n: :lst_price: List Price, float, readonly
..

:lst_price: List Price, float, readonly

.. i18n: :produce_delay: Manufacturing Lead Time, float
..

:produce_delay: Manufacturing Lead Time, float

.. i18n:     *Average time to produce this product. This is only for the production order and, if it is a multi-level bill of material, it's only for the level of this product. Different delays will be summed for all levels and purchase orders.*
..

    *Average time to produce this product. This is only for the production order and, if it is a multi-level bill of material, it's only for the level of this product. Different delays will be summed for all levels and purchase orders.*

.. i18n: :seller_ids: Partners, one2many
..

:seller_ids: Partners, one2many

.. i18n: :airport_to: Airport Arrival, many2one
..

:airport_to: Airport Arrival, many2one

.. i18n: :price_margin: Variant Price Margin, float
..

:price_margin: Variant Price Margin, float
