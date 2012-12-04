
.. module:: account_payment_epassporte
    :synopsis: Import ePassporte Payments 
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

    <div class="js-kit-rating" title="" permalink="" standalone="yes" path="/account_payment_epassporte"></div>
    <script src="http://js-kit.com/ratings.js"></script>

Import ePassporte Payments (*account_payment_epassporte*)
=========================================================
:Module: account_payment_epassporte
:Name: Import ePassporte Payments
:Version: 5.0.1.0
:Author: Zikzakmedia
:Directory: account_payment_epassporte
:Web: www.zikzakmedia.com
:Official module: no
:Quality certified: no

Description
-----------

::

  Import ePassporte Payments from a CSV file.
  
  Adds a wizard in bank statements to select a CSV file with ePassporte payments lines like this:
  
  "Transaction Date","Posted Date","Description","Amount in USD","Balance"
  3/27/2009,3/27/2009,"b2p Fee",-2.00,17816.06
  3/27/2009,3/27/2009,"b2p particularaccount",-11.17,17818.06
  3/23/2009,3/24/2009,"b2b Fee",-2.00,17829.23
  3/23/2009,3/24/2009,"b2b businessaccount",-111.51,17831.23
  
  Checks if the bank statement currency and ePassporte file currency (USD in the example) are the same.
  Tries to fill the partner information from the ePassporte account (businessaccount and particularaccount in the example). This ePassporte account is searched in the partner bank account field (the bank name of ePassporte accounts must be 'EPASSPORTE').
  If the 'Search invoice to reconcile' option is checked, tries to reconcile with an open invoice with the same partner, same amount+-accuracy, same date+-accuracy and payment type 'EPASSPORTE'.
  
  First we must define an ePassporte importation configuration:
      * The account for the ePassporte fees.
      * If you want to insert the ePassporte transactions in the bank statement or only show the warning or error messages.
      * If you want to reconcile with open invoices (giving an amount and date accuracy to search the invoices).

Download links
--------------

You can download this module as a zip file in the following version:

(No download links available)


Dependencies
------------

 * :mod:`base`
 * :mod:`account`
 * :mod:`account_payment_extension`

Reports
-------

None


Menus
-------

 * Financial Management/Configuration/Epassporte Payment Import Configuration

Views
-----

 * account.payment.epassporte.import.config (tree)
 * account.payment.epassporte.import.config (form)


Objects
-------

Object: Epassporte payments Configuration (account.payment.epassporte.import.config)
####################################################################################



:name: Name, char





:activate_insert: Active Insert, boolean

    *Check this box if you want to insert the ePassporte transactions in the bank statement. If not, it only shows the warning or error messages.*



:account_expenditure_id: Payment fee account, many2one, required

    *Account for the ePassporte fees.*



:invoice_date_accuracy: Invoice date accuracy, integer

    *Payment date accuracy (number of days) on searching an invoice to reconcile.*



:active: Active, boolean





:invoice_reconcile: Search invoice to reconcile, boolean

    *Check this box when you want to find an open invoice to reconcile with same partner, same amount+-accuracy, same date+-accuracy and payment type 'EPASSPORTE'.*



:invoice_amount_accuracy: Invoice amount accuracy (%), float

    *Payment amount accuracy (% ratio between 0-1) on searching an invoice to reconcile.*
