
.. module:: board_service
    :synopsis: Dashboard for Service Profile 
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

    <div class="js-kit-rating" title="" permalink="" standalone="yes" path="/board_service"></div>
    <script src="http://js-kit.com/ratings.js"></script>

Dashboard for Service Profile (*board_service*)
===============================================
:Module: board_service
:Name: Dashboard for Service Profile
:Version: 5.0.1.0
:Author: Tiny
:Directory: board_service
:Web: http://www.openerp.com
:Official module: no
:Quality certified: no

Description
-----------

::

  This module displays three dashboards for the logged in user:
          
          A. Dashboard 1: Weekly Dashboard
                     - Draft Forecasts Lines
                     - Turnover by Product and Month
                     - Aged Receivables
                     - Timesheet to Validate
                     - Sales pipeline
                     - Planning Statistics
                      
                  This dashboard is reachable from Dashboards/Service Profile/Weekly Dashboard.
             
          B. Dashboard 2: Daily Dashboard
                     - Open Tasks
                     - Pending Tasks
                     - Inbox
                     - Meeting of the Day
                     - Department's Timesheet Lines of last 3 days.
          
                  This dashboard is reachable from Dashboards/Service Profile/Daily Dashboard.
                  
          C. Dashboard 3 : Random Activities
                     - Random Timesheet Lines from the past 15 days
                     - Random Tasks Closed within the past 15 days
                     - Random Cases Closed within the past 15 days
                     - Random Open Cases Created within the past 15 days
                     - Random Sales Orders Created within the past 15 days
                     - Random Invoices Created within the past 15 days 
  
                  This dashboard is reachable from Dashboards/Service Profile/Random Activities(Within Last 15 Days).

Download links
--------------

You can download this module as a zip file in the following version:

  * `5.0 <http://www.openerp.com/download/modules/5.0/board_service.zip>`_
  * `trunk <http://www.openerp.com/download/modules/trunk/board_service.zip>`_


Dependencies
------------

 * :mod:`base`
 * :mod:`project_gtd`
 * :mod:`board_project`
 * :mod:`sale_forecast`
 * :mod:`crm_configuration`
 * :mod:`report_account`
 * :mod:`report_analytic_planning`
 * :mod:`report_sale`
 * :mod:`report_crm`
 * :mod:`report_task`
 * :mod:`report_timesheet`

Reports
-------

None


Menus
-------

 * Dashboards/Service Profile
 * Dashboards/Service Profile/Weekly Dashboard
 * Dashboards/Service Profile/Daily Dashboard
 * Dashboards/Service Profile/Random Activities(Within Last 15 Days)

Views
-----

 * sale.forecast.line.tree (tree)
 * sale.forecast.line.form (form)
 * board.service.weekly.form (form)
 * CRM - Meetings Tree (tree)
 * project.task.tree (tree)
 * board.service.daily.form (form)
 * board.service.random.activitiy.form (form)


Objects
-------

None
