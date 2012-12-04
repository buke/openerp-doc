
.. module:: product_qt
    :synopsis: Products & Pricelists- Define quality control and testing parameters in product 
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

    <div class="js-kit-rating" title="" permalink="" standalone="yes" path="/product_qt"></div>
    <script src="http://js-kit.com/ratings.js"></script>

Products & Pricelists- Define quality control and testing parameters in product (*product_qt*)
==============================================================================================
:Module: product_qt
:Name: Products & Pricelists- Define quality control and testing parameters in product
:Version: 5.0.1.0
:Author: Tiny
:Directory: product_qt
:Web: 
:Official module: no
:Quality certified: no

Description
-----------

::

  This module add quality control and testing parameters in product
      1> configure QC parameters for particular product.
      2> QC testing on purchased raw material.
      3> QC testing during production.
      3> QC testing on finished goods.

Download links
--------------

You can download this module as a zip file in the following version:

  * `5.0 <http://www.openerp.com/download/modules/5.0/product_qt.zip>`_
  * `trunk <http://www.openerp.com/download/modules/trunk/product_qt.zip>`_


Dependencies
------------

 * :mod:`base`
 * :mod:`mrp_operations`

Reports
-------

None


Menus
-------

 * Stock Management/Testing Result
 * Stock Management/Testing Result/Testing Result

Views
-----

 * quality.testing.form (form)
 * quality.testing.tree (tree)
 * quality.testing.config.tree (tree)
 * quality.testing.config.form (form)
 * \* INHERIT product.testing.form (form)
 * \* INHERIT quality.testing.form (form)
 * \* INHERIT quality.testing.move.form (form)
 * testing_result.tree (tree)
 * testing_result.form (form)
 * \* INHERIT quality.testing.mrp.production.form (form)
 * \* INHERIT quality.testing.mrp.production.form (form)
 * \* INHERIT quality.testing.mrp.production.tree (tree)
 * \* INHERIT quality.testing.mrp.form (form)


Objects
-------

Object: quality testings (quality.test)
#######################################



:name: Test Case, char





:description: Description, text




Object: testing.result (testing.result)
#######################################



:product: Product, many2one, readonly





:type: Testing Type, selection, readonly





:test_date: Testing Date, date





:test_case: Cases, one2many





:tester: Tested By, many2one




Object: quality test configuration (quality.test.config)
########################################################



:product_idf: Product, many2one





:max_limit: Max Limit, float

    *Maximum Limit of measure*



:actual_val: Actual Value, float





:name: Test Case, many2one





:min_limit: Min Limit, float

    *Minimum Limit of measure*



:state: Status, selection, readonly





:product_idr: Product, many2one





:product_idp: Product, many2one





:test_id: Test Result, many2one





:uom: UOM, many2one


