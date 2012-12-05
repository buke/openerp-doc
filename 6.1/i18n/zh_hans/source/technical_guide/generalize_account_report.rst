
.. i18n: .. module:: generalize_account_report
.. i18n:     :synopsis: generalize account report module 
.. i18n:     :noindex:
.. i18n: .. 
..

.. module:: generalize_account_report
    :synopsis: generalize account report module 
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
.. i18n:     <div class="js-kit-rating" title="" permalink="" standalone="yes" path="/generalize_account_report"></div>
.. i18n:     <script src="http://js-kit.com/ratings.js"></script>
..

.. raw:: html

    <div class="js-kit-rating" title="" permalink="" standalone="yes" path="/generalize_account_report"></div>
    <script src="http://js-kit.com/ratings.js"></script>

.. i18n: generalize account report module (*generalize_account_report*)
.. i18n: ==============================================================
.. i18n: :Module: generalize_account_report
.. i18n: :Name: generalize account report module
.. i18n: :Version: 5.0.0.1
.. i18n: :Author: Tiny/Axelor
.. i18n: :Directory: generalize_account_report
.. i18n: :Web: 
.. i18n: :Official module: no
.. i18n: :Quality certified: no
..

generalize account report module (*generalize_account_report*)
==============================================================
:Module: generalize_account_report
:Name: generalize account report module
:Version: 5.0.0.1
:Author: Tiny/Axelor
:Directory: generalize_account_report
:Web: 
:Official module: no
:Quality certified: no

.. i18n: Description
.. i18n: -----------
..

Description
-----------

.. i18n: ::
.. i18n: 
.. i18n:   Module to handle account in generalize manner and print the report.
..

::

  Module to handle account in generalize manner and print the report.

.. i18n: Download links
.. i18n: --------------
..

Download links
--------------

.. i18n: You can download this module as a zip file in the following version:
..

You can download this module as a zip file in the following version:

.. i18n: (No download links available)
..

(No download links available)

.. i18n: Dependencies
.. i18n: ------------
..

Dependencies
------------

.. i18n:  * :mod:`base`
.. i18n:  * :mod:`account_voucher`
..

 * :mod:`base`
 * :mod:`account_voucher`

.. i18n: Reports
.. i18n: -------
..

Reports
-------

.. i18n:  * Final Horizontal Report
.. i18n: 
.. i18n:  * Final Vertical Report
..

 * Final Horizontal Report

 * Final Vertical Report

.. i18n: Menus
.. i18n: -------
..

Menus
-------

.. i18n:  * Financial Management/Legal Statements/Generalize Account Report
.. i18n:  * Financial Management/Legal Statements/Generalize Account Report/Generalize Account Report
..

 * Financial Management/Legal Statements/Generalize Account Report
 * Financial Management/Legal Statements/Generalize Account Report/Generalize Account Report

.. i18n: Views
.. i18n: -----
..

Views
-----

.. i18n:  * generalize_account_report.tree (tree)
.. i18n:  * generalize_account_report.form (form)
.. i18n:  * group.detail.configuration.tree (tree)
.. i18n:  * group.detail.configuration.form (form)
..

 * generalize_account_report.tree (tree)
 * generalize_account_report.form (form)
 * group.detail.configuration.tree (tree)
 * group.detail.configuration.form (form)

.. i18n: Objects
.. i18n: -------
..

Objects
-------

.. i18n: Object: Generalize Account Report (generalize.account.report)
.. i18n: #############################################################
..

Object: Generalize Account Report (generalize.account.report)
#############################################################

.. i18n: :name: Name, char, required
..

:name: Name, char, required

.. i18n: :end_date: End Date, date
..

:end_date: End Date, date

.. i18n: :gr_detail: Documents, one2many
..

:gr_detail: Documents, one2many

.. i18n: :Loss_tran_acc: Loss Transfer Account, many2one
..

:Loss_tran_acc: Loss Transfer Account, many2one

.. i18n: :company_id: Company, many2one, required
..

:company_id: Company, many2one, required

.. i18n: :fiscal_year: Fiscal Year, many2one, required
..

:fiscal_year: Fiscal Year, many2one, required

.. i18n: :st_date: Start Date, date
..

:st_date: Start Date, date

.. i18n: :profit_tran_acc: Profit Transfer Account, many2one
..

:profit_tran_acc: Profit Transfer Account, many2one

.. i18n: :type: Report type, selection, required
..

:type: Report type, selection, required

.. i18n: :final_type: Final Account Type, selection, required
..

:final_type: Final Account Type, selection, required

.. i18n: Object: Group Configuration (group.detail.configuration)
.. i18n: ########################################################
..

Object: Group Configuration (group.detail.configuration)
########################################################

.. i18n: :acc_gr_name: Account, many2one, required
..

:acc_gr_name: Account, many2one, required

.. i18n: :pos_name: Position Name, selection, required
..

:pos_name: Position Name, selection, required

.. i18n: :name: Name, char, required
..

:name: Name, char, required

.. i18n: :gdc_id: Geralize Account, many2one
..

:gdc_id: Geralize Account, many2one

.. i18n: :sequence: Sequence, integer, required
..

:sequence: Sequence, integer, required
