
.. i18n: .. module:: base_report_creator
.. i18n:     :synopsis: Report Creator (Official, Quality Certified)
.. i18n:     :noindex:
.. i18n: .. 
..

.. module:: base_report_creator
    :synopsis: Report Creator (Official, Quality Certified)
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
.. i18n:     <div class="js-kit-rating" title="" permalink="" standalone="yes" path="/base_report_creator"></div>
.. i18n:     <script src="http://js-kit.com/ratings.js"></script>
..

.. raw:: html

    <div class="js-kit-rating" title="" permalink="" standalone="yes" path="/base_report_creator"></div>
    <script src="http://js-kit.com/ratings.js"></script>

.. i18n: Report Creator (*base_report_creator*)
.. i18n: ======================================
.. i18n: :Module: base_report_creator
.. i18n: :Name: Report Creator
.. i18n: :Version: 5.0.1.0
.. i18n: :Author: Tiny & Axelor
.. i18n: :Directory: base_report_creator
.. i18n: :Web: 
.. i18n: :Official module: yes
.. i18n: :Quality certified: yes
..

Report Creator (*base_report_creator*)
======================================
:Module: base_report_creator
:Name: Report Creator
:Version: 5.0.1.0
:Author: Tiny & Axelor
:Directory: base_report_creator
:Web: 
:Official module: yes
:Quality certified: yes

.. i18n: Description
.. i18n: -----------
..

Description
-----------

.. i18n: ::
.. i18n: 
.. i18n:   This modules allows you to create any statistic
.. i18n:   report on several object. It's a SQL query builder and browser
.. i18n:   for and users.
.. i18n:   
.. i18n:   After installing the module, it adds a menu to define custom report in
.. i18n:   the "Dashboard" menu.
..

::

  This modules allows you to create any statistic
  report on several object. It's a SQL query builder and browser
  for and users.
  
  After installing the module, it adds a menu to define custom report in
  the "Dashboard" menu.

.. i18n: Download links
.. i18n: --------------
..

Download links
--------------

.. i18n: You can download this module as a zip file in the following version:
..

You can download this module as a zip file in the following version:

.. i18n:   * `5.0 <http://www.openerp.com/download/modules/5.0/base_report_creator.zip>`_
.. i18n:   * `trunk <http://www.openerp.com/download/modules/trunk/base_report_creator.zip>`_
..

  * `5.0 <http://www.openerp.com/download/modules/5.0/base_report_creator.zip>`_
  * `trunk <http://www.openerp.com/download/modules/trunk/base_report_creator.zip>`_

.. i18n: Dependencies
.. i18n: ------------
..

Dependencies
------------

.. i18n:  * :mod:`base`
.. i18n:  * :mod:`board`
..

 * :mod:`base`
 * :mod:`board`

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

.. i18n:  * Dashboards/Configuration/Custom Reports
.. i18n:  * Dashboards/Custom Reports
..

 * Dashboards/Configuration/Custom Reports
 * Dashboards/Custom Reports

.. i18n: Views
.. i18n: -----
..

Views
-----

.. i18n:  * base_report_creator.report.tree (tree)
.. i18n:  * base_report_creator.report.form (form)
.. i18n:  * base_report_creator.report.simple.tree (tree)
..

 * base_report_creator.report.tree (tree)
 * base_report_creator.report.form (form)
 * base_report_creator.report.simple.tree (tree)

.. i18n: Objects
.. i18n: -------
..

Objects
-------

.. i18n: Object: Report (base_report_creator.report)
.. i18n: ###########################################
..

Object: Report (base_report_creator.report)
###########################################

.. i18n: :model_ids: Reported Objects, many2many
..

:model_ids: Reported Objects, many2many

.. i18n: :filter_ids: Filters, one2many
..

:filter_ids: Filters, one2many

.. i18n: :name: Report Name, char, required
..

:name: Report Name, char, required

.. i18n: :sql_query: SQL Query, text, readonly
..

:sql_query: SQL Query, text, readonly

.. i18n: :view_graph_type: Graph Type, selection, required
..

:view_graph_type: Graph Type, selection, required

.. i18n: :view_type2: Second View, selection
..

:view_type2: Second View, selection

.. i18n: :view_type1: First View, selection, required
..

:view_type1: First View, selection, required

.. i18n: :state: Status, selection, required
..

:state: Status, selection, required

.. i18n: :view_type3: Third View, selection
..

:view_type3: Third View, selection

.. i18n: :field_ids: Fields to Display, one2many
..

:field_ids: Fields to Display, one2many

.. i18n: :active: Active, boolean
..

:active: Active, boolean

.. i18n: :group_ids: Authorized Groups, many2many
..

:group_ids: Authorized Groups, many2many

.. i18n: :type: Report Type, selection, required
..

:type: Report Type, selection, required

.. i18n: :view_graph_orientation: Graph Orientation, selection, required
..

:view_graph_orientation: Graph Orientation, selection, required

.. i18n: Object: Display Fields (base_report_creator.report.fields)
.. i18n: ##########################################################
..

Object: Display Fields (base_report_creator.report.fields)
##########################################################

.. i18n: :calendar_mode: Calendar Mode, selection
..

:calendar_mode: Calendar Mode, selection

.. i18n: :group_method: Grouping Method, selection, required
..

:group_method: Grouping Method, selection, required

.. i18n: :sequence: Sequence, integer
..

:sequence: Sequence, integer

.. i18n: :field_id: Field, many2one
..

:field_id: Field, many2one

.. i18n: :graph_mode: Graph Mode, selection
..

:graph_mode: Graph Mode, selection

.. i18n: :report_id: Report, many2one
..

:report_id: Report, many2one

.. i18n: Object: Report Filters (base_report_creator.report.filter)
.. i18n: ##########################################################
..

Object: Report Filters (base_report_creator.report.filter)
##########################################################

.. i18n: :expression: Value, text, required
..

:expression: Value, text, required

.. i18n:     *Provide an expression for the field based on which you want to filter the records.
.. i18n:     e.g. res_partner.id=3*
..

    *Provide an expression for the field based on which you want to filter the records.
    e.g. res_partner.id=3*

.. i18n: :name: Filter Name, char, required
..

:name: Filter Name, char, required

.. i18n: :condition: Condition, selection
..

:condition: Condition, selection

.. i18n: :report_id: Report, many2one
..

:report_id: Report, many2one
