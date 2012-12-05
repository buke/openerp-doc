
.. i18n: .. module:: sale_forecast
.. i18n:     :synopsis: Sales Forecasts, goals and statistics 
.. i18n:     :noindex:
.. i18n: .. 
..

.. module:: sale_forecast
    :synopsis: Sales Forecasts, goals and statistics 
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
.. i18n:     <div class="js-kit-rating" title="" permalink="" standalone="yes" path="/sale_forecast"></div>
.. i18n:     <script src="http://js-kit.com/ratings.js"></script>
..

.. raw:: html

    <div class="js-kit-rating" title="" permalink="" standalone="yes" path="/sale_forecast"></div>
    <script src="http://js-kit.com/ratings.js"></script>

.. i18n: Sales Forecasts, goals and statistics (*sale_forecast*)
.. i18n: =======================================================
.. i18n: :Module: sale_forecast
.. i18n: :Name: Sales Forecasts, goals and statistics
.. i18n: :Version: 5.0.1.0
.. i18n: :Author: Tiny
.. i18n: :Directory: sale_forecast
.. i18n: :Web: http://www.openerp.com
.. i18n: :Official module: no
.. i18n: :Quality certified: no
..

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

.. i18n: Description
.. i18n: -----------
..

Description
-----------

.. i18n: ::
.. i18n: 
.. i18n:   This module allows manager to do their sales forecast.
.. i18n:   Different reports are set up for forecast and sales analysis.
..

::

  This module allows manager to do their sales forecast.
  Different reports are set up for forecast and sales analysis.

.. i18n: Download links
.. i18n: --------------
..

Download links
--------------

.. i18n: You can download this module as a zip file in the following version:
..

You can download this module as a zip file in the following version:

.. i18n:   * `5.0 <http://www.openerp.com/download/modules/5.0/sale_forecast.zip>`_
.. i18n:   * `trunk <http://www.openerp.com/download/modules/trunk/sale_forecast.zip>`_
..

  * `5.0 <http://www.openerp.com/download/modules/5.0/sale_forecast.zip>`_
  * `trunk <http://www.openerp.com/download/modules/trunk/sale_forecast.zip>`_

.. i18n: Dependencies
.. i18n: ------------
..

Dependencies
------------

.. i18n:  * :mod:`account`
.. i18n:  * :mod:`account_invoice_salesman`
.. i18n:  * :mod:`crm`
.. i18n:  * :mod:`sale`
..

 * :mod:`account`
 * :mod:`account_invoice_salesman`
 * :mod:`crm`
 * :mod:`sale`

.. i18n: Reports
.. i18n: -------
..

Reports
-------

.. i18n:  * Sale Forecast
.. i18n: 
.. i18n:  * Sales Forecast By Salesman
..

 * Sale Forecast

 * Sales Forecast By Salesman

.. i18n: Menus
.. i18n: -------
..

Menus
-------

.. i18n:  * Sales Management/Sales Forecasts
.. i18n:  * Sales Management/Sales Forecasts/New Sales Forecasts
.. i18n:  * Sales Management/Sales Forecasts/My Managing Sales Forecast
.. i18n:  * Sales Management/Sales Forecasts/Current Sales Forecast
.. i18n:  * Sales Management/Sales Forecasts/Forecast Reports
.. i18n:  * Sales Management/Sales Forecasts/Forecast Reports/Number Of Invoice
.. i18n:  * Sales Management/Sales Forecasts/Forecast Reports/Amount Invoiced
.. i18n:  * Sales Management/Sales Forecasts/Forecast Reports/Cases
.. i18n:  * Sales Management/Sales Forecasts/Forecast Reports/Amount Sales
.. i18n:  * Sales Management/Sales Forecasts/Forecast Reports/Number of Sales order
..

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

.. i18n: Views
.. i18n: -----
..

Views
-----

.. i18n:  * sale_forecast.tree (tree)
.. i18n:  * sale_forecast.form (form)
.. i18n:  * sale.forecast.line.graph (graph)
..

 * sale_forecast.tree (tree)
 * sale_forecast.form (form)
 * sale.forecast.line.graph (graph)

.. i18n: Objects
.. i18n: -------
..

Objects
-------

.. i18n: Object: Sales Forecast (sale.forecast)
.. i18n: ######################################
..

Object: Sales Forecast (sale.forecast)
######################################

.. i18n: :user_id: Responsible, many2one, required
..

:user_id: Responsible, many2one, required

.. i18n: :name: Sales Forecast, char, required
..

:name: Sales Forecast, char, required

.. i18n: :date_from: Start Period, date, required
..

:date_from: Start Period, date, required

.. i18n: :line_ids: Forecast lines, one2many
..

:line_ids: Forecast lines, one2many

.. i18n: :note: Notes, text
..

:note: Notes, text

.. i18n: :state: State, selection, required
..

:state: State, selection, required

.. i18n: :date_to: End Period, date, required
..

:date_to: End Period, date, required

.. i18n: :forecast_rate: Progress (%), float, readonly
..

:forecast_rate: Progress (%), float, readonly

.. i18n: Object: Forecast Line (sale.forecast.line)
.. i18n: ##########################################
..

Object: Forecast Line (sale.forecast.line)
##########################################

.. i18n: :state_cancel: Cancel, boolean
..

:state_cancel: Cancel, boolean

.. i18n: :computation_type: Computation Base On, selection, required
..

:computation_type: Computation Base On, selection, required

.. i18n: :state_draft: Draft, boolean
..

:state_draft: Draft, boolean

.. i18n: :feedback: Feedback Comment, text
..

:feedback: Feedback Comment, text

.. i18n: :user_id: Salesman, many2one, required
..

:user_id: Salesman, many2one, required

.. i18n: :state_confirmed: Confirmed, boolean
..

:state_confirmed: Confirmed, boolean

.. i18n: :crm_case_categ: Case Category, many2many
..

:crm_case_categ: Case Category, many2many

.. i18n: :note: Note, text
..

:note: Note, text

.. i18n: :amount: Value Forecasted, float
..

:amount: Value Forecasted, float

.. i18n: :computed_amount: Real Value, float, readonly
..

:computed_amount: Real Value, float, readonly

.. i18n: :final_evolution: Performance, selection
..

:final_evolution: Performance, selection

.. i18n: :forecast_rate: Progress (%), float, readonly
..

:forecast_rate: Progress (%), float, readonly

.. i18n: :state_done: Done, boolean
..

:state_done: Done, boolean

.. i18n: :product_categ: Product Category, many2many
..

:product_categ: Product Category, many2many

.. i18n: :product_product: Products, many2many
..

:product_product: Products, many2many

.. i18n: :crm_case_section: Case Section, many2many
..

:crm_case_section: Case Section, many2many

.. i18n: :forecast_id: Forecast, many2one
..

:forecast_id: Forecast, many2one
