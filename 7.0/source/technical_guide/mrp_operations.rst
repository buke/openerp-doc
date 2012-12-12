
.. module:: mrp_operations
    :synopsis: Workcenter Production start end workflow (Official, Quality Certified)
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

    <div class="js-kit-rating" title="" permalink="" standalone="yes" path="/mrp_operations"></div>
    <script src="http://js-kit.com/ratings.js"></script>

Workcenter Production start end workflow (*mrp_operations*)
===========================================================
:Module: mrp_operations
:Name: Workcenter Production start end workflow
:Version: 5.0.1.0
:Author: Tiny
:Directory: mrp_operations
:Web: http://www.openerp.com
:Official module: yes
:Quality certified: yes

Description
-----------

::

  This module adds state, date_start,date_stop in production order operation lines
       (in the "Workcenters" tab)
       State: draft, confirm, done, cancel
       When finishing/confirming,cancelling production orders set all state lines to the according state
       Create menus:
           Production Management > All Operations
           Production Management > All Operations > Operations To Do (state="confirm")
       Which is a view on "Workcenters" lines in production order,
       editable tree
  
      Add buttons in the form view of production order under workcenter tab:
      * start (set state to confirm), set date_start
      * done (set state to done), set date_stop
      * set to draft (set state to draft)
      * cancel set state to cancel
  
      When the production order becomes "ready to produce", operations must
      become 'confirmed'. When the production order is done, all operations
      must become done.
  
      The field delay is the delay(stop date - start date).
      So that we can compare the theoretic delay and real delay.

Download links
--------------

You can download this module as a zip file in the following version:

  * `5.0 <http://www.openerp.com/download/modules/5.0/mrp_operations.zip>`_
  * `trunk <http://www.openerp.com/download/modules/trunk/mrp_operations.zip>`_


Dependencies
------------

 * :mod:`stock`
 * :mod:`hr`
 * :mod:`purchase`
 * :mod:`product`
 * :mod:`mrp`

Reports
-------

 * Workcenters Barcode

 * Start/Stop Barcode

Menus
-------

 * Manufacturing/All Work Orders
 * Manufacturing/All Work Orders/Work Orders to Do
 * Manufacturing/All Work Orders/Future Work Orders
 * Manufacturing/All Work Orders/Work Orders Planning
 * Manufacturing/Configuration/Start - Stop Codes
 * Manufacturing/Work Order Events Using Bar Codes

Views
-----

 * mrp.production.workcenter.line.tree (tree)
 * mrp.production.workcenter.line.form (form)
 * mrp.production.workcenter.line.calendar (calendar)
 * mrp.production.workcenter.line.gantt (gantt)
 * mrp.production.code.tree (tree)
 * mrp.production.code.form (form)
 * mrp.production.operation.tree (tree)
 * graph.in.hrs.workcenter (graph)
 * \* INHERIT mrp.production.allow_reorder.form (form)
 * mrp.perations.calendar (calendar)


Objects
-------

Object: mrp_operations.operation.code (mrp_operations.operation.code)
#####################################################################



:start_stop: Status, selection, required





:code: Code, char, required





:name: Operation Name, char, required




Object: mrp_operations.operation (mrp_operations.operation)
###########################################################



:code_id: Code, many2one, required





:date_finished: End Date, datetime





:date_start: Start Date, datetime





:production_id: Production, many2one, required





:order_date: Order Date, date, readonly





:workcenter_id: Workcenter, many2one, required


