
.. module:: stock_planning
    :synopsis: Master Procurement Schedule 
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

    <div class="js-kit-rating" title="" permalink="" standalone="yes" path="/stock_planning"></div>
    <script src="http://js-kit.com/ratings.js"></script>

Master Procurement Schedule (*stock_planning*)
==============================================
:Module: stock_planning
:Name: Master Procurement Schedule
:Version: 5.0.1.0
:Author: Tiny
:Directory: stock_planning
:Web: 
:Official module: no
:Quality certified: no

Description
-----------

::

  This module allows you to manage the planning of procurements based on sales
  forecasts, confirmed orders (customers and suppliers), stock movements, etc.
  You can plan expected outputs and inputs for each warehouses. It also works
  to manage all kind of procurements like purchase orders. That's why it is
  called Master Procurement Schedule instead of the classic Master Production
  Schedule terminology.

Download links
--------------

You can download this module as a zip file in the following version:

  * `4.2 <http://www.openerp.com/download/modules/4.2/stock_planning.zip>`_
  * `5.0 <http://www.openerp.com/download/modules/5.0/stock_planning.zip>`_
  * `trunk <http://www.openerp.com/download/modules/trunk/stock_planning.zip>`_


Dependencies
------------

 * :mod:`stock`
 * :mod:`sale`

Reports
-------

None


Menus
-------

 * Sales Management/Configuration/Create Sales Periods
 * Sales Management/Configuration/Stock and Sales Periods
 * Stock Management/Procurement Forecast
 * Sales Management/Sales Forecasts
 * Sales Management/Sales Forecasts/All Sales Forecasts
 * Sales Management/Sales Forecasts/All Sales Forecasts/Sales Forecast of Current Period
 * Sales Management/Sales Forecasts/My Sales Forecasts
 * Sales Management/Sales Forecasts/My Sales Forecasts/My Forecasts of Current Period
 * Stock Management/Procurement Forecast/Master Procurement Schedule

Views
-----

 * stock.planning.period.form (form)
 * stock.period.form (form)
 * stock.period.tree (tree)
 * stock.planning.sale.prevision.form (form)
 * stock.planning.sale.prevision.tree (tree)
 * stock.planning.sale.prevision.graph (graph)
 * stock.planning.form (form)
 * stock.planning.tree (tree)


Objects
-------

Object: stock.planning.period (stock.planning.period)
#####################################################



:date_stop: End Date, date, required





:date_start: Start Date, date, required





:name: Period Name, char





:period_ids: Periods, one2many




Object: stock.period (stock.period)
###################################



:date_stop: End Date, datetime, required





:date_start: Start Date, datetime, required





:name: Period Name, char





:state: State, selection




Object: stock.planning.sale.prevision (stock.planning.sale.prevision)
#####################################################################



:user_id: Salesman, many2one, readonly





:name: Name, char





:product_uom: Product UoM, many2one, required, readonly





:state: State, selection, readonly





:period_id: Period, many2one, required





:product_qty: Product Quantity, float, required, readonly





:product_amt: Product Amount, float, readonly





:amt_sold: Real Amount Sold, float, readonly





:product_id: Product, many2one, required, readonly




Object: stock.planning (stock.planning)
#######################################



:outgoing: Confirmed Out, float, readonly





:line_time: Past/Future, char, readonly





:incoming: Confirmed In, float, readonly





:product_id: Product, many2one, required





:product_uom: UoM, many2one, required





:incoming_left: Delta In, float, readonly





:warehouse_id: Warehouse, many2one





:stock_start: Stock Simulation, float, readonly





:state: State, selection, readonly





:outgoing_left: Delta Out, float, readonly





:period_id: Period, many2one, required





:planned_outgoing: Forecast Out, float, required





:to_procure: Forecast In, float, required





:planned_sale: Sales Forecast, float, readonly





:name: Name, char


