
.. i18n: .. module:: nan_quality_control
.. i18n:     :synopsis: Quality Control 
.. i18n:     :noindex:
.. i18n: .. 
..

.. module:: nan_quality_control
    :synopsis: Quality Control 
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
.. i18n:     <div class="js-kit-rating" title="" permalink="" standalone="yes" path="/nan_quality_control"></div>
.. i18n:     <script src="http://js-kit.com/ratings.js"></script>
..

.. raw:: html

    <div class="js-kit-rating" title="" permalink="" standalone="yes" path="/nan_quality_control"></div>
    <script src="http://js-kit.com/ratings.js"></script>

.. i18n: Quality Control (*nan_quality_control*)
.. i18n: =======================================
.. i18n: :Module: nan_quality_control
.. i18n: :Name: Quality Control
.. i18n: :Version: 5.0.0.1
.. i18n: :Author: NaN for Trod y Avia, S.L.
.. i18n: :Directory: nan_quality_control
.. i18n: :Web: 
.. i18n: :Official module: no
.. i18n: :Quality certified: no
..

Quality Control (*nan_quality_control*)
=======================================
:Module: nan_quality_control
:Name: Quality Control
:Version: 5.0.0.1
:Author: NaN for Trod y Avia, S.L.
:Directory: nan_quality_control
:Web: 
:Official module: no
:Quality certified: no

.. i18n: Description
.. i18n: -----------
..

Description
-----------

.. i18n: ::
.. i18n: 
.. i18n:   This module provides a generic infrastructure for quality tests. The idea is that it can be later be reused for doing quality tests in production lots but also in any other areas a company may desire.
..

::

  This module provides a generic infrastructure for quality tests. The idea is that it can be later be reused for doing quality tests in production lots but also in any other areas a company may desire.

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

.. i18n:  * :mod:`product`
..

 * :mod:`product`

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

.. i18n:  * Quality Control
.. i18n:  * Quality Control/Configuration
.. i18n:  * Quality Control/Configuration/Method
.. i18n:  * Quality Control/Configuration/Test Template
.. i18n:  * Quality Control/Configuration/Proof
.. i18n:  * Quality Control/Test Lines
.. i18n:  * Quality Control/Tests
..

 * Quality Control
 * Quality Control/Configuration
 * Quality Control/Configuration/Method
 * Quality Control/Configuration/Test Template
 * Quality Control/Configuration/Proof
 * Quality Control/Test Lines
 * Quality Control/Tests

.. i18n: Views
.. i18n: -----
..

Views
-----

.. i18n:  * qc.proof.method.form (form)
.. i18n:  * qc.proof.method.tree (tree)
.. i18n:  * qc.posible.value.form (form)
.. i18n:  * qc.posible_value.tree (tree)
.. i18n:  * qc.proof.synonym (form)
.. i18n:  * qc.proof.synonym.tree (tree)
.. i18n:  * qc.proof.form (form)
.. i18n:  * qc.proof.tree (tree)
.. i18n:  * qc.test.template.form (form)
.. i18n:  * qc.test.template_tree (tree)
.. i18n:  * qc.test.template.form2 (form)
.. i18n:  * qc.test.template.line.form (form)
.. i18n:  * qc.test.template,line.tree (tree)
.. i18n:  * qc.test.set.template.wizard (form)
.. i18n:  * qc.test.form (form)
.. i18n:  * qc.test.tree (tree)
.. i18n:  * qc.test.line.form (form)
.. i18n:  * qc.test.line.tree (tree)
..

 * qc.proof.method.form (form)
 * qc.proof.method.tree (tree)
 * qc.posible.value.form (form)
 * qc.posible_value.tree (tree)
 * qc.proof.synonym (form)
 * qc.proof.synonym.tree (tree)
 * qc.proof.form (form)
 * qc.proof.tree (tree)
 * qc.test.template.form (form)
 * qc.test.template_tree (tree)
 * qc.test.template.form2 (form)
 * qc.test.template.line.form (form)
 * qc.test.template,line.tree (tree)
 * qc.test.set.template.wizard (form)
 * qc.test.form (form)
 * qc.test.tree (tree)
 * qc.test.line.form (form)
 * qc.test.line.tree (tree)

.. i18n: Objects
.. i18n: -------
..

Objects
-------

.. i18n: Object: Method (qc.proof.method)
.. i18n: ################################
..

Object: Method (qc.proof.method)
################################

.. i18n: :active: Active, boolean
..

:active: Active, boolean

.. i18n: :name: Name, char, required
..

:name: Name, char, required

.. i18n: Object: qc.posible.value (qc.posible.value)
.. i18n: ###########################################
..

Object: qc.posible.value (qc.posible.value)
###########################################

.. i18n: :active: Active, boolean
..

:active: Active, boolean

.. i18n: :name: Name, char, required
..

:name: Name, char, required

.. i18n: Object: qc.proof (qc.proof)
.. i18n: ###########################
..

Object: qc.proof (qc.proof)
###########################

.. i18n: :name: Name, char, required
..

:name: Name, char, required

.. i18n: :posible_values_ids: Possible Values, many2many
..

:posible_values_ids: Possible Values, many2many

.. i18n: :ref: Code, char
..

:ref: Code, char

.. i18n: :synonyms: Synonyms, char, readonly
..

:synonyms: Synonyms, char, readonly

.. i18n: :synonym_ids: Synonyms, one2many
..

:synonym_ids: Synonyms, one2many

.. i18n: :active: Active, boolean
..

:active: Active, boolean

.. i18n: :type: Type, selection, required
..

:type: Type, selection, required

.. i18n: Object: qc.proof.synonym (qc.proof.synonym)
.. i18n: ###########################################
..

Object: qc.proof.synonym (qc.proof.synonym)
###########################################

.. i18n: :proof_id: Proof, many2one, required
..

:proof_id: Proof, many2one, required

.. i18n: :name: Name, char, required
..

:name: Name, char, required

.. i18n: Object: qc.test.template.category (qc.test.template.category)
.. i18n: #############################################################
..

Object: qc.test.template.category (qc.test.template.category)
#############################################################

.. i18n: :active: Active, boolean
..

:active: Active, boolean

.. i18n:     *The active field allows you to hide the category without removing it.*
..

    *The active field allows you to hide the category without removing it.*

.. i18n: :parent_id: Parent Category, many2one
..

:parent_id: Parent Category, many2one

.. i18n: :child_ids: Child Categories, one2many
..

:child_ids: Child Categories, one2many

.. i18n: :complete_name: Full Name, char, readonly
..

:complete_name: Full Name, char, readonly

.. i18n: :name: Category Name, char, required
..

:name: Category Name, char, required

.. i18n: Object: Test Template (qc.test.template)
.. i18n: ########################################
..

Object: Test Template (qc.test.template)
########################################

.. i18n: :name: Name, char, required
..

:name: Name, char, required

.. i18n: :fill_correct_values: Fill With Correct Values, boolean
..

:fill_correct_values: Fill With Correct Values, boolean

.. i18n: :object_id: Reference Object, reference
..

:object_id: Reference Object, reference

.. i18n: :active: Active, boolean
..

:active: Active, boolean

.. i18n: :category_id: Category, many2one
..

:category_id: Category, many2one

.. i18n: :type: Type, selection
..

:type: Type, selection

.. i18n: :test_template_line_ids: Lines, one2many
..

:test_template_line_ids: Lines, one2many

.. i18n: Object: qc.test.template.line (qc.test.template.line)
.. i18n: #####################################################
..

Object: qc.test.template.line (qc.test.template.line)
#####################################################

.. i18n: :proof_id: Proof, many2one, required
..

:proof_id: Proof, many2one, required

.. i18n: :min_value: Min, float
..

:min_value: Min, float

.. i18n: :method_id: Method, many2one
..

:method_id: Method, many2one

.. i18n: :test_template_id: Test Template, many2one
..

:test_template_id: Test Template, many2one

.. i18n: :max_value: Max, float
..

:max_value: Max, float

.. i18n: :notes: Notes, text
..

:notes: Notes, text

.. i18n: :sequence: Sequence, integer, required
..

:sequence: Sequence, integer, required

.. i18n: :valid_value: Valid Value, many2one
..

:valid_value: Valid Value, many2one

.. i18n: :uom_id: Uom, many2one
..

:uom_id: Uom, many2one

.. i18n: :type: Type, selection, readonly
..

:type: Type, selection, readonly

.. i18n: Object: qc.test (qc.test)
.. i18n: #########################
..

Object: qc.test (qc.test)
#########################

.. i18n: :test_internal_note: Internal Note, text
..

:test_internal_note: Internal Note, text

.. i18n: :name: Date, datetime, required, readonly
..

:name: Date, datetime, required, readonly

.. i18n: :success: Success, boolean, readonly
..

:success: Success, boolean, readonly

.. i18n:     *This field will be active if all tests have succeeded.*
..

    *This field will be active if all tests have succeeded.*

.. i18n: :test_template_id: Test, many2one
..

:test_template_id: Test, many2one

.. i18n: :enabled: Enabled, boolean, readonly
..

:enabled: Enabled, boolean, readonly

.. i18n:     *If a quality control test is not enabled it means it can not be moved from "Quality Success" or "Quality Failed" state.*
..

    *If a quality control test is not enabled it means it can not be moved from "Quality Success" or "Quality Failed" state.*

.. i18n: :object_id: Reference, reference, readonly
..

:object_id: Reference, reference, readonly

.. i18n: :state: State, selection, readonly
..

:state: State, selection, readonly

.. i18n: :test_external_note: External Note, text
..

:test_external_note: External Note, text

.. i18n: :test_line_ids: Test Lines, one2many
..

:test_line_ids: Test Lines, one2many

.. i18n: Object: qc.test.line (qc.test.line)
.. i18n: ###################################
..

Object: qc.test.line (qc.test.line)
###################################

.. i18n: :proof_id: Proof, many2one, readonly
..

:proof_id: Proof, many2one, readonly

.. i18n: :min_value: Min, float, readonly
..

:min_value: Min, float, readonly

.. i18n:     *Minimum valid value if it is a quantitative proof.*
..

    *Minimum valid value if it is a quantitative proof.*

.. i18n: :method_id: Method, many2one, readonly
..

:method_id: Method, many2one, readonly

.. i18n: :success: Success?, boolean, readonly
..

:success: Success?, boolean, readonly

.. i18n: :actual_value_qt: Qt.Value, float
..

:actual_value_qt: Qt.Value, float

.. i18n:     *Value of the result if it is a quantitative proof.*
..

    *Value of the result if it is a quantitative proof.*

.. i18n: :max_value: Max, float, readonly
..

:max_value: Max, float, readonly

.. i18n:     *Maximum valid value if it is a quantitative proof.*
..

    *Maximum valid value if it is a quantitative proof.*

.. i18n: :notes: Notes, text, readonly
..

:notes: Notes, text, readonly

.. i18n: :test_template_line_id: Test Template Line, many2one, readonly
..

:test_template_line_id: Test Template Line, many2one, readonly

.. i18n: :test_id: Test, many2one
..

:test_id: Test, many2one

.. i18n: :valid_value: Valid Value, many2one, readonly
..

:valid_value: Valid Value, many2one, readonly

.. i18n:     *Value that should have the result to be valid if it is a qualitative proof.*
..

    *Value that should have the result to be valid if it is a qualitative proof.*

.. i18n: :uom_id: Uom, many2one, readonly
..

:uom_id: Uom, many2one, readonly

.. i18n:     *UoM for minimum and maximum values if it is a quantitative proof.*
..

    *UoM for minimum and maximum values if it is a quantitative proof.*

.. i18n: :proof_type: Proof Type, selection, readonly
..

:proof_type: Proof Type, selection, readonly

.. i18n: :test_uom_id: Uom Test, many2one
..

:test_uom_id: Uom Test, many2one

.. i18n:     *UoM of the value of the result if it is a quantitative proof.*
..

    *UoM of the value of the result if it is a quantitative proof.*

.. i18n: :actual_value_ql: Ql.Value, many2one
..

:actual_value_ql: Ql.Value, many2one

.. i18n:     *Value of the result if it is a qualitative proof.*
..

    *Value of the result if it is a qualitative proof.*

.. i18n: Object: qc.test.set.template.wizard (qc.test.set.template.wizard)
.. i18n: #################################################################
..

Object: qc.test.set.template.wizard (qc.test.set.template.wizard)
#################################################################

.. i18n: :test_template_id: Template, many2one
..

:test_template_id: Template, many2one
