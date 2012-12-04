
.. module:: civil_engineering
    :synopsis: Civil Engineering 
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

    <div class="js-kit-rating" title="" permalink="" standalone="yes" path="/civil_engineering"></div>
    <script src="http://js-kit.com/ratings.js"></script>

Civil Engineering (*civil_engineering*)
=======================================
:Module: civil_engineering
:Name: Civil Engineering
:Version: 5.0.0.1
:Author: Zikzakmedia
:Directory: civil_engineering
:Web: www.zikzakmedia.com
:Official module: no
:Quality certified: no

Description
-----------

::

  Civil Engineering Works:
  
  * Adds a new menu to manage civil engineering works: Location, agents and other consultancies, work data, structure data and assignments to projects.
  
  * New entities for civil engineering works (all these entities have an hierarchical structure and a tree view, civil engineering works can be filtered from the tree view):
      * Work Class
      * Work Use
      * Structure Type
      * Foundation Type
      * Structural Model Abstraction
      * Structural Modeling Software. 
  
  * Adds a new tab in the project, sale, and purchase forms to relate these objects to civil engineering works

Download links
--------------

You can download this module as a zip file in the following version:

(No download links available)


Dependencies
------------

 * :mod:`base`
 * :mod:`project`
 * :mod:`sale`
 * :mod:`purchase`

Reports
-------

None


Menus
-------

 * Civil Engineering
 * Civil Engineering/Configuration
 * Civil Engineering/Configuration/Categories
 * Civil Engineering/Configuration/Categories/Work Classes
 * Civil Engineering/Configuration/Categories/Work Uses
 * Civil Engineering/Configuration/Structure
 * Civil Engineering/Configuration/Structure/Structure Types
 * Civil Engineering/Configuration/Structure/Foundation Types
 * Civil Engineering/Configuration/Structure/Structural Model Abstractions
 * Civil Engineering/Configuration/Structure/Structural Modeling Software
 * Civil Engineering/Configuration/Civil Engineering Areas
 * Civil Engineering/Civil Engineering Works
 * Civil Engineering/Civil Engineering Works/Works by Work Class
 * Civil Engineering/Civil Engineering Works/Works by Work Use
 * Civil Engineering/Civil Engineering Works/Structure
 * Civil Engineering/Civil Engineering Works/Structure/Works by Structure Type
 * Civil Engineering/Civil Engineering Works/Structure/Works by Foundation Type
 * Civil Engineering/Civil Engineering Works/Structure/Works by Model Abstraction
 * Civil Engineering/Civil Engineering Works/Structure/Works by Modeling Software
 * Civil Engineering/Work Project Assignments

Views
-----

 * civil_engineering.work.form (form)
 * civil_engineering.work.tree (tree)
 * civil_engineering.area.form (form)
 * civil_engineering.area.tree (tree)
 * civil_engineering.work.project.form (form)
 * civil_engineering.work.project.tree (tree)
 * civil_engineering.civil_engineering.workclassform (form)
 * civil_engineering.civil_engineering.workclass.list (tree)
 * civil_engineering.civil_engineering.workclass.tree (tree)
 * civil_engineering.civil_engineering.workuseform (form)
 * civil_engineering.civil_engineering.workuse.list (tree)
 * civil_engineering.civil_engineering.workuse.tree (tree)
 * civil_engineering.civil_engineering.structuretypeform (form)
 * civil_engineering.civil_engineering.structuretype.list (tree)
 * civil_engineering.civil_engineering.structuretype.tree (tree)
 * civil_engineering.civil_engineering.foundationtypeform (form)
 * civil_engineering.civil_engineering.foundationtype.list (tree)
 * civil_engineering.civil_engineering.foundationtype.tree (tree)
 * civil_engineering.civil_engineering.modelabstractionform (form)
 * civil_engineering.civil_engineering.modelabstraction.list (tree)
 * civil_engineering.civil_engineering.modelabstraction.tree (tree)
 * civil_engineering.civil_engineering.modelingsoftwareform (form)
 * civil_engineering.civil_engineering.modelingsoftware.list (tree)
 * civil_engineering.civil_engineering.modelingsoftware.tree (tree)
 * \* INHERIT sale.order.form.civilengineering (form)
 * \* INHERIT purchase.order.form.civilengineering (form)
 * \* INHERIT project.project.form.civilengineering (form)


Objects
-------

Object: Civil Engineering Work Class (civil_engineering.workclass)
##################################################################



:active: Active, boolean

    *The active field allows you to hide the work class without removing it.*



:parent_id: Parent Work Class, many2one





:child_ids: Child Work Class, one2many





:complete_name: Full Name, char, readonly





:name: Name, char




Object: Civil Engineering Work Use (civil_engineering.workuse)
##############################################################



:active: Active, boolean

    *The active field allows you to hide the Work Use without removing it.*



:parent_id: Parent Work Use, many2one





:child_ids: Child Work Use, one2many





:complete_name: Full Name, char, readonly





:name: Name, char




Object: Civil Engineering Structure Type (civil_engineering.structuretype)
##########################################################################



:active: Active, boolean

    *The active field allows you to hide the Structure Type without removing it.*



:parent_id: Parent Structure Type, many2one





:child_ids: Child Structure Type, one2many





:complete_name: Full Name, char, readonly





:name: Name, char




Object: Civil Engineering Foundation Type (civil_engineering.foundationtype)
############################################################################



:active: Active, boolean

    *The active field allows you to hide the Foundation Type without removing it.*



:parent_id: Parent Foundation Type, many2one





:child_ids: Child Foundation Type, one2many





:complete_name: Full Name, char, readonly





:name: Name, char




Object: Civil Engineering Model Structural (civil_engineering.modelabstraction)
###############################################################################



:active: Active, boolean

    *The active field allows you to hide the Structural Model Abstraction without removing it.*



:parent_id: Parent Structural Model Abstraction, many2one





:child_ids: Child Structural Model Abstraction, one2many





:complete_name: Full Name, char, readonly





:name: Name, char




Object: Civil Engineering Modeling Software (civil_engineering.modelingsoftware)
################################################################################



:active: Active, boolean

    *The active field allows you to hide the Modeling Software without removing it.*



:parent_id: Parent Modeling Software, many2one





:child_ids: Child Modeling Software, one2many





:complete_name: Full Name, char, readonly





:name: Name, char




Object: Civil Engineering Area (civil_engineering.area)
#######################################################



:name: Name, char, required




Object: Civil Engineering Work (civil_engineering.work)
#######################################################



:floors_above_ground_level: Floors above ground level, integer





:structuretype_id: Structure Type, many2one





:workclass_id: Work Class, many2one, required





:workuse_id: Work Use, many2one, required





:work_builder: Work builder, many2one





:project_manager: Project manager, many2one





:civil_engineer: Civil engineer, many2one





:modelabstraction_id: Structural Model Abstraction, many2one





:geotechnics: Geotechnics, many2one





:constructed_area: Constructed area, float





:city: City, char





:project_ids: Project, one2many





:country_id: Country, many2one





:foundationtype_id: Foundation Type, many2one





:location: Location, char





:work_safety: Work safety, many2one





:structure_construction_cost: Structure construction cost, float





:work_owner: Work owner, many2one





:floors_under_ground_level: Floors under ground level, integer





:work_construction_cost: Work construction cost, float





:plant_engineering: Plant engineering, many2one





:modelingsoftware_id: Structure Modeling Software, many2one





:main_city: Main city, char





:name: Work description, char, required





:structural_engineering: Structural engineering, many2one





:architecture: Architecture, many2one





:state_id: State, many2one





:distance_between_supports: Distance between supports, float




Object: Civil Engineering Work Project (civil_engineering.work.project)
#######################################################################



:area_id: Area, many2one, required





:project_id: Project, many2one, required





:work_id: Work, many2one, required





:sequence: Sequence, integer


