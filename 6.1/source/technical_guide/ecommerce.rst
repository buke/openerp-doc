
.. module:: ecommerce
    :synopsis: E-Commerce 
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

    <div class="js-kit-rating" title="" permalink="" standalone="yes" path="/ecommerce"></div>
    <script src="http://js-kit.com/ratings.js"></script>

E-Commerce (*ecommerce*)
========================
:Module: ecommerce
:Name: E-Commerce
:Version: 5.0.1.0
:Author: Tiny
:Directory: ecommerce
:Web: http://www.openerp.com
:Official module: no
:Quality certified: no

Description
-----------

::

  ecommerce users can order on the website, orders are automatically imported in OpenERP.
  
  You can export products, product's categories, product images and create links between
  categories of products, currency and languages to website.
  
  Delivery of products manage by carriers.
  
  Different payment methods are available for users to make payment.
  
  You can display products in table on website using rows and columns specified in webshop.

Download links
--------------

You can download this module as a zip file in the following version:

  * `5.0 <http://www.openerp.com/download/modules/5.0/ecommerce.zip>`_
  * `trunk <http://www.openerp.com/download/modules/trunk/ecommerce.zip>`_


Dependencies
------------

 * :mod:`delivery`

Reports
-------

 * Shipping Invoice

Menus
-------

 * Ecommerce
 * Ecommerce/Configuration
 * Ecommerce/Configuration/Web Shop
 * Ecommerce/Configuration/New Web Shop
 * Ecommerce/Products
 * Ecommerce/Products/Ecommerce Products by Category
 * Ecommerce/Payment Configuration
 * Ecommerce/Payment Configuration/Payment
 * Ecommerce/Configuration/Payment method
 * Ecommerce/Payment Configuration/Payment Received
 * Ecommerce/Payment Configuration/Credit Cards
 * Ecommerce/Partners
 * Ecommerce/Partners/Partners
 * Ecommerce/Partners/Partner Contacts
 * Ecommerce/Products/Product Reviews
 * Ecommerce/Products/Search Parameters
 * Ecommerce/Sales Orders
 * Ecommerce/Sales Orders/Ecommerce Sales Orders

Views
-----

 * ecommerce.shop.tree (tree)
 * Web Shop (form)
 * ecommerce.product.category.form (form)
 * ecommerce.product.category.tree (tree)
 * ecommerce.payment.tree (tree)
 * ecommerce.payment.form (form)
 * ecommerce.payment.method.tree (tree)
 * ecommerce.payment.method.form (form)
 * ecommerce.payment.received.tree (tree)
 * ecommerce.payment.received.form (form)
 * ecommerce.creditcard.tree (tree)
 * ecommerce.creditcard.form (form)
 * ecommerce.partner.tree (tree)
 * ecommerce.partner.form (form)
 * ecommerce.partner.address.tree (tree)
 * ecommerce.partner.address.form (form)
 * \* INHERIT product.form (form)
 * \* INHERIT ecommerce.pricelist.version (form)
 * ecommerce.reviews.tree (tree)
 * ecommerce.reviews.form (form)
 * ecommerce.search.tree (tree)
 * ecommerce.search.form (form)
 * saleorder.form (form)
 * saleorder.tree (tree)
 * orderline.form (form)
 * orderline.tree (tree)


Objects
-------

Object: ecommerce partner (ecommerce.partner)
#############################################



:lang: Language, many2one





:address_ids: Contacts, one2many





:last_name: Last Name, char





:name: Name, char, required

    *Its ecommerce partner name and address*



:category_ids: Categories, many2many





:company_name: Company Name, char





:active: Active, boolean




Object: ecommerce partner address (ecommerce.partner.address)
#############################################################



:username: Contact Name, char





:city: City, char





:fax: Fax, char





:zip: Zip, char





:mobile: Mobile, char





:partner_id: Partner, many2one





:street2: Street2, char





:country_id: Country, many2one





:phone: Phone, char





:street: Street, char





:state_id: State, many2one





:type: Address Type, selection





:email: E-Mail, char




Object: search parameters (ecommerce.search)
############################################



:code: Product fields, many2one, required





:name: Name, char, required

    *Search parameter name which you want to display at website*


Object: Reviews about product (ecommerce.product.reviews)
#########################################################



:rating: Rating, integer





:reviewdate: Review Date, date





:customer_id: Customer, many2one, required





:product_id: Product, many2one, required





:review: Review, text




Object: payment method (ecommerce.payment.method)
#################################################



:name: Name, char, required





:shortcut: Shortcut, char, required




Object: Credit Cards (ecommerce.creditcard)
###########################################



:code: Code, char, required





:name: Card Name, char, required




Object: ecommerce payment (ecommerce.payment)
#############################################



:biz_account: Business E-mail Id, char

    *Paypal business account Id.*



:bank_name: Bank Name, char





:chequepay_to: Account Owner, char





:name: Payment Method, selection, required





:zip: Zip, char





:city: City, char





:street2: Street2, char





:country_id: Country, many2one





:bic: BIC number or SWIFT, char





:creditcard_ids: Credit Cards, many2many





:transaction_dtl_ids: Transaction History, one2many

    *Transaction detail with the uniq transaction id.*



:cancel_url: Cancel URL, char

    *Cancel url which is set at the paypal account.*



:street: Street, char





:state_id: State, many2one





:return_url: Return URL, char

    *Return url which is set at the paypal account.*



:acc_number: Account Number, char

    *Bank account number*


Object: ecommerce payment received (ecommerce.payment.received)
###############################################################



:saleorder_id: Sales Order, many2one





:invoice_id: Invoice, many2one





:paypal_acc_id: Paypal Account, many2one, required





:transaction_date: Date Payment, date, required

    *Transaction finish date.*



:partner_id: Partner, many2one, required





:transaction_id: Transaction Id, char, readonly

    *Its Unique id which is generated from the paypal.*


Object: ecommerce shop (ecommerce.shop)
#######################################



:column_configuration: No. of Columns, integer

    *Add number of columns for products which you want to configure at website*



:search_ids: Search On, many2many

    *Add the search parameters which you are allow from the website.*



:delivery_ids: Delivery, many2many

    *Add the carriers which you use for the shipping.*



:payment_method_ids: Payment Methods, many2many





:language_ids: Language, many2many

    *Add the language options for the online customers.*



:currency_ids: Currency, many2many

    *Add the currency options for the online customers.*



:company_id: Company, many2one





:shop_id: Sale Shop, many2one, required





:image_width: Width in Pixel, integer

    *Add product image width in pixels.*



:image_height: Height in Pixel, integer

    *Add product image height in pixels.*



:category_ids: Categories, one2many

    *Add the product categories which you want to displayed on the website.*



:row_configuration: No. of Rows, integer

    *Add number of rows for products which you want to configure at website*



:name: Name, char, required

    *Name of the shop which you are configure at website.*


Object: ecommerce category (ecommerce.category)
###############################################



:child_ids: Child Categories, one2many





:category_id: Tiny Category, many2one

    *It display the product which are under the openerp category.*



:web_id: Web Shop, many2one





:name: E-commerce Category, char, required

    *Add the category name which you want to display at the website.*



:parent_category_id: Parent Category, many2one




Object: ecommerce saleorder (ecommerce.saleorder)
#################################################



:epartner_add_id: Contact Address, many2one





:web_id: Web Shop, many2one, required





:name: Order Reference, char, required





:epartner_shipping_id: Shipping Address, many2one





:order_id: Sale Order, many2one





:note: Notes, text





:orderline_ids: Order Lines, one2many





:epartner_id: Ecommerce Partner, many2one, required





:pricelist_id: Pricelist, many2one, required





:date_order: Date Ordered, date, required





:epartner_invoice_id: Invoice Address, many2one




Object: ecommerce order line (ecommerce.order.line)
###################################################



:product_id: Product, many2one





:order_id: eOrder Ref, many2one





:product_uom_id: Product UOM, many2one, required





:price_unit: Unit Price, float, required





:product_qty: Quantity, float, required





:name: Description, char, required


