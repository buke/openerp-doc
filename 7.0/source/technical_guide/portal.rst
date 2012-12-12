
.. module:: portal
    :synopsis: Portal Management 
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

    <div class="js-kit-rating" title="" permalink="" standalone="yes" path="/portal"></div>
    <script src="http://js-kit.com/ratings.js"></script>

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

Description
-----------

::

  Base module to manage portal:
      - define new menu entry with associated actions.
      - add/delete menu entry easily.
      - on-the-fly rules and access control creation.

Download links
--------------

You can download this module as a zip file in the following version:

  * `5.0 <http://www.openerp.com/download/modules/5.0/portal.zip>`_
  * `trunk <http://www.openerp.com/download/modules/trunk/portal.zip>`_


Dependencies
------------

 * :mod:`base`

Reports
-------

None


Menus
-------

 * Portal
 * Portal/Configuration
 * Portal/Customer Portal
 * Portal/Configuration/Portals
 * Portal/Configuration/Available Models
 * Portal/Configuration/Create Menu

Views
-----

 * Portal (form)
 * Portal (tree)
 * Portal Model (form)
 * \* INHERIT ir.actions.report.custom.form.inherit (form)
 * \* INHERIT ir.actions.report_xml.form.inherit (form)
 * \* INHERIT ir.actions.wizards.form.inherit (form)
 * \* INHERIT ir.actions.windows.form.inherit (form)
 * Portal : Install extra modules (form)


Objects
-------

Object: Portal (portal.portal)
##############################



:menu_id: Main Menu, many2one, required





:menu_action_id: User Menu Action, many2one, readonly

    *Default main menu for the users of the portal. This field is auto-completed at creation.*



:name: Portal Name, char, required





:company_id: Company, many2one, required





:home_action_id: User Home Action, many2one

    *Complete this field to provide a Home menu different from the Main menu.*



:group_id: Associated Group, many2one, required




Object: Portal Model (portal.model)
###################################



:model_id: Model, many2one, required





:rule_group_id: Rule group, many2one





:view_ids: Views, many2many





:name: Name, char




Object: portal.config.install_modules_wizard (portal.config.install_modules_wizard)
###################################################################################



:portal_service: Portal for Service Module, boolean





:portal_sale: Portal for Sale Module, boolean





:portal_account: Portal for Account Module, boolean





:portal_analytic: Portal for Analytic Account Module, boolean


