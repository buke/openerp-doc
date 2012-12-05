
.. i18n: .. module:: purchase_journal
.. i18n:     :synopsis: Managing sales and deliveries by journal 
.. i18n:     :noindex:
.. i18n: .. 
..

.. module:: purchase_journal
    :synopsis: Managing sales and deliveries by journal 
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
.. i18n:     <div class="js-kit-rating" title="" permalink="" standalone="yes" path="/purchase_journal"></div>
.. i18n:     <script src="http://js-kit.com/ratings.js"></script>
..

.. raw:: html

    <div class="js-kit-rating" title="" permalink="" standalone="yes" path="/purchase_journal"></div>
    <script src="http://js-kit.com/ratings.js"></script>

.. i18n: Managing sales and deliveries by journal (*purchase_journal*)
.. i18n: =============================================================
.. i18n: :Module: purchase_journal
.. i18n: :Name: Managing sales and deliveries by journal
.. i18n: :Version: 5.0.1.0
.. i18n: :Author: Tiny
.. i18n: :Directory: purchase_journal
.. i18n: :Web: http://www.openerp.com
.. i18n: :Official module: no
.. i18n: :Quality certified: no
..

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

.. i18n: Description
.. i18n: -----------
..

Description
-----------

.. i18n: ::
.. i18n: 
.. i18n:   None
..

::

  None

.. i18n: Download links
.. i18n: --------------
..

Download links
--------------

.. i18n: You can download this module as a zip file in the following version:
..

You can download this module as a zip file in the following version:

.. i18n:   * `5.0 <http://www.openerp.com/download/modules/5.0/purchase_journal.zip>`_
.. i18n:   * `trunk <http://www.openerp.com/download/modules/trunk/purchase_journal.zip>`_
..

  * `5.0 <http://www.openerp.com/download/modules/5.0/purchase_journal.zip>`_
  * `trunk <http://www.openerp.com/download/modules/trunk/purchase_journal.zip>`_

.. i18n: Dependencies
.. i18n: ------------
..

Dependencies
------------

.. i18n:  * :mod:`stock`
.. i18n:  * :mod:`purchase`
..

 * :mod:`stock`
 * :mod:`purchase`

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

.. i18n:  * Purchase Management/Configuration
.. i18n:  * Purchase Management/Configuration/Purchases Journals
.. i18n:  * Purchase Management/Purchases by Journal
.. i18n:  * Purchase Management/Purchases by Journal/My Open Journals
.. i18n:  * Purchase Management/Purchases by Journal/All Open Journals
.. i18n:  * Purchase Management/Reporting
.. i18n:  * Purchase Management/Reporting/This Month
.. i18n:  * Purchase Management/Reporting/This Month/Purchases by Journal
.. i18n:  * Purchase Management/Reporting/All Months
.. i18n:  * Purchase Management/Reporting/All Months/Purchases by Journal
..

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

.. i18n: Views
.. i18n: -----
..

Views
-----

.. i18n:  * \* INHERIT stock.picking.journal.view.form (form)
.. i18n:  * \* INHERIT stock.picking.purchase.journal.view.tree (tree)
.. i18n:  * purchase_journal.purchase.journal.form (form)
.. i18n:  * purchase_journal.purchase.journal.tree (tree)
.. i18n:  * \* INHERIT purchase.order.journal.view.form (form)
.. i18n:  * \* INHERIT purchase.order.journal.view.tree (tree)
.. i18n:  * purchase_journal.purchase.stats.tree (tree)
.. i18n:  * purchase_journal.purchase.stats.form (form)
..

 * \* INHERIT stock.picking.journal.view.form (form)
 * \* INHERIT stock.picking.purchase.journal.view.tree (tree)
 * purchase_journal.purchase.journal.form (form)
 * purchase_journal.purchase.journal.tree (tree)
 * \* INHERIT purchase.order.journal.view.form (form)
 * \* INHERIT purchase.order.journal.view.tree (tree)
 * purchase_journal.purchase.stats.tree (tree)
 * purchase_journal.purchase.stats.form (form)

.. i18n: Objects
.. i18n: -------
..

Objects
-------

.. i18n: Object: purchase Journal (purchase_journal.purchase.journal)
.. i18n: ############################################################
..

Object: purchase Journal (purchase_journal.purchase.journal)
############################################################

.. i18n: :code: Code, char, required
..

:code: Code, char, required

.. i18n: :user_id: Responsible, many2one, required
..

:user_id: Responsible, many2one, required

.. i18n: :name: Journal, char, required
..

:name: Journal, char, required

.. i18n: :note: Note, text
..

:note: Note, text

.. i18n: :state: Creation date, selection, required
..

:state: Creation date, selection, required

.. i18n: :purchase_stats_ids: purchase Stats, one2many, readonly
..

:purchase_stats_ids: purchase Stats, one2many, readonly

.. i18n: :date: Journal date, date, required
..

:date: Journal date, date, required

.. i18n: :date_created: Creation date, date, required, readonly
..

:date_created: Creation date, date, required, readonly

.. i18n: :date_validation: Validation date, date, readonly
..

:date_validation: Validation date, date, readonly

.. i18n: Object: Purchases Orders by Journal (purchase_journal.purchase.stats)
.. i18n: #####################################################################
..

Object: Purchases Orders by Journal (purchase_journal.purchase.stats)
#####################################################################

.. i18n: :count: # of Lines, integer, readonly
..

:count: # of Lines, integer, readonly

.. i18n: :price_total: Total Price, float, readonly
..

:price_total: Total Price, float, readonly

.. i18n: :name: Month, date, readonly
..

:name: Month, date, readonly

.. i18n: :state: Order State, selection, readonly
..

:state: Order State, selection, readonly

.. i18n: :journal_id: Journal, many2one, readonly
..

:journal_id: Journal, many2one, readonly

.. i18n: :price_average: Average Price, float, readonly
..

:price_average: Average Price, float, readonly

.. i18n: :quantity: Quantities, float, readonly
..

:quantity: Quantities, float, readonly
