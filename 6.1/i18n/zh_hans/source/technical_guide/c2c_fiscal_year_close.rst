
.. i18n: .. module:: c2c_fiscal_year_close
.. i18n:     :synopsis: c2c close fiscal year 
.. i18n:     :noindex:
.. i18n: .. 
..

.. module:: c2c_fiscal_year_close
    :synopsis: c2c close fiscal year 
    :noindex:
.. 

.. i18n: .. raw:: html
.. i18n: 
.. i18n:     <link rel="stylesheet" href="../_static/hide_objects_in_sidebar.css" type="text/css" />
..

.. raw:: html

    <link rel="stylesheet" href="../_static/hide_objects_in_sidebar.css" type="text/css" />

.. i18n: c2c close fiscal year (*c2c_fiscal_year_close*)
.. i18n: ===============================================
.. i18n: :Module: c2c_fiscal_year_close
.. i18n: :Name: c2c close fiscal year
.. i18n: :Version: 0.6
.. i18n: :Author: Camptocamp SA
.. i18n: :Directory: c2c_fiscal_year_close
.. i18n: :Web: 
.. i18n: :Official module: no
.. i18n: :Quality certified: no
..

c2c close fiscal year (*c2c_fiscal_year_close*)
===============================================
:Module: c2c_fiscal_year_close
:Name: c2c close fiscal year
:Version: 0.6
:Author: Camptocamp SA
:Directory: c2c_fiscal_year_close
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
.. i18n:   	This module addresses the wizard "close fiscal year" of the 4.2 version
.. i18n:   	of OpenERP => it allows:
.. i18n:   
.. i18n:   	- Closing at any time
.. i18n:   	- Correctly report non-reconciled entries (positions open)
.. i18n:   	- Automatic transfer actual year result to the balance sheet
.. i18n:   	- Automatic closing of periods fiscal year
.. i18n:   	- News data checking
.. i18n:   	- Checking of the "closing type" of the accounts (compared to the
.. i18n:   	"closing type" of the "type of account")
.. i18n:   
.. i18n:   	The module work is :
.. i18n:   
.. i18n:   	1. tests (opening and closing journal, dates, previous fiscal years
.. i18n:   	status, etc. ..)
.. i18n:   	2. transfer the actual year result to the balance sheet
.. i18n:   	3. transfer the account balance of "balance" type to the new fiscal year
.. i18n:   	4. transfer of 31.12 non reconciles entries to the new fiscal year
.. i18n:   	(based on the dates of reconciled entries)
.. i18n:   	5. Reconciliation of the "new entries" entry to remove the conflict with
.. i18n:   	the initial invoice entry
.. i18n:   	6. closing periods and fiscal year
.. i18n:   
.. i18n:   	The module does not:
.. i18n:   	- Be able to re-open closed fiscal year (but we're available if you want
.. i18n:   	us to develop it :-) )
.. i18n:   	- Separate the step of transferring account balance and the step of
.. i18n:   	closing (=> we can develop that feature if necessary)
.. i18n:   
.. i18n:   	Here are the steps to allow the closing of fiscal year :
.. i18n:   
.. i18n:   	=> The following screencast will explain in detail how to do: http://www.screencast.com/t/lXLRJoQca
.. i18n:   
.. i18n:   	0. !!!!!!!!!!! MAKE A BACKUP OF THE DATABASE !!!!!!!!!!!
.. i18n:   	1. verify that the "types of closing" specified on the "type of
.. i18n:   	accounts" are correct
.. i18n:   	2. launch the "Finance -> Charts -> Charts of Account -> trouble accounts" list which give you the list of all the
.. i18n:   	accounts which the type of closing is different than that specified the
.. i18n:   	type of account
.. i18n:   	3. start the wizard closing "Finance -> End of Year Treatments -> close a fiscal year" specifying the asking fields
.. i18n:   	4. press OK
.. i18n:   
.. i18n:   	Camptocamp is open to support you in the process of closing on site or
.. i18n:   	remotely.
..

::

  	This module addresses the wizard "close fiscal year" of the 4.2 version
  	of OpenERP => it allows:
  
  	- Closing at any time
  	- Correctly report non-reconciled entries (positions open)
  	- Automatic transfer actual year result to the balance sheet
  	- Automatic closing of periods fiscal year
  	- News data checking
  	- Checking of the "closing type" of the accounts (compared to the
  	"closing type" of the "type of account")
  
  	The module work is :
  
  	1. tests (opening and closing journal, dates, previous fiscal years
  	status, etc. ..)
  	2. transfer the actual year result to the balance sheet
  	3. transfer the account balance of "balance" type to the new fiscal year
  	4. transfer of 31.12 non reconciles entries to the new fiscal year
  	(based on the dates of reconciled entries)
  	5. Reconciliation of the "new entries" entry to remove the conflict with
  	the initial invoice entry
  	6. closing periods and fiscal year
  
  	The module does not:
  	- Be able to re-open closed fiscal year (but we're available if you want
  	us to develop it :-) )
  	- Separate the step of transferring account balance and the step of
  	closing (=> we can develop that feature if necessary)
  
  	Here are the steps to allow the closing of fiscal year :
  
  	=> The following screencast will explain in detail how to do: http://www.screencast.com/t/lXLRJoQca
  
  	0. !!!!!!!!!!! MAKE A BACKUP OF THE DATABASE !!!!!!!!!!!
  	1. verify that the "types of closing" specified on the "type of
  	accounts" are correct
  	2. launch the "Finance -> Charts -> Charts of Account -> trouble accounts" list which give you the list of all the
  	accounts which the type of closing is different than that specified the
  	type of account
  	3. start the wizard closing "Finance -> End of Year Treatments -> close a fiscal year" specifying the asking fields
  	4. press OK
  
  	Camptocamp is open to support you in the process of closing on site or
  	remotely.

.. i18n: Download links
.. i18n: --------------
..

Download links
--------------

.. i18n: You can download this module as a zip file in the following version:
..

You can download this module as a zip file in the following version:

.. i18n:   * `4.2 <http://www.openerp.com/download/modules/4.2/c2c_fiscal_year_close.zip>`_
.. i18n:   	
..

  * `4.2 <http://www.openerp.com/download/modules/4.2/c2c_fiscal_year_close.zip>`_
  	

.. i18n: Dependencies
.. i18n: ------------
..

Dependencies
------------

.. i18n:  * :mod:`base`
.. i18n:  * :mod:`account`
..

 * :mod:`base`
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

.. i18n: None
..

None

.. i18n: Views
.. i18n: -----
..

Views
-----

.. i18n: None
..

None

.. i18n: Objects
.. i18n: -------
..

Objects
-------

.. i18n: None
..

None
