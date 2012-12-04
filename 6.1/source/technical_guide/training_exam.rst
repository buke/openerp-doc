
.. module:: training_exam
    :synopsis: training_exam 
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

    <div class="js-kit-rating" title="" permalink="" standalone="yes" path="/training_exam"></div>
    <script src="http://js-kit.com/ratings.js"></script>

Training Exam (*training_exam*)
===============================

:Module: training_exam
:Name: Training Exam
:Version: 0.0.1
:Author: Tiny SPRL
:Directory: training_exam
:Web: http://www.openerp.com
:Official module: no
:Quality certified: no

Description
-----------

This module adds the exam management for the training management

Download links
--------------

You can download this module as a zip file in the following version:

  * `5.0 <http://www.openerp.com/download/modules/5.0/training_exam.zip>`_ 
  * `trunk <http://www.openerp.com/download/modules/trunk/training_exam.zip>`_


Dependencies
------------

  * :mod:`training`


Reports
-------

  * Training Cancellation
  * Training Confirmation

Menus
-------

None

Views
-----

  * \* INHERIT training.course.form.with.questionnaires (form)
  * training.question.form (form)
  * training.question.tree (tree)
  * training.questionnaire.form (form)
  * training.questionnaire.tree (tree)
  * training.planned_exam.form (form)
  * training.planned_exam.tree (tree)
  * training.planned_exam.calendar (calendar)
  * \* INHERIT training.offer.form.with.questionnaires (form)
  * training.exam_answer.form (form)
  * training.exam_answer.tree (tree)
  * training.exam.result.form (form)
  * training.exam.result.tree (tree)
  * training.exam_answer.form (form)
  * training.exam_answer.tree (tree)
  * \* INHERIT training.subscription.line.form.inherited (form)


Objects
-------


None


