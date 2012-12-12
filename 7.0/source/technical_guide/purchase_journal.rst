
.. module:: purchase_journal
    :synopsis: Managing sales and deliveries by journal 
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

    <div class="js-kit-rating" title="" permalink="" standalone="yes" path="/purchase_journal"></div>
    <script src="http://js-kit.com/ratings.js"></script>

Managing sales and deliveries by journal (*purchase_journal*)
=============================================================
:Module: purchase_journal
:Name: Managing sales and deliveries by journal
:Version: 5.0.1.0
:Author: Tiny
:Directory: purchase_journal
:Web: http://www.openerp.com
:Official module: no
:Quality certified: no

Description
-----------

::

  None

Download links
--------------

You can download this module as a zip file in the following version:

  * `5.0 <http://www.openerp.com/download/modules/5.0/purchase_journal.zip>`_
  * `trunk <http://www.openerp.com/download/modules/trunk/purchase_journal.zip>`_


Dependencies
------------

 * :mod:`stock`
 * :mod:`purchase`

Reports
-------

None


Menus
-------

 * Purchase Management/Configuration
 * Purchase Management/Configuration/Purchases Journals
 * Purchase Management/Purchases by Journal
 * Purchase Management/Purchases by Journal/My Open Journals
 * Purchase Management/Purchases by Journal/All Open Journals
 * Purchase Management/Reporting
 * Purchase Management/Reporting/This Month
 * Purchase Management/Reporting/This Month/Purchases by Journal
 * Purchase Management/Reporting/All Months
 * Purchase Management/Reporting/All Months/Purchases by Journal

Views
-----

 * \* INHERIT stock.picking.journal.view.form (form)
 * \* INHERIT stock.picking.purchase.journal.view.tree (tree)
 * purchase_journal.purchase.journal.form (form)
 * purchase_journal.purchase.journal.tree (tree)
 * \* INHERIT purchase.order.journal.view.form (form)
 * \* INHERIT purchase.order.journal.view.tree (tree)
 * purchase_journal.purchase.stats.tree (tree)
 * purchase_journal.purchase.stats.form (form)


Objects
-------

Object: purchase Journal (purchase_journal.purchase.journal)
############################################################



:code: Code, char, required





:user_id: Responsible, many2one, required





:name: Journal, char, required





:note: Note, text





:state: Creation date, selection, required





:purchase_stats_ids: purchase Stats, one2many, readonly





:date: Journal date, date, required





:date_created: Creation date, date, required, readonly





:date_validation: Validation date, date, readonly




Object: Purchases Orders by Journal (purchase_journal.purchase.stats)
#####################################################################



:count: # of Lines, integer, readonly





:price_total: Total Price, float, readonly





:name: Month, date, readonly





:state: Order State, selection, readonly





:journal_id: Journal, many2one, readonly





:price_average: Average Price, float, readonly





:quantity: Quantities, float, readonly


