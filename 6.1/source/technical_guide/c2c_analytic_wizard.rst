
.. module:: c2c_analytic_wizard
    :synopsis: Analytic wizard and tools for services companies 
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

    <div class="js-kit-rating" title="" permalink="" standalone="yes" path="/c2c_analytic_wizard"></div>
    <script src="http://js-kit.com/ratings.js"></script>

Analytic wizard and tools for services companies (*c2c_analytic_wizard*)
========================================================================
:Module: c2c_analytic_wizard
:Name: Analytic wizard and tools for services companies
:Version: 5.0.1.3
:Author: Camptocamp
:Directory: c2c_analytic_wizard
:Web: http://www.camptocamp.com
:Official module: no
:Quality certified: no

Description
-----------

::

  Add wizard to manage analytic account and invoicing :
   - Associate Analytic Lines to invoice (from an invoice or from analytic line directly)
   - Dissociate Analytic Lines from an invoice
   - Create blank invoice from Analytic Account (with all information completed)
   - Create invoice from Analytic Lines
   - Get all invoice from Analytic Account (with recursion in child account)
   - Get Analytic Lines from Analytic Account (with recursion in child account)
   - Get Analytic Lines from an invoice for controlling
  Add report for on analytic account showing the indicators et open invoice.
  
  -----------------------------------------------------------------------------------------------
  
  Ce module comprend un set de wizard pour faciliter la gestion des entreprises de service travaillant avec les comptes analytiques,
  par exemple pour la gestion de projet. Il apporte une réelle plus-value en terme d'ergonomie. Ces wizards améliorent la facturation du travail
  effectué depuis un projet (compte analytique), permettent d'associer / dissocier des lignes analytiques d'une facture ou encore d'obtenir 
  la liste des factures relatives à un projet.
  Ajoute egalement un rapport affichant le détails d'un compte analytique et ses factures ouvertes

Download links
--------------

You can download this module as a zip file in the following version:

  * `4.2 <http://www.openerp.com/download/modules/4.2/c2c_analytic_wizard.zip>`_
  * `5.0 <http://www.openerp.com/download/modules/5.0/c2c_analytic_wizard.zip>`_
  * `trunk <http://www.openerp.com/download/modules/trunk/c2c_analytic_wizard.zip>`_


Dependencies
------------

 * :mod:`base`
 * :mod:`account`
 * :mod:`product`
 * :mod:`account_analytic_analysis`
 * :mod:`c2c_reporting_tools`
 * :mod:`hr_timesheet_invoice`
 * :mod:`account_tax_include`

Reports
-------

 * Indicator Report

Menus
-------


None


Views
-----

 * \* INHERIT indicator.account.detail.form (form)


Objects
-------

None
