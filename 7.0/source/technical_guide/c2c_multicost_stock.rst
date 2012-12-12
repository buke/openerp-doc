
.. module:: c2c_multicost_stock
    :synopsis: Multi-Costs Handling in stock 
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

    <div class="js-kit-rating" title="" permalink="" standalone="yes" path="/c2c_multicost_stock"></div>
    <script src="http://js-kit.com/ratings.js"></script>

Multi-Costs Handling in stock (*c2c_multicost_stock*)
=====================================================
:Module: c2c_multicost_stock
:Name: Multi-Costs Handling in stock
:Version: 5.0.1.0
:Author: Camptocamp
:Directory: c2c_multicost_stock
:Web: http://camptocamp.com
:Official module: no
:Quality certified: no

Description
-----------

::

  This improves multi-company in OpenERP regarding product costs in company. Refer
  to c2c_multicost_base description for more information...
  
  What has been done here:
  
   * Add price type on company as a property (with default value based on standard price)
  
   * Stock accounting
    * Use the price type currency and field for cost valuation
    * Into stock move for standard price
    * Into stock move for average price
  
  This module needs to be installed if you install both stock and c2c_multicost_base.

Download links
--------------

You can download this module as a zip file in the following version:

(No download links available)


Dependencies
------------

 * :mod:`stock`
 * :mod:`c2c_multicost_base`

Reports
-------

None


Menus
-------


None


Views
-----


None



Objects
-------

None
