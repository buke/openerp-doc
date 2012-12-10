
.. i18n: .. module:: report_mrp
.. i18n:     :synopsis: MRP Management - Reporting (Official, Quality Certified)
.. i18n:     :noindex:
.. i18n: .. 
..

.. module:: report_mrp
    :synopsis: MRP Management - Reporting (Official, Quality Certified)
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
.. i18n:     <div class="js-kit-rating" title="" permalink="" standalone="yes" path="/report_mrp"></div>
.. i18n:     <script src="http://js-kit.com/ratings.js"></script>
..

.. raw:: html

    <div class="js-kit-rating" title="" permalink="" standalone="yes" path="/report_mrp"></div>
    <script src="http://js-kit.com/ratings.js"></script>

.. i18n: MRP Management - Reporting (*report_mrp*)
.. i18n: =========================================
.. i18n: :Module: report_mrp
.. i18n: :Name: MRP Management - Reporting
.. i18n: :Version: 5.0.1.0
.. i18n: :Author: Tiny
.. i18n: :Directory: report_mrp
.. i18n: :Web: http://www.openerp.com
.. i18n: :Official module: yes
.. i18n: :Quality certified: yes
..

MRP Management - Reporting (*report_mrp*)
=========================================
:Module: report_mrp
:Name: MRP Management - Reporting
:Version: 5.0.1.0
:Author: Tiny
:Directory: report_mrp
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
.. i18n:   A module that adds new reports based on MRP cases.
.. i18n:       Workcenter loads, Weekly Stock value variation
..

::

  A module that adds new reports based on MRP cases.
      Workcenter loads, Weekly Stock value variation

.. i18n: Download links
.. i18n: --------------
..

Download links
--------------

.. i18n: You can download this module as a zip file in the following version:
..

You can download this module as a zip file in the following version:

.. i18n:   * `4.2 <http://www.openerp.com/download/modules/4.2/report_mrp.zip>`_
.. i18n:   * `5.0 <http://www.openerp.com/download/modules/5.0/report_mrp.zip>`_
.. i18n:   * `trunk <http://www.openerp.com/download/modules/trunk/report_mrp.zip>`_
..

  * `4.2 <http://www.openerp.com/download/modules/4.2/report_mrp.zip>`_
  * `5.0 <http://www.openerp.com/download/modules/5.0/report_mrp.zip>`_
  * `trunk <http://www.openerp.com/download/modules/trunk/report_mrp.zip>`_

.. i18n: Dependencies
.. i18n: ------------
..

Dependencies
------------

.. i18n:  * :mod:`mrp`
..

 * :mod:`mrp`

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

.. i18n:  * Manufacturing/Reporting
.. i18n:  * Manufacturing/Reporting/Workcenter Loads
.. i18n:  * Manufacturing/Reporting/Weekly Stock Value Variation
..

 * Manufacturing/Reporting
 * Manufacturing/Reporting/Workcenter Loads
 * Manufacturing/Reporting/Weekly Stock Value Variation

.. i18n: Views
.. i18n: -----
..

Views
-----

.. i18n:  * report.workcenter.load.tree (tree)
.. i18n:  * report.workcenter.load.graph (graph)
.. i18n:  * report.workcenter.load.form (form)
.. i18n:  * report.mrp.inout.tree (tree)
.. i18n:  * report.mrp.inout.form (form)
.. i18n:  * report.mrp.inout.graph (graph)
..

 * report.workcenter.load.tree (tree)
 * report.workcenter.load.graph (graph)
 * report.workcenter.load.form (form)
 * report.mrp.inout.tree (tree)
 * report.mrp.inout.form (form)
 * report.mrp.inout.graph (graph)

.. i18n: Objects
.. i18n: -------
..

Objects
-------

.. i18n: Object: Workcenter Load (report.workcenter.load)
.. i18n: ################################################
..

Object: Workcenter Load (report.workcenter.load)
################################################

.. i18n: :workcenter_id: Workcenter, many2one, required
..

:workcenter_id: Workcenter, many2one, required

.. i18n: :name: Week, char, required
..

:name: Week, char, required

.. i18n: :hour: Nbr of hour, float
..

:hour: Nbr of hour, float

.. i18n: :cycle: Nbr of cycle, float
..

:cycle: Nbr of cycle, float

.. i18n: Object: Stock value variation (report.mrp.inout)
.. i18n: ################################################
..

Object: Stock value variation (report.mrp.inout)
################################################

.. i18n: :date: Week, char, required
..

:date: Week, char, required

.. i18n: :value: Stock value, float, required
..

:value: Stock value, float, required
