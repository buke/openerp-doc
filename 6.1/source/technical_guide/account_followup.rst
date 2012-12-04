
.. module:: account_followup
    :synopsis: Accounting follow-ups management (Official, Quality Certified)
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

    <div class="js-kit-rating" title="" permalink="" standalone="yes" path="/account_followup"></div>
    <script src="http://js-kit.com/ratings.js"></script>

Accounting follow-ups management (*account_followup*)
=====================================================
:Module: account_followup
:Name: Accounting follow-ups management
:Version: 5.0.1.0
:Author: Tiny
:Directory: account_followup
:Web: http://www.openerp.com
:Official module: yes
:Quality certified: yes

Description
-----------

::

  Modules to automate letters for unpaid invoices, with multi-level recalls.
  
      You can define your multiple levels of recall through the menu:
          Financial Management/Configuration/Payment Terms/Follow-Ups
  
      Once it's defined, you can automatically prints recall every days
      through simply clicking on the menu:
          Financial_Management/Periodical_Processing/Print_Follow-Ups
  
      It will generate a PDF with all the letters according to the
      different levels of recall defined. You can define different policies
      for different companies.
  
  
      Note that if you want to change the followup level for a given partner/account entry, you can do it in the menu:
          Financial_Management/Reporting/Follow-Ups/All Receivable Entries

Download links
--------------

You can download this module as a zip file in the following version:

  * `4.2 <http://www.openerp.com/download/modules/4.2/account_followup.zip>`_
  * `5.0 <http://www.openerp.com/download/modules/5.0/account_followup.zip>`_
  * `trunk <http://www.openerp.com/download/modules/trunk/account_followup.zip>`_


Dependencies
------------

 * :mod:`account`

Reports
-------

 * Followup Report

Menus
-------

 * Financial Management/Periodical Processing/Send followups
 * Financial Management/Reporting/Follow-Ups
 * Financial Management/Configuration/Follow-Ups
 * Financial Management/Reporting/Follow-Ups/All receivable entries
 * Financial Management/Reporting/Follow-Ups/All payable entries

Views
-----

 * account_followup.stat.form (form)
 * account_followup.stat.tree (tree)
 * account_followup.followup.line.tree (tree)
 * account_followup.followup.line.form (form)
 * account_followup.followup.form (form)
 * account_followup.followup.tree (tree)
 * account.move.line.partner.tree (tree)
 * \* INHERIT account.move.line.form.followup (form)
 * \* INHERIT account.move.line.tree.followup (form)
 * \* INHERIT res.company.followup.form.inherit (form)


Objects
-------

Object: Follow-Ups (account_followup.followup)
##############################################



:followup_line: Follow-Up, one2many





:description: Description, text





:name: Name, char, required





:company_id: Company, many2one




Object: Follow-Ups Criteria (account_followup.followup.line)
############################################################



:description: Printed Message, text





:sequence: Sequence, integer





:delay: Days of delay, integer





:start: Type of Term, selection, required





:followup_id: Follow Ups, many2one, required





:name: Name, char, required




Object: Followup statistics (account_followup.stat)
###################################################



:balance: Balance, float, readonly





:account_type: Account Type, selection, readonly





:name: Partner, many2one, readonly





:date_move: First move, date, readonly





:credit: Credit, float, readonly





:date_move_last: Last move, date, readonly





:date_followup: Latest followup, date, readonly





:debit: Debit, float, readonly





:followup_id: Follow Ups, many2one, readonly


