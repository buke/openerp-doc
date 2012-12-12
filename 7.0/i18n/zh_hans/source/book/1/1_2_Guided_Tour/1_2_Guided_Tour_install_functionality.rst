
.. i18n: .. index::
.. i18n:   single: module; new functionality
..

.. index::
  single: module; new functionality

.. i18n: Installing New Functionality
.. i18n: ============================
..

Installing New Functionality
============================

.. i18n: All of OpenERP's functionality is contained in its many and various modules. Many of these, the
.. i18n: core modules, are automatically loaded during the initial installation of the system and can be
.. i18n: updated online later. Although they are mostly not installed in your database at the outset, they are
.. i18n: available on your computer for immediate installation. Additional modules can also be loaded online
.. i18n: from the official OpenERP site http://openerp.com. These modules are inactive when they are loaded
.. i18n: into the system, and can then be installed in a separate step.
..

All of OpenERP's functionality is contained in its many and various modules. Many of these, the
core modules, are automatically loaded during the initial installation of the system and can be
updated online later. Although they are mostly not installed in your database at the outset, they are
available on your computer for immediate installation. Additional modules can also be loaded online
from the official OpenERP site http://openerp.com. These modules are inactive when they are loaded
into the system, and can then be installed in a separate step.

.. i18n: You will start by checking if there are any updates available online that apply to your initial
.. i18n: installation. Then you will install a CRM module to complete your existing database.
..

You will start by checking if there are any updates available online that apply to your initial
installation. Then you will install a CRM module to complete your existing database.

.. i18n: .. index::
.. i18n:   single: module; upgrading
..

.. index::
  single: module; upgrading

.. i18n: Updating the Modules list
.. i18n: -------------------------
..

Updating the Modules list
-------------------------

.. i18n: Click :menuselection:`Administration --> Modules --> Update Modules List` to start the
.. i18n: updating tool. The :guilabel:`Module Update` window opens notifying the user that
.. i18n: OpenERP will look at the server side for adding new modules and updating
.. i18n: existing ones.
..

Click :menuselection:`Administration --> Modules --> Update Modules List` to start the
updating tool. The :guilabel:`Module Update` window opens notifying the user that
OpenERP will look at the server side for adding new modules and updating
existing ones.

.. i18n: Click :guilabel:`Update` to start the update on the server side. When it is
.. i18n: complete, you will see a :guilabel:`Module update result` section indicating how many new modules were added
.. i18n: and how many existing modules were updated. Click :guilabel:`Open Modules` to return to the updated list.
..

Click :guilabel:`Update` to start the update on the server side. When it is
complete, you will see a :guilabel:`Module update result` section indicating how many new modules were added
and how many existing modules were updated. Click :guilabel:`Open Modules` to return to the updated list.

.. i18n: .. note:: Modules
.. i18n: 
.. i18n: 	All the modules available on your computer can be found in the addons directory of your OpenERP
.. i18n: 	server. Each module there is represented by a directory carrying the name of the module or by a
.. i18n: 	file with the module name and .zip appended to it. The file is in ZIP archive format and replicates
.. i18n: 	the directory structure of unzipped modules.
..

.. note:: Modules

	All the modules available on your computer can be found in the addons directory of your OpenERP
	server. Each module there is represented by a directory carrying the name of the module or by a
	file with the module name and .zip appended to it. The file is in ZIP archive format and replicates
	the directory structure of unzipped modules.

.. i18n: .. tip:: Searching through the whole list
.. i18n: 
.. i18n: 	The list of modules shows only the first available modules. In the web client you can search or
.. i18n: 	follow the First / Previous / Next / Last links to get to any point in the whole list, and you can
.. i18n: 	change the number of entries listed by clicking the row number indicators between :guilabel:`Previous` 
.. i18n: 	and :guilabel:`Next`
.. i18n: 	and selecting a different number from the default of 20.
.. i18n: 
.. i18n: 	If you use the GTK client you can search, as you would with the web client, or use the selection field
.. i18n: 	(currently showing 80) to
.. i18n: 	the top right of the window to change the number of entries returned by the search from its default
.. i18n: 	limit of 80, or its default offset of 0 (starting at the first entry) in the whole list.
..

.. tip:: Searching through the whole list

	The list of modules shows only the first available modules. In the web client you can search or
	follow the First / Previous / Next / Last links to get to any point in the whole list, and you can
	change the number of entries listed by clicking the row number indicators between :guilabel:`Previous` 
	and :guilabel:`Next`
	and selecting a different number from the default of 20.

	If you use the GTK client you can search, as you would with the web client, or use the selection field
	(currently showing 80) to
	the top right of the window to change the number of entries returned by the search from its default
	limit of 80, or its default offset of 0 (starting at the first entry) in the whole list.

.. i18n: .. index::
.. i18n:   single: module; installing
..

.. index::
  single: module; installing

.. i18n: The Configuration / Reconfigure Wizard
.. i18n: --------------------------------------
..

The Configuration / Reconfigure Wizard
--------------------------------------

.. i18n: One of the new features of OpenERP is the :guilabel:`Configuration` wizard. Once run, the :guilabel:`Reconfigure` shortcut will appear. This wizard provides an easy way to install modules, thanks to its user-friendly and easy-to-use interface. The user may invoke this wizard at his own convenience using the shortcut :guilabel:`Reconfigure`, found just below the database and user name in the web-client or in the Shortcut menu in the GTK client. The same Configuration dialog box appears that you may have encountered at the time of installing a new database. Why did we call it the :guilabel:`Reconfigure` wizard? Indeed, because it allows the user to review installed applications and install related additional features or simply to install new applications on the fly.
..

One of the new features of OpenERP is the :guilabel:`Configuration` wizard. Once run, the :guilabel:`Reconfigure` shortcut will appear. This wizard provides an easy way to install modules, thanks to its user-friendly and easy-to-use interface. The user may invoke this wizard at his own convenience using the shortcut :guilabel:`Reconfigure`, found just below the database and user name in the web-client or in the Shortcut menu in the GTK client. The same Configuration dialog box appears that you may have encountered at the time of installing a new database. Why did we call it the :guilabel:`Reconfigure` wizard? Indeed, because it allows the user to review installed applications and install related additional features or simply to install new applications on the fly.

.. i18n: When you go through the various steps in the wizard, you will come across some options that are checked and greyed. These are applications already installed. In the \ ``openerp_ch02`` \ database configuration, you may see that the \ ``Customer Relationship Management`` \ option is already checked because this Business Application has been installed in this database.
.. i18n: Install extra applications simply by checking the corresponding options and clicking :guilabel:`Install` or click :guilabel:`Skip` to stop the configuration. You will eventually also come across the :guilabel:`CRM Application Configuration` step which you may use to add features to your CRM application. For now, select the \ ``Claims`` \ option and click :guilabel:`Configure`. This will in turn install the :mod:`crm_claim` module.
..

When you go through the various steps in the wizard, you will come across some options that are checked and greyed. These are applications already installed. In the \ ``openerp_ch02`` \ database configuration, you may see that the \ ``Customer Relationship Management`` \ option is already checked because this Business Application has been installed in this database.
Install extra applications simply by checking the corresponding options and clicking :guilabel:`Install` or click :guilabel:`Skip` to stop the configuration. You will eventually also come across the :guilabel:`CRM Application Configuration` step which you may use to add features to your CRM application. For now, select the \ ``Claims`` \ option and click :guilabel:`Configure`. This will in turn install the :mod:`crm_claim` module.

.. i18n: .. figure:: images/reconfigure_wizard.png
.. i18n:    :scale: 75
.. i18n:    :align: center
.. i18n: 
.. i18n:    *Reconfigure wizard showing Customer Relationship Management application as installed*
..

.. figure:: images/reconfigure_wizard.png
   :scale: 75
   :align: center

   *Reconfigure wizard showing Customer Relationship Management application as installed*

.. i18n: You may continue adding features this way, skip configuration steps or simply exit from this wizard. When you feel the need to
.. i18n: load your system with additional features, you may invoke the :guilabel:`Reconfigure` wizard again at any point.
..

You may continue adding features this way, skip configuration steps or simply exit from this wizard. When you feel the need to
load your system with additional features, you may invoke the :guilabel:`Reconfigure` wizard again at any point.

.. i18n: .. note:: You can also change the Configuration Wizard through the :menuselection:`Administration --> Configuration --> Configuration Wizards --> Configuration Wizards`.
..

.. note:: You can also change the Configuration Wizard through the :menuselection:`Administration --> Configuration --> Configuration Wizards --> Configuration Wizards`.

.. i18n: Installing an Application / Module from the Modules list
.. i18n: --------------------------------------------------------
..

Installing an Application / Module from the Modules list
--------------------------------------------------------

.. i18n: .. index::
.. i18n:    single: module; google maps
..

.. index::
   single: module; google maps

.. i18n: You will now install a module named :mod:`google_map`, which will enable you to add a feature to the partner form to open the location directly in Google Maps. This is part of the core installation, so you do not need to load anything to make this work.
..

You will now install a module named :mod:`google_map`, which will enable you to add a feature to the partner form to open the location directly in Google Maps. This is part of the core installation, so you do not need to load anything to make this work.

.. i18n: Open the list of modules from :menuselection:`Administration --> Modules --> Modules`. Search for the module by entering the name :mod:`google_map` in the :guilabel:`Name` field on the search screen then clicking it in the list that appears to open it. The form that describes the module gives you useful information such as its version number, its status and a review of its
.. i18n: functionality. Click :guilabel:`Schedule for Installation` and the status of the module changes to :guilabel:`To be installed`.
..

Open the list of modules from :menuselection:`Administration --> Modules --> Modules`. Search for the module by entering the name :mod:`google_map` in the :guilabel:`Name` field on the search screen then clicking it in the list that appears to open it. The form that describes the module gives you useful information such as its version number, its status and a review of its
functionality. Click :guilabel:`Schedule for Installation` and the status of the module changes to :guilabel:`To be installed`.

.. i18n: .. tip:: From now on you can schedule and install modules from list view too. Notice the buttons on the right side and the action button to install.
..

.. tip:: From now on you can schedule and install modules from list view too. Notice the buttons on the right side and the action button to install.

.. i18n: .. figure:: images/install_google_map_module.png
.. i18n:    :scale: 75
.. i18n:    :align: center
.. i18n: 
.. i18n:    *Installation of the Google Maps module*
..

.. figure:: images/install_google_map_module.png
   :scale: 75
   :align: center

   *Installation of the Google Maps module*

.. i18n: .. tip::  Technical Guide
.. i18n: 
.. i18n: 	If you select a module in any of the module lists by clicking on a module line and then on
.. i18n: 	:guilabel:`Technical Guide` at the top right of the window, OpenERP produces a technical report
.. i18n: 	on that module. It is helpful only if the module is installed.
.. i18n: 
.. i18n: 	This report comprises a list of all the objects and all the fields along with their descriptions.
.. i18n: 	The report adapts to your system and reflects any modifications you have made and all the other
.. i18n: 	modules you have installed.
..

.. tip::  Technical Guide

	If you select a module in any of the module lists by clicking on a module line and then on
	:guilabel:`Technical Guide` at the top right of the window, OpenERP produces a technical report
	on that module. It is helpful only if the module is installed.

	This report comprises a list of all the objects and all the fields along with their descriptions.
	The report adapts to your system and reflects any modifications you have made and all the other
	modules you have installed.

.. i18n: Then, either use the menu :menuselection:`Administration --> Modules --> Apply Scheduled Upgrades`, or from the :guilabel:`Actions` section click :guilabel:`Apply Scheduled Upgrades`, then :guilabel:`Start update` on the :guilabel:`Module Upgrade`
.. i18n: form that appears. Close the window when the operation has completed. Return to the :guilabel:`Sales` menu; you will
.. i18n: see the new menu :menuselection:`Products` has become available.
..

Then, either use the menu :menuselection:`Administration --> Modules --> Apply Scheduled Upgrades`, or from the :guilabel:`Actions` section click :guilabel:`Apply Scheduled Upgrades`, then :guilabel:`Start update` on the :guilabel:`Module Upgrade`
form that appears. Close the window when the operation has completed. Return to the :guilabel:`Sales` menu; you will
see the new menu :menuselection:`Products` has become available.

.. i18n: .. tip::  Refreshing the menu in the GTK Client
.. i18n: 
.. i18n: 	After an update in the GTK client you will have to open a new menu to refresh the content –
.. i18n: 	otherwise you will not see the new menu item. To do that, use the window menu :menuselection:`Form -->
.. i18n: 	Reload / Undo` or use the shortcut :kbd:`Ctrl+R`.
..

.. tip::  Refreshing the menu in the GTK Client

	After an update in the GTK client you will have to open a new menu to refresh the content –
	otherwise you will not see the new menu item. To do that, use the window menu :menuselection:`Form -->
	Reload / Undo` or use the shortcut :kbd:`Ctrl+R`.

.. i18n: Installing a Module with its Dependencies
.. i18n: -----------------------------------------
..

Installing a Module with its Dependencies
-----------------------------------------

.. i18n: .. index::
.. i18n:    single: module; stock
..

.. index::
   single: module; stock

.. i18n: Now install the Warehouse Management module using the same process as before.
.. i18n: Start from :menuselection:`Administration --> Modules --> Modules`.
..

Now install the Warehouse Management module using the same process as before.
Start from :menuselection:`Administration --> Modules --> Modules`.

.. i18n: 	#.  Get the list of modules, and search for the :mod:`stock` module in that list.
.. i18n: 	
.. i18n: 	#.  Schedule the module for installation by clicking :guilabel:`Schedule for Installation`.
.. i18n: 	
.. i18n: 	#.  Do the same for :mod:`account`. 
.. i18n: 	
.. i18n: 	#.  Click :guilabel:`Apply Scheduled Upgrades` on the action toolbar to the right.
.. i18n: 
.. i18n: 	#.  Click :guilabel:`Start update` to install both modules. 
.. i18n: 	
.. i18n: 	#.  After a few seconds, when the installation is complete, you may close this dialog box.
.. i18n: 	
.. i18n: 	#.  You will see details of all the features installed by the modules on a new
.. i18n: 	    :guilabel:`Features` tab on the module form. 
..

	#.  Get the list of modules, and search for the :mod:`stock` module in that list.
	
	#.  Schedule the module for installation by clicking :guilabel:`Schedule for Installation`.
	
	#.  Do the same for :mod:`account`. 
	
	#.  Click :guilabel:`Apply Scheduled Upgrades` on the action toolbar to the right.

	#.  Click :guilabel:`Start update` to install both modules. 
	
	#.  After a few seconds, when the installation is complete, you may close this dialog box.
	
	#.  You will see details of all the features installed by the modules on a new
	    :guilabel:`Features` tab on the module form. 

.. i18n: When you return to the :menuselection:`Warehouse` menu, you will find the new menu items under it like
.. i18n: :menuselection:`Warehouse --> Warehouse Management --> Incoming Shipments`, :menuselection:`Warehouse --> Products Moves`,  which are a part of the Warehouse management system. You will also see all the accounting functions that are now available in the :menuselection:`Accounting` menu.
..

When you return to the :menuselection:`Warehouse` menu, you will find the new menu items under it like
:menuselection:`Warehouse --> Warehouse Management --> Incoming Shipments`, :menuselection:`Warehouse --> Products Moves`,  which are a part of the Warehouse management system. You will also see all the accounting functions that are now available in the :menuselection:`Accounting` menu.

.. i18n: There is no particular relationship between the modules installed and the menus added. Most of the
.. i18n: core modules add complete menus but some also add sub-menus to menus already in the system. Other
.. i18n: modules add menus and sub-menus as they need. Modules can also add additional fields to existing
.. i18n: forms, or simply additional demonstration data or some settings specific to a given requirement.
..

There is no particular relationship between the modules installed and the menus added. Most of the
core modules add complete menus but some also add sub-menus to menus already in the system. Other
modules add menus and sub-menus as they need. Modules can also add additional fields to existing
forms, or simply additional demonstration data or some settings specific to a given requirement.

.. i18n: .. index::
.. i18n:   single: module; dependencies
.. i18n: ..
..

.. index::
  single: module; dependencies
..

.. i18n: .. note::  Dependencies Between Modules
.. i18n: 
.. i18n: 	The module form shows two tabs before it is installed. 
.. i18n: 	The first tab gives basic information about the module, and the
.. i18n: 	second gives a list of modules that this module depends on. So when you install a module, OpenERP
.. i18n: 	automatically selects all the necessary dependencies to install this module.
.. i18n: 
.. i18n: 	That is also how you develop the profile modules: they simply define a list of modules that you want
.. i18n: 	in your profile as a set of dependencies.
..

.. note::  Dependencies Between Modules

	The module form shows two tabs before it is installed. 
	The first tab gives basic information about the module, and the
	second gives a list of modules that this module depends on. So when you install a module, OpenERP
	automatically selects all the necessary dependencies to install this module.

	That is also how you develop the profile modules: they simply define a list of modules that you want
	in your profile as a set of dependencies.

.. i18n: Although you can install a module and all its dependencies at once, you cannot remove them in one
.. i18n: fell swoop – you would have to uninstall module by module. Uninstalling is more complex than
.. i18n: installing because you have to handle existing system data.
..

Although you can install a module and all its dependencies at once, you cannot remove them in one
fell swoop – you would have to uninstall module by module. Uninstalling is more complex than
installing because you have to handle existing system data.

.. i18n: .. note::  Uninstalling Modules
.. i18n: 
.. i18n: 	Although it works quite well, uninstalling modules is not perfect in OpenERP. It is not guaranteed
.. i18n: 	to return the system exactly to the state it was in before installation.
.. i18n: 
.. i18n: 	So it is recommended that you make a backup of the database before installing your new modules so
.. i18n: 	that you can test the new modules and decide whether they are suitable or not. If they are not, then
.. i18n: 	you can return to your backup. If they are, then you will probably still reinstall the modules on
.. i18n: 	your backup so that you do not have to delete all your test data.
.. i18n: 
.. i18n: 	If you wanted to uninstall, you would use the menu :menuselection:`Administration --> Modules
.. i18n: 	--> Modules` and then uninstall them in the inverse order of their
.. i18n: 	dependencies: ``stock``, ``account``.
..

.. note::  Uninstalling Modules

	Although it works quite well, uninstalling modules is not perfect in OpenERP. It is not guaranteed
	to return the system exactly to the state it was in before installation.

	So it is recommended that you make a backup of the database before installing your new modules so
	that you can test the new modules and decide whether they are suitable or not. If they are not, then
	you can return to your backup. If they are, then you will probably still reinstall the modules on
	your backup so that you do not have to delete all your test data.

	If you wanted to uninstall, you would use the menu :menuselection:`Administration --> Modules
	--> Modules` and then uninstall them in the inverse order of their
	dependencies: ``stock``, ``account``.

.. i18n: Installing Additional Functionality
.. i18n: -----------------------------------
..

Installing Additional Functionality
-----------------------------------

.. i18n: To discover the full range of OpenERP's possibilities, you can install many additional modules.
.. i18n: Installing them with their demonstration data provides a convenient way of exploring the whole core
.. i18n: system. When you build on the \ ``openerp_ch02``\   database, you will automatically include
.. i18n: demonstration data because you checked the :guilabel:`Load Demonstration Data` checkbox when you originally
.. i18n: created the database.
..

To discover the full range of OpenERP's possibilities, you can install many additional modules.
Installing them with their demonstration data provides a convenient way of exploring the whole core
system. When you build on the \ ``openerp_ch02``\   database, you will automatically include
demonstration data because you checked the :guilabel:`Load Demonstration Data` checkbox when you originally
created the database.

.. i18n: .. index::
.. i18n:    single: module; importing
.. i18n: ..
..

.. index::
   single: module; importing
..

.. i18n: Click :menuselection:`Administration --> Modules --> Modules` to give you an
.. i18n: overview of all of the modules available for installation.
..

Click :menuselection:`Administration --> Modules --> Modules` to give you an
overview of all of the modules available for installation.

.. i18n: To test several modules, you will not have to install them all one by one. You can use the dependencies
.. i18n: between modules to load several at once.
..

To test several modules, you will not have to install them all one by one. You can use the dependencies
between modules to load several at once.

.. i18n: .. Copyright © Open Object Press. All rights reserved.
..

.. Copyright © Open Object Press. All rights reserved.

.. i18n: .. You may take electronic copy of this publication and distribute it if you don't
.. i18n: .. change the content. You can also print a copy to be read by yourself only.
..

.. You may take electronic copy of this publication and distribute it if you don't
.. change the content. You can also print a copy to be read by yourself only.

.. i18n: .. We have contracts with different publishers in different countries to sell and
.. i18n: .. distribute paper or electronic based versions of this book (translated or not)
.. i18n: .. in bookstores. This helps to distribute and promote the OpenERP product. It
.. i18n: .. also helps us to create incentives to pay contributors and authors using author
.. i18n: .. rights of these sales.
..

.. We have contracts with different publishers in different countries to sell and
.. distribute paper or electronic based versions of this book (translated or not)
.. in bookstores. This helps to distribute and promote the OpenERP product. It
.. also helps us to create incentives to pay contributors and authors using author
.. rights of these sales.

.. i18n: .. Due to this, grants to translate, modify or sell this book are strictly
.. i18n: .. forbidden, unless Tiny SPRL (representing Open Object Press) gives you a
.. i18n: .. written authorisation for this.
..

.. Due to this, grants to translate, modify or sell this book are strictly
.. forbidden, unless Tiny SPRL (representing Open Object Press) gives you a
.. written authorisation for this.

.. i18n: .. Many of the designations used by manufacturers and suppliers to distinguish their
.. i18n: .. products are claimed as trademarks. Where those designations appear in this book,
.. i18n: .. and Open Object Press was aware of a trademark claim, the designations have been
.. i18n: .. printed in initial capitals.
..

.. Many of the designations used by manufacturers and suppliers to distinguish their
.. products are claimed as trademarks. Where those designations appear in this book,
.. and Open Object Press was aware of a trademark claim, the designations have been
.. printed in initial capitals.

.. i18n: .. While every precaution has been taken in the preparation of this book, the publisher
.. i18n: .. and the authors assume no responsibility for errors or omissions, or for damages
.. i18n: .. resulting from the use of the information contained herein.
..

.. While every precaution has been taken in the preparation of this book, the publisher
.. and the authors assume no responsibility for errors or omissions, or for damages
.. resulting from the use of the information contained herein.

.. i18n: .. Published by Open Object Press, Grand Rosière, Belgium
..

.. Published by Open Object Press, Grand Rosière, Belgium
