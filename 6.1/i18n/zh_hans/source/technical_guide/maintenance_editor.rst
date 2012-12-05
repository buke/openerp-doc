
.. i18n: .. module:: maintenance_editor
.. i18n:     :synopsis: Maintenance Editor 
.. i18n:     :noindex:
.. i18n: .. 
..

.. module:: maintenance_editor
    :synopsis: Maintenance Editor 
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
.. i18n:     <div class="js-kit-rating" title="" permalink="" standalone="yes" path="/maintenance_editor"></div>
.. i18n:     <script src="http://js-kit.com/ratings.js"></script>
..

.. raw:: html

    <div class="js-kit-rating" title="" permalink="" standalone="yes" path="/maintenance_editor"></div>
    <script src="http://js-kit.com/ratings.js"></script>

.. i18n: Maintenance Editor (*maintenance_editor*)
.. i18n: =========================================
.. i18n: :Module: maintenance_editor
.. i18n: :Name: Maintenance Editor
.. i18n: :Version: 5.0.1.1
.. i18n: :Author: Tiny
.. i18n: :Directory: maintenance_editor
.. i18n: :Web: 
.. i18n: :Official module: no
.. i18n: :Quality certified: no
..

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

.. i18n: Description
.. i18n: -----------
..

Description
-----------

.. i18n: ::
.. i18n: 
.. i18n:   module to manage maintenance contracts:
..

::

  module to manage maintenance contracts:

.. i18n: Download links
.. i18n: --------------
..

Download links
--------------

.. i18n: You can download this module as a zip file in the following version:
..

You can download this module as a zip file in the following version:

.. i18n:   * `5.0 <http://www.openerp.com/download/modules/5.0/maintenance_editor.zip>`_
.. i18n:   * `trunk <http://www.openerp.com/download/modules/trunk/maintenance_editor.zip>`_
..

  * `5.0 <http://www.openerp.com/download/modules/5.0/maintenance_editor.zip>`_
  * `trunk <http://www.openerp.com/download/modules/trunk/maintenance_editor.zip>`_

.. i18n: Dependencies
.. i18n: ------------
..

Dependencies
------------

.. i18n:  * :mod:`base`
.. i18n:  * :mod:`product`
.. i18n:  * :mod:`crm`
..

 * :mod:`base`
 * :mod:`product`
 * :mod:`crm`

.. i18n: Reports
.. i18n: -------
..

Reports
-------

.. i18n:  * Basic Contract
.. i18n: 
.. i18n:  * SMB Contract
.. i18n: 
.. i18n:  * Corporate Contract
..

 * Basic Contract

 * SMB Contract

 * Corporate Contract

.. i18n: Menus
.. i18n: -------
..

Menus
-------

.. i18n:  * Administration/Modules Management/Maintenance Editor
.. i18n:  * Administration/Modules Management/Maintenance Editor/Maintenance Contracts
.. i18n:  * Administration/Modules Management/Maintenance Editor/Maintenance Modules
.. i18n:  * Administration/Modules Management/Maintenance Editor/Maintenance Contract Types
.. i18n:  * Administration/Modules Management/Maintenance Editor/Maintenance Modules/Refresh Module List
..

 * Administration/Modules Management/Maintenance Editor
 * Administration/Modules Management/Maintenance Editor/Maintenance Contracts
 * Administration/Modules Management/Maintenance Editor/Maintenance Modules
 * Administration/Modules Management/Maintenance Editor/Maintenance Contract Types
 * Administration/Modules Management/Maintenance Editor/Maintenance Modules/Refresh Module List

.. i18n: Views
.. i18n: -----
..

Views
-----

.. i18n:  * maintenance.maintenance.tree (tree)
.. i18n:  * maintenance.maintenance.form (form)
.. i18n:  * maintenance.maintenance.module.tree (tree)
.. i18n:  * maintenance.maintenance.module.form (form)
.. i18n:  * maintenance.contract.type.form (form)
..

 * maintenance.maintenance.tree (tree)
 * maintenance.maintenance.form (form)
 * maintenance.maintenance.module.tree (tree)
 * maintenance.maintenance.module.form (form)
 * maintenance.contract.type.form (form)

.. i18n: Objects
.. i18n: -------
..

Objects
-------

.. i18n: Object: maintenance modules (maintenance.maintenance.module)
.. i18n: ############################################################
..

Object: maintenance modules (maintenance.maintenance.module)
############################################################

.. i18n: :path: Path, char, readonly
..

:path: Path, char, readonly

.. i18n: :version: Version, char, readonly
..

:version: Version, char, readonly

.. i18n: :name: Name, char, required, readonly
..

:name: Name, char, required, readonly

.. i18n: :certificate: Certificate Code, char, required, readonly
..

:certificate: Certificate Code, char, required, readonly

.. i18n: Object: maintenance.contract.type (maintenance.contract.type)
.. i18n: #############################################################
..

Object: maintenance.contract.type (maintenance.contract.type)
#############################################################

.. i18n: :crm_case_categ_id: CRM Case Category, many2one, required
..

:crm_case_categ_id: CRM Case Category, many2one, required

.. i18n: :name: Name, char, required
..

:name: Name, char, required

.. i18n: :crm_case_section_id: CRM Case Section, many2one, required
..

:crm_case_section_id: CRM Case Section, many2one, required

.. i18n: :product_id: Product, many2one
..

:product_id: Product, many2one

.. i18n: Object: maintenance contract (maintenance.maintenance)
.. i18n: ######################################################
..

Object: maintenance contract (maintenance.maintenance)
######################################################

.. i18n: :name: Contract ID, char, required
..

:name: Contract ID, char, required

.. i18n: :type_id: Contract Type, many2one, required
..

:type_id: Contract Type, many2one, required

.. i18n: :module_ids: Modules, many2many
..

:module_ids: Modules, many2many

.. i18n: :date_from: Date From, date, required
..

:date_from: Date From, date, required

.. i18n: :note: Note, text
..

:note: Note, text

.. i18n: :state: State, selection, readonly
..

:state: State, selection, readonly

.. i18n: :date_to: Date To, date, required
..

:date_to: Date To, date, required

.. i18n: :partner_invoice_id: Address, many2one
..

:partner_invoice_id: Address, many2one

.. i18n: :password: Password, char, required
..

:password: Password, char, required

.. i18n: :partner_id: Partner, many2one, required
..

:partner_id: Partner, many2one, required
