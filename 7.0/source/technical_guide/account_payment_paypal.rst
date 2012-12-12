
.. module:: account_payment_paypal
    :synopsis: Import Paypal Payments 
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

    <div class="js-kit-rating" title="" permalink="" standalone="yes" path="/account_payment_paypal"></div>
    <script src="http://js-kit.com/ratings.js"></script>

Import Paypal Payments (*account_payment_paypal*)
=================================================
:Module: account_payment_paypal
:Name: Import Paypal Payments
:Version: 5.0.1.0
:Author: Zikzakmedia
:Directory: account_payment_paypal
:Web: www.zikzakmedia.com
:Official module: no
:Quality certified: no

Description
-----------

::

  Import Paypal Payments from a CSV file.
  
  Adds a wizard in bank statements to select a CSV file with Paypal payments lines like this:
  
  Date, Time, Time Zone, Name, Type, Status, Currency, Gross, Fee, Net, From Email Address, To Email Address, Transaction ID, Counterparty Status, Address Status, Item Title, Item ID, Shipping and Handling Amount, Insurance Amount, Sales Tax, Option 1 Name, Option 1 Value, Option 2 Name, Option 2 Value, Auction Site, Buyer ID, Item URL, Closing Date, Escrow Id, Invoice Id, Reference Txn ID, Invoice Number, Custom Number, Receipt ID, Balance, Address Line 1, Address Line 2/District, Town/City, State/Province/Region/County/Territory/Prefecture/Republic, Zip/Postal Code, Country, Contact Phone Number, 
  "25/03/2009", "23:45:35", "GMT+02:00", "Computer Company", "Web Accept Payment Received", "Completed", "EUR", "20,00", "-0,89","19,11", "from1@email.com", "to@email.com","0LN645674B531493M","Non-U.S. - Verified", "Non-U.S.","Item1 title", "1", "0,00","","0,00","usr", "45678","","","","","","","","","","","","","1.315,74", "address1","","city1","state1", "zip1","country1","",
  "28/03/2009","21:58:54","GMT+02:00", "John Smith", "Web Accept Payment Received", "Completed", "USD","20,00","-0,94","19,06", "from2@email.com", "to@email.com", "6V823569E37342433", "Verified","Confirmed","Item 2 title","1", "0,00","","0,00","usr", "34567","","","", "","","","","","","","","", "20.979,99", "address2","", "city2","state2","zip2","country2","",
  
  These fields are optional: Address Line 1, Address Line 2/District, Town/City, State/Province/Region/County/Territory/Prefecture/Republic, Zip/Postal Code, Country, Contact Phone Number.
  
  Only the Paypal payment lines with the same currency as the bank statement are imported. And if 'Status completed' option is checked, only the Paypal payment lines with status field = 'Completed' are imported.
  
  Paypal transactions are classified as:
      * customer: 'Type' in ['Web Accept Payment Received', 'Payment Received', 'Subscription Payment Received', 'Refund']
      * supplier: 'Type' in ['Credit']
      * general: Other cases, 'Type' in ['Transfer', 'Chargeback Settlement', ...]
  
  Tries to fill the partner and invoice to conciliate from the Paypal transaction ID. If not, try to find the partner with the from (customer) or to (supplier) email addresses (from1@email.com or to@email.com in the example) and, if the 'Search invoice to reconcile' option is checked, try to conciliate it with an open invoice with the same partner, same amount+-accuracy, same date+-accuracy and payment type 'PAYPAL'.
  
  The from/to Paypal email address (it can be considered as a Paypal account) is searched in the partner bank account field (the bank name of Paypal accounts must be 'PAYPAL').
  
  First we must define a Paypal importation configuration:
      * The account for the Paypal fees.
      * If you want to insert the Paypal transactions in the bank statement or only show the warning or error messages.
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

 * Financial Management/Configuration/Paypal Payment Import Configuration

Views
-----

 * account.payment.paypal.import.config (tree)
 * account.payment.paypal.import.config (form)


Objects
-------

Object: Paypal payments Configuration (account.payment.paypal.import.config)
############################################################################



:status_completed: Status completed, boolean

    *Check this box if you want to process only the Paypal transactions with the status field = 'Completed'.*



:name: Name, char





:activate_insert: Active Insert, boolean

    *Check this box if you want to insert the Paypal transactions in the bank statement. If not, it only shows the warning or error messages.*



:account_expenditure_id: Payment fee account, many2one, required

    *Account for the Paypal fees.*



:invoice_date_accuracy: Invoice date accuracy, integer

    *Payment date accuracy (number of days) on searching an invoice to reconcile.*



:active: Active, boolean





:invoice_reconcile: Search invoice to reconcile, boolean

    *Check this box when, if an invoice to reconcile have not found by the Paypal transaction ID, you want to find an open invoice with same partner, same amount+-accuracy, same date+-accuracy and payment type 'PAYPAL'.*



:invoice_amount_accuracy: Invoice amount accuracy (%), float

    *Payment amount accuracy (% ratio between 0-1) on searching an invoice to reconcile.*
