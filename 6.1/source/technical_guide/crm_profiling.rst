
.. module:: crm_profiling
    :synopsis: crm_profiling management (Official, Quality Certified)
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

    <div class="js-kit-rating" title="" permalink="" standalone="yes" path="/crm_profiling"></div>
    <script src="http://js-kit.com/ratings.js"></script>

crm_profiling management (*crm_profiling*)
==========================================
:Module: crm_profiling
:Name: crm_profiling management
:Version: 5.0.1.3
:Author: Tiny
:Directory: crm_profiling
:Web: http://www.openerp.com
:Official module: yes
:Quality certified: yes

Description
-----------

::

  This module allows users to perform segmentation within partners.
      It uses the profiles criteria from the earlier segmentation module and improve it. Thanks to the new concept of questionnaire. You can now regroup questions into a questionnaire and directly use it on a partner.
  
      It also has been merged with the earlier CRM & SRM segmentation tool because they were overlapping.
  
      The menu items related are in "CRM & SRM\Configuration\Segmentations"
  
  
      * Note: this module is not compatible with the module segmentation, since it's the same which has been renamed.

Download links
--------------

You can download this module as a zip file in the following version:

  * `4.2 <http://www.openerp.com/download/modules/4.2/crm_profiling.zip>`_
  * `5.0 <http://www.openerp.com/download/modules/5.0/crm_profiling.zip>`_
  * `trunk <http://www.openerp.com/download/modules/trunk/crm_profiling.zip>`_


Dependencies
------------

 * :mod:`base`
 * :mod:`crm`

Reports
-------

None


Menus
-------

 * CRM & SRM/Configuration/Segmentations/Questionnaires
 * CRM & SRM/Configuration/Segmentations/Questions

Views
-----

 * Questionnaires (tree)
 * Questionnaires (form)
 * Answers (tree)
 * Answers (form)
 * Questions (tree)
 * Questions (form)
 * \* INHERIT res.partner.profile.form (form)
 * crm.segmentation.tree (tree)


Objects
-------

Object: Question (crm_profiling.question)
#########################################



:answers_ids: Available answers, one2many





:name: Question, char, required




Object: Questionnaire (crm_profiling.questionnaire)
###################################################



:description: Description, text, required





:name: Questionnaire, char, required





:questions_ids: Questions, many2many




Object: Answer (crm_profiling.answer)
#####################################



:name: Answer, char, required





:question_id: Question, many2one


