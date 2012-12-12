
.. module:: l10n_be
    :synopsis: Belgium - Plan Comptable Minimum Normalise (Official, Quality Certified)
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

    <div class="js-kit-rating" title="" permalink="" standalone="yes" path="/l10n_be"></div>
    <script src="http://js-kit.com/ratings.js"></script>

Belgium - Plan Comptable Minimum Normalise (*l10n_be*)
======================================================
:Module: l10n_be
:Name: Belgium - Plan Comptable Minimum Normalise
:Version: 5.0.1.1
:Author: Tiny
:Directory: l10n_be
:Web: 
:Official module: yes
:Quality certified: yes

Description
-----------

::

  This is the base module to manage the accounting chart for Belgium in OpenERP.
  
      After Installing this module, the Configuration wizard for accounting is launched.
      * We have the account templates which can be helpful to generate Charts of Accounts.
      * On that particular wizard, you will be asked to pass the name of the company, the chart template to follow, the number of digits to generate the code for your account and Bank account, currency to create Journals.
          Thus, the pure copy of Chart Template is generated.
      * This is the same wizard that runs from Financial Management/Configuration/Financial Accounting/Financial Accounts/Generate Chart of Accounts from a Chart Template.
  
      Wizards provided by this module:
      * Enlist the partners with their related VAT and invoiced amounts. Prepares an XML file format. Path to access : Financial Management/Reporting/Listing of VAT Customers.
      * Prepares an XML file for Vat Declaration of the Main company of the User currently logged in. Path to access : Financial Management/Reporting/Listing of VAT Customers.

Download links
--------------

You can download this module as a zip file in the following version:

  * `4.2 <http://www.openerp.com/download/modules/4.2/l10n_be.zip>`_
  * `5.0 <http://www.openerp.com/download/modules/5.0/l10n_be.zip>`_
  * `trunk <http://www.openerp.com/download/modules/trunk/l10n_be.zip>`_


Dependencies
------------

 * :mod:`account`
 * :mod:`account_report`
 * :mod:`base_vat`
 * :mod:`base_iban`
 * :mod:`account_chart`

Reports
-------

None


Menus
-------

 * Financial Management/Legal Statements/Belgium Statements
 * Financial Management/Legal Statements/Belgium Statements/Annual Listing of VAT-Subjected Customers
 * Financial Management/Legal Statements/Belgium Statements/Periodical VAT Declaration
 * Financial Management/Legal Statements/Belgium Statements/Partner VAT intra

Views
-----


None



Objects
-------

None
