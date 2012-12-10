
.. i18n: .. module:: crm_timesheet
.. i18n:     :synopsis: CRM Timesheet 
.. i18n:     :noindex:
.. i18n: .. 
..

.. module:: crm_timesheet
    :synopsis: CRM Timesheet 
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
.. i18n:     <div class="js-kit-rating" title="" permalink="" standalone="yes" path="/crm_timesheet"></div>
.. i18n:     <script src="http://js-kit.com/ratings.js"></script>
..

.. raw:: html

    <div class="js-kit-rating" title="" permalink="" standalone="yes" path="/crm_timesheet"></div>
    <script src="http://js-kit.com/ratings.js"></script>

.. i18n: CRM Timesheet (*crm_timesheet*)
.. i18n: ===============================
.. i18n: :Module: crm_timesheet
.. i18n: :Name: CRM Timesheet
.. i18n: :Version: 5.0.1.0.2
.. i18n: :Author: Syleam
.. i18n: :Directory: crm_timesheet
.. i18n: :Web: 
.. i18n: :Official module: no
.. i18n: :Quality certified: yes
..

CRM Timesheet (*crm_timesheet*)
===============================
:Module: crm_timesheet
:Name: CRM Timesheet
:Version: 5.0.1.0.2
:Author: Syleam
:Directory: crm_timesheet
:Web: 
:Official module: no
:Quality certified: yes

.. i18n: Description
.. i18n: -----------
..

Description
-----------

.. i18n: ::
.. i18n: 
.. i18n:   Add timesheet on CRM (the same method as task's project),
.. i18n:       On partner form, CRM Analytic tab, define analytic account by CRM Section
.. i18n:       Define the default analytic account on each section
.. i18n:       Fill your summary work on the crm case.
..

::

  Add timesheet on CRM (the same method as task's project),
      On partner form, CRM Analytic tab, define analytic account by CRM Section
      Define the default analytic account on each section
      Fill your summary work on the crm case.

.. i18n: Download links
.. i18n: --------------
..

Download links
--------------

.. i18n: You can download this module as a zip file in the following version:
..

You can download this module as a zip file in the following version:

.. i18n:   * `5.0 <http://www.openerp.com/download/modules/5.0/crm_timesheet.zip>`_
..

  * `5.0 <http://www.openerp.com/download/modules/5.0/crm_timesheet.zip>`_

.. i18n: Dependencies
.. i18n: ------------
..

Dependencies
------------

.. i18n:  * :mod:`base`
.. i18n:  * :mod:`crm`
.. i18n:  * :mod:`hr_timesheet`
..

 * :mod:`base`
 * :mod:`crm`
 * :mod:`hr_timesheet`

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

.. i18n: None
..

None

.. i18n: Views
.. i18n: -----
..

Views
-----

.. i18n:  * \* INHERIT crm.case.case.work.form (form)
.. i18n:  * \* INHERIT res.partner.crm.analytic.form (form)
.. i18n:  * \* INHERIT crm.case.section.analytic.form (form)
..

 * \* INHERIT crm.case.case.work.form (form)
 * \* INHERIT res.partner.crm.analytic.form (form)
 * \* INHERIT crm.case.section.analytic.form (form)

.. i18n: Objects
.. i18n: -------
..

Objects
-------

.. i18n: Object: CRM Partner Analytic Account (res.partner.crm.analytic)
.. i18n: ###############################################################
..

Object: CRM Partner Analytic Account (res.partner.crm.analytic)
###############################################################

.. i18n: :partner_id: Partner, many2one, required
..

:partner_id: Partner, many2one, required

.. i18n: :section_id: Section, many2one, required
..

:section_id: Section, many2one, required

.. i18n: :account_id: Analytic Account, many2one
..

:account_id: Analytic Account, many2one

.. i18n: Object: CRM summary work (crm.case.work)
.. i18n: ########################################
..

Object: CRM summary work (crm.case.work)
########################################

.. i18n: :user_id: Done by, many2one, required
..

:user_id: Done by, many2one, required

.. i18n: :name: Work summary, char
..

:name: Work summary, char

.. i18n: :hours: Time spent, float
..

:hours: Time spent, float

.. i18n: :case_id: Case, many2one, required
..

:case_id: Case, many2one, required

.. i18n: :date: Date, datetime
..

:date: Date, datetime

.. i18n: :hr_analytic_timesheet_id: Related Timeline Id, integer
..

:hr_analytic_timesheet_id: Related Timeline Id, integer
