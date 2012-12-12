
.. module:: base_external_referentials
    :synopsis: Base External Referentials 
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

    <div class="js-kit-rating" title="" permalink="" standalone="yes" path="/base_external_referentials"></div>
    <script src="http://js-kit.com/ratings.js"></script>

Base External Referentials (*base_external_referentials*)
=========================================================
:Module: base_external_referentials
:Name: Base External Referentials
:Version: 5.0.1.0
:Author: Raphaël Valyi (Akretion.com), Sharoon Thomas (Openlabs.co.in)
:Directory: base_external_referentials
:Web: http://www.akretion.com, http://openlabs.co.in/
:Official module: no
:Quality certified: no

Description
-----------

::

  This module provide an abstract common minimal base to add any additional external id columns
  to some OpenObject table, pointing to some external referential.
  A referential is abstract and minimal at this stage, it only has:
  * a name
  * a location (possibly webservice URL, database connection URL...); the connection method will tell it...
  * referential credentials (user name + password)
  * placeholders for custom in and out mapping for OpenERP object fields.
  
  OpenERP already has limited supported to external ids using the ir_model_data and the id
  fields in the loaded data such as XML or CSV. We think that's OK to store all referential ids
  into the same ir_model_data table: yes it makes it large, but synchronisation operations involve
  a network bottleneck anyway, so it's largely OK and negligible to have a large table here.
  The existing ir_model_data feature of OpenERP is mostly thought as an mono-external referential
  (even if the module key of ir_model_data plays some referential scoping role). Here we just push
  the concept further to assume multiple external ids for OpenERP entities and add the possibility
  to customize their field mapping directly in OpenERP to accommodate the external systems.

Download links
--------------

You can download this module as a zip file in the following version:

(No download links available)


Dependencies
------------

 * :mod:`base`

Reports
-------

None


Menus
-------

 * Administration/Customization/Database Structure/External Referentials

Views
-----

 * external_referential_form_view (form)
 * external_referential_tree_view (tree)


Objects
-------

Object: External Referential Type (Ex. Magento, Spree) (external.referential.type)
##################################################################################



:name: Name, char, required, readonly




Object: The source mapping records (external.mapping.template)
##############################################################



:model_id: OpenERP Model, many2one, required





:external_update_method: Update Method, char





:type_id: External Referential Type, many2one





:external_key_name: External field used as key, char





:external_delete_method: Delete Method, char





:external_get_method: Get Method, char





:external_create_method: Create Method, char





:model: Model Name, char





:external_list_method: List Method, char




Object: The source mapping line records (external.mappinglines.template)
########################################################################



:model_id: OpenERP Model, many2one





:external_field: External Field, char





:in_function: Import in OpenERP Mapping Python Function, text





:type_id: External Referential Type, many2one





:out_function: Export from OpenERP Mapping Python Function, text





:model: Model Name, char





:type: Type, selection





:external_type: External Type, selection




Object: External Referential (external.referential)
###################################################



:apipass: Password, char





:name: Name, char, required





:type_id: Referential Type, many2one





:apiusername: User Name, char





:location: Location, char





:mapping_ids: Mappings, one2many




Object: Field Mapping (external.mapping.line)
#############################################



:external_field: External Field, char





:in_function: Import in OpenERP Mapping Python Function, text





:name_function: Full Name, char, readonly





:out_function: Export from OpenERP Mapping Python Function, text





:field_id: OpenERP Field, many2one





:mapping_id: External Mapping, many2one





:related_model_id: Related Model, many2one





:type: Type, selection





:external_type: External Type, selection




Object: External Mapping (external.mapping)
###########################################



:model_id: OpenERP Model, many2one, required





:external_update_method: Update Method, char





:external_key_name: External field used as key, char, required





:external_delete_method: Delete Method, char





:related_model_ids: Related Inherited Models, one2many, readonly

    *potentially inherited through '_inherits' model, used for mapping field selection*



:external_get_method: Get Method, char





:external_create_method: Create Method, char





:referential_id: External Referential, many2one, required





:mapping_ids: Mappings Lines, one2many





:model: Model Name, char





:external_list_method: List Method, char


