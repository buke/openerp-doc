
.. module:: nan_stock_production_lot_quality_control
    :synopsis: Production Lot Quality Control 
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

    <div class="js-kit-rating" title="" permalink="" standalone="yes" path="/nan_stock_production_lot_quality_control"></div>
    <script src="http://js-kit.com/ratings.js"></script>

Production Lot Quality Control (*nan_stock_production_lot_quality_control*)
===========================================================================
:Module: nan_stock_production_lot_quality_control
:Name: Production Lot Quality Control
:Version: 5.0.0.1
:Author: NaN for Trod y Avia, S.L.
:Directory: nan_stock_production_lot_quality_control
:Web: 
:Official module: no
:Quality certified: no

Description
-----------

::

  This module adds two quality controls to production lots on arrival and after production. The idea is that the first
  test will be 'Generic' and check for things like correct packaging. The second will be specific to the product in question.

Download links
--------------

You can download this module as a zip file in the following version:

(No download links available)


Dependencies
------------

 * :mod:`stock`
 * :mod:`nan_quality_control`

Reports
-------

None


Menus
-------

 * Quality Control/Production Lot Tests
 * Quality Control/Production Lot Tests/Draft Tests
 * Quality Control/Production Lot Tests/Confirmed Tests
 * Quality Control/Production Lot Tests/Valid Tests
 * Quality Control/Production Lot Tests/Invalid Tests

Views
-----

 * \* INHERIT product.product.form.quality (form)
 * \* INHERIT stock.production.lot.form.workflow (form)


Objects
-------

None
