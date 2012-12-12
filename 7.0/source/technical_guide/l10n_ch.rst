
.. module:: l10n_ch
    :synopsis: Switzerland localisation corrected by Camptocamp 
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

    <div class="js-kit-rating" title="" permalink="" standalone="yes" path="/l10n_ch"></div>
    <script src="http://js-kit.com/ratings.js"></script>

Switzerland localisation corrected by Camptocamp (*l10n_ch*)
============================================================
:Module: l10n_ch
:Name: Switzerland localisation corrected by Camptocamp
:Version: 5.0.5.0
:Author: Camptocamp SA
:Directory: l10n_ch
:Web: http://www.camptocamp.com
:Official module: no
:Quality certified: no

Description
-----------

::

  Swiss localisation :
   - DTA generation for a lot of paiment types
   - BVR management (number generation, report, etc..)
   - Import account move from the bank file (like v11 etc..)
   - Simplify the way you handle the bank statement for reconciliation
  
  You can also add with this module one of the following account plan:
   - l10n_ch_c2c_pcg
  
  
      
  ------------------------------------------------------------------------
      
  Module incluant la localisation Suisse de TinyERP revu et corrigé par Camptocamp. Cette nouvelle version 
  comprend la gestion et l'émissionde BVR, le paiement électronique via DTA (pour les banques, le système postal est en développement) 
  et l'import du relevé de compte depuis la banque de manière automatisée. 
  De plus, nous avons intégré la définition de toutes les banques Suisses(adresse, swift et clearing).
  
  Par ailleurs, conjointement à ce module, nous proposons 1 plan comptables issus de l'USAM :
  
  
   - l10n_ch_c2c_pcg
   
  --------------------------------------------------------------------------
  TODO :
  - Implement bvr import partial reconciliation
  - Replace wizard by osv_memory when possible
  - Add missing HELP
  - Finish code comment
  - Improve demo data

Download links
--------------

You can download this module as a zip file in the following version:

  * `4.2 <http://www.openerp.com/download/modules/4.2/l10n_ch.zip>`_
  * `5.0 <http://www.openerp.com/download/modules/5.0/l10n_ch.zip>`_
  * `trunk <http://www.openerp.com/download/modules/trunk/l10n_ch.zip>`_


Dependencies
------------

 * :mod:`base`
 * :mod:`account`
 * :mod:`base_vat`
 * :mod:`base_iban`
 * :mod:`account_payment`
 * :mod:`account_tax_include`

Reports
-------

 * BVR A4 Sheet

 * Invoice with BVR

Menus
-------


None


Views
-----

 * \* INHERIT partner - bank inherit (form)
 * \* INHERIT partner - bank inherit (form)
 * \* INHERIT account.bank.statement.form.inherit (form)
 * \* INHERIT res.company.form.inherit.bvr (form)
 * \* INHERIT account.invoice.supplier.form.inherit (form)
 * \* INHERIT account.invoice.supplier.form.inherit (form)
 * \* INHERIT account.invoice.form.inherit (form)
 * \* INHERIT res.bank.form (form)
 * \* INHERIT res.bank.tree (tree)
 * \* INHERIT res.partner_partner_bank.form (form)
 * account.journal.todo.form (form)


Objects
-------

Object: account.journal.todo (account.journal.todo)
###################################################



:default_debit_account_id: Default Debit Account, many2one

    *The Default Debit Account of the account journal*



:default_credit_account_id: Default Credit Account, many2one

    *The Default Credit Account of the account journal*



:name: Journal to set, many2one, readonly

    *the currently edited account journal*
