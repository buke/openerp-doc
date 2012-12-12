
.. module:: multi_company_product
    :synopsis: MultiCompany Product 
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

    <div class="js-kit-rating" title="" permalink="" standalone="yes" path="/multi_company_product"></div>
    <script src="http://js-kit.com/ratings.js"></script>

MultiCompany Product (*multi_company_product*)
==============================================
:Module: multi_company_product
:Name: MultiCompany Product
:Version: 5.0.1.1
:Author: Axelor
:Directory: multi_company_product
:Web: http://www.axelor.com
:Official module: no
:Quality certified: no

Description
-----------

::

  The Module allows to define each product for many companies with their cost price and sale price
      and that update cost price and sale price as per userwise company, for the purpose of multicompany

Download links
--------------

You can download this module as a zip file in the following version:

  * `5.0 <http://www.openerp.com/download/modules/5.0/multi_company_product.zip>`_
  * `trunk <http://www.openerp.com/download/modules/trunk/multi_company_product.zip>`_


Dependencies
------------

 * :mod:`base`
 * :mod:`product`

Reports
-------

None


Menus
-------


None


Views
-----

 * \* INHERIT product.supplierinfo.form.view (form)
 * \* INHERIT product.supplierinfo.tree.view (tree)
 * company.wise.cost.price.form (form)
 * company.wise.cost.price.tree (tree)
 * company.wise.sale.price.form (form)
 * company.wise.sale.price.tree (tree)
 * \* INHERIT product.normal.form (form)


Objects
-------

Object: Company Wise Cost Price (company.wise.cost.price)
#########################################################



:currency_id: Currency, many2one, readonly





:standard_price: Cost Price, float, required

    *The cost of the product for accounting stock valuation. It can serves as a base price for supplier price.*



:product_id: Product Id, many2one





:company_id: Company, many2one




Object: Company Wise Sale Price (company.wise.sale.price)
#########################################################



:currency_id: Currency, many2one, readonly





:list_price: Sale Price, float, required

    *Base price for computing the customer price. Sometimes called the catalog price.*



:product_id: Product Id, many2one





:company_id: Company, many2one


