
.. i18n: .. module:: account_regularization
.. i18n:     :synopsis: Account Regularizations 
.. i18n:     :noindex:
.. i18n: .. 
..

.. module:: account_regularization
    :synopsis: Account Regularizations 
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
.. i18n:     <div class="js-kit-rating" title="" permalink="" standalone="yes" path="/account_regularization"></div>
.. i18n:     <script src="http://js-kit.com/ratings.js"></script>
..

.. raw:: html

    <div class="js-kit-rating" title="" permalink="" standalone="yes" path="/account_regularization"></div>
    <script src="http://js-kit.com/ratings.js"></script>

.. i18n: Account Regularizations (*account_regularization*)
.. i18n: ==================================================
.. i18n: :Module: account_regularization
.. i18n: :Name: Account Regularizations
.. i18n: :Version: 5.0.1.0
.. i18n: :Author: ACYSOS S.L.
.. i18n: :Directory: account_regularization
.. i18n: :Web: 
.. i18n: :Official module: no
.. i18n: :Quality certified: no
..

Account Regularizations (*account_regularization*)
==================================================
:Module: account_regularization
:Name: Account Regularizations
:Version: 5.0.1.0
:Author: ACYSOS S.L.
:Directory: account_regularization
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
.. i18n:   This module creates a new object in accounting, 
.. i18n:   	very similar to the account models named account.regularization. 
.. i18n:   	Within this object you can define regularization moves, 
.. i18n:   	This is, accounting moves that will automatically calculate the balance of a set of accounts, 
.. i18n:   	Set it to 0 and transfer the difference to a new account. This is used, for example with tax declarations or in some countries to create the 'Profit and Loss' regularization
..

::

  This module creates a new object in accounting, 
  	very similar to the account models named account.regularization. 
  	Within this object you can define regularization moves, 
  	This is, accounting moves that will automatically calculate the balance of a set of accounts, 
  	Set it to 0 and transfer the difference to a new account. This is used, for example with tax declarations or in some countries to create the 'Profit and Loss' regularization

.. i18n: Download links
.. i18n: --------------
..

Download links
--------------

.. i18n: You can download this module as a zip file in the following version:
..

You can download this module as a zip file in the following version:

.. i18n:   * `4.2 <http://www.openerp.com/download/modules/4.2/account_regularization.zip>`_
.. i18n:   * `5.0 <http://www.openerp.com/download/modules/5.0/account_regularization.zip>`_
.. i18n:   * `trunk <http://www.openerp.com/download/modules/trunk/account_regularization.zip>`_
..

  * `4.2 <http://www.openerp.com/download/modules/4.2/account_regularization.zip>`_
  * `5.0 <http://www.openerp.com/download/modules/5.0/account_regularization.zip>`_
  * `trunk <http://www.openerp.com/download/modules/trunk/account_regularization.zip>`_

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

.. i18n: None
..

None

.. i18n: Menus
.. i18n: -------
..

Menus
-------

.. i18n:  * Financial Management/Periodical Processing/Regularizations
..

 * Financial Management/Periodical Processing/Regularizations

.. i18n: Views
.. i18n: -----
..

Views
-----

.. i18n:  * account.regularization.form (form)
..

 * account.regularization.form (form)

.. i18n: Objects
.. i18n: -------
..

Objects
-------

.. i18n: Object: Account Regularization Model (account.regularization)
.. i18n: #############################################################
..

Object: Account Regularization Model (account.regularization)
#############################################################

.. i18n: :balance_calc: Regularization time calculation, selection, required
..

:balance_calc: Regularization time calculation, selection, required

.. i18n: :name: Name, char, required
..

:name: Name, char, required

.. i18n: :credit_account_id: Result account, credit, many2one, required
..

:credit_account_id: Result account, credit, many2one, required

.. i18n: :move_ids: Regularization Moves, one2many
..

:move_ids: Regularization Moves, one2many

.. i18n: :account_ids: Accounts to balance, many2many, required
..

:account_ids: Accounts to balance, many2many, required

.. i18n: :debit_account_id: Result account, debit, many2one, required
..

:debit_account_id: Result account, debit, many2one, required
