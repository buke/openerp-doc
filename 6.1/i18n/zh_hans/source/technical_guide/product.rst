
.. i18n: .. module:: product
.. i18n:     :synopsis: Products & Pricelists (Official, Quality Certified)
.. i18n:     :noindex:
.. i18n: .. 
..

.. module:: product
    :synopsis: Products & Pricelists (Official, Quality Certified)
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
.. i18n:     <div class="js-kit-rating" title="" permalink="" standalone="yes" path="/product"></div>
.. i18n:     <script src="http://js-kit.com/ratings.js"></script>
..

.. raw:: html

    <div class="js-kit-rating" title="" permalink="" standalone="yes" path="/product"></div>
    <script src="http://js-kit.com/ratings.js"></script>

.. i18n: Products & Pricelists (*product*)
.. i18n: =================================
.. i18n: :Module: product
.. i18n: :Name: Products & Pricelists
.. i18n: :Version: 5.0.1.1
.. i18n: :Author: Tiny
.. i18n: :Directory: product
.. i18n: :Web: 
.. i18n: :Official module: yes
.. i18n: :Quality certified: yes
..

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

.. i18n: Description
.. i18n: -----------
..

Description
-----------

.. i18n: ::
.. i18n: 
.. i18n:   This is the base module for managing products and pricelists in OpenERP.
.. i18n:   
.. i18n:       Products support variants, different pricing methods, suppliers
.. i18n:       information, make to stock/order, different unit of measures,
.. i18n:       packaging and properties.
.. i18n:   
.. i18n:       Pricelists support:
.. i18n:       * Multiple-level of discount (by product, category, quantities)
.. i18n:       * Compute price based on different criteria:
.. i18n:           * Other pricelist,
.. i18n:           * Cost price,
.. i18n:           * List price,
.. i18n:           * Supplier price, ...
.. i18n:       Pricelists preferences by product and/or partners.
.. i18n:   
.. i18n:       Print product labels with barcode.
..

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

.. i18n: Download links
.. i18n: --------------
..

Download links
--------------

.. i18n: You can download this module as a zip file in the following version:
..

You can download this module as a zip file in the following version:

.. i18n:   * `4.2 <http://www.openerp.com/download/modules/4.2/product.zip>`_
.. i18n:   * `5.0 <http://www.openerp.com/download/modules/5.0/product.zip>`_
.. i18n:   * `trunk <http://www.openerp.com/download/modules/trunk/product.zip>`_
..

  * `4.2 <http://www.openerp.com/download/modules/4.2/product.zip>`_
  * `5.0 <http://www.openerp.com/download/modules/5.0/product.zip>`_
  * `trunk <http://www.openerp.com/download/modules/trunk/product.zip>`_

.. i18n: Dependencies
.. i18n: ------------
..

Dependencies
------------

.. i18n:  * :mod:`base`
.. i18n:  * :mod:`process`
..

 * :mod:`base`
 * :mod:`process`

.. i18n: Reports
.. i18n: -------
..

Reports
-------

.. i18n:  * Products Labels
.. i18n: 
.. i18n:  * Product Pricelist
..

 * Products Labels

 * Product Pricelist

.. i18n: Menus
.. i18n: -------
..

Menus
-------

.. i18n:  * Products
.. i18n:  * Products/Configuration
.. i18n:  * Products/Products
.. i18n:  * Products/Products by Category
.. i18n:  * Products/Configuration/Products Categories
.. i18n:  * Products/Configuration/Units of Measure
.. i18n:  * Products/Configuration/Units of Measure/Units of Measure
.. i18n:  * Products/Configuration/Units of Measure/Units of Measure Categories
.. i18n:  * Products/Configuration/Packaging
.. i18n:  * Products/Pricelists
.. i18n:  * Products/Pricelists/Pricelist Versions
.. i18n:  * Products/Pricelists/Pricelists
.. i18n:  * Products/Configuration/Prices Computations
.. i18n:  * Products/Configuration/Prices Computations/Prices Types
.. i18n:  * Products/Configuration/Prices Computations/Pricelists Types
..

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

.. i18n: Views
.. i18n: -----
..

Views
-----

.. i18n:  * product.product.tree (tree)
.. i18n:  * product.normal.form (form)
.. i18n:  * product.category.form (form)
.. i18n:  * product.category.list (tree)
.. i18n:  * product.category.tree (tree)
.. i18n:  * product.uom.tree (tree)
.. i18n:  * product.uom.form (form)
.. i18n:  * product.uom.categ.form (form)
.. i18n:  * product.ul.form.view (form)
.. i18n:  * product.ul.tree (tree)
.. i18n:  * product.packaging.tree.view (tree)
.. i18n:  * product.packaging.form.view (form)
.. i18n:  * product.supplierinfo.form.view (form)
.. i18n:  * product.supplierinfo.tree.view (tree)
.. i18n:  * product.variant.form (form)
.. i18n:  * product.variant.tree (tree)
.. i18n:  * product.template.product.tree (tree)
.. i18n:  * product.template.product.form (form)
.. i18n:  * product.pricelist.version.form (form)
.. i18n:  * product.pricelist.version.tree (tree)
.. i18n:  * product.pricelist.item.tree (tree)
.. i18n:  * product.pricelist.item.form (form)
.. i18n:  * product.pricelist.tree (tree)
.. i18n:  * product.pricelist.form (form)
.. i18n:  * product.price.type.form (form)
.. i18n:  * product.pricelist.type.form (form)
.. i18n:  * \* INHERIT res.partner.product.property.form.inherit (form)
..

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

.. i18n: Objects
.. i18n: -------
..

Objects
-------

.. i18n: Object: Product uom categ (product.uom.categ)
.. i18n: #############################################
..

Object: Product uom categ (product.uom.categ)
#############################################

.. i18n: :name: Name, char, required
..

:name: Name, char, required

.. i18n: Object: Product Unit of Measure (product.uom)
.. i18n: #############################################
..

Object: Product Unit of Measure (product.uom)
#############################################

.. i18n: :name: Name, char, required
..

:name: Name, char, required

.. i18n: :factor_inv: Factor, float, readonly
..

:factor_inv: Factor, float, readonly

.. i18n:     *The coefficient for the formula:
.. i18n:     coeff (base unit) = 1 (this unit). Factor = 1 / Rate.*
..

    *The coefficient for the formula:
    coeff (base unit) = 1 (this unit). Factor = 1 / Rate.*

.. i18n: :rounding: Rounding Precision, float, required
..

:rounding: Rounding Precision, float, required

.. i18n:     *The computed quantity will be a multiple of this value. Use 1.0 for products that can not be split.*
..

    *The computed quantity will be a multiple of this value. Use 1.0 for products that can not be split.*

.. i18n: :factor: Rate, float, required
..

:factor: Rate, float, required

.. i18n:     *The coefficient for the formula:
.. i18n:     1 (base unit) = coeff (this unit). Rate = 1 / Factor.*
..

    *The coefficient for the formula:
    1 (base unit) = coeff (this unit). Rate = 1 / Factor.*

.. i18n: :active: Active, boolean
..

:active: Active, boolean

.. i18n: :category_id: UoM Category, many2one, required
..

:category_id: UoM Category, many2one, required

.. i18n:     *Unit of Measure of a category can be converted between each others in the same category.*
..

    *Unit of Measure of a category can be converted between each others in the same category.*

.. i18n: :factor_inv_data: Factor, float
..

:factor_inv_data: Factor, float

.. i18n: Object: Shipping Unit (product.ul)
.. i18n: ##################################
..

Object: Shipping Unit (product.ul)
##################################

.. i18n: :type: Type, selection, required
..

:type: Type, selection, required

.. i18n: :name: Name, char, required
..

:name: Name, char, required

.. i18n: Object: Product Category (product.category)
.. i18n: ###########################################
..

Object: Product Category (product.category)
###########################################

.. i18n: :parent_id: Parent Category, many2one
..

:parent_id: Parent Category, many2one

.. i18n: :child_id: Child Categories, one2many
..

:child_id: Child Categories, one2many

.. i18n: :complete_name: Name, char, readonly
..

:complete_name: Name, char, readonly

.. i18n: :name: Name, char, required
..

:name: Name, char, required

.. i18n: :sequence: Sequence, integer
..

:sequence: Sequence, integer

.. i18n: Object: Product Template (product.template)
.. i18n: ###########################################
..

Object: Product Template (product.template)
###########################################

.. i18n: :warranty: Warranty (months), float
..

:warranty: Warranty (months), float

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

.. i18n: :standard_price: Cost Price, float, required
..

:standard_price: Cost Price, float, required

.. i18n:     *The cost of the product for accounting stock valuation. It can serves as a base price for supplier price.*
..

    *The cost of the product for accounting stock valuation. It can serves as a base price for supplier price.*

.. i18n: :mes_type: Measure Type, selection, required
..

:mes_type: Measure Type, selection, required

.. i18n: :uom_id: Default UoM, many2one, required
..

:uom_id: Default UoM, many2one, required

.. i18n:     *Default Unit of Measure used for all stock operation.*
..

    *Default Unit of Measure used for all stock operation.*

.. i18n: :description_purchase: Purchase Description, text
..

:description_purchase: Purchase Description, text

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

.. i18n: :loc_case: Case, char
..

:loc_case: Case, char

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

.. i18n: :procure_method: Procure Method, selection, required
..

:procure_method: Procure Method, selection, required

.. i18n:     *'Make to Stock': When needed, take from the stock or wait until re-supplying. 'Make to Order': When needed, purchase or produce for the procurement request.*
..

    *'Make to Stock': When needed, take from the stock or wait until re-supplying. 'Make to Order': When needed, purchase or produce for the procurement request.*

.. i18n: :cost_method: Costing Method, selection, required
..

:cost_method: Costing Method, selection, required

.. i18n:     *Standard Price: the cost price is fixed and recomputed periodically (usually at the end of the year), Average Price: the cost price is recomputed at each reception of products.*
..

    *Standard Price: the cost price is fixed and recomputed periodically (usually at the end of the year), Average Price: the cost price is recomputed at each reception of products.*

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

.. i18n: :sale_delay: Customer Lead Time, float
..

:sale_delay: Customer Lead Time, float

.. i18n:     *This is the average time between the confirmation of the customer order and the delivery of the finished products. It's the time you promise to your customers.*
..

    *This is the average time between the confirmation of the customer order and the delivery of the finished products. It's the time you promise to your customers.*

.. i18n: :name: Name, char, required
..

:name: Name, char, required

.. i18n: :description_sale: Sale Description, text
..

:description_sale: Sale Description, text

.. i18n: :categ_id: Category, many2one, required
..

:categ_id: Category, many2one, required

.. i18n: :produce_delay: Manufacturing Lead Time, float
..

:produce_delay: Manufacturing Lead Time, float

.. i18n:     *Average time to produce this product. This is only for the production order and, if it is a multi-level bill of material, it's only for the level of this product. Different delays will be summed for all levels and purchase orders.*
..

    *Average time to produce this product. This is only for the production order and, if it is a multi-level bill of material, it's only for the level of this product. Different delays will be summed for all levels and purchase orders.*

.. i18n: :seller_ids: Partners, one2many
..

:seller_ids: Partners, one2many

.. i18n: Object: Product (product.product)
.. i18n: #################################
..

Object: Product (product.product)
#################################

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

.. i18n: :virtual_available: Virtual Stock, float, readonly
..

:virtual_available: Virtual Stock, float, readonly

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

.. i18n: :outgoing_qty: Outgoing, float, readonly
..

:outgoing_qty: Outgoing, float, readonly

.. i18n: :procure_method: Procure Method, selection, required
..

:procure_method: Procure Method, selection, required

.. i18n:     *'Make to Stock': When needed, take from the stock or wait until re-supplying. 'Make to Order': When needed, purchase or produce for the procurement request.*
..

    *'Make to Stock': When needed, take from the stock or wait until re-supplying. 'Make to Order': When needed, purchase or produce for the procurement request.*

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

.. i18n: :price_margin: Variant Price Margin, float
..

:price_margin: Variant Price Margin, float

.. i18n: Object: Packaging (product.packaging)
.. i18n: #####################################
..

Object: Packaging (product.packaging)
#####################################

.. i18n: :code: Code, char
..

:code: Code, char

.. i18n:     *The code of the transport unit.*
..

    *The code of the transport unit.*

.. i18n: :product_id: Product, many2one, required
..

:product_id: Product, many2one, required

.. i18n: :weight: Total Package Weight, float
..

:weight: Total Package Weight, float

.. i18n:     *The weight of a full of products palet or box.*
..

    *The weight of a full of products palet or box.*

.. i18n: :sequence: Sequence, integer
..

:sequence: Sequence, integer

.. i18n: :ul_qty: Package by layer, integer
..

:ul_qty: Package by layer, integer

.. i18n: :ean: EAN, char
..

:ean: EAN, char

.. i18n:     *The EAN code of the package unit.*
..

    *The EAN code of the package unit.*

.. i18n: :qty: Quantity by Package, float
..

:qty: Quantity by Package, float

.. i18n:     *The total number of products you can put by palet or box.*
..

    *The total number of products you can put by palet or box.*

.. i18n: :ul: Type of Package, many2one, required
..

:ul: Type of Package, many2one, required

.. i18n: :length: Length, float
..

:length: Length, float

.. i18n:     *The length of the package*
..

    *The length of the package*

.. i18n: :rows: Number of Layer, integer, required
..

:rows: Number of Layer, integer, required

.. i18n:     *The number of layer on a palet or box*
..

    *The number of layer on a palet or box*

.. i18n: :weight_ul: Empty Package Weight, float
..

:weight_ul: Empty Package Weight, float

.. i18n:     *The weight of the empty UL*
..

    *The weight of the empty UL*

.. i18n: :height: Height, float
..

:height: Height, float

.. i18n:     *The height of the package*
..

    *The height of the package*

.. i18n: :width: Width, float
..

:width: Width, float

.. i18n:     *The width of the package*
..

    *The width of the package*

.. i18n: :name: Description, char
..

:name: Description, char

.. i18n: Object: Information about a product supplier (product.supplierinfo)
.. i18n: ###################################################################
..

Object: Information about a product supplier (product.supplierinfo)
###################################################################

.. i18n: :pricelist_ids: Supplier Pricelist, one2many
..

:pricelist_ids: Supplier Pricelist, one2many

.. i18n: :product_id: Product, many2one, required
..

:product_id: Product, many2one, required

.. i18n: :sequence: Priority, integer
..

:sequence: Priority, integer

.. i18n: :qty: Minimal Quantity, float, required
..

:qty: Minimal Quantity, float, required

.. i18n:     *The minimal quantity to purchase for this supplier, expressed in the default unit of measure.*
..

    *The minimal quantity to purchase for this supplier, expressed in the default unit of measure.*

.. i18n: :delay: Delivery Delay, integer, required
..

:delay: Delivery Delay, integer, required

.. i18n:     *Delay in days between the confirmation of the purchase order and the reception of the products in your warehouse. Used by the scheduler for automatic computation of the purchase order planning.*
..

    *Delay in days between the confirmation of the purchase order and the reception of the products in your warehouse. Used by the scheduler for automatic computation of the purchase order planning.*

.. i18n: :product_code: Partner Product Code, char
..

:product_code: Partner Product Code, char

.. i18n:     *Code of the product for this partner, will be used when printing a request for quotation. Keep empty to use the internal one.*
..

    *Code of the product for this partner, will be used when printing a request for quotation. Keep empty to use the internal one.*

.. i18n: :product_name: Partner Product Name, char
..

:product_name: Partner Product Name, char

.. i18n:     *Name of the product for this partner, will be used when printing a request for quotation. Keep empty to use the internal one.*
..

    *Name of the product for this partner, will be used when printing a request for quotation. Keep empty to use the internal one.*

.. i18n: :name: Partner, many2one, required
..

:name: Partner, many2one, required

.. i18n:     *Supplier of this product*
..

    *Supplier of this product*

.. i18n: Object: pricelist.partnerinfo (pricelist.partnerinfo)
.. i18n: #####################################################
..

Object: pricelist.partnerinfo (pricelist.partnerinfo)
#####################################################

.. i18n: :min_quantity: Quantity, float, required
..

:min_quantity: Quantity, float, required

.. i18n: :price: Unit Price, float, required
..

:price: Unit Price, float, required

.. i18n: :suppinfo_id: Partner Information, many2one, required
..

:suppinfo_id: Partner Information, many2one, required

.. i18n: :name: Description, char
..

:name: Description, char

.. i18n: Object: Price type (product.price.type)
.. i18n: #######################################
..

Object: Price type (product.price.type)
#######################################

.. i18n: :active: Active, boolean
..

:active: Active, boolean

.. i18n: :field: Product Field, selection, required
..

:field: Product Field, selection, required

.. i18n:     *Associated field in the product form.*
..

    *Associated field in the product form.*

.. i18n: :currency_id: Currency, many2one, required
..

:currency_id: Currency, many2one, required

.. i18n:     *The currency the field is expressed in.*
..

    *The currency the field is expressed in.*

.. i18n: :name: Price Name, char, required
..

:name: Price Name, char, required

.. i18n:     *Name of this kind of price.*
..

    *Name of this kind of price.*

.. i18n: Object: Pricelist Type (product.pricelist.type)
.. i18n: ###############################################
..

Object: Pricelist Type (product.pricelist.type)
###############################################

.. i18n: :name: Name, char, required
..

:name: Name, char, required

.. i18n: :key: Key, char, required
..

:key: Key, char, required

.. i18n:     *Used in the code to select specific prices based on the context. Keep unchanged.*
..

    *Used in the code to select specific prices based on the context. Keep unchanged.*

.. i18n: Object: Pricelist (product.pricelist)
.. i18n: #####################################
..

Object: Pricelist (product.pricelist)
#####################################

.. i18n: :active: Active, boolean
..

:active: Active, boolean

.. i18n: :currency_id: Currency, many2one, required
..

:currency_id: Currency, many2one, required

.. i18n: :type: Pricelist Type, selection, required
..

:type: Pricelist Type, selection, required

.. i18n: :name: Pricelist Name, char, required
..

:name: Pricelist Name, char, required

.. i18n: :version_id: Pricelist Versions, one2many
..

:version_id: Pricelist Versions, one2many

.. i18n: Object: Pricelist Version (product.pricelist.version)
.. i18n: #####################################################
..

Object: Pricelist Version (product.pricelist.version)
#####################################################

.. i18n: :items_id: Price List Items, one2many, required
..

:items_id: Price List Items, one2many, required

.. i18n: :name: Name, char, required
..

:name: Name, char, required

.. i18n: :date_end: End Date, date
..

:date_end: End Date, date

.. i18n:     *Ending date for this pricelist version to be valid.*
..

    *Ending date for this pricelist version to be valid.*

.. i18n: :date_start: Start Date, date
..

:date_start: Start Date, date

.. i18n:     *Starting date for this pricelist version to be valid.*
..

    *Starting date for this pricelist version to be valid.*

.. i18n: :active: Active, boolean
..

:active: Active, boolean

.. i18n:     *When a version is duplicated it is set to non active, so that the dates do not overlaps with original version. You should change the dates and reactivate the pricelist*
..

    *When a version is duplicated it is set to non active, so that the dates do not overlaps with original version. You should change the dates and reactivate the pricelist*

.. i18n: :pricelist_id: Price List, many2one, required
..

:pricelist_id: Price List, many2one, required

.. i18n: Object: Pricelist item (product.pricelist.item)
.. i18n: ###############################################
..

Object: Pricelist item (product.pricelist.item)
###############################################

.. i18n: :price_round: Price Rounding, float
..

:price_round: Price Rounding, float

.. i18n:     *Sets the price so that it is a multiple of this value.
.. i18n:     Rounding is applied after the discount and before the surcharge.
.. i18n:     To have prices that end in 9.99, set rounding 10, surcharge -0.01*
..

    *Sets the price so that it is a multiple of this value.
    Rounding is applied after the discount and before the surcharge.
    To have prices that end in 9.99, set rounding 10, surcharge -0.01*

.. i18n: :name: Rule Name, char
..

:name: Rule Name, char

.. i18n:     *Explicit rule name for this pricelist line.*
..

    *Explicit rule name for this pricelist line.*

.. i18n: :base_pricelist_id: If Other Pricelist, many2one
..

:base_pricelist_id: If Other Pricelist, many2one

.. i18n: :sequence: Sequence, integer, required
..

:sequence: Sequence, integer, required

.. i18n: :price_max_margin: Max. Price Margin, float
..

:price_max_margin: Max. Price Margin, float

.. i18n: :price_version_id: Price List Version, many2one, required
..

:price_version_id: Price List Version, many2one, required

.. i18n: :product_tmpl_id: Product Template, many2one
..

:product_tmpl_id: Product Template, many2one

.. i18n:     *Set a template if this rule only apply to a template of product. Keep empty for all products*
..

    *Set a template if this rule only apply to a template of product. Keep empty for all products*

.. i18n: :product_id: Product, many2one
..

:product_id: Product, many2one

.. i18n:     *Set a product if this rule only apply to one product. Keep empty for all products*
..

    *Set a product if this rule only apply to one product. Keep empty for all products*

.. i18n: :base: Based on, selection, required
..

:base: Based on, selection, required

.. i18n:     *The mode for computing the price for this rule.*
..

    *The mode for computing the price for this rule.*

.. i18n: :min_quantity: Min. Quantity, integer, required
..

:min_quantity: Min. Quantity, integer, required

.. i18n:     *The rule only applies if the partner buys/sells more than this quantity.*
..

    *The rule only applies if the partner buys/sells more than this quantity.*

.. i18n: :price_surcharge: Price Surcharge, float
..

:price_surcharge: Price Surcharge, float

.. i18n: :price_min_margin: Min. Price Margin, float
..

:price_min_margin: Min. Price Margin, float

.. i18n: :categ_id: Product Category, many2one
..

:categ_id: Product Category, many2one

.. i18n:     *Set a category of product if this rule only apply to products of a category and his children. Keep empty for all products*
..

    *Set a category of product if this rule only apply to products of a category and his children. Keep empty for all products*

.. i18n: :price_discount: Price Discount, float
..

:price_discount: Price Discount, float
