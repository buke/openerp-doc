
.. i18n: .. module:: base_external_referentials
.. i18n:     :synopsis: Base External Referentials 
.. i18n:     :noindex:
.. i18n: .. 
..

.. module:: base_external_referentials
    :synopsis: Base External Referentials 
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
.. i18n:     <div class="js-kit-rating" title="" permalink="" standalone="yes" path="/base_external_referentials"></div>
.. i18n:     <script src="http://js-kit.com/ratings.js"></script>
..

.. raw:: html

    <div class="js-kit-rating" title="" permalink="" standalone="yes" path="/base_external_referentials"></div>
    <script src="http://js-kit.com/ratings.js"></script>

.. i18n: Base External Referentials (*base_external_referentials*)
.. i18n: =========================================================
.. i18n: :Module: base_external_referentials
.. i18n: :Name: Base External Referentials
.. i18n: :Version: 5.0.1.0
.. i18n: :Author: Raphaël Valyi (Akretion.com), Sharoon Thomas (Openlabs.co.in)
.. i18n: :Directory: base_external_referentials
.. i18n: :Web: http://www.akretion.com, http://openlabs.co.in/
.. i18n: :Official module: no
.. i18n: :Quality certified: no
..

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

.. i18n: Description
.. i18n: -----------
..

Description
-----------

.. i18n: ::
.. i18n: 
.. i18n:   This module provide an abstract common minimal base to add any additional external id columns
.. i18n:   to some OpenObject table, pointing to some external referential.
.. i18n:   A referential is abstract and minimal at this stage, it only has:
.. i18n:   * a name
.. i18n:   * a location (possibly webservice URL, database connection URL...); the connection method will tell it...
.. i18n:   * referential credentials (user name + password)
.. i18n:   * placeholders for custom in and out mapping for OpenERP object fields.
.. i18n:   
.. i18n:   OpenERP already has limited supported to external ids using the ir_model_data and the id
.. i18n:   fields in the loaded data such as XML or CSV. We think that's OK to store all referential ids
.. i18n:   into the same ir_model_data table: yes it makes it large, but synchronisation operations involve
.. i18n:   a network bottleneck anyway, so it's largely OK and negligible to have a large table here.
.. i18n:   The existing ir_model_data feature of OpenERP is mostly thought as an mono-external referential
.. i18n:   (even if the module key of ir_model_data plays some referential scoping role). Here we just push
.. i18n:   the concept further to assume multiple external ids for OpenERP entities and add the possibility
.. i18n:   to customize their field mapping directly in OpenERP to accommodate the external systems.
..

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

.. i18n: Download links
.. i18n: --------------
..

Download links
--------------

.. i18n: You can download this module as a zip file in the following version:
..

You can download this module as a zip file in the following version:

.. i18n: (No download links available)
..

(No download links available)

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

.. i18n:  * Administration/Customization/Database Structure/External Referentials
..

 * Administration/Customization/Database Structure/External Referentials

.. i18n: Views
.. i18n: -----
..

Views
-----

.. i18n:  * external_referential_form_view (form)
.. i18n:  * external_referential_tree_view (tree)
..

 * external_referential_form_view (form)
 * external_referential_tree_view (tree)

.. i18n: Objects
.. i18n: -------
..

Objects
-------

.. i18n: Object: External Referential Type (Ex. Magento, Spree) (external.referential.type)
.. i18n: ##################################################################################
..

Object: External Referential Type (Ex. Magento, Spree) (external.referential.type)
##################################################################################

.. i18n: :name: Name, char, required, readonly
..

:name: Name, char, required, readonly

.. i18n: Object: The source mapping records (external.mapping.template)
.. i18n: ##############################################################
..

Object: The source mapping records (external.mapping.template)
##############################################################

.. i18n: :model_id: OpenERP Model, many2one, required
..

:model_id: OpenERP Model, many2one, required

.. i18n: :external_update_method: Update Method, char
..

:external_update_method: Update Method, char

.. i18n: :type_id: External Referential Type, many2one
..

:type_id: External Referential Type, many2one

.. i18n: :external_key_name: External field used as key, char
..

:external_key_name: External field used as key, char

.. i18n: :external_delete_method: Delete Method, char
..

:external_delete_method: Delete Method, char

.. i18n: :external_get_method: Get Method, char
..

:external_get_method: Get Method, char

.. i18n: :external_create_method: Create Method, char
..

:external_create_method: Create Method, char

.. i18n: :model: Model Name, char
..

:model: Model Name, char

.. i18n: :external_list_method: List Method, char
..

:external_list_method: List Method, char

.. i18n: Object: The source mapping line records (external.mappinglines.template)
.. i18n: ########################################################################
..

Object: The source mapping line records (external.mappinglines.template)
########################################################################

.. i18n: :model_id: OpenERP Model, many2one
..

:model_id: OpenERP Model, many2one

.. i18n: :external_field: External Field, char
..

:external_field: External Field, char

.. i18n: :in_function: Import in OpenERP Mapping Python Function, text
..

:in_function: Import in OpenERP Mapping Python Function, text

.. i18n: :type_id: External Referential Type, many2one
..

:type_id: External Referential Type, many2one

.. i18n: :out_function: Export from OpenERP Mapping Python Function, text
..

:out_function: Export from OpenERP Mapping Python Function, text

.. i18n: :model: Model Name, char
..

:model: Model Name, char

.. i18n: :type: Type, selection
..

:type: Type, selection

.. i18n: :external_type: External Type, selection
..

:external_type: External Type, selection

.. i18n: Object: External Referential (external.referential)
.. i18n: ###################################################
..

Object: External Referential (external.referential)
###################################################

.. i18n: :apipass: Password, char
..

:apipass: Password, char

.. i18n: :name: Name, char, required
..

:name: Name, char, required

.. i18n: :type_id: Referential Type, many2one
..

:type_id: Referential Type, many2one

.. i18n: :apiusername: User Name, char
..

:apiusername: User Name, char

.. i18n: :location: Location, char
..

:location: Location, char

.. i18n: :mapping_ids: Mappings, one2many
..

:mapping_ids: Mappings, one2many

.. i18n: Object: Field Mapping (external.mapping.line)
.. i18n: #############################################
..

Object: Field Mapping (external.mapping.line)
#############################################

.. i18n: :external_field: External Field, char
..

:external_field: External Field, char

.. i18n: :in_function: Import in OpenERP Mapping Python Function, text
..

:in_function: Import in OpenERP Mapping Python Function, text

.. i18n: :name_function: Full Name, char, readonly
..

:name_function: Full Name, char, readonly

.. i18n: :out_function: Export from OpenERP Mapping Python Function, text
..

:out_function: Export from OpenERP Mapping Python Function, text

.. i18n: :field_id: OpenERP Field, many2one
..

:field_id: OpenERP Field, many2one

.. i18n: :mapping_id: External Mapping, many2one
..

:mapping_id: External Mapping, many2one

.. i18n: :related_model_id: Related Model, many2one
..

:related_model_id: Related Model, many2one

.. i18n: :type: Type, selection
..

:type: Type, selection

.. i18n: :external_type: External Type, selection
..

:external_type: External Type, selection

.. i18n: Object: External Mapping (external.mapping)
.. i18n: ###########################################
..

Object: External Mapping (external.mapping)
###########################################

.. i18n: :model_id: OpenERP Model, many2one, required
..

:model_id: OpenERP Model, many2one, required

.. i18n: :external_update_method: Update Method, char
..

:external_update_method: Update Method, char

.. i18n: :external_key_name: External field used as key, char, required
..

:external_key_name: External field used as key, char, required

.. i18n: :external_delete_method: Delete Method, char
..

:external_delete_method: Delete Method, char

.. i18n: :related_model_ids: Related Inherited Models, one2many, readonly
..

:related_model_ids: Related Inherited Models, one2many, readonly

.. i18n:     *potentially inherited through '_inherits' model, used for mapping field selection*
..

    *potentially inherited through '_inherits' model, used for mapping field selection*

.. i18n: :external_get_method: Get Method, char
..

:external_get_method: Get Method, char

.. i18n: :external_create_method: Create Method, char
..

:external_create_method: Create Method, char

.. i18n: :referential_id: External Referential, many2one, required
..

:referential_id: External Referential, many2one, required

.. i18n: :mapping_ids: Mappings Lines, one2many
..

:mapping_ids: Mappings Lines, one2many

.. i18n: :model: Model Name, char
..

:model: Model Name, char

.. i18n: :external_list_method: List Method, char
..

:external_list_method: List Method, char
