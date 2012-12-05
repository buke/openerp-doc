
.. i18n: .. module:: portal
.. i18n:     :synopsis: Portal Management 
.. i18n:     :noindex:
.. i18n: .. 
..

.. module:: portal
    :synopsis: Portal Management 
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
.. i18n:     <div class="js-kit-rating" title="" permalink="" standalone="yes" path="/portal"></div>
.. i18n:     <script src="http://js-kit.com/ratings.js"></script>
..

.. raw:: html

    <div class="js-kit-rating" title="" permalink="" standalone="yes" path="/portal"></div>
    <script src="http://js-kit.com/ratings.js"></script>

.. i18n: Portal Management (*portal*)
.. i18n: ============================
.. i18n: :Module: portal
.. i18n: :Name: Portal Management
.. i18n: :Version: 5.0.0.1
.. i18n: :Author: Tiny
.. i18n: :Directory: portal
.. i18n: :Web: http://www.openerp.com
.. i18n: :Official module: no
.. i18n: :Quality certified: no
..

Portal Management (*portal*)
============================
:Module: portal
:Name: Portal Management
:Version: 5.0.0.1
:Author: Tiny
:Directory: portal
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
.. i18n:   Base module to manage portal:
.. i18n:       - define new menu entry with associated actions.
.. i18n:       - add/delete menu entry easily.
.. i18n:       - on-the-fly rules and access control creation.
..

::

  Base module to manage portal:
      - define new menu entry with associated actions.
      - add/delete menu entry easily.
      - on-the-fly rules and access control creation.

.. i18n: Download links
.. i18n: --------------
..

Download links
--------------

.. i18n: You can download this module as a zip file in the following version:
..

You can download this module as a zip file in the following version:

.. i18n:   * `5.0 <http://www.openerp.com/download/modules/5.0/portal.zip>`_
.. i18n:   * `trunk <http://www.openerp.com/download/modules/trunk/portal.zip>`_
..

  * `5.0 <http://www.openerp.com/download/modules/5.0/portal.zip>`_
  * `trunk <http://www.openerp.com/download/modules/trunk/portal.zip>`_

.. i18n: Dependencies
.. i18n: ------------
..

Dependencies
------------

.. i18n:  * :mod:`base`
..

 * :mod:`base`

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

.. i18n:  * Portal
.. i18n:  * Portal/Configuration
.. i18n:  * Portal/Customer Portal
.. i18n:  * Portal/Configuration/Portals
.. i18n:  * Portal/Configuration/Available Models
.. i18n:  * Portal/Configuration/Create Menu
..

 * Portal
 * Portal/Configuration
 * Portal/Customer Portal
 * Portal/Configuration/Portals
 * Portal/Configuration/Available Models
 * Portal/Configuration/Create Menu

.. i18n: Views
.. i18n: -----
..

Views
-----

.. i18n:  * Portal (form)
.. i18n:  * Portal (tree)
.. i18n:  * Portal Model (form)
.. i18n:  * \* INHERIT ir.actions.report.custom.form.inherit (form)
.. i18n:  * \* INHERIT ir.actions.report_xml.form.inherit (form)
.. i18n:  * \* INHERIT ir.actions.wizards.form.inherit (form)
.. i18n:  * \* INHERIT ir.actions.windows.form.inherit (form)
.. i18n:  * Portal : Install extra modules (form)
..

 * Portal (form)
 * Portal (tree)
 * Portal Model (form)
 * \* INHERIT ir.actions.report.custom.form.inherit (form)
 * \* INHERIT ir.actions.report_xml.form.inherit (form)
 * \* INHERIT ir.actions.wizards.form.inherit (form)
 * \* INHERIT ir.actions.windows.form.inherit (form)
 * Portal : Install extra modules (form)

.. i18n: Objects
.. i18n: -------
..

Objects
-------

.. i18n: Object: Portal (portal.portal)
.. i18n: ##############################
..

Object: Portal (portal.portal)
##############################

.. i18n: :menu_id: Main Menu, many2one, required
..

:menu_id: Main Menu, many2one, required

.. i18n: :menu_action_id: User Menu Action, many2one, readonly
..

:menu_action_id: User Menu Action, many2one, readonly

.. i18n:     *Default main menu for the users of the portal. This field is auto-completed at creation.*
..

    *Default main menu for the users of the portal. This field is auto-completed at creation.*

.. i18n: :name: Portal Name, char, required
..

:name: Portal Name, char, required

.. i18n: :company_id: Company, many2one, required
..

:company_id: Company, many2one, required

.. i18n: :home_action_id: User Home Action, many2one
..

:home_action_id: User Home Action, many2one

.. i18n:     *Complete this field to provide a Home menu different from the Main menu.*
..

    *Complete this field to provide a Home menu different from the Main menu.*

.. i18n: :group_id: Associated Group, many2one, required
..

:group_id: Associated Group, many2one, required

.. i18n: Object: Portal Model (portal.model)
.. i18n: ###################################
..

Object: Portal Model (portal.model)
###################################

.. i18n: :model_id: Model, many2one, required
..

:model_id: Model, many2one, required

.. i18n: :rule_group_id: Rule group, many2one
..

:rule_group_id: Rule group, many2one

.. i18n: :view_ids: Views, many2many
..

:view_ids: Views, many2many

.. i18n: :name: Name, char
..

:name: Name, char

.. i18n: Object: portal.config.install_modules_wizard (portal.config.install_modules_wizard)
.. i18n: ###################################################################################
..

Object: portal.config.install_modules_wizard (portal.config.install_modules_wizard)
###################################################################################

.. i18n: :portal_service: Portal for Service Module, boolean
..

:portal_service: Portal for Service Module, boolean

.. i18n: :portal_sale: Portal for Sale Module, boolean
..

:portal_sale: Portal for Sale Module, boolean

.. i18n: :portal_account: Portal for Account Module, boolean
..

:portal_account: Portal for Account Module, boolean

.. i18n: :portal_analytic: Portal for Analytic Account Module, boolean
..

:portal_analytic: Portal for Analytic Account Module, boolean
