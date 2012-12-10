
.. i18n: .. module:: account_report
.. i18n:     :synopsis: Reporting for accounting (Official, Quality Certified)
.. i18n:     :noindex:
.. i18n: .. 
..

.. module:: account_report
    :synopsis: Reporting for accounting (Official, Quality Certified)
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
.. i18n:     <div class="js-kit-rating" title="" permalink="" standalone="yes" path="/account_report"></div>
.. i18n:     <script src="http://js-kit.com/ratings.js"></script>
..

.. raw:: html

    <div class="js-kit-rating" title="" permalink="" standalone="yes" path="/account_report"></div>
    <script src="http://js-kit.com/ratings.js"></script>

.. i18n: Reporting for accounting (*account_report*)
.. i18n: ===========================================
.. i18n: :Module: account_report
.. i18n: :Name: Reporting for accounting
.. i18n: :Version: 5.0.1.1
.. i18n: :Author: Tiny
.. i18n: :Directory: account_report
.. i18n: :Web: http://www.openerp.com
.. i18n: :Official module: yes
.. i18n: :Quality certified: yes
..

Reporting for accounting (*account_report*)
===========================================
:Module: account_report
:Name: Reporting for accounting
:Version: 5.0.1.1
:Author: Tiny
:Directory: account_report
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
.. i18n:   Financial and accounting reporting
.. i18n:       Fiscal statements
.. i18n:       Indicators
..

::

  Financial and accounting reporting
      Fiscal statements
      Indicators

.. i18n: Download links
.. i18n: --------------
..

Download links
--------------

.. i18n: You can download this module as a zip file in the following version:
..

You can download this module as a zip file in the following version:

.. i18n:   * `4.2 <http://www.openerp.com/download/modules/4.2/account_report.zip>`_
.. i18n:   * `5.0 <http://www.openerp.com/download/modules/5.0/account_report.zip>`_
.. i18n:   * `trunk <http://www.openerp.com/download/modules/trunk/account_report.zip>`_
..

  * `4.2 <http://www.openerp.com/download/modules/4.2/account_report.zip>`_
  * `5.0 <http://www.openerp.com/download/modules/5.0/account_report.zip>`_
  * `trunk <http://www.openerp.com/download/modules/trunk/account_report.zip>`_

.. i18n: Dependencies
.. i18n: ------------
..

Dependencies
------------

.. i18n:  * :mod:`account`
..

 * :mod:`account`

.. i18n: Reports
.. i18n: -------
..

Reports
-------

.. i18n:  * Fiscal Statements
.. i18n: 
.. i18n:  * Indicators
.. i18n: 
.. i18n:  * Print Indicators in PDF
..

 * Fiscal Statements

 * Indicators

 * Print Indicators in PDF

.. i18n: Menus
.. i18n: -------
..

Menus
-------

.. i18n:  * Financial Management/Configuration/Custom reporting
.. i18n:  * Financial Management/Configuration/Custom reporting/New Reporting Item Formula
.. i18n:  * Financial Management/Reporting/Custom reporting
.. i18n:  * Financial Management/Reporting/Custom reporting/Fiscal Statements reporting
.. i18n:  * Financial Management/Reporting/Custom reporting/Indicators reporting
.. i18n:  * Financial Management/Reporting/Custom reporting/Other reports
.. i18n:  * Financial Management/Reporting/Custom reporting/Print Indicators
..

 * Financial Management/Configuration/Custom reporting
 * Financial Management/Configuration/Custom reporting/New Reporting Item Formula
 * Financial Management/Reporting/Custom reporting
 * Financial Management/Reporting/Custom reporting/Fiscal Statements reporting
 * Financial Management/Reporting/Custom reporting/Indicators reporting
 * Financial Management/Reporting/Custom reporting/Other reports
 * Financial Management/Reporting/Custom reporting/Print Indicators

.. i18n: Views
.. i18n: -----
..

Views
-----

.. i18n:  * account.report.report.form (form)
.. i18n:  * account.report.report.tree.simple (tree)
.. i18n:  * account.report.report.tree (tree)
.. i18n:  * account.report.history1 (tree)
.. i18n:  * account.report.history2 (form)
.. i18n:  * account.report.history3 (graph)
..

 * account.report.report.form (form)
 * account.report.report.tree.simple (tree)
 * account.report.report.tree (tree)
 * account.report.history1 (tree)
 * account.report.history2 (form)
 * account.report.history3 (graph)

.. i18n: Objects
.. i18n: -------
..

Objects
-------

.. i18n: Object: Account reporting (account.report.report)
.. i18n: #################################################
..

Object: Account reporting (account.report.report)
#################################################

.. i18n: :status: Status, selection, readonly
..

:status: Status, selection, readonly

.. i18n: :note: Note, text
..

:note: Note, text

.. i18n: :disp_tree: Display Tree, boolean
..

:disp_tree: Display Tree, boolean

.. i18n:     *When the indicators are printed, if one indicator is set with this field to True, then it will display one more graphs with all its children in tree*
..

    *When the indicators are printed, if one indicator is set with this field to True, then it will display one more graphs with all its children in tree*

.. i18n: :code: Code, char, required
..

:code: Code, char, required

.. i18n: :name: Name, char, required
..

:name: Name, char, required

.. i18n: :sequence: Sequence, integer
..

:sequence: Sequence, integer

.. i18n: :type: Type, selection, required
..

:type: Type, selection, required

.. i18n: :child_ids: Children, one2many
..

:child_ids: Children, one2many

.. i18n: :badness_limit: Badness Indicator Limit, float
..

:badness_limit: Badness Indicator Limit, float

.. i18n:     *This Value sets the limit of badness.*
..

    *This Value sets the limit of badness.*

.. i18n: :goodness_limit: Goodness Indicator Limit, float
..

:goodness_limit: Goodness Indicator Limit, float

.. i18n:     *This Value sets the limit of goodness.*
..

    *This Value sets the limit of goodness.*

.. i18n: :parent_id: Parent, many2one
..

:parent_id: Parent, many2one

.. i18n: :amount: Value, float, readonly
..

:amount: Value, float, readonly

.. i18n: :disp_graph: Display As Graph, boolean
..

:disp_graph: Display As Graph, boolean

.. i18n:     *If the field is set to True, information will be printed as a Graph, otherwise as an array.*
..

    *If the field is set to True, information will be printed as a Graph, otherwise as an array.*

.. i18n: :active: Active, boolean
..

:active: Active, boolean

.. i18n: :expression: Expression, char, required
..

:expression: Expression, char, required

.. i18n: Object: Indicator (account.report.history)
.. i18n: ##########################################
..

Object: Indicator (account.report.history)
##########################################

.. i18n: :tmp: temp, integer, readonly
..

:tmp: temp, integer, readonly

.. i18n: :fiscalyear_id: Fiscal Year, many2one, readonly
..

:fiscalyear_id: Fiscal Year, many2one, readonly

.. i18n: :period_id: Period, many2one, readonly
..

:period_id: Period, many2one, readonly

.. i18n: :name: Indicator, many2one, readonly
..

:name: Indicator, many2one, readonly

.. i18n: :val: Value, float, readonly
..

:val: Value, float, readonly
