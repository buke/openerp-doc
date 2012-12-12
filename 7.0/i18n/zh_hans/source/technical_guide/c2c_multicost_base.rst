
.. i18n: .. module:: c2c_multicost_base
.. i18n:     :synopsis: Multi-Costs Handling base 
.. i18n:     :noindex:
.. i18n: .. 
..

.. module:: c2c_multicost_base
    :synopsis: Multi-Costs Handling base 
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
.. i18n:     <div class="js-kit-rating" title="" permalink="" standalone="yes" path="/c2c_multicost_base"></div>
.. i18n:     <script src="http://js-kit.com/ratings.js"></script>
..

.. raw:: html

    <div class="js-kit-rating" title="" permalink="" standalone="yes" path="/c2c_multicost_base"></div>
    <script src="http://js-kit.com/ratings.js"></script>

.. i18n: Multi-Costs Handling base (*c2c_multicost_base*)
.. i18n: ================================================
.. i18n: :Module: c2c_multicost_base
.. i18n: :Name: Multi-Costs Handling base
.. i18n: :Version: 5.0.1.0
.. i18n: :Author: Camptocamp
.. i18n: :Directory: c2c_multicost_base
.. i18n: :Web: http://camptocamp.com
.. i18n: :Official module: no
.. i18n: :Quality certified: no
..

Multi-Costs Handling base (*c2c_multicost_base*)
================================================
:Module: c2c_multicost_base
:Name: Multi-Costs Handling base
:Version: 5.0.1.0
:Author: Camptocamp
:Directory: c2c_multicost_base
:Web: http://camptocamp.com
:Official module: no
:Quality certified: no

.. i18n: Description
.. i18n: -----------
..

Description
-----------

.. i18n: ::
.. i18n: 
.. i18n:   This improves OpenERP multi-cost handling, overall for multi-company, regarding to product costs. It also improves
.. i18n:   the multi-currency handling into analytic accounting.
.. i18n:   
.. i18n:   This module (as all c2c_multicost*) is a backport to current stable from our work merged in the trunk branch of OpenERP.
.. i18n:   
.. i18n:   What has been done here:
.. i18n:   
.. i18n:    * Add price type on company as a property (with default value based on standard price)
.. i18n:   
.. i18n:    * Analytic accounting
.. i18n:     * Use the price type currency and field for cost valuation (including timesheet)
.. i18n:     * Add multi-currency on analytic lines (similar to financial accounting)
.. i18n:     * Allow to share the same product between company employees, with different cost for each one
.. i18n:     * Correct all "costs" indicators into analytic account to base them on the correct currency (owner's company)
.. i18n:   
.. i18n:    * By default, nothing change for single company implementation (base the cost valuation on standard price)
.. i18n:   
.. i18n:    * Factorise part of function field into analytic accounting
.. i18n:   
.. i18n:   As a result, we can now share the same product between companies that don't have the same currency and/or same cost price. 
.. i18n:   We can also manage one field per company on the product form to store the cost for a given price type (and so for a given company).
.. i18n:   
.. i18n:   
.. i18n:   Warning !! 
.. i18n:   
.. i18n:   This module change some functions signatures in some object. In order to have it running properly,
.. i18n:   you need to install every c2c_multicost_*, where * is the name of the already install module.
.. i18n:   
.. i18n:   Example : If you're using hr_expense, then don't forget to install c2c_multicost_expense.
.. i18n:   
.. i18n:   Please, also verify that one of your specific modules on concerned methodes.
.. i18n:        
.. i18n:   How to setup:
.. i18n:   -------------
.. i18n:   
.. i18n:   This module won't change anything unless you assign a different price_type to your company. This price type has
.. i18n:   to point on one of the product.product "float" field as the costing value for this company. The currency used is the one
.. i18n:   define into the price type. It has to be the same than your company currency !
.. i18n:   
.. i18n:   Example 1 :
.. i18n:   
.. i18n:   Your company is in EUR. You can setup a different price type for your company. Let it point on a new product.product field,
.. i18n:   lets say "my_new_product_cost_price" (this field needs to be defined in one of your specific module). Now this new field
.. i18n:   will be used as the new cost price for all product.
.. i18n:   
.. i18n:   Example 2 :
.. i18n:   
.. i18n:   You have two companies, one in CHF and the other in EUR. Assuming each of your company has its own price type pointing on
.. i18n:   their own float field, you can now have one product but a different cost for each company.
.. i18n:   
.. i18n:   Company 1 (EUR) -> price type "Cost EUR", pointing on "standard_price"
.. i18n:   
.. i18n:   Company 2 (CHF) -> price type "Cost CHF", pointing on "standard_price_chf"
.. i18n:   
.. i18n:   With this configuration, you can also easily update your costs price with a simple .csv import using one of the 
.. i18n:   client (GTK or Web).
..

::

  This improves OpenERP multi-cost handling, overall for multi-company, regarding to product costs. It also improves
  the multi-currency handling into analytic accounting.
  
  This module (as all c2c_multicost*) is a backport to current stable from our work merged in the trunk branch of OpenERP.
  
  What has been done here:
  
   * Add price type on company as a property (with default value based on standard price)
  
   * Analytic accounting
    * Use the price type currency and field for cost valuation (including timesheet)
    * Add multi-currency on analytic lines (similar to financial accounting)
    * Allow to share the same product between company employees, with different cost for each one
    * Correct all "costs" indicators into analytic account to base them on the correct currency (owner's company)
  
   * By default, nothing change for single company implementation (base the cost valuation on standard price)
  
   * Factorise part of function field into analytic accounting
  
  As a result, we can now share the same product between companies that don't have the same currency and/or same cost price. 
  We can also manage one field per company on the product form to store the cost for a given price type (and so for a given company).
  
  
  Warning !! 
  
  This module change some functions signatures in some object. In order to have it running properly,
  you need to install every c2c_multicost_*, where * is the name of the already install module.
  
  Example : If you're using hr_expense, then don't forget to install c2c_multicost_expense.
  
  Please, also verify that one of your specific modules on concerned methodes.
       
  How to setup:
  -------------
  
  This module won't change anything unless you assign a different price_type to your company. This price type has
  to point on one of the product.product "float" field as the costing value for this company. The currency used is the one
  define into the price type. It has to be the same than your company currency !
  
  Example 1 :
  
  Your company is in EUR. You can setup a different price type for your company. Let it point on a new product.product field,
  lets say "my_new_product_cost_price" (this field needs to be defined in one of your specific module). Now this new field
  will be used as the new cost price for all product.
  
  Example 2 :
  
  You have two companies, one in CHF and the other in EUR. Assuming each of your company has its own price type pointing on
  their own float field, you can now have one product but a different cost for each company.
  
  Company 1 (EUR) -> price type "Cost EUR", pointing on "standard_price"
  
  Company 2 (CHF) -> price type "Cost CHF", pointing on "standard_price_chf"
  
  With this configuration, you can also easily update your costs price with a simple .csv import using one of the 
  client (GTK or Web).

.. i18n: Download links
.. i18n: --------------
..

Download links
--------------

.. i18n: You can download this module as a zip file in the following version:
..

You can download this module as a zip file in the following version:

.. i18n: (No download links available)
..

(No download links available)

.. i18n: Dependencies
.. i18n: ------------
..

Dependencies
------------

.. i18n:  * :mod:`account`
.. i18n:  * :mod:`account_analytic_analysis`
.. i18n:  * :mod:`product`
..

 * :mod:`account`
 * :mod:`account_analytic_analysis`
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

.. i18n:  * \* INHERIT res.company.product.property.form.inherit (form)
..

 * \* INHERIT res.company.product.property.form.inherit (form)

.. i18n: Objects
.. i18n: -------
..

Objects
-------

.. i18n: None
..

None
