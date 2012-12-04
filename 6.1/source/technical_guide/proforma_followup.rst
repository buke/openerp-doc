
.. module:: proforma_followup
    :synopsis: Pro-forma invoices and their payments Management 
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

    <div class="js-kit-rating" title="" permalink="" standalone="yes" path="/proforma_followup"></div>
    <script src="http://js-kit.com/ratings.js"></script>

Pro-forma invoices and their payments Management (*proforma_followup*)
======================================================================
:Module: proforma_followup
:Name: Pro-forma invoices and their payments Management
:Version: 5.0.1.0
:Author: Tiny
:Directory: proforma_followup
:Web: http://www.openerp.com
:Official module: no
:Quality certified: no

Description
-----------

::

  Once a pro-forma invoice is created, the module sends automatically mail 
          and call actions after X days.
          It's the same principle than account_followup but for proforma invoice only. 
          Only followups by email, no need to do reports. 
          Also, at each steps, we should be able to call several functions. 
          (for example, if a pro-forma is cancelled, it will close a delivery order)

Download links
--------------

You can download this module as a zip file in the following version:

  * `5.0 <http://www.openerp.com/download/modules/5.0/proforma_followup.zip>`_
  * `trunk <http://www.openerp.com/download/modules/trunk/proforma_followup.zip>`_


Dependencies
------------

 * :mod:`account`

Reports
-------

None


Menus
-------

 * Financial Management/Configuration/Proforma Followups

Views
-----

 * proforma.proforma.line.tree (tree)
 * proforma.proforma.line.form (form)
 * proforma.proforma.form (form)
 * account.proforma.tree (tree)


Objects
-------

Object: proforma.followup_step (proforma.followup_step)
#######################################################



:proforma_line: Proforma Follow-Up Line, one2many





:state: Status, selection





:description: Description, text





:name: Name, char, required





:company_id: Company, many2one




Object: PRO-Forma Followup Criteria (proforma.followup.line)
############################################################



:function: Function, char





:name: Name, char, required





:call_function: Call function?, boolean





:sequence: Sequence, integer





:args: Arguments, text





:days: Days of delay, integer





:email_body: E-mail Body, text





:send_email: Send E-mail?, boolean





:cancel_invoice: Cancel Invoice?, boolean





:model: Object, char





:followup_id: Proforma step, many2one, required





:subject: Subject, char


