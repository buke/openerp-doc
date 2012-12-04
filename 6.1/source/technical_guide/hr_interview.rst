
.. module:: hr_interview
    :synopsis: Human Resources (Interview Evaluation) 
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

    <div class="js-kit-rating" title="" permalink="" standalone="yes" path="/hr_interview"></div>
    <script src="http://js-kit.com/ratings.js"></script>

Human Resources (Interview Evaluation) (*hr_interview*)
=======================================================
:Module: hr_interview
:Name: Human Resources (Interview Evaluation)
:Version: 5.0.1.0
:Author: Tiny
:Directory: hr_interview
:Web: http://www.openerp.com
:Official module: no
:Quality certified: no

Description
-----------

::

  This module stores all the educational and professional details of candidates who appear for interview. While taking an interview, the interviewers can evaluate the candidate's performance on the basis of categories. The candidate is evaluated based on different evaluations, which are related to categories.
  
  Example: Candidate X to be evaluated for Y Category(Category reflects the recruitment criteria). Category Y has several question types: DBMS questions, OOP questions, Communication skills, etc.

Download links
--------------

You can download this module as a zip file in the following version:

  * `5.0 <http://www.openerp.com/download/modules/5.0/hr_interview.zip>`_
  * `trunk <http://www.openerp.com/download/modules/trunk/hr_interview.zip>`_


Dependencies
------------

 * :mod:`base`
 * :mod:`hr`
 * :mod:`crm`
 * :mod:`smtpclient`

Reports
-------

 * Candidate's Summary

Menus
-------

 * Human Resources/Configuration/Candidate Categories
 * Human Resources/Interview
 * Human Resources/Interview/All Interviews
 * Human Resources/Interview/New Interview
 * Human Resources/Interview/All Interviews/Selected Candidates
 * Human Resources/Interview/All Interviews/Cancel Candidates
 * Human Resources/Interview/All Interviews/Rejected Candidates
 * Human Resources/Interview/All Interviews/Scheduled Candidates
 * Human Resources/Configuration/Candidate Experience

Views
-----

 * cand.categ.search (form)
 * cand.categ.tree (tree)
 * hr.interview.tree (tree)
 * hr.interview.form (form)
 * technical.skill.form (form)
 * technical.skill.tree (tree)
 * candidate.experience.form (form)
 * candidate.experience.tree (tree)
 * category.question.form (form)
 * category.question.tree (tree)
 * hr.interview.log.form (form)
 * hr.interview.log.tree (tree)


Objects
-------

Object: Category Of Candidate (candidate.category)
##################################################



:code: Code, char, required





:question_ids: Question, one2many





:name: Name, char, required




Object: Question Category (Question Belongs to Which Category) (category.question)
##################################################################################



:tot_marks: Total Marks, integer, required





:name: Question, char, required





:category_id: Category, many2one




Object: Candidate Experience (candidate.experience)
###################################################



:code: Code, char, required





:name: Name, char, required





:special: Specialization, char




Object: Interview Evaluation (hr.interview)
###########################################



:evaluator_ids: Evaluator, many2many





:history_log_ids: Interview Logs, one2many, readonly





:name: Candidate Name, char, required





:performance: Performance (%), float, readonly





:tech_skills_ids: Technology Skills, one2many





:mobile_no: Mobile, char





:category_id: Category, many2one





:remarks: Remarks, text





:state: State, selection, readonly





:reference_id: Reference, many2one





:experience_id: Experience, many2one





:date: Scheduled Date, datetime





:exam_date: Exam On, datetime





:crm_case_id: Case, many2one





:education: Education, selection





:email: E-mail, char, required





:hr_id: Interview ID, char




Object: Technical Skill Of Candidate (technical.skill)
######################################################



:remarks: Remarks, text





:obt_marks: Obtained Marks, float





:tot_marks: Total Marks, float, required





:candidate_id: Candidate ID, many2one





:name: Category, char, required




Object: HR interview log (hr.interview.log)
###########################################



:date: Date, datetime





:history_id: History ID, many2one





:user_id: User Name, many2one





:state: State, char


