
=====================================
Configuration Wizards Functionality
=====================================

Configuration wizards are launched automatically on creation of a new database. You must develop configuration wizards per application to:

	1. Help the user decide which features (modules) to install
	
	2. Help the user configure the system

For the point (1), fewer user-installed modules make it easier to understand the system. So, most features are proposed as extra in the configuration wizards.

For the point (2), where possible, it's better to provide a default configuration that works for most companies instead of developing a configuration wizard.

Don't forget that configuration wizards are to help users tailor the system to their requirements, not to ask complex questions for very specific configurations.

OpenERP allows users to configure their installation to their business's needs. When a user creates a database they can choose one or more applications. They will then see some configuration wizards to add modules related to the chosen application(s) and so, their needs.  For example, if the user has chosen “Project” they will see a wizard to configure Project Management.

.. figure:: Pictures/2.1.Project_management.png
   :align: center


