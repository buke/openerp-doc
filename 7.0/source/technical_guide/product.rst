
.. module:: product
    :synopsis: Products & Pricelists (Official, Quality Certified)
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

    <div class="js-kit-rating" title="" permalink="" standalone="yes" path="/product"></div>
    <script src="http://js-kit.com/ratings.js"></script>

Products & Pricelists (*product*)
=================================
:Module: product
:Name: Products & Pricelists
:Version: 5.0.1.1
:Author: Tiny
:Directory: product
:Web: 
:Official module: yes
:Quality certified: yes

Description
-----------

::

  This is the base module for managing products and pricelists in OpenERP.
  
      Products support variants, different pricing methods, suppliers
      information, make to stock/order, different unit of measures,
      packaging and properties.
  
      Pricelists support:
      * Multiple-level of discount (by product, category, quantities)
      * Compute price based on different criteria:
          * Other pricelist,
          * Cost price,
          * List price,
          * Supplier price, ...
      Pricelists preferences by product and/or partners.
  
      Print product labels with barcode.

Download links
--------------

You can download this module as a zip file in the following version:

  * `4.2 <http://www.openerp.com/download/modules/4.2/product.zip>`_
  * `5.0 <http://www.openerp.com/download/modules/5.0/product.zip>`_
  * `trunk <http://www.openerp.com/download/modules/trunk/product.zip>`_


Dependencies
------------

 * :mod:`base`
 * :mod:`process`

Reports
-------

 * Products Labels

 * Product Pricelist

Menus
-------

 * Products
 * Products/Configuration
 * Products/Products
 * Products/Products by Category
 * Products/Configuration/Products Categories
 * Products/Configuration/Units of Measure
 * Products/Configuration/Units of Measure/Units of Measure
 * Products/Configuration/Units of Measure/Units of Measure Categories
 * Products/Configuration/Packaging
 * Products/Pricelists
 * Products/Pricelists/Pricelist Versions
 * Products/Pricelists/Pricelists
 * Products/Configuration/Prices Computations
 * Products/Configuration/Prices Computations/Prices Types
 * Products/Configuration/Prices Computations/Pricelists Types

Views
-----

 * product.product.tree (tree)
 * product.normal.form (form)
 * product.category.form (form)
 * product.category.list (tree)
 * product.category.tree (tree)
 * product.uom.tree (tree)
 * product.uom.form (form)
 * product.uom.categ.form (form)
 * product.ul.form.view (form)
 * product.ul.tree (tree)
 * product.packaging.tree.view (tree)
 * product.packaging.form.view (form)
 * product.supplierinfo.form.view (form)
 * product.supplierinfo.tree.view (tree)
 * product.variant.form (form)
 * product.variant.tree (tree)
 * product.template.product.tree (tree)
 * product.template.product.form (form)
 * product.pricelist.version.form (form)
 * product.pricelist.version.tree (tree)
 * product.pricelist.item.tree (tree)
 * product.pricelist.item.form (form)
 * product.pricelist.tree (tree)
 * product.pricelist.form (form)
 * product.price.type.form (form)
 * product.pricelist.type.form (form)
 * \* INHERIT res.partner.product.property.form.inherit (form)


Objects
-------

Object: Product uom categ (product.uom.categ)
#############################################



:name: Name, char, required




Object: Product Unit of Measure (product.uom)
#############################################



:name: Name, char, required





:factor_inv: Factor, float, readonly

    *The coefficient for the formula:
    coeff (base unit) = 1 (this unit). Factor = 1 / Rate.*



:rounding: Rounding Precision, float, required

    *The computed quantity will be a multiple of this value. Use 1.0 for products that can not be split.*



:factor: Rate, float, required

    *The coefficient for the formula:
    1 (base unit) = coeff (this unit). Rate = 1 / Factor.*



:active: Active, boolean





:category_id: UoM Category, many2one, required

    *Unit of Measure of a category can be converted between each others in the same category.*



:factor_inv_data: Factor, float




Object: Shipping Unit (product.ul)
##################################



:type: Type, selection, required





:name: Name, char, required




Object: Product Category (product.category)
###########################################



:parent_id: Parent Category, many2one





:child_id: Child Categories, one2many





:complete_name: Name, char, readonly





:name: Name, char, required





:sequence: Sequence, integer




Object: Product Template (product.template)
###########################################



:warranty: Warranty (months), float





:supply_method: Supply method, selection, required

    *Produce will generate production order or tasks, according to the product type. Purchase will trigger purchase orders when requested.*



:uos_id: Unit of Sale, many2one

    *Used by companies that manages two unit of measure: invoicing and stock management. For example, in food industries, you will manage a stock of ham but invoice in Kg. Keep empty to use the default UOM.*



:list_price: Sale Price, float

    *Base price for computing the customer price. Sometimes called the catalog price.*



:weight: Gross weight, float

    *The gross weight in Kg.*



:standard_price: Cost Price, float, required

    *The cost of the product for accounting stock valuation. It can serves as a base price for supplier price.*



:mes_type: Measure Type, selection, required





:uom_id: Default UoM, many2one, required

    *Default Unit of Measure used for all stock operation.*



:description_purchase: Purchase Description, text





:uos_coeff: UOM -> UOS Coeff, float

    *Coefficient to convert UOM to UOS
    uos = uom * coeff*



:seller_delay: Supplier Lead Time, integer, readonly

    *This is the average delay in days between the purchase order confirmation and the reception of goods for this product and for the default supplier. It is used by the scheduler to order requests based on reordering delays.*



:purchase_ok: Can be Purchased, boolean

    *Determine if the product is visible in the list of products within a selection from a purchase order line.*



:product_manager: Product Manager, many2one





:company_id: Company, many2one





:state: Status, selection

    *Tells the user if he can use the product or not.*



:loc_rack: Rack, char





:uom_po_id: Purchase UoM, many2one, required

    *Default Unit of Measure used for purchase orders. It must be in the same category as the default unit of measure.*



:type: Product Type, selection, required

    *Will change the way procurements are processed. Consumables are stockable products with infinite stock, or for use when you have no stock management in the system.*



:loc_case: Case, char





:description: Description, text





:weight_net: Net weight, float

    *The net weight in Kg.*



:volume: Volume, float

    *The volume in m3.*



:procure_method: Procure Method, selection, required

    *'Make to Stock': When needed, take from the stock or wait until re-supplying. 'Make to Order': When needed, purchase or produce for the procurement request.*



:cost_method: Costing Method, selection, required

    *Standard Price: the cost price is fixed and recomputed periodically (usually at the end of the year), Average Price: the cost price is recomputed at each reception of products.*



:loc_row: Row, char





:sale_ok: Can be sold, boolean

    *Determine if the product can be visible in the list of product within a selection from a sale order line.*



:rental: Rentable Product, boolean





:sale_delay: Customer Lead Time, float

    *This is the average time between the confirmation of the customer order and the delivery of the finished products. It's the time you promise to your customers.*



:name: Name, char, required





:description_sale: Sale Description, text





:categ_id: Category, many2one, required





:produce_delay: Manufacturing Lead Time, float

    *Average time to produce this product. This is only for the production order and, if it is a multi-level bill of material, it's only for the level of this product. Different delays will be summed for all levels and purchase orders.*



:seller_ids: Partners, one2many




Object: Product (product.product)
#################################



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





:lst_price: List Price, float, readonly





:produce_delay: Manufacturing Lead Time, float

    *Average time to produce this product. This is only for the production order and, if it is a multi-level bill of material, it's only for the level of this product. Different delays will be summed for all levels and purchase orders.*



:seller_ids: Partners, one2many





:price_margin: Variant Price Margin, float




Object: Packaging (product.packaging)
#####################################



:code: Code, char

    *The code of the transport unit.*



:product_id: Product, many2one, required





:weight: Total Package Weight, float

    *The weight of a full of products palet or box.*



:sequence: Sequence, integer





:ul_qty: Package by layer, integer





:ean: EAN, char

    *The EAN code of the package unit.*



:qty: Quantity by Package, float

    *The total number of products you can put by palet or box.*



:ul: Type of Package, many2one, required





:length: Length, float

    *The length of the package*



:rows: Number of Layer, integer, required

    *The number of layer on a palet or box*



:weight_ul: Empty Package Weight, float

    *The weight of the empty UL*



:height: Height, float

    *The height of the package*



:width: Width, float

    *The width of the package*



:name: Description, char




Object: Information about a product supplier (product.supplierinfo)
###################################################################



:pricelist_ids: Supplier Pricelist, one2many





:product_id: Product, many2one, required





:sequence: Priority, integer





:qty: Minimal Quantity, float, required

    *The minimal quantity to purchase for this supplier, expressed in the default unit of measure.*



:delay: Delivery Delay, integer, required

    *Delay in days between the confirmation of the purchase order and the reception of the products in your warehouse. Used by the scheduler for automatic computation of the purchase order planning.*



:product_code: Partner Product Code, char

    *Code of the product for this partner, will be used when printing a request for quotation. Keep empty to use the internal one.*



:product_name: Partner Product Name, char

    *Name of the product for this partner, will be used when printing a request for quotation. Keep empty to use the internal one.*



:name: Partner, many2one, required

    *Supplier of this product*


Object: pricelist.partnerinfo (pricelist.partnerinfo)
#####################################################



:min_quantity: Quantity, float, required





:price: Unit Price, float, required





:suppinfo_id: Partner Information, many2one, required





:name: Description, char




Object: Price type (product.price.type)
#######################################



:active: Active, boolean





:field: Product Field, selection, required

    *Associated field in the product form.*



:currency_id: Currency, many2one, required

    *The currency the field is expressed in.*



:name: Price Name, char, required

    *Name of this kind of price.*


Object: Pricelist Type (product.pricelist.type)
###############################################



:name: Name, char, required





:key: Key, char, required

    *Used in the code to select specific prices based on the context. Keep unchanged.*


Object: Pricelist (product.pricelist)
#####################################



:active: Active, boolean





:currency_id: Currency, many2one, required





:type: Pricelist Type, selection, required





:name: Pricelist Name, char, required





:version_id: Pricelist Versions, one2many




Object: Pricelist Version (product.pricelist.version)
#####################################################



:items_id: Price List Items, one2many, required





:name: Name, char, required





:date_end: End Date, date

    *Ending date for this pricelist version to be valid.*



:date_start: Start Date, date

    *Starting date for this pricelist version to be valid.*



:active: Active, boolean

    *When a version is duplicated it is set to non active, so that the dates do not overlaps with original version. You should change the dates and reactivate the pricelist*



:pricelist_id: Price List, many2one, required




Object: Pricelist item (product.pricelist.item)
###############################################



:price_round: Price Rounding, float

    *Sets the price so that it is a multiple of this value.
    Rounding is applied after the discount and before the surcharge.
    To have prices that end in 9.99, set rounding 10, surcharge -0.01*



:name: Rule Name, char

    *Explicit rule name for this pricelist line.*



:base_pricelist_id: If Other Pricelist, many2one





:sequence: Sequence, integer, required





:price_max_margin: Max. Price Margin, float





:price_version_id: Price List Version, many2one, required





:product_tmpl_id: Product Template, many2one

    *Set a template if this rule only apply to a template of product. Keep empty for all products*



:product_id: Product, many2one

    *Set a product if this rule only apply to one product. Keep empty for all products*



:base: Based on, selection, required

    *The mode for computing the price for this rule.*



:min_quantity: Min. Quantity, integer, required

    *The rule only applies if the partner buys/sells more than this quantity.*



:price_surcharge: Price Surcharge, float





:price_min_margin: Min. Price Margin, float





:categ_id: Product Category, many2one

    *Set a category of product if this rule only apply to products of a category and his children. Keep empty for all products*



:price_discount: Price Discount, float


