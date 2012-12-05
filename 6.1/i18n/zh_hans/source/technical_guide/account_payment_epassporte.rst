
.. i18n: .. module:: account_payment_epassporte
.. i18n:     :synopsis: Import ePassporte Payments 
.. i18n:     :noindex:
.. i18n: .. 
..

.. module:: account_payment_epassporte
    :synopsis: Import ePassporte Payments 
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
.. i18n:     <div class="js-kit-rating" title="" permalink="" standalone="yes" path="/account_payment_epassporte"></div>
.. i18n:     <script src="http://js-kit.com/ratings.js"></script>
..

.. raw:: html

    <div class="js-kit-rating" title="" permalink="" standalone="yes" path="/account_payment_epassporte"></div>
    <script src="http://js-kit.com/ratings.js"></script>

.. i18n: Import ePassporte Payments (*account_payment_epassporte*)
.. i18n: =========================================================
.. i18n: :Module: account_payment_epassporte
.. i18n: :Name: Import ePassporte Payments
.. i18n: :Version: 5.0.1.0
.. i18n: :Author: Zikzakmedia
.. i18n: :Directory: account_payment_epassporte
.. i18n: :Web: www.zikzakmedia.com
.. i18n: :Official module: no
.. i18n: :Quality certified: no
..

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

.. i18n: Description
.. i18n: -----------
..

Description
-----------

.. i18n: ::
.. i18n: 
.. i18n:   Import ePassporte Payments from a CSV file.
.. i18n:   
.. i18n:   Adds a wizard in bank statements to select a CSV file with ePassporte payments lines like this:
.. i18n:   
.. i18n:   "Transaction Date","Posted Date","Description","Amount in USD","Balance"
.. i18n:   3/27/2009,3/27/2009,"b2p Fee",-2.00,17816.06
.. i18n:   3/27/2009,3/27/2009,"b2p particularaccount",-11.17,17818.06
.. i18n:   3/23/2009,3/24/2009,"b2b Fee",-2.00,17829.23
.. i18n:   3/23/2009,3/24/2009,"b2b businessaccount",-111.51,17831.23
.. i18n:   
.. i18n:   Checks if the bank statement currency and ePassporte file currency (USD in the example) are the same.
.. i18n:   Tries to fill the partner information from the ePassporte account (businessaccount and particularaccount in the example). This ePassporte account is searched in the partner bank account field (the bank name of ePassporte accounts must be 'EPASSPORTE').
.. i18n:   If the 'Search invoice to reconcile' option is checked, tries to reconcile with an open invoice with the same partner, same amount+-accuracy, same date+-accuracy and payment type 'EPASSPORTE'.
.. i18n:   
.. i18n:   First we must define an ePassporte importation configuration:
.. i18n:       * The account for the ePassporte fees.
.. i18n:       * If you want to insert the ePassporte transactions in the bank statement or only show the warning or error messages.
.. i18n:       * If you want to reconcile with open invoices (giving an amount and date accuracy to search the invoices).
..

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

.. i18n:  * Financial Management/Configuration/Epassporte Payment Import Configuration
..

 * Financial Management/Configuration/Epassporte Payment Import Configuration

.. i18n: Views
.. i18n: -----
..

Views
-----

.. i18n:  * account.payment.epassporte.import.config (tree)
.. i18n:  * account.payment.epassporte.import.config (form)
..

 * account.payment.epassporte.import.config (tree)
 * account.payment.epassporte.import.config (form)

.. i18n: Objects
.. i18n: -------
..

Objects
-------

.. i18n: Object: Epassporte payments Configuration (account.payment.epassporte.import.config)
.. i18n: ####################################################################################
..

Object: Epassporte payments Configuration (account.payment.epassporte.import.config)
####################################################################################

.. i18n: :name: Name, char
..

:name: Name, char

.. i18n: :activate_insert: Active Insert, boolean
..

:activate_insert: Active Insert, boolean

.. i18n:     *Check this box if you want to insert the ePassporte transactions in the bank statement. If not, it only shows the warning or error messages.*
..

    *Check this box if you want to insert the ePassporte transactions in the bank statement. If not, it only shows the warning or error messages.*

.. i18n: :account_expenditure_id: Payment fee account, many2one, required
..

:account_expenditure_id: Payment fee account, many2one, required

.. i18n:     *Account for the ePassporte fees.*
..

    *Account for the ePassporte fees.*

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

.. i18n:     *Check this box when you want to find an open invoice to reconcile with same partner, same amount+-accuracy, same date+-accuracy and payment type 'EPASSPORTE'.*
..

    *Check this box when you want to find an open invoice to reconcile with same partner, same amount+-accuracy, same date+-accuracy and payment type 'EPASSPORTE'.*

.. i18n: :invoice_amount_accuracy: Invoice amount accuracy (%), float
..

:invoice_amount_accuracy: Invoice amount accuracy (%), float

.. i18n:     *Payment amount accuracy (% ratio between 0-1) on searching an invoice to reconcile.*
..

    *Payment amount accuracy (% ratio between 0-1) on searching an invoice to reconcile.*
