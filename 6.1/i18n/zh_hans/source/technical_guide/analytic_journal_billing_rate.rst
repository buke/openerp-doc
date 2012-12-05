
.. i18n: .. module:: analytic_journal_billing_rate
.. i18n:     :synopsis: Analytic Journal Billing Rate (Official, Quality Certified)
.. i18n:     :noindex:
.. i18n: .. 
..

.. module:: analytic_journal_billing_rate
    :synopsis: Analytic Journal Billing Rate (Official, Quality Certified)
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
.. i18n:     <div class="js-kit-rating" title="" permalink="" standalone="yes" path="/analytic_journal_billing_rate"></div>
.. i18n:     <script src="http://js-kit.com/ratings.js"></script>
..

.. raw:: html

    <div class="js-kit-rating" title="" permalink="" standalone="yes" path="/analytic_journal_billing_rate"></div>
    <script src="http://js-kit.com/ratings.js"></script>

.. i18n: Analytic Journal Billing Rate (*analytic_journal_billing_rate*)
.. i18n: ===============================================================
.. i18n: :Module: analytic_journal_billing_rate
.. i18n: :Name: Analytic Journal Billing Rate
.. i18n: :Version: 5.0.1.0
.. i18n: :Author: Tiny
.. i18n: :Directory: analytic_journal_billing_rate
.. i18n: :Web: http://www.openerp.com
.. i18n: :Official module: yes
.. i18n: :Quality certified: yes
..

Analytic Journal Billing Rate (*analytic_journal_billing_rate*)
===============================================================
:Module: analytic_journal_billing_rate
:Name: Analytic Journal Billing Rate
:Version: 5.0.1.0
:Author: Tiny
:Directory: analytic_journal_billing_rate
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
.. i18n:   This module allows you to define what is the default invoicing rate for a specific journal on a given account. This is mostly used when a user encode his timesheet: the values are retrieved and the fields are auto-filled... but the possibility to change these values is still available.
.. i18n:   
.. i18n:       Obviously if no data has been recorded for the current account, the default value is given as usual by the account data so that this module is perfectly compatible with older configurations.
..

::

  This module allows you to define what is the default invoicing rate for a specific journal on a given account. This is mostly used when a user encode his timesheet: the values are retrieved and the fields are auto-filled... but the possibility to change these values is still available.
  
      Obviously if no data has been recorded for the current account, the default value is given as usual by the account data so that this module is perfectly compatible with older configurations.

.. i18n: Download links
.. i18n: --------------
..

Download links
--------------

.. i18n: You can download this module as a zip file in the following version:
..

You can download this module as a zip file in the following version:

.. i18n:   * `5.0 <http://www.openerp.com/download/modules/5.0/analytic_journal_billing_rate.zip>`_
.. i18n:   * `trunk <http://www.openerp.com/download/modules/trunk/analytic_journal_billing_rate.zip>`_
..

  * `5.0 <http://www.openerp.com/download/modules/5.0/analytic_journal_billing_rate.zip>`_
  * `trunk <http://www.openerp.com/download/modules/trunk/analytic_journal_billing_rate.zip>`_

.. i18n: Dependencies
.. i18n: ------------
..

Dependencies
------------

.. i18n:  * :mod:`analytic_user_function`
.. i18n:  * :mod:`account`
.. i18n:  * :mod:`hr_timesheet_invoice`
..

 * :mod:`analytic_user_function`
 * :mod:`account`
 * :mod:`hr_timesheet_invoice`

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

.. i18n:  * analytic_journal_rate_grid.tree (tree)
.. i18n:  * analytic_journal_rate_grid.form (form)
.. i18n:  * \* INHERIT account.analytic.account.form (form)
.. i18n:  * \* INHERIT hr.timesheet.sheet.form (form)
.. i18n:  * \* INHERIT hr.analytic.timesheet.form (form)
.. i18n:  * \* INHERIT hr.analytic.timesheet.form (form)
..

 * analytic_journal_rate_grid.tree (tree)
 * analytic_journal_rate_grid.form (form)
 * \* INHERIT account.analytic.account.form (form)
 * \* INHERIT hr.timesheet.sheet.form (form)
 * \* INHERIT hr.analytic.timesheet.form (form)
 * \* INHERIT hr.analytic.timesheet.form (form)

.. i18n: Objects
.. i18n: -------
..

Objects
-------

.. i18n: Object: Relation table between journals and billing rates (analytic_journal_rate_grid)
.. i18n: ######################################################################################
..

Object: Relation table between journals and billing rates (analytic_journal_rate_grid)
######################################################################################

.. i18n: :rate_id: Invoicing Rate, many2one
..

:rate_id: Invoicing Rate, many2one

.. i18n: :journal_id: Analytic Journal, many2one, required
..

:journal_id: Analytic Journal, many2one, required

.. i18n: :account_id: Analytic Account, many2one, required
..

:account_id: Analytic Account, many2one, required
