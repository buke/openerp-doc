
.. i18n: .. module:: multi_company_product
.. i18n:     :synopsis: MultiCompany Product 
.. i18n:     :noindex:
.. i18n: .. 
..

.. module:: multi_company_product
    :synopsis: MultiCompany Product 
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
.. i18n:     <div class="js-kit-rating" title="" permalink="" standalone="yes" path="/multi_company_product"></div>
.. i18n:     <script src="http://js-kit.com/ratings.js"></script>
..

.. raw:: html

    <div class="js-kit-rating" title="" permalink="" standalone="yes" path="/multi_company_product"></div>
    <script src="http://js-kit.com/ratings.js"></script>

.. i18n: MultiCompany Product (*multi_company_product*)
.. i18n: ==============================================
.. i18n: :Module: multi_company_product
.. i18n: :Name: MultiCompany Product
.. i18n: :Version: 5.0.1.1
.. i18n: :Author: Axelor
.. i18n: :Directory: multi_company_product
.. i18n: :Web: http://www.axelor.com
.. i18n: :Official module: no
.. i18n: :Quality certified: no
..

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

.. i18n: Description
.. i18n: -----------
..

Description
-----------

.. i18n: ::
.. i18n: 
.. i18n:   The Module allows to define each product for many companies with their cost price and sale price
.. i18n:       and that update cost price and sale price as per userwise company, for the purpose of multicompany
..

::

  The Module allows to define each product for many companies with their cost price and sale price
      and that update cost price and sale price as per userwise company, for the purpose of multicompany

.. i18n: Download links
.. i18n: --------------
..

Download links
--------------

.. i18n: You can download this module as a zip file in the following version:
..

You can download this module as a zip file in the following version:

.. i18n:   * `5.0 <http://www.openerp.com/download/modules/5.0/multi_company_product.zip>`_
.. i18n:   * `trunk <http://www.openerp.com/download/modules/trunk/multi_company_product.zip>`_
..

  * `5.0 <http://www.openerp.com/download/modules/5.0/multi_company_product.zip>`_
  * `trunk <http://www.openerp.com/download/modules/trunk/multi_company_product.zip>`_

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

.. i18n: None
..

None

.. i18n: Views
.. i18n: -----
..

Views
-----

.. i18n:  * \* INHERIT product.supplierinfo.form.view (form)
.. i18n:  * \* INHERIT product.supplierinfo.tree.view (tree)
.. i18n:  * company.wise.cost.price.form (form)
.. i18n:  * company.wise.cost.price.tree (tree)
.. i18n:  * company.wise.sale.price.form (form)
.. i18n:  * company.wise.sale.price.tree (tree)
.. i18n:  * \* INHERIT product.normal.form (form)
..

 * \* INHERIT product.supplierinfo.form.view (form)
 * \* INHERIT product.supplierinfo.tree.view (tree)
 * company.wise.cost.price.form (form)
 * company.wise.cost.price.tree (tree)
 * company.wise.sale.price.form (form)
 * company.wise.sale.price.tree (tree)
 * \* INHERIT product.normal.form (form)

.. i18n: Objects
.. i18n: -------
..

Objects
-------

.. i18n: Object: Company Wise Cost Price (company.wise.cost.price)
.. i18n: #########################################################
..

Object: Company Wise Cost Price (company.wise.cost.price)
#########################################################

.. i18n: :currency_id: Currency, many2one, readonly
..

:currency_id: Currency, many2one, readonly

.. i18n: :standard_price: Cost Price, float, required
..

:standard_price: Cost Price, float, required

.. i18n:     *The cost of the product for accounting stock valuation. It can serves as a base price for supplier price.*
..

    *The cost of the product for accounting stock valuation. It can serves as a base price for supplier price.*

.. i18n: :product_id: Product Id, many2one
..

:product_id: Product Id, many2one

.. i18n: :company_id: Company, many2one
..

:company_id: Company, many2one

.. i18n: Object: Company Wise Sale Price (company.wise.sale.price)
.. i18n: #########################################################
..

Object: Company Wise Sale Price (company.wise.sale.price)
#########################################################

.. i18n: :currency_id: Currency, many2one, readonly
..

:currency_id: Currency, many2one, readonly

.. i18n: :list_price: Sale Price, float, required
..

:list_price: Sale Price, float, required

.. i18n:     *Base price for computing the customer price. Sometimes called the catalog price.*
..

    *Base price for computing the customer price. Sometimes called the catalog price.*

.. i18n: :product_id: Product Id, many2one
..

:product_id: Product Id, many2one

.. i18n: :company_id: Company, many2one
..

:company_id: Company, many2one
