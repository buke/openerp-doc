
.. i18n: .. module:: account_coda_2_1_d
.. i18n:     :synopsis: Account CODA Version 2.1 D - Helps to import bank statements from .csv file. 
.. i18n:     :noindex:
.. i18n: .. 
..

.. module:: account_coda_2_1_d
    :synopsis: Account CODA Version 2.1 D - Helps to import bank statements from .csv file. 
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
.. i18n:     <div class="js-kit-rating" title="" permalink="" standalone="yes" path="/account_coda_2_1_d"></div>
.. i18n:     <script src="http://js-kit.com/ratings.js"></script>
..

.. raw:: html

    <div class="js-kit-rating" title="" permalink="" standalone="yes" path="/account_coda_2_1_d"></div>
    <script src="http://js-kit.com/ratings.js"></script>

.. i18n: Account CODA Version 2.1 D - Helps to import bank statements from .csv file. (*account_coda_2_1_d*)
.. i18n: ===================================================================================================
.. i18n: :Module: account_coda_2_1_d
.. i18n: :Name: Account CODA Version 2.1 D - Helps to import bank statements from .csv file.
.. i18n: :Version: 5.0.1.0.1
.. i18n: :Author: OpenERP
.. i18n: :Directory: account_coda_2_1_d
.. i18n: :Web: 
.. i18n: :Official module: no
.. i18n: :Quality certified: no
..

Account CODA Version 2.1 D - Helps to import bank statements from .csv file. (*account_coda_2_1_d*)
===================================================================================================
:Module: account_coda_2_1_d
:Name: Account CODA Version 2.1 D - Helps to import bank statements from .csv file.
:Version: 5.0.1.0.1
:Author: OpenERP
:Directory: account_coda_2_1_d
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
.. i18n:   Module provides functionality to import
.. i18n:       bank statements from .csv file.
.. i18n:       Import coda file wizard is used to import bank statements.
..

::

  Module provides functionality to import
      bank statements from .csv file.
      Import coda file wizard is used to import bank statements.

.. i18n: Download links
.. i18n: --------------
..

Download links
--------------

.. i18n: You can download this module as a zip file in the following version:
..

You can download this module as a zip file in the following version:

.. i18n:   * `5.0 <http://www.openerp.com/download/modules/5.0/account_coda_2_1_d.zip>`_
.. i18n:   * `trunk <http://www.openerp.com/download/modules/trunk/account_coda_2_1_d.zip>`_
..

  * `5.0 <http://www.openerp.com/download/modules/5.0/account_coda_2_1_d.zip>`_
  * `trunk <http://www.openerp.com/download/modules/trunk/account_coda_2_1_d.zip>`_

.. i18n: Dependencies
.. i18n: ------------
..

Dependencies
------------

.. i18n:  * :mod:`base`
.. i18n:  * :mod:`account`
.. i18n:  * :mod:`account_report`
.. i18n:  * :mod:`base_iban`
..

 * :mod:`base`
 * :mod:`account`
 * :mod:`account_report`
 * :mod:`base_iban`

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

.. i18n:  * Financial Management/Reporting/Coda Statements
.. i18n:  * Financial Management/Periodical Processing/Import Coda Statements
..

 * Financial Management/Reporting/Coda Statements
 * Financial Management/Periodical Processing/Import Coda Statements

.. i18n: Views
.. i18n: -----
..

Views
-----

.. i18n:  * account.coda.form (form)
.. i18n:  * account.coda.tree (tree)
..

 * account.coda.form (form)
 * account.coda.tree (tree)

.. i18n: Objects
.. i18n: -------
..

Objects
-------

.. i18n: Object: CODA Format For Account (account.coda)
.. i18n: ##############################################
..

Object: CODA Format For Account (account.coda)
##############################################

.. i18n: :user_id: User, many2one, readonly
..

:user_id: User, many2one, readonly

.. i18n: :name: Coda File, binary, readonly
..

:name: Coda File, binary, readonly

.. i18n: :journal_id: Bank Journal, many2one, readonly
..

:journal_id: Bank Journal, many2one, readonly

.. i18n: :note: Import Log, text, readonly
..

:note: Import Log, text, readonly

.. i18n: :date: Import Date, date, readonly
..

:date: Import Date, date, readonly

.. i18n: :statement_id: Generated Bank Statement, many2one, readonly
..

:statement_id: Generated Bank Statement, many2one, readonly
