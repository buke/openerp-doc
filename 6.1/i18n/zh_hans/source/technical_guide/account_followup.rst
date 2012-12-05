
.. i18n: .. module:: account_followup
.. i18n:     :synopsis: Accounting follow-ups management (Official, Quality Certified)
.. i18n:     :noindex:
.. i18n: .. 
..

.. module:: account_followup
    :synopsis: Accounting follow-ups management (Official, Quality Certified)
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
.. i18n:     <div class="js-kit-rating" title="" permalink="" standalone="yes" path="/account_followup"></div>
.. i18n:     <script src="http://js-kit.com/ratings.js"></script>
..

.. raw:: html

    <div class="js-kit-rating" title="" permalink="" standalone="yes" path="/account_followup"></div>
    <script src="http://js-kit.com/ratings.js"></script>

.. i18n: Accounting follow-ups management (*account_followup*)
.. i18n: =====================================================
.. i18n: :Module: account_followup
.. i18n: :Name: Accounting follow-ups management
.. i18n: :Version: 5.0.1.0
.. i18n: :Author: Tiny
.. i18n: :Directory: account_followup
.. i18n: :Web: http://www.openerp.com
.. i18n: :Official module: yes
.. i18n: :Quality certified: yes
..

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

.. i18n: Description
.. i18n: -----------
..

Description
-----------

.. i18n: ::
.. i18n: 
.. i18n:   Modules to automate letters for unpaid invoices, with multi-level recalls.
.. i18n:   
.. i18n:       You can define your multiple levels of recall through the menu:
.. i18n:           Financial Management/Configuration/Payment Terms/Follow-Ups
.. i18n:   
.. i18n:       Once it's defined, you can automatically prints recall every days
.. i18n:       through simply clicking on the menu:
.. i18n:           Financial_Management/Periodical_Processing/Print_Follow-Ups
.. i18n:   
.. i18n:       It will generate a PDF with all the letters according to the
.. i18n:       different levels of recall defined. You can define different policies
.. i18n:       for different companies.
.. i18n:   
.. i18n:   
.. i18n:       Note that if you want to change the followup level for a given partner/account entry, you can do it in the menu:
.. i18n:           Financial_Management/Reporting/Follow-Ups/All Receivable Entries
..

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

.. i18n: Download links
.. i18n: --------------
..

Download links
--------------

.. i18n: You can download this module as a zip file in the following version:
..

You can download this module as a zip file in the following version:

.. i18n:   * `4.2 <http://www.openerp.com/download/modules/4.2/account_followup.zip>`_
.. i18n:   * `5.0 <http://www.openerp.com/download/modules/5.0/account_followup.zip>`_
.. i18n:   * `trunk <http://www.openerp.com/download/modules/trunk/account_followup.zip>`_
..

  * `4.2 <http://www.openerp.com/download/modules/4.2/account_followup.zip>`_
  * `5.0 <http://www.openerp.com/download/modules/5.0/account_followup.zip>`_
  * `trunk <http://www.openerp.com/download/modules/trunk/account_followup.zip>`_

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

.. i18n:  * Followup Report
..

 * Followup Report

.. i18n: Menus
.. i18n: -------
..

Menus
-------

.. i18n:  * Financial Management/Periodical Processing/Send followups
.. i18n:  * Financial Management/Reporting/Follow-Ups
.. i18n:  * Financial Management/Configuration/Follow-Ups
.. i18n:  * Financial Management/Reporting/Follow-Ups/All receivable entries
.. i18n:  * Financial Management/Reporting/Follow-Ups/All payable entries
..

 * Financial Management/Periodical Processing/Send followups
 * Financial Management/Reporting/Follow-Ups
 * Financial Management/Configuration/Follow-Ups
 * Financial Management/Reporting/Follow-Ups/All receivable entries
 * Financial Management/Reporting/Follow-Ups/All payable entries

.. i18n: Views
.. i18n: -----
..

Views
-----

.. i18n:  * account_followup.stat.form (form)
.. i18n:  * account_followup.stat.tree (tree)
.. i18n:  * account_followup.followup.line.tree (tree)
.. i18n:  * account_followup.followup.line.form (form)
.. i18n:  * account_followup.followup.form (form)
.. i18n:  * account_followup.followup.tree (tree)
.. i18n:  * account.move.line.partner.tree (tree)
.. i18n:  * \* INHERIT account.move.line.form.followup (form)
.. i18n:  * \* INHERIT account.move.line.tree.followup (form)
.. i18n:  * \* INHERIT res.company.followup.form.inherit (form)
..

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

.. i18n: Objects
.. i18n: -------
..

Objects
-------

.. i18n: Object: Follow-Ups (account_followup.followup)
.. i18n: ##############################################
..

Object: Follow-Ups (account_followup.followup)
##############################################

.. i18n: :followup_line: Follow-Up, one2many
..

:followup_line: Follow-Up, one2many

.. i18n: :description: Description, text
..

:description: Description, text

.. i18n: :name: Name, char, required
..

:name: Name, char, required

.. i18n: :company_id: Company, many2one
..

:company_id: Company, many2one

.. i18n: Object: Follow-Ups Criteria (account_followup.followup.line)
.. i18n: ############################################################
..

Object: Follow-Ups Criteria (account_followup.followup.line)
############################################################

.. i18n: :description: Printed Message, text
..

:description: Printed Message, text

.. i18n: :sequence: Sequence, integer
..

:sequence: Sequence, integer

.. i18n: :delay: Days of delay, integer
..

:delay: Days of delay, integer

.. i18n: :start: Type of Term, selection, required
..

:start: Type of Term, selection, required

.. i18n: :followup_id: Follow Ups, many2one, required
..

:followup_id: Follow Ups, many2one, required

.. i18n: :name: Name, char, required
..

:name: Name, char, required

.. i18n: Object: Followup statistics (account_followup.stat)
.. i18n: ###################################################
..

Object: Followup statistics (account_followup.stat)
###################################################

.. i18n: :balance: Balance, float, readonly
..

:balance: Balance, float, readonly

.. i18n: :account_type: Account Type, selection, readonly
..

:account_type: Account Type, selection, readonly

.. i18n: :name: Partner, many2one, readonly
..

:name: Partner, many2one, readonly

.. i18n: :date_move: First move, date, readonly
..

:date_move: First move, date, readonly

.. i18n: :credit: Credit, float, readonly
..

:credit: Credit, float, readonly

.. i18n: :date_move_last: Last move, date, readonly
..

:date_move_last: Last move, date, readonly

.. i18n: :date_followup: Latest followup, date, readonly
..

:date_followup: Latest followup, date, readonly

.. i18n: :debit: Debit, float, readonly
..

:debit: Debit, float, readonly

.. i18n: :followup_id: Follow Ups, many2one, readonly
..

:followup_id: Follow Ups, many2one, readonly
