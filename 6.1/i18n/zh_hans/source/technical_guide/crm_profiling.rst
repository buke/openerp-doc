
.. i18n: .. module:: crm_profiling
.. i18n:     :synopsis: crm_profiling management (Official, Quality Certified)
.. i18n:     :noindex:
.. i18n: .. 
..

.. module:: crm_profiling
    :synopsis: crm_profiling management (Official, Quality Certified)
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
.. i18n:     <div class="js-kit-rating" title="" permalink="" standalone="yes" path="/crm_profiling"></div>
.. i18n:     <script src="http://js-kit.com/ratings.js"></script>
..

.. raw:: html

    <div class="js-kit-rating" title="" permalink="" standalone="yes" path="/crm_profiling"></div>
    <script src="http://js-kit.com/ratings.js"></script>

.. i18n: crm_profiling management (*crm_profiling*)
.. i18n: ==========================================
.. i18n: :Module: crm_profiling
.. i18n: :Name: crm_profiling management
.. i18n: :Version: 5.0.1.3
.. i18n: :Author: Tiny
.. i18n: :Directory: crm_profiling
.. i18n: :Web: http://www.openerp.com
.. i18n: :Official module: yes
.. i18n: :Quality certified: yes
..

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

.. i18n: Description
.. i18n: -----------
..

Description
-----------

.. i18n: ::
.. i18n: 
.. i18n:   This module allows users to perform segmentation within partners.
.. i18n:       It uses the profiles criteria from the earlier segmentation module and improve it. Thanks to the new concept of questionnaire. You can now regroup questions into a questionnaire and directly use it on a partner.
.. i18n:   
.. i18n:       It also has been merged with the earlier CRM & SRM segmentation tool because they were overlapping.
.. i18n:   
.. i18n:       The menu items related are in "CRM & SRM\Configuration\Segmentations"
.. i18n:   
.. i18n:   
.. i18n:       * Note: this module is not compatible with the module segmentation, since it's the same which has been renamed.
..

::

  This module allows users to perform segmentation within partners.
      It uses the profiles criteria from the earlier segmentation module and improve it. Thanks to the new concept of questionnaire. You can now regroup questions into a questionnaire and directly use it on a partner.
  
      It also has been merged with the earlier CRM & SRM segmentation tool because they were overlapping.
  
      The menu items related are in "CRM & SRM\Configuration\Segmentations"
  
  
      * Note: this module is not compatible with the module segmentation, since it's the same which has been renamed.

.. i18n: Download links
.. i18n: --------------
..

Download links
--------------

.. i18n: You can download this module as a zip file in the following version:
..

You can download this module as a zip file in the following version:

.. i18n:   * `4.2 <http://www.openerp.com/download/modules/4.2/crm_profiling.zip>`_
.. i18n:   * `5.0 <http://www.openerp.com/download/modules/5.0/crm_profiling.zip>`_
.. i18n:   * `trunk <http://www.openerp.com/download/modules/trunk/crm_profiling.zip>`_
..

  * `4.2 <http://www.openerp.com/download/modules/4.2/crm_profiling.zip>`_
  * `5.0 <http://www.openerp.com/download/modules/5.0/crm_profiling.zip>`_
  * `trunk <http://www.openerp.com/download/modules/trunk/crm_profiling.zip>`_

.. i18n: Dependencies
.. i18n: ------------
..

Dependencies
------------

.. i18n:  * :mod:`base`
.. i18n:  * :mod:`crm`
..

 * :mod:`base`
 * :mod:`crm`

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

.. i18n:  * CRM & SRM/Configuration/Segmentations/Questionnaires
.. i18n:  * CRM & SRM/Configuration/Segmentations/Questions
..

 * CRM & SRM/Configuration/Segmentations/Questionnaires
 * CRM & SRM/Configuration/Segmentations/Questions

.. i18n: Views
.. i18n: -----
..

Views
-----

.. i18n:  * Questionnaires (tree)
.. i18n:  * Questionnaires (form)
.. i18n:  * Answers (tree)
.. i18n:  * Answers (form)
.. i18n:  * Questions (tree)
.. i18n:  * Questions (form)
.. i18n:  * \* INHERIT res.partner.profile.form (form)
.. i18n:  * crm.segmentation.tree (tree)
..

 * Questionnaires (tree)
 * Questionnaires (form)
 * Answers (tree)
 * Answers (form)
 * Questions (tree)
 * Questions (form)
 * \* INHERIT res.partner.profile.form (form)
 * crm.segmentation.tree (tree)

.. i18n: Objects
.. i18n: -------
..

Objects
-------

.. i18n: Object: Question (crm_profiling.question)
.. i18n: #########################################
..

Object: Question (crm_profiling.question)
#########################################

.. i18n: :answers_ids: Available answers, one2many
..

:answers_ids: Available answers, one2many

.. i18n: :name: Question, char, required
..

:name: Question, char, required

.. i18n: Object: Questionnaire (crm_profiling.questionnaire)
.. i18n: ###################################################
..

Object: Questionnaire (crm_profiling.questionnaire)
###################################################

.. i18n: :description: Description, text, required
..

:description: Description, text, required

.. i18n: :name: Questionnaire, char, required
..

:name: Questionnaire, char, required

.. i18n: :questions_ids: Questions, many2many
..

:questions_ids: Questions, many2many

.. i18n: Object: Answer (crm_profiling.answer)
.. i18n: #####################################
..

Object: Answer (crm_profiling.answer)
#####################################

.. i18n: :name: Answer, char, required
..

:name: Answer, char, required

.. i18n: :question_id: Question, many2one
..

:question_id: Question, many2one
