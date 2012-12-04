
.. module:: md_hr_contract
    :synopsis: Pilot Human Resource Management 
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

    <div class="js-kit-rating" title="" permalink="" standalone="yes" path="/md_hr_contract"></div>
    <script src="http://js-kit.com/ratings.js"></script>

Pilot Human Resource Management (*md_hr_contract*)
==================================================
:Module: md_hr_contract
:Name: Pilot Human Resource Management
:Version: 5.0.1.0
:Author: Tiny
:Directory: md_hr_contract
:Web: 
:Official module: no
:Quality certified: no

Description
-----------

::

  Contract Module for human resource management. You can manage:
      * Contract of the employee
      * Availability of the employee
      and many more.................

Download links
--------------

You can download this module as a zip file in the following version:

  * `5.0 <http://www.openerp.com/download/modules/5.0/md_hr_contract.zip>`_
  * `trunk <http://www.openerp.com/download/modules/trunk/md_hr_contract.zip>`_


Dependencies
------------

 * :mod:`base`
 * :mod:`hr`
 * :mod:`hr_contract`

Reports
-------

None


Menus
-------


None


Views
-----

 * \* INHERIT md.hr.contract.form1 (form)
 * \* INHERIT md.hr.contract.form2 (form)
 * \* INHERIT md.hr.contract.form3 (form)
 * \* INHERIT md.hr.contract.form4 (form)
 * \* INHERIT md.hr.contract.form5 (form)
 * \* INHERIT md.hr.employee.form1 (form)
 * md.hr.contract.availability.form (form)
 * md.hr.contract.availability.tree (tree)
 * \* INHERIT hr.department.form (form)


Objects
-------

Object: HR Contract Availability (md.hr.contract.availability)
##############################################################



:to_hour: To, time





:from_hour: From, time





:contract_id: Contract, many2one





:day: Day, selection


