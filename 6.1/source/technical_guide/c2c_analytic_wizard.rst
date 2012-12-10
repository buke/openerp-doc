
.. i18n: .. module:: c2c_analytic_wizard
.. i18n:     :synopsis: Analytic wizard and tools for services companies 
.. i18n:     :noindex:
.. i18n: .. 
..

.. module:: c2c_analytic_wizard
    :synopsis: Analytic wizard and tools for services companies 
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
.. i18n:     <div class="js-kit-rating" title="" permalink="" standalone="yes" path="/c2c_analytic_wizard"></div>
.. i18n:     <script src="http://js-kit.com/ratings.js"></script>
..

.. raw:: html

    <div class="js-kit-rating" title="" permalink="" standalone="yes" path="/c2c_analytic_wizard"></div>
    <script src="http://js-kit.com/ratings.js"></script>

.. i18n: Analytic wizard and tools for services companies (*c2c_analytic_wizard*)
.. i18n: ========================================================================
.. i18n: :Module: c2c_analytic_wizard
.. i18n: :Name: Analytic wizard and tools for services companies
.. i18n: :Version: 5.0.1.3
.. i18n: :Author: Camptocamp
.. i18n: :Directory: c2c_analytic_wizard
.. i18n: :Web: http://www.camptocamp.com
.. i18n: :Official module: no
.. i18n: :Quality certified: no
..

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

.. i18n: Description
.. i18n: -----------
..

Description
-----------

.. i18n: ::
.. i18n: 
.. i18n:   Add wizard to manage analytic account and invoicing :
.. i18n:    - Associate Analytic Lines to invoice (from an invoice or from analytic line directly)
.. i18n:    - Dissociate Analytic Lines from an invoice
.. i18n:    - Create blank invoice from Analytic Account (with all information completed)
.. i18n:    - Create invoice from Analytic Lines
.. i18n:    - Get all invoice from Analytic Account (with recursion in child account)
.. i18n:    - Get Analytic Lines from Analytic Account (with recursion in child account)
.. i18n:    - Get Analytic Lines from an invoice for controlling
.. i18n:   Add report for on analytic account showing the indicators et open invoice.
.. i18n:   
.. i18n:   -----------------------------------------------------------------------------------------------
.. i18n:   
.. i18n:   Ce module comprend un set de wizard pour faciliter la gestion des entreprises de service travaillant avec les comptes analytiques,
.. i18n:   par exemple pour la gestion de projet. Il apporte une réelle plus-value en terme d'ergonomie. Ces wizards améliorent la facturation du travail
.. i18n:   effectué depuis un projet (compte analytique), permettent d'associer / dissocier des lignes analytiques d'une facture ou encore d'obtenir 
.. i18n:   la liste des factures relatives à un projet.
.. i18n:   Ajoute egalement un rapport affichant le détails d'un compte analytique et ses factures ouvertes
..

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

.. i18n: Download links
.. i18n: --------------
..

Download links
--------------

.. i18n: You can download this module as a zip file in the following version:
..

You can download this module as a zip file in the following version:

.. i18n:   * `4.2 <http://www.openerp.com/download/modules/4.2/c2c_analytic_wizard.zip>`_
.. i18n:   * `5.0 <http://www.openerp.com/download/modules/5.0/c2c_analytic_wizard.zip>`_
.. i18n:   * `trunk <http://www.openerp.com/download/modules/trunk/c2c_analytic_wizard.zip>`_
..

  * `4.2 <http://www.openerp.com/download/modules/4.2/c2c_analytic_wizard.zip>`_
  * `5.0 <http://www.openerp.com/download/modules/5.0/c2c_analytic_wizard.zip>`_
  * `trunk <http://www.openerp.com/download/modules/trunk/c2c_analytic_wizard.zip>`_

.. i18n: Dependencies
.. i18n: ------------
..

Dependencies
------------

.. i18n:  * :mod:`base`
.. i18n:  * :mod:`account`
.. i18n:  * :mod:`product`
.. i18n:  * :mod:`account_analytic_analysis`
.. i18n:  * :mod:`c2c_reporting_tools`
.. i18n:  * :mod:`hr_timesheet_invoice`
.. i18n:  * :mod:`account_tax_include`
..

 * :mod:`base`
 * :mod:`account`
 * :mod:`product`
 * :mod:`account_analytic_analysis`
 * :mod:`c2c_reporting_tools`
 * :mod:`hr_timesheet_invoice`
 * :mod:`account_tax_include`

.. i18n: Reports
.. i18n: -------
..

Reports
-------

.. i18n:  * Indicator Report
..

 * Indicator Report

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

.. i18n:  * \* INHERIT indicator.account.detail.form (form)
..

 * \* INHERIT indicator.account.detail.form (form)

.. i18n: Objects
.. i18n: -------
..

Objects
-------

.. i18n: None
..

None
