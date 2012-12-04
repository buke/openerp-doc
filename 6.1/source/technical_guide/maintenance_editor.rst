
.. module:: maintenance_editor
    :synopsis: Maintenance Editor 
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

    <div class="js-kit-rating" title="" permalink="" standalone="yes" path="/maintenance_editor"></div>
    <script src="http://js-kit.com/ratings.js"></script>

Maintenance Editor (*maintenance_editor*)
=========================================
:Module: maintenance_editor
:Name: Maintenance Editor
:Version: 5.0.1.1
:Author: Tiny
:Directory: maintenance_editor
:Web: 
:Official module: no
:Quality certified: no

Description
-----------

::

  module to manage maintenance contracts:

Download links
--------------

You can download this module as a zip file in the following version:

  * `5.0 <http://www.openerp.com/download/modules/5.0/maintenance_editor.zip>`_
  * `trunk <http://www.openerp.com/download/modules/trunk/maintenance_editor.zip>`_


Dependencies
------------

 * :mod:`base`
 * :mod:`product`
 * :mod:`crm`

Reports
-------

 * Basic Contract

 * SMB Contract

 * Corporate Contract

Menus
-------

 * Administration/Modules Management/Maintenance Editor
 * Administration/Modules Management/Maintenance Editor/Maintenance Contracts
 * Administration/Modules Management/Maintenance Editor/Maintenance Modules
 * Administration/Modules Management/Maintenance Editor/Maintenance Contract Types
 * Administration/Modules Management/Maintenance Editor/Maintenance Modules/Refresh Module List

Views
-----

 * maintenance.maintenance.tree (tree)
 * maintenance.maintenance.form (form)
 * maintenance.maintenance.module.tree (tree)
 * maintenance.maintenance.module.form (form)
 * maintenance.contract.type.form (form)


Objects
-------

Object: maintenance modules (maintenance.maintenance.module)
############################################################



:path: Path, char, readonly





:version: Version, char, readonly





:name: Name, char, required, readonly





:certificate: Certificate Code, char, required, readonly




Object: maintenance.contract.type (maintenance.contract.type)
#############################################################



:crm_case_categ_id: CRM Case Category, many2one, required





:name: Name, char, required





:crm_case_section_id: CRM Case Section, many2one, required





:product_id: Product, many2one




Object: maintenance contract (maintenance.maintenance)
######################################################



:name: Contract ID, char, required





:type_id: Contract Type, many2one, required





:module_ids: Modules, many2many





:date_from: Date From, date, required





:note: Note, text





:state: State, selection, readonly





:date_to: Date To, date, required





:partner_invoice_id: Address, many2one





:password: Password, char, required





:partner_id: Partner, many2one, required


