
.. module:: comparison
    :synopsis: ERP Comparisons 
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

    <div class="js-kit-rating" title="" permalink="" standalone="yes" path="/comparison"></div>
    <script src="http://js-kit.com/ratings.js"></script>

ERP Comparisons (*comparison*)
==============================
:Module: comparison
:Name: ERP Comparisons
:Version: 5.0.0.1
:Author: Tiny
:Directory: comparison
:Web: http://www.openerp.com
:Official module: no
:Quality certified: no

Description
-----------

::

  This module manages the backend of a collaborative comparison website amongst
  different products.

Download links
--------------

You can download this module as a zip file in the following version:

  * `5.0 <http://www.openerp.com/download/modules/5.0/comparison.zip>`_
  * `trunk <http://www.openerp.com/download/modules/trunk/comparison.zip>`_


Dependencies
------------

 * :mod:`base`

Reports
-------

None


Menus
-------

 * ERP Comparison
 * ERP Comparison/Configuration
 * ERP Comparison/Configuration/Users
 * ERP Comparison/Configuration/Items
 * ERP Comparison/Configuration/Criterias
 * ERP Comparison/Criterias Structure
 * ERP Comparison/Reporting
 * ERP Comparison/Reporting/Results of the Comparisons
 * ERP Comparison/Configuration/Vote Values(Criterias)
 * ERP Comparison/Votes
 * ERP Comparison/Votes/New Vote
 * ERP Comparison/Suggestions
 * ERP Comparison/Suggestions/New Suggestion
 * ERP Comparison/Configuration/Item Packs
 * ERP Comparison/Periodical Processing
 * ERP Comparison/Periodical Processing/Criterias
 * ERP Comparison/Periodical Processing/Votes
 * ERP Comparison/Periodical Processing/Ponderation Suggestions
 * ERP Comparison/Periodical Processing/Criterias/Draft Criterias
 * ERP Comparison/Periodical Processing/Criterias/Cancelled Criterias
 * ERP Comparison/Periodical Processing/Votes/Draft Votes
 * ERP Comparison/Periodical Processing/Votes/Cancelled Votes
 * ERP Comparison/Periodical Processing/Ponderation Suggestions/Draft Suggestions
 * ERP Comparison/Periodical Processing/Ponderation Suggestions/Cancelled Suggestions
 * ERP Comparison/Periodical Processing/Recompute All Evaluations

Views
-----

 * comparison.user.form (form)
 * comparison.user.tree (tree)
 * comparison.item.form (form)
 * comparison.item.tree (tree)
 * comparison.factor.form (form)
 * comparison.factor.list (tree)
 * comparison.factor.tree (tree)
 * comparison.factor.result.tree (tree)
 * comparison.vote.values.form (form)
 * comparison.vote.values.tree (tree)
 * comparison.vote.form (form)
 * comparison.vote.tree (tree)
 * comparison.ponderation.suggestion.form (form)
 * comparison.ponderation.suggestion.tree (tree)
 * evaluation.pack.form (form)
 * evaluation.pack.tree (tree)


Objects
-------

Object: comparison.user (comparison.user)
#########################################



:name: Name, char, required





:suggestion_ids: Ponderation Suggestions, one2many





:vote_ids: Votes, one2many





:factor_ids: Factors, one2many





:active: Active, boolean





:password: Password, char, required





:email: Email, char, required




Object: comparison.item (comparison.item)
#########################################



:load_default: Load by Default, boolean

    *This option if checked, will let the Item display on Evaluation Matrix, by default.*



:code: Code, char, required





:user_id: User, many2one





:name: Software, char, required





:result_ids: Results, one2many





:sequence: Sequence, integer





:note: Description, text





:state: Status, selection, required





:version: Version, char, required




Object: comparison.factor (comparison.factor)
#############################################



:user_id: User, many2one





:name: Factor Name, char, required





:result_ids: Results, one2many





:sequence: Sequence, integer





:child_ids: Child Factors, one2many





:note: Note, text





:parent_id: Parent Factor, many2one





:state: Status, selection, required





:ponderation: Ponderation, float





:pond_computed: Computed Ponderation, float, readonly





:type: Type, selection, required




Object: comparison.vote.values (comparison.vote.values)
#######################################################



:name: Vote Type, char, required





:factor: Factor, float, required




Object: comparison.vote (comparison.vote)
#########################################



:user_id: User, many2one





:factor_id: Factor, many2one, required





:note: Note, text





:state: Status, selection, required, readonly





:score_id: Value, many2one, required





:item_id: Item, many2one, required




Object: comparison.factor.result (comparison.factor.result)
###########################################################



:item_id: Item, many2one, required, readonly





:factor_id: Factor, many2one, required, readonly





:votes: Votes, float, readonly





:result: Goodness(%), float, readonly




Object: comparison.ponderation.suggestion (comparison.ponderation.suggestion)
#############################################################################



:user_id: User, many2one, required





:factor_id: Factor, many2one, required





:effect: Ponderation Effect, selection

    *Select Positive if your suggestion has greater poderation value than the current value, negative otherwise.*



:note: Suggestion, text





:state: State, selection, readonly





:ponderation: Ponderation, float, required




Object: Evaluation Pack for Easy Comparison (evaluation.pack)
#############################################################



:name: Name, char, required





:item_ids: Items, many2many


