
.. module:: sale_forecast
    :synopsis: Sales Forecasts, goals and statistics 
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

    <div class="js-kit-rating" title="" permalink="" standalone="yes" path="/sale_forecast"></div>
    <script src="http://js-kit.com/ratings.js"></script>

Sales Forecasts, goals and statistics (*sale_forecast*)
=======================================================
:Module: sale_forecast
:Name: Sales Forecasts, goals and statistics
:Version: 5.0.1.0
:Author: Tiny
:Directory: sale_forecast
:Web: http://www.openerp.com
:Official module: no
:Quality certified: no

Description
-----------

::

  This module allows manager to do their sales forecast.
  Different reports are set up for forecast and sales analysis.

Download links
--------------

You can download this module as a zip file in the following version:

  * `5.0 <http://www.openerp.com/download/modules/5.0/sale_forecast.zip>`_
  * `trunk <http://www.openerp.com/download/modules/trunk/sale_forecast.zip>`_


Dependencies
------------

 * :mod:`account`
 * :mod:`account_invoice_salesman`
 * :mod:`crm`
 * :mod:`sale`

Reports
-------

 * Sale Forecast

 * Sales Forecast By Salesman

Menus
-------

 * Sales Management/Sales Forecasts
 * Sales Management/Sales Forecasts/New Sales Forecasts
 * Sales Management/Sales Forecasts/My Managing Sales Forecast
 * Sales Management/Sales Forecasts/Current Sales Forecast
 * Sales Management/Sales Forecasts/Forecast Reports
 * Sales Management/Sales Forecasts/Forecast Reports/Number Of Invoice
 * Sales Management/Sales Forecasts/Forecast Reports/Amount Invoiced
 * Sales Management/Sales Forecasts/Forecast Reports/Cases
 * Sales Management/Sales Forecasts/Forecast Reports/Amount Sales
 * Sales Management/Sales Forecasts/Forecast Reports/Number of Sales order

Views
-----

 * sale_forecast.tree (tree)
 * sale_forecast.form (form)
 * sale.forecast.line.graph (graph)


Objects
-------

Object: Sales Forecast (sale.forecast)
######################################



:user_id: Responsible, many2one, required





:name: Sales Forecast, char, required





:date_from: Start Period, date, required





:line_ids: Forecast lines, one2many





:note: Notes, text





:state: State, selection, required





:date_to: End Period, date, required





:forecast_rate: Progress (%), float, readonly




Object: Forecast Line (sale.forecast.line)
##########################################



:state_cancel: Cancel, boolean





:computation_type: Computation Base On, selection, required





:state_draft: Draft, boolean





:feedback: Feedback Comment, text





:user_id: Salesman, many2one, required





:state_confirmed: Confirmed, boolean





:crm_case_categ: Case Category, many2many





:note: Note, text





:amount: Value Forecasted, float





:computed_amount: Real Value, float, readonly





:final_evolution: Performance, selection





:forecast_rate: Progress (%), float, readonly





:state_done: Done, boolean





:product_categ: Product Category, many2many





:product_product: Products, many2many





:crm_case_section: Case Section, many2many





:forecast_id: Forecast, many2one


