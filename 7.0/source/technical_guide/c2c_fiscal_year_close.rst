
.. module:: c2c_fiscal_year_close
    :synopsis: c2c close fiscal year 
    :noindex:
.. 

.. raw:: html

    <link rel="stylesheet" href="../_static/hide_objects_in_sidebar.css" type="text/css" />

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

Description
-----------

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

Download links
--------------

You can download this module as a zip file in the following version:

  * `4.2 <http://www.openerp.com/download/modules/4.2/c2c_fiscal_year_close.zip>`_
  	

Dependencies
------------

 * :mod:`base`
 * :mod:`account`

Reports
-------

None


Menus
-------


None


Views
-----


None



Objects
-------

None
