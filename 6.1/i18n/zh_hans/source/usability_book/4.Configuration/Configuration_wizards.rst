.. i18n: =====================================
.. i18n: Configuration Wizards Functionality
.. i18n: =====================================
..

=====================================
配置向导功能
=====================================

.. i18n: Configuration wizards are launched automatically on creation of a new database. You must develop configuration wizards per application to:
..

配置向导会在创建新数据库后自动启动。你需要为每个应用套件开发配置向导：

.. i18n: 	1. Help the user decide which features (modules) to install
.. i18n: 	
.. i18n: 	2. Help the user configure the system
..

	1. 让用户选择安装哪些功能（模块）
	
	2. 帮助用户配置系统

.. i18n: For the point (1), fewer user-installed modules make it easier to understand the system. So, most features are proposed as extra in the configuration wizards.
..

第一点中，让用户选择越少越容易理解系统。因此，大部分功能在配置向导中都是属于额外选项。

.. i18n: For the point (2), where possible, it's better to provide a default configuration that works for most companies instead of developing a configuration wizard.
..

第二点中，对大多数企业，最好是提供一个默认的配置，而不是开发一个配置向导。

.. i18n: Don't forget that configuration wizards are to help users tailor the system to their requirements, not to ask complex questions for very specific configurations.
..

切记配置向导的作用是让用户按需定制系统，而不是问用户一些非常技术化、复杂的问题去配置系统。

.. i18n: OpenERP allows users to configure their installation to their business's needs. When a user creates a database they can choose one or more applications. They will then see some configuration wizards to add modules related to the chosen application(s) and so, their needs.  For example, if the user has chosen “Project” they will see a wizard to configure Project Management.
..

OpenERP 允许用户按照业务需求配置安装。当用户创建完数据库之后，就可以选择一个或多个业务套件。
然后就可以看到相关的配置向导。比如，如果用户选择“项目管理” ，然后就会看到一个关于项目管理的配置向导。

.. i18n: .. figure:: Pictures/2.1.Project_management.png
.. i18n:    :align: center
..

.. figure:: Pictures/2.1.Project_management.png
   :align: center
