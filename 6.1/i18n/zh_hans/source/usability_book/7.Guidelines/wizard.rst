.. i18n: =====================
.. i18n: Configuration wizards
.. i18n: =====================
..

=====================
配置向导
=====================

.. i18n: A common layout for all wizards
.. i18n: -------------------------------
..

普通向导布局
-------------------------------

.. i18n: * Adapted title to each application : as introduced, chosen application leads to one configuration wizard. The configuration wizard must have a title related to the application. 
.. i18n: * Picture and information on the left : all wizards must have one business picture and an explanation text regarding the business application to configure.  
.. i18n: * Objects (Documents) to configure on the right : all objects related to the application must be chosen with selection box. Must be placed on the right.
.. i18n: * Allow user to Skip or Configure : Each wizard must have 2 buttons, one to Skip and one to configure. These buttons must be placed on the bottom right. 
.. i18n: * Progress bar : to allow user see where he is in configuration, all wizards have to have a progress bar with the percentage of completion of database.
.. i18n: * Separators : Each part of the wizard must be separated by a separator bar 
..

* 标题要符合应用套件内容：正如之前介绍，选择安装应用之后就会有一个配置向导。该配置向导的标题必须与应用套件相关。
* Picture and information on the left : all wizards must have one business picture and an explanation text regarding the business application to configure.  
* Objects (Documents) to configure on the right : all objects related to the application must be chosen with selection box. Must be placed on the right.
* Allow user to Skip or Configure : Each wizard must have 2 buttons, one to Skip and one to configure. These buttons must be placed on the bottom right. 
* Progress bar : to allow user see where he is in configuration, all wizards have to have a progress bar with the percentage of completion of database.
* Separators : Each part of the wizard must be separated by a separator bar 

.. i18n: Configuration wizards are optional
.. i18n: -----------------------------------
..

可选的配置向导
-----------------------------------

.. i18n: Configuration wizards are optional. The system must be usable and configured by default even if the administrator skips all steps during the configuration process. Configuration wizards are available only to:
..

Configuration wizards are optional. The system must be usable and configured by default even if the administrator skips all steps during the configuration process. Configuration wizards are available only to:

.. i18n: 1. Propose new features to install (a set of modules)
.. i18n: 2. Change the default configuration of the system (and not configure the system !)
..

1. Propose new features to install (a set of modules)
2. Change the default configuration of the system (and not configure the system !)

.. i18n: Configuration wizards are part of the applications
.. i18n: --------------------------------------------------
..

配置向导为应用的一部分
--------------------------------------------------

.. i18n: Most of the application wizards must be part of one application. Be sure that:
..

Most of the application wizards must be part of one application. Be sure that:

.. i18n: * The application this configuration wizard belongs to is explicit
.. i18n: * Terminology are dedicated to the application context. As an example, in a project management application, don't talk about analytic account or entries but talk about projects and timesheets. Avoid configuration wizards that are related to several applications.
..

* The application this configuration wizard belongs to is explicit
* Terminology are dedicated to the application context. As an example, in a project management application, don't talk about analytic account or entries but talk about projects and timesheets. Avoid configuration wizards that are related to several applications.

.. i18n: Configuration wizards and extended/simplified views
.. i18n: ---------------------------------------------------
..

配置向导与扩展/简单试图
---------------------------------------------------

.. i18n: Be sure you use extended/simplified views features also in configuration wizards. In order to simplify the configuration process, some options or wizards must be available in extended views only.
..

Be sure you use extended/simplified views features also in configuration wizards. In order to simplify the configuration process, some options or wizards must be available in extended views only.
