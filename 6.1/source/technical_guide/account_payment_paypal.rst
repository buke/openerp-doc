
.. i18n: .. module:: account_payment_paypal
.. i18n:     :synopsis: Import Paypal Payments 
.. i18n:     :noindex:
.. i18n: .. 
..

.. module:: account_payment_paypal
    :synopsis: Import Paypal Payments 
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
.. i18n:     <div class="js-kit-rating" title="" permalink="" standalone="yes" path="/account_payment_paypal"></div>
.. i18n:     <script src="http://js-kit.com/ratings.js"></script>
..

.. raw:: html

    <div class="js-kit-rating" title="" permalink="" standalone="yes" path="/account_payment_paypal"></div>
    <script src="http://js-kit.com/ratings.js"></script>

.. i18n: Import Paypal Payments (*account_payment_paypal*)
.. i18n: =================================================
.. i18n: :Module: account_payment_paypal
.. i18n: :Name: Import Paypal Payments
.. i18n: :Version: 5.0.1.0
.. i18n: :Author: Zikzakmedia
.. i18n: :Directory: account_payment_paypal
.. i18n: :Web: www.zikzakmedia.com
.. i18n: :Official module: no
.. i18n: :Quality certified: no
..

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

.. i18n: Description
.. i18n: -----------
..

Description
-----------

.. i18n: ::
.. i18n: 
.. i18n:   Import Paypal Payments from a CSV file.
.. i18n:   
.. i18n:   Adds a wizard in bank statements to select a CSV file with Paypal payments lines like this:
.. i18n:   
.. i18n:   Date, Time, Time Zone, Name, Type, Status, Currency, Gross, Fee, Net, From Email Address, To Email Address, Transaction ID, Counterparty Status, Address Status, Item Title, Item ID, Shipping and Handling Amount, Insurance Amount, Sales Tax, Option 1 Name, Option 1 Value, Option 2 Name, Option 2 Value, Auction Site, Buyer ID, Item URL, Closing Date, Escrow Id, Invoice Id, Reference Txn ID, Invoice Number, Custom Number, Receipt ID, Balance, Address Line 1, Address Line 2/District, Town/City, State/Province/Region/County/Territory/Prefecture/Republic, Zip/Postal Code, Country, Contact Phone Number, 
.. i18n:   "25/03/2009", "23:45:35", "GMT+02:00", "Computer Company", "Web Accept Payment Received", "Completed", "EUR", "20,00", "-0,89","19,11", "from1@email.com", "to@email.com","0LN645674B531493M","Non-U.S. - Verified", "Non-U.S.","Item1 title", "1", "0,00","","0,00","usr", "45678","","","","","","","","","","","","","1.315,74", "address1","","city1","state1", "zip1","country1","",
.. i18n:   "28/03/2009","21:58:54","GMT+02:00", "John Smith", "Web Accept Payment Received", "Completed", "USD","20,00","-0,94","19,06", "from2@email.com", "to@email.com", "6V823569E37342433", "Verified","Confirmed","Item 2 title","1", "0,00","","0,00","usr", "34567","","","", "","","","","","","","","", "20.979,99", "address2","", "city2","state2","zip2","country2","",
.. i18n:   
.. i18n:   These fields are optional: Address Line 1, Address Line 2/District, Town/City, State/Province/Region/County/Territory/Prefecture/Republic, Zip/Postal Code, Country, Contact Phone Number.
.. i18n:   
.. i18n:   Only the Paypal payment lines with the same currency as the bank statement are imported. And if 'Status completed' option is checked, only the Paypal payment lines with status field = 'Completed' are imported.
.. i18n:   
.. i18n:   Paypal transactions are classified as:
.. i18n:       * customer: 'Type' in ['Web Accept Payment Received', 'Payment Received', 'Subscription Payment Received', 'Refund']
.. i18n:       * supplier: 'Type' in ['Credit']
.. i18n:       * general: Other cases, 'Type' in ['Transfer', 'Chargeback Settlement', ...]
.. i18n:   
.. i18n:   Tries to fill the partner and invoice to conciliate from the Paypal transaction ID. If not, try to find the partner with the from (customer) or to (supplier) email addresses (from1@email.com or to@email.com in the example) and, if the 'Search invoice to reconcile' option is checked, try to conciliate it with an open invoice with the same partner, same amount+-accuracy, same date+-accuracy and payment type 'PAYPAL'.
.. i18n:   
.. i18n:   The from/to Paypal email address (it can be considered as a Paypal account) is searched in the partner bank account field (the bank name of Paypal accounts must be 'PAYPAL').
.. i18n:   
.. i18n:   First we must define a Paypal importation configuration:
.. i18n:       * The account for the Paypal fees.
.. i18n:       * If you want to insert the Paypal transactions in the bank statement or only show the warning or error messages.
.. i18n:       * If you want to reconcile with open invoices (giving an amount and date accuracy to search the invoices).
..

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
.. i18n:  * :mod:`account`
.. i18n:  * :mod:`account_payment_extension`
..

 * :mod:`base`
 * :mod:`account`
 * :mod:`account_payment_extension`

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

.. i18n:  * Financial Management/Configuration/Paypal Payment Import Configuration
..

 * Financial Management/Configuration/Paypal Payment Import Configuration

.. i18n: Views
.. i18n: -----
..

Views
-----

.. i18n:  * account.payment.paypal.import.config (tree)
.. i18n:  * account.payment.paypal.import.config (form)
..

 * account.payment.paypal.import.config (tree)
 * account.payment.paypal.import.config (form)

.. i18n: Objects
.. i18n: -------
..

Objects
-------

.. i18n: Object: Paypal payments Configuration (account.payment.paypal.import.config)
.. i18n: ############################################################################
..

Object: Paypal payments Configuration (account.payment.paypal.import.config)
############################################################################

.. i18n: :status_completed: Status completed, boolean
..

:status_completed: Status completed, boolean

.. i18n:     *Check this box if you want to process only the Paypal transactions with the status field = 'Completed'.*
..

    *Check this box if you want to process only the Paypal transactions with the status field = 'Completed'.*

.. i18n: :name: Name, char
..

:name: Name, char

.. i18n: :activate_insert: Active Insert, boolean
..

:activate_insert: Active Insert, boolean

.. i18n:     *Check this box if you want to insert the Paypal transactions in the bank statement. If not, it only shows the warning or error messages.*
..

    *Check this box if you want to insert the Paypal transactions in the bank statement. If not, it only shows the warning or error messages.*

.. i18n: :account_expenditure_id: Payment fee account, many2one, required
..

:account_expenditure_id: Payment fee account, many2one, required

.. i18n:     *Account for the Paypal fees.*
..

    *Account for the Paypal fees.*

.. i18n: :invoice_date_accuracy: Invoice date accuracy, integer
..

:invoice_date_accuracy: Invoice date accuracy, integer

.. i18n:     *Payment date accuracy (number of days) on searching an invoice to reconcile.*
..

    *Payment date accuracy (number of days) on searching an invoice to reconcile.*

.. i18n: :active: Active, boolean
..

:active: Active, boolean

.. i18n: :invoice_reconcile: Search invoice to reconcile, boolean
..

:invoice_reconcile: Search invoice to reconcile, boolean

.. i18n:     *Check this box when, if an invoice to reconcile have not found by the Paypal transaction ID, you want to find an open invoice with same partner, same amount+-accuracy, same date+-accuracy and payment type 'PAYPAL'.*
..

    *Check this box when, if an invoice to reconcile have not found by the Paypal transaction ID, you want to find an open invoice with same partner, same amount+-accuracy, same date+-accuracy and payment type 'PAYPAL'.*

.. i18n: :invoice_amount_accuracy: Invoice amount accuracy (%), float
..

:invoice_amount_accuracy: Invoice amount accuracy (%), float

.. i18n:     *Payment amount accuracy (% ratio between 0-1) on searching an invoice to reconcile.*
..

    *Payment amount accuracy (% ratio between 0-1) on searching an invoice to reconcile.*
