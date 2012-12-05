
.. i18n: .. module:: mrp_operations
.. i18n:     :synopsis: Workcenter Production start end workflow (Official, Quality Certified)
.. i18n:     :noindex:
.. i18n: .. 
..

.. module:: mrp_operations
    :synopsis: Workcenter Production start end workflow (Official, Quality Certified)
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
.. i18n:     <div class="js-kit-rating" title="" permalink="" standalone="yes" path="/mrp_operations"></div>
.. i18n:     <script src="http://js-kit.com/ratings.js"></script>
..

.. raw:: html

    <div class="js-kit-rating" title="" permalink="" standalone="yes" path="/mrp_operations"></div>
    <script src="http://js-kit.com/ratings.js"></script>

.. i18n: Workcenter Production start end workflow (*mrp_operations*)
.. i18n: ===========================================================
.. i18n: :Module: mrp_operations
.. i18n: :Name: Workcenter Production start end workflow
.. i18n: :Version: 5.0.1.0
.. i18n: :Author: Tiny
.. i18n: :Directory: mrp_operations
.. i18n: :Web: http://www.openerp.com
.. i18n: :Official module: yes
.. i18n: :Quality certified: yes
..

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

.. i18n: Description
.. i18n: -----------
..

Description
-----------

.. i18n: ::
.. i18n: 
.. i18n:   This module adds state, date_start,date_stop in production order operation lines
.. i18n:        (in the "Workcenters" tab)
.. i18n:        State: draft, confirm, done, cancel
.. i18n:        When finishing/confirming,cancelling production orders set all state lines to the according state
.. i18n:        Create menus:
.. i18n:            Production Management > All Operations
.. i18n:            Production Management > All Operations > Operations To Do (state="confirm")
.. i18n:        Which is a view on "Workcenters" lines in production order,
.. i18n:        editable tree
.. i18n:   
.. i18n:       Add buttons in the form view of production order under workcenter tab:
.. i18n:       * start (set state to confirm), set date_start
.. i18n:       * done (set state to done), set date_stop
.. i18n:       * set to draft (set state to draft)
.. i18n:       * cancel set state to cancel
.. i18n:   
.. i18n:       When the production order becomes "ready to produce", operations must
.. i18n:       become 'confirmed'. When the production order is done, all operations
.. i18n:       must become done.
.. i18n:   
.. i18n:       The field delay is the delay(stop date - start date).
.. i18n:       So that we can compare the theoretic delay and real delay.
..

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

.. i18n: Download links
.. i18n: --------------
..

Download links
--------------

.. i18n: You can download this module as a zip file in the following version:
..

You can download this module as a zip file in the following version:

.. i18n:   * `5.0 <http://www.openerp.com/download/modules/5.0/mrp_operations.zip>`_
.. i18n:   * `trunk <http://www.openerp.com/download/modules/trunk/mrp_operations.zip>`_
..

  * `5.0 <http://www.openerp.com/download/modules/5.0/mrp_operations.zip>`_
  * `trunk <http://www.openerp.com/download/modules/trunk/mrp_operations.zip>`_

.. i18n: Dependencies
.. i18n: ------------
..

Dependencies
------------

.. i18n:  * :mod:`stock`
.. i18n:  * :mod:`hr`
.. i18n:  * :mod:`purchase`
.. i18n:  * :mod:`product`
.. i18n:  * :mod:`mrp`
..

 * :mod:`stock`
 * :mod:`hr`
 * :mod:`purchase`
 * :mod:`product`
 * :mod:`mrp`

.. i18n: Reports
.. i18n: -------
..

Reports
-------

.. i18n:  * Workcenters Barcode
.. i18n: 
.. i18n:  * Start/Stop Barcode
..

 * Workcenters Barcode

 * Start/Stop Barcode

.. i18n: Menus
.. i18n: -------
..

Menus
-------

.. i18n:  * Manufacturing/All Work Orders
.. i18n:  * Manufacturing/All Work Orders/Work Orders to Do
.. i18n:  * Manufacturing/All Work Orders/Future Work Orders
.. i18n:  * Manufacturing/All Work Orders/Work Orders Planning
.. i18n:  * Manufacturing/Configuration/Start - Stop Codes
.. i18n:  * Manufacturing/Work Order Events Using Bar Codes
..

 * Manufacturing/All Work Orders
 * Manufacturing/All Work Orders/Work Orders to Do
 * Manufacturing/All Work Orders/Future Work Orders
 * Manufacturing/All Work Orders/Work Orders Planning
 * Manufacturing/Configuration/Start - Stop Codes
 * Manufacturing/Work Order Events Using Bar Codes

.. i18n: Views
.. i18n: -----
..

Views
-----

.. i18n:  * mrp.production.workcenter.line.tree (tree)
.. i18n:  * mrp.production.workcenter.line.form (form)
.. i18n:  * mrp.production.workcenter.line.calendar (calendar)
.. i18n:  * mrp.production.workcenter.line.gantt (gantt)
.. i18n:  * mrp.production.code.tree (tree)
.. i18n:  * mrp.production.code.form (form)
.. i18n:  * mrp.production.operation.tree (tree)
.. i18n:  * graph.in.hrs.workcenter (graph)
.. i18n:  * \* INHERIT mrp.production.allow_reorder.form (form)
.. i18n:  * mrp.perations.calendar (calendar)
..

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

.. i18n: Objects
.. i18n: -------
..

Objects
-------

.. i18n: Object: mrp_operations.operation.code (mrp_operations.operation.code)
.. i18n: #####################################################################
..

Object: mrp_operations.operation.code (mrp_operations.operation.code)
#####################################################################

.. i18n: :start_stop: Status, selection, required
..

:start_stop: Status, selection, required

.. i18n: :code: Code, char, required
..

:code: Code, char, required

.. i18n: :name: Operation Name, char, required
..

:name: Operation Name, char, required

.. i18n: Object: mrp_operations.operation (mrp_operations.operation)
.. i18n: ###########################################################
..

Object: mrp_operations.operation (mrp_operations.operation)
###########################################################

.. i18n: :code_id: Code, many2one, required
..

:code_id: Code, many2one, required

.. i18n: :date_finished: End Date, datetime
..

:date_finished: End Date, datetime

.. i18n: :date_start: Start Date, datetime
..

:date_start: Start Date, datetime

.. i18n: :production_id: Production, many2one, required
..

:production_id: Production, many2one, required

.. i18n: :order_date: Order Date, date, readonly
..

:order_date: Order Date, date, readonly

.. i18n: :workcenter_id: Workcenter, many2one, required
..

:workcenter_id: Workcenter, many2one, required
