
.. module:: account_asset
    :synopsis: Asset management 
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

    <div class="js-kit-rating" title="" permalink="" standalone="yes" path="/account_asset"></div>
    <script src="http://js-kit.com/ratings.js"></script>

Asset management (*account_asset*)
==================================
:Module: account_asset
:Name: Asset management
:Version: 5.0.1.0
:Author: Tiny
:Directory: account_asset
:Web: http://www.openerp.com
:Official module: no
:Quality certified: no

Description
-----------

::

  Financial and accounting asset management.
      Allows to define
      * Asset category. 
      * Assets.
      *Asset usage period and property.

Download links
--------------

You can download this module as a zip file in the following version:

  * `5.0 <http://www.openerp.com/download/modules/5.0/account_asset.zip>`_
  * `trunk <http://www.openerp.com/download/modules/trunk/account_asset.zip>`_


Dependencies
------------

 * :mod:`account`
 * :mod:`account_simulation`

Reports
-------

None


Menus
-------

 * Financial Management/Periodical Processing/Compute assets
 * Financial Management/Configuration/Assets
 * Financial Management/Configuration/Assets/Asset Category
 * Financial Management/Configuration/Assets/Asset
 * Financial Management/Assets
 * Financial Management/Assets/Asset Hierarchy
 * Financial Management/Assets/Assets
 * Financial Management/Assets/Assets/Draft Assets
 * Financial Management/Assets/Assets/Open Assets

Views
-----

 * account.asset.category.form (form)
 * account.asset.category.tree (tree)
 * account.asset.property.tree (tree)
 * account.asset.asset.form (form)
 * account.asset.property.history.form (form)
 * account.asset.property.history.tree (tree)
 * account.asset.board.form (form)
 * account.asset.board.tree (tree)
 * account.asset.asset.tree (tree)
 * \* INHERIT account.invoice.line.form (form)


Objects
-------

Object: Asset category (account.asset.category)
###############################################



:note: Note, text





:code: Asset code, char





:name: Asset category, char, required




Object: Asset (account.asset.asset)
###################################



:property_ids: Asset method name, one2many, readonly





:note: Note, text





:code: Asset code, char





:name: Asset, char, required





:sequence: Sequence, integer





:child_ids: Childs asset, one2many





:entry_ids: Entries, one2many, readonly





:localisation: Localisation, char





:date: Date, date, required





:state: Global state, selection, required





:period_id: Period, many2one, required, readonly





:parent_id: Parent asset, many2one





:value_total: Total value, float, readonly





:active: Active, boolean





:category_id: Asset category, many2one





:partner_id: Partner, many2one




Object: Asset property (account.asset.property)
###############################################



:asset_id: Asset, many2one, required





:board_ids: Asset board, one2many





:entry_asset_ids: Asset Entries, many2many





:history_ids: History, one2many, readonly





:method_progress_factor: Progressif factor, float, readonly





:method_end: Ending date, date





:account_asset_id: Asset account, many2one, required





:journal_id: Journal, many2one, required





:method: Computation method, selection, required, readonly





:journal_analytic_id: Analytic journal, many2one





:date: Date created, date





:method_time: Time method, selection, required, readonly





:state: State, selection, required





:method_period: Period per interval, integer, readonly





:value_residual: Residual value, float, readonly





:value_total: Gross value, float, readonly





:account_analytic_id: Analytic account, many2one





:account_actif_id: Depreciation account, many2one, required





:type: Depr. method type, selection, required





:method_delay: Number of interval, integer, readonly





:name: Method name, char




Object: Asset history (account.asset.property.history)
######################################################



:user_id: User, many2one, required





:name: History name, char





:method_end: Ending date, date





:asset_property_id: Method, many2one, required





:note: Note, text





:method_delay: Number of interval, integer





:method_period: Period per interval, integer





:date: Date, date, required




Object: Asset board (account.asset.board)
#########################################



:asset_id: Asset, many2one, required





:value_gross: Gross value, float, required





:value_asset_cumul: Cumul. value, float, required





:name: Asset name, char, required





:value_asset: Asset Value, float, required





:value_net: Net value, float, required


