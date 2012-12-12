
.. module:: crm_timesheet
    :synopsis: CRM Timesheet 
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

    <div class="js-kit-rating" title="" permalink="" standalone="yes" path="/crm_timesheet"></div>
    <script src="http://js-kit.com/ratings.js"></script>

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

Description
-----------

::

  Add timesheet on CRM (the same method as task's project),
      On partner form, CRM Analytic tab, define analytic account by CRM Section
      Define the default analytic account on each section
      Fill your summary work on the crm case.

Download links
--------------

You can download this module as a zip file in the following version:

  * `5.0 <http://www.openerp.com/download/modules/5.0/crm_timesheet.zip>`_


Dependencies
------------

 * :mod:`base`
 * :mod:`crm`
 * :mod:`hr_timesheet`

Reports
-------

None


Menus
-------


None


Views
-----

 * \* INHERIT crm.case.case.work.form (form)
 * \* INHERIT res.partner.crm.analytic.form (form)
 * \* INHERIT crm.case.section.analytic.form (form)


Objects
-------

Object: CRM Partner Analytic Account (res.partner.crm.analytic)
###############################################################



:partner_id: Partner, many2one, required





:section_id: Section, many2one, required





:account_id: Analytic Account, many2one




Object: CRM summary work (crm.case.work)
########################################



:user_id: Done by, many2one, required





:name: Work summary, char





:hours: Time spent, float





:case_id: Case, many2one, required





:date: Date, datetime





:hr_analytic_timesheet_id: Related Timeline Id, integer


