
.. module:: nan_quality_control
    :synopsis: Quality Control 
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

    <div class="js-kit-rating" title="" permalink="" standalone="yes" path="/nan_quality_control"></div>
    <script src="http://js-kit.com/ratings.js"></script>

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

Description
-----------

::

  This module provides a generic infrastructure for quality tests. The idea is that it can be later be reused for doing quality tests in production lots but also in any other areas a company may desire.

Download links
--------------

You can download this module as a zip file in the following version:

(No download links available)


Dependencies
------------

 * :mod:`product`

Reports
-------

None


Menus
-------

 * Quality Control
 * Quality Control/Configuration
 * Quality Control/Configuration/Method
 * Quality Control/Configuration/Test Template
 * Quality Control/Configuration/Proof
 * Quality Control/Test Lines
 * Quality Control/Tests

Views
-----

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


Objects
-------

Object: Method (qc.proof.method)
################################



:active: Active, boolean





:name: Name, char, required




Object: qc.posible.value (qc.posible.value)
###########################################



:active: Active, boolean





:name: Name, char, required




Object: qc.proof (qc.proof)
###########################



:name: Name, char, required





:posible_values_ids: Possible Values, many2many





:ref: Code, char





:synonyms: Synonyms, char, readonly





:synonym_ids: Synonyms, one2many





:active: Active, boolean





:type: Type, selection, required




Object: qc.proof.synonym (qc.proof.synonym)
###########################################



:proof_id: Proof, many2one, required





:name: Name, char, required




Object: qc.test.template.category (qc.test.template.category)
#############################################################



:active: Active, boolean

    *The active field allows you to hide the category without removing it.*



:parent_id: Parent Category, many2one





:child_ids: Child Categories, one2many





:complete_name: Full Name, char, readonly





:name: Category Name, char, required




Object: Test Template (qc.test.template)
########################################



:name: Name, char, required





:fill_correct_values: Fill With Correct Values, boolean





:object_id: Reference Object, reference





:active: Active, boolean





:category_id: Category, many2one





:type: Type, selection





:test_template_line_ids: Lines, one2many




Object: qc.test.template.line (qc.test.template.line)
#####################################################



:proof_id: Proof, many2one, required





:min_value: Min, float





:method_id: Method, many2one





:test_template_id: Test Template, many2one





:max_value: Max, float





:notes: Notes, text





:sequence: Sequence, integer, required





:valid_value: Valid Value, many2one





:uom_id: Uom, many2one





:type: Type, selection, readonly




Object: qc.test (qc.test)
#########################



:test_internal_note: Internal Note, text





:name: Date, datetime, required, readonly





:success: Success, boolean, readonly

    *This field will be active if all tests have succeeded.*



:test_template_id: Test, many2one





:enabled: Enabled, boolean, readonly

    *If a quality control test is not enabled it means it can not be moved from "Quality Success" or "Quality Failed" state.*



:object_id: Reference, reference, readonly





:state: State, selection, readonly





:test_external_note: External Note, text





:test_line_ids: Test Lines, one2many




Object: qc.test.line (qc.test.line)
###################################



:proof_id: Proof, many2one, readonly





:min_value: Min, float, readonly

    *Minimum valid value if it is a quantitative proof.*



:method_id: Method, many2one, readonly





:success: Success?, boolean, readonly





:actual_value_qt: Qt.Value, float

    *Value of the result if it is a quantitative proof.*



:max_value: Max, float, readonly

    *Maximum valid value if it is a quantitative proof.*



:notes: Notes, text, readonly





:test_template_line_id: Test Template Line, many2one, readonly





:test_id: Test, many2one





:valid_value: Valid Value, many2one, readonly

    *Value that should have the result to be valid if it is a qualitative proof.*



:uom_id: Uom, many2one, readonly

    *UoM for minimum and maximum values if it is a quantitative proof.*



:proof_type: Proof Type, selection, readonly





:test_uom_id: Uom Test, many2one

    *UoM of the value of the result if it is a quantitative proof.*



:actual_value_ql: Ql.Value, many2one

    *Value of the result if it is a qualitative proof.*


Object: qc.test.set.template.wizard (qc.test.set.template.wizard)
#################################################################



:test_template_id: Template, many2one


