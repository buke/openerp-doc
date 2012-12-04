
.. module:: esale_osc
    :synopsis: OScommerce Interface / ZenCart 
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

    <div class="js-kit-rating" title="" permalink="" standalone="yes" path="/esale_osc"></div>
    <script src="http://js-kit.com/ratings.js"></script>

OScommerce Interface / ZenCart (*esale_osc*)
============================================
:Module: esale_osc
:Name: OScommerce Interface / ZenCart
:Version: 5.0.1.0
:Author: Axelor/Zikzakmedia
:Directory: esale_osc
:Web: www.aulaerp.com/cursos-aulaerp/configuracion-y-funcionamiento-del-conector-openerp-oscommerce.html
:Official module: no
:Quality certified: no

Description
-----------

::

  OSCommerce (Zencart) eCommerce interface synchronisation.
  
  Syncro Oscommerce to Openerp
   1. Import/upgrade categories.
   2. Import/upgrade products. 
   3. Import Orders on selected status. On importing order, if not exists, customer is created automatically 
  
  Syncro Openerp to Oscommerce
   1. Export products, prices, image, specials.
   2. Export Stocks. 
   3. Change Oscommerce Order status and include comments. Upload Osc Status and comments. 
  
  Developed by Tiny, Axelor, Zikzakmedia and Ana Juaristi

Download links
--------------

You can download this module as a zip file in the following version:

  * `5.0 <http://www.openerp.com/download/modules/5.0/esale_osc.zip>`_
  * `trunk <http://www.openerp.com/download/modules/trunk/esale_osc.zip>`_


Dependencies
------------

 * :mod:`product`
 * :mod:`stock`
 * :mod:`sale`
 * :mod:`account_payment`

Reports
-------

None


Menus
-------

 * Sales Management/Internet Sales
 * Sales Management/Internet Sales/Websites
 * Sales Management/Internet Sales/Web sale orders
 * Sales Management/Internet Sales/Web sale orders/New order
 * Sales Management/Internet Sales/Web sale orders/Request for quotation
 * Sales Management/Internet Sales/Web sale orders/Waiting invoice
 * Sales Management/Internet Sales/Web sale orders/In progress
 * Sales Management/Internet Sales/Invoices
 * Sales Management/Internet Sales/Invoices/Draft
 * Sales Management/Internet Sales/Invoices/PRO-FORMA
 * Sales Management/Internet Sales/Invoices/Opened
 * Sales Management/Internet Sales/Synchronize products and stocks to all OScommerce web shops
 * Sales Management/Internet Sales/Update stocks to all OScommerce web shops
 * Sales Management/Internet Sales/Import sale orders from all OScommerce web shops
 * Sales Management/Internet Sales/Manufacturers

Views
-----

 * esale.oscom.web.form (form)
 * esale.oscom.web.form (tree)
 * esale.oscom.language.web.form (form)
 * esale.oscom.language.web.tree (tree)
 * esale.oscom.tax.web.form (form)
 * esale.oscom.tax.web.tree (tree)
 * esale.oscom.pay.typ.form (form)
 * esale.oscom.pay.typ.tree (tree)
 * esale.oscom.status.form (form)
 * esale.oscom.status.tree (tree)
 * esale.oscom.category.web.form (form)
 * esale.oscom.category.web.v (tree)
 * esale.oscom.product.web.form (form)
 * esale.oscom.saleorder.tree (tree)
 * \* INHERIT esale.oscom.saleorder.form (form)
 * \* INHERIT esale.oscom.product.add.oscom.fields (form)
 * esale.oscom.product.maufacturer.view.form (form)
 * esale.oscom.product.maufacturer.view.tree (tree)


Objects
-------

Object: esale.oscom.web (esale.oscom.web)
#########################################



:pay_typ_ids: Payment types, one2many





:name: Name, char, required





:download_number: Download number, integer

    *Osc product number to download by block. You should find the optimum block to download for your shop*



:url: URL, char, required





:language_ids: Languages, one2many





:category_ids: Categories, one2many





:esale_account_id: Dest. account, many2one, required

    *Payment account for web invoices.*



:shop_id: Sale shop, many2one, required





:intermediate: Intermediate Status, many2one

    *Select intermediate status for Osc downloaded Orders*



:product_ids: Web products, one2many





:active: Active, boolean





:date_download_from: Date Download From, date

    *Specify date since you want to download modified or new products*



:price_type: Price type, selection, required





:status_ids: Osc Status, one2many





:tax_ids: Taxes, one2many




Object: esale_oscom Tax (esale.oscom.tax)
#########################################



:web_id: Website, many2one





:name: Tax name, char, required, readonly





:esale_oscom_id: OScommerce Id, integer





:tax_id: OpenERP tax, many2one




Object: esale_oscom Status (esale.oscom.status)
###############################################



:download: Download Orders on Status, boolean





:web_id: Website, many2one





:name: Status name, char, required, readonly





:esale_oscom_id: OScommerce Id, integer





:language_id: Language Id, integer




Object: esale_oscom Category (esale.oscom.category)
###################################################



:category_id: OpenERP category, many2one





:web_id: Website, many2one





:name: Name, char, required, readonly





:esale_oscom_id: OScommerce Id, integer, required




Object: esale_oscom PayType (esale.oscom.paytype)
#################################################



:payment_id: OpenERP payment, many2one





:paytyp: Payment type, selection





:web_id: Website, many2one





:name: Name, char, required, readonly





:journal_id: OpenERP payment journal, many2one





:esale_oscom_id: OScommerce Id, integer, required




Object: esale_oscom Language (esale.oscom.lang)
###############################################



:web_id: Website, many2one





:name: Name, char, required, readonly





:esale_oscom_id: OScommerce Id, integer, required





:language_id: OpenERP language, many2one




Object: esale_oscom Product (esale.oscom.product)
#################################################



:web_id: Website, many2one





:name: Name, char, required, readonly





:esale_oscom_id: OScommerce product Id, integer





:product_id: OpenERP product, many2one




Object: Product Manufacturer that produces the product (product.manufacturer)
#############################################################################



:manufacturer_url: URL, char





:name: Name, char, required


