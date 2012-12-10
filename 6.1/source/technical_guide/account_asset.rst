
.. i18n: .. module:: account_asset
.. i18n:     :synopsis: Asset management 
.. i18n:     :noindex:
.. i18n: .. 
..

.. module:: account_asset
    :synopsis: Asset management 
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
.. i18n:     <div class="js-kit-rating" title="" permalink="" standalone="yes" path="/account_asset"></div>
.. i18n:     <script src="http://js-kit.com/ratings.js"></script>
..

.. raw:: html

    <div class="js-kit-rating" title="" permalink="" standalone="yes" path="/account_asset"></div>
    <script src="http://js-kit.com/ratings.js"></script>

.. i18n: Asset management (*account_asset*)
.. i18n: ==================================
.. i18n: :Module: account_asset
.. i18n: :Name: Asset management
.. i18n: :Version: 5.0.1.0
.. i18n: :Author: Tiny
.. i18n: :Directory: account_asset
.. i18n: :Web: http://www.openerp.com
.. i18n: :Official module: no
.. i18n: :Quality certified: no
..

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

.. i18n: Description
.. i18n: -----------
..

Description
-----------

.. i18n: ::
.. i18n: 
.. i18n:   Financial and accounting asset management.
.. i18n:       Allows to define
.. i18n:       * Asset category. 
.. i18n:       * Assets.
.. i18n:       *Asset usage period and property.
..

::

  Financial and accounting asset management.
      Allows to define
      * Asset category. 
      * Assets.
      *Asset usage period and property.

.. i18n: Download links
.. i18n: --------------
..

Download links
--------------

.. i18n: You can download this module as a zip file in the following version:
..

You can download this module as a zip file in the following version:

.. i18n:   * `5.0 <http://www.openerp.com/download/modules/5.0/account_asset.zip>`_
.. i18n:   * `trunk <http://www.openerp.com/download/modules/trunk/account_asset.zip>`_
..

  * `5.0 <http://www.openerp.com/download/modules/5.0/account_asset.zip>`_
  * `trunk <http://www.openerp.com/download/modules/trunk/account_asset.zip>`_

.. i18n: Dependencies
.. i18n: ------------
..

Dependencies
------------

.. i18n:  * :mod:`account`
.. i18n:  * :mod:`account_simulation`
..

 * :mod:`account`
 * :mod:`account_simulation`

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

.. i18n:  * Financial Management/Periodical Processing/Compute assets
.. i18n:  * Financial Management/Configuration/Assets
.. i18n:  * Financial Management/Configuration/Assets/Asset Category
.. i18n:  * Financial Management/Configuration/Assets/Asset
.. i18n:  * Financial Management/Assets
.. i18n:  * Financial Management/Assets/Asset Hierarchy
.. i18n:  * Financial Management/Assets/Assets
.. i18n:  * Financial Management/Assets/Assets/Draft Assets
.. i18n:  * Financial Management/Assets/Assets/Open Assets
..

 * Financial Management/Periodical Processing/Compute assets
 * Financial Management/Configuration/Assets
 * Financial Management/Configuration/Assets/Asset Category
 * Financial Management/Configuration/Assets/Asset
 * Financial Management/Assets
 * Financial Management/Assets/Asset Hierarchy
 * Financial Management/Assets/Assets
 * Financial Management/Assets/Assets/Draft Assets
 * Financial Management/Assets/Assets/Open Assets

.. i18n: Views
.. i18n: -----
..

Views
-----

.. i18n:  * account.asset.category.form (form)
.. i18n:  * account.asset.category.tree (tree)
.. i18n:  * account.asset.property.tree (tree)
.. i18n:  * account.asset.asset.form (form)
.. i18n:  * account.asset.property.history.form (form)
.. i18n:  * account.asset.property.history.tree (tree)
.. i18n:  * account.asset.board.form (form)
.. i18n:  * account.asset.board.tree (tree)
.. i18n:  * account.asset.asset.tree (tree)
.. i18n:  * \* INHERIT account.invoice.line.form (form)
..

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

.. i18n: Objects
.. i18n: -------
..

Objects
-------

.. i18n: Object: Asset category (account.asset.category)
.. i18n: ###############################################
..

Object: Asset category (account.asset.category)
###############################################

.. i18n: :note: Note, text
..

:note: Note, text

.. i18n: :code: Asset code, char
..

:code: Asset code, char

.. i18n: :name: Asset category, char, required
..

:name: Asset category, char, required

.. i18n: Object: Asset (account.asset.asset)
.. i18n: ###################################
..

Object: Asset (account.asset.asset)
###################################

.. i18n: :property_ids: Asset method name, one2many, readonly
..

:property_ids: Asset method name, one2many, readonly

.. i18n: :note: Note, text
..

:note: Note, text

.. i18n: :code: Asset code, char
..

:code: Asset code, char

.. i18n: :name: Asset, char, required
..

:name: Asset, char, required

.. i18n: :sequence: Sequence, integer
..

:sequence: Sequence, integer

.. i18n: :child_ids: Childs asset, one2many
..

:child_ids: Childs asset, one2many

.. i18n: :entry_ids: Entries, one2many, readonly
..

:entry_ids: Entries, one2many, readonly

.. i18n: :localisation: Localisation, char
..

:localisation: Localisation, char

.. i18n: :date: Date, date, required
..

:date: Date, date, required

.. i18n: :state: Global state, selection, required
..

:state: Global state, selection, required

.. i18n: :period_id: Period, many2one, required, readonly
..

:period_id: Period, many2one, required, readonly

.. i18n: :parent_id: Parent asset, many2one
..

:parent_id: Parent asset, many2one

.. i18n: :value_total: Total value, float, readonly
..

:value_total: Total value, float, readonly

.. i18n: :active: Active, boolean
..

:active: Active, boolean

.. i18n: :category_id: Asset category, many2one
..

:category_id: Asset category, many2one

.. i18n: :partner_id: Partner, many2one
..

:partner_id: Partner, many2one

.. i18n: Object: Asset property (account.asset.property)
.. i18n: ###############################################
..

Object: Asset property (account.asset.property)
###############################################

.. i18n: :asset_id: Asset, many2one, required
..

:asset_id: Asset, many2one, required

.. i18n: :board_ids: Asset board, one2many
..

:board_ids: Asset board, one2many

.. i18n: :entry_asset_ids: Asset Entries, many2many
..

:entry_asset_ids: Asset Entries, many2many

.. i18n: :history_ids: History, one2many, readonly
..

:history_ids: History, one2many, readonly

.. i18n: :method_progress_factor: Progressif factor, float, readonly
..

:method_progress_factor: Progressif factor, float, readonly

.. i18n: :method_end: Ending date, date
..

:method_end: Ending date, date

.. i18n: :account_asset_id: Asset account, many2one, required
..

:account_asset_id: Asset account, many2one, required

.. i18n: :journal_id: Journal, many2one, required
..

:journal_id: Journal, many2one, required

.. i18n: :method: Computation method, selection, required, readonly
..

:method: Computation method, selection, required, readonly

.. i18n: :journal_analytic_id: Analytic journal, many2one
..

:journal_analytic_id: Analytic journal, many2one

.. i18n: :date: Date created, date
..

:date: Date created, date

.. i18n: :method_time: Time method, selection, required, readonly
..

:method_time: Time method, selection, required, readonly

.. i18n: :state: State, selection, required
..

:state: State, selection, required

.. i18n: :method_period: Period per interval, integer, readonly
..

:method_period: Period per interval, integer, readonly

.. i18n: :value_residual: Residual value, float, readonly
..

:value_residual: Residual value, float, readonly

.. i18n: :value_total: Gross value, float, readonly
..

:value_total: Gross value, float, readonly

.. i18n: :account_analytic_id: Analytic account, many2one
..

:account_analytic_id: Analytic account, many2one

.. i18n: :account_actif_id: Depreciation account, many2one, required
..

:account_actif_id: Depreciation account, many2one, required

.. i18n: :type: Depr. method type, selection, required
..

:type: Depr. method type, selection, required

.. i18n: :method_delay: Number of interval, integer, readonly
..

:method_delay: Number of interval, integer, readonly

.. i18n: :name: Method name, char
..

:name: Method name, char

.. i18n: Object: Asset history (account.asset.property.history)
.. i18n: ######################################################
..

Object: Asset history (account.asset.property.history)
######################################################

.. i18n: :user_id: User, many2one, required
..

:user_id: User, many2one, required

.. i18n: :name: History name, char
..

:name: History name, char

.. i18n: :method_end: Ending date, date
..

:method_end: Ending date, date

.. i18n: :asset_property_id: Method, many2one, required
..

:asset_property_id: Method, many2one, required

.. i18n: :note: Note, text
..

:note: Note, text

.. i18n: :method_delay: Number of interval, integer
..

:method_delay: Number of interval, integer

.. i18n: :method_period: Period per interval, integer
..

:method_period: Period per interval, integer

.. i18n: :date: Date, date, required
..

:date: Date, date, required

.. i18n: Object: Asset board (account.asset.board)
.. i18n: #########################################
..

Object: Asset board (account.asset.board)
#########################################

.. i18n: :asset_id: Asset, many2one, required
..

:asset_id: Asset, many2one, required

.. i18n: :value_gross: Gross value, float, required
..

:value_gross: Gross value, float, required

.. i18n: :value_asset_cumul: Cumul. value, float, required
..

:value_asset_cumul: Cumul. value, float, required

.. i18n: :name: Asset name, char, required
..

:name: Asset name, char, required

.. i18n: :value_asset: Asset Value, float, required
..

:value_asset: Asset Value, float, required

.. i18n: :value_net: Net value, float, required
..

:value_net: Net value, float, required
