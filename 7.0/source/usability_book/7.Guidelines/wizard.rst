=====================
Configuration wizards
=====================

A common layout for all wizards
-------------------------------

* Adapted title to each application : as introduced, chosen application leads to one configuration wizard. Then the configuration wizard  has to have a title related to the application. 
* Picture and information on the left : all wizards have to have one business picture and an explanation text regarding the business application to configure.  
* Objects (Documents) to configure on the right : all objects related to the application must be chosen with selection box. And have to be placed on the right
* Allow user to Skip or Configure : each wizard has to have 2 buttons, one to Skip and one to configure. These buttons have to be placed below on the right. 
* Progress bar : to allow user see where he is in configuration, all wizards have to have a progress bar with the percentage of completion of database. Separators : Each parts of the wizard has to be separated by a separator bar 


Configuration wizards are optional
-----------------------------------

Configuration wizards are optional. The system must be usable and configured by default even if the administrator skips all steps during the configuration process. Configuration wizards are available only to:

1. Propose new features to install (a set of modules)
2. Change the default configuration of the system (and not configure the system !)

Configuration wizards are part of the applications
--------------------------------------------------

Most of the application wizards must be part of one application. Be sure that:

* The application this configuration wizard belongs to is explicit
* Terminology are dedicated to the application context. As an example, in a project management application, don't talk about analytic account or entries but talk about projects and timesheets. Avoid configuration wizards that are related to several applications.

Configuration wizards and extended/simplified views
---------------------------------------------------

Be sure you use extended/simplified views features also in configuration wizards. In order to simplify the configuration process, some options or wizards must be available in extended views only.
