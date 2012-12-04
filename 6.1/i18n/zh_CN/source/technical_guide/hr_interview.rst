
.. i18n: .. module:: hr_interview
.. i18n:     :synopsis: Human Resources (Interview Evaluation) 
.. i18n:     :noindex:
.. i18n: .. 
..

.. module:: hr_interview
    :synopsis: Human Resources (Interview Evaluation) 
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
.. i18n:     <div class="js-kit-rating" title="" permalink="" standalone="yes" path="/hr_interview"></div>
.. i18n:     <script src="http://js-kit.com/ratings.js"></script>
..

.. raw:: html

    <div class="js-kit-rating" title="" permalink="" standalone="yes" path="/hr_interview"></div>
    <script src="http://js-kit.com/ratings.js"></script>

.. i18n: Human Resources (Interview Evaluation) (*hr_interview*)
.. i18n: =======================================================
.. i18n: :Module: hr_interview
.. i18n: :Name: Human Resources (Interview Evaluation)
.. i18n: :Version: 5.0.1.0
.. i18n: :Author: Tiny
.. i18n: :Directory: hr_interview
.. i18n: :Web: http://www.openerp.com
.. i18n: :Official module: no
.. i18n: :Quality certified: no
..

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

.. i18n: Description
.. i18n: -----------
..

Description
-----------

.. i18n: ::
.. i18n: 
.. i18n:   This module stores all the educational and professional details of candidates who appear for interview. While taking an interview, the interviewers can evaluate the candidate's performance on the basis of categories. The candidate is evaluated based on different evaluations, which are related to categories.
.. i18n:   
.. i18n:   Example: Candidate X to be evaluated for Y Category(Category reflects the recruitment criteria). Category Y has several question types: DBMS questions, OOP questions, Communication skills, etc.
..

::

  This module stores all the educational and professional details of candidates who appear for interview. While taking an interview, the interviewers can evaluate the candidate's performance on the basis of categories. The candidate is evaluated based on different evaluations, which are related to categories.
  
  Example: Candidate X to be evaluated for Y Category(Category reflects the recruitment criteria). Category Y has several question types: DBMS questions, OOP questions, Communication skills, etc.

.. i18n: Download links
.. i18n: --------------
..

Download links
--------------

.. i18n: You can download this module as a zip file in the following version:
..

You can download this module as a zip file in the following version:

.. i18n:   * `5.0 <http://www.openerp.com/download/modules/5.0/hr_interview.zip>`_
.. i18n:   * `trunk <http://www.openerp.com/download/modules/trunk/hr_interview.zip>`_
..

  * `5.0 <http://www.openerp.com/download/modules/5.0/hr_interview.zip>`_
  * `trunk <http://www.openerp.com/download/modules/trunk/hr_interview.zip>`_

.. i18n: Dependencies
.. i18n: ------------
..

Dependencies
------------

.. i18n:  * :mod:`base`
.. i18n:  * :mod:`hr`
.. i18n:  * :mod:`crm`
.. i18n:  * :mod:`smtpclient`
..

 * :mod:`base`
 * :mod:`hr`
 * :mod:`crm`
 * :mod:`smtpclient`

.. i18n: Reports
.. i18n: -------
..

Reports
-------

.. i18n:  * Candidate's Summary
..

 * Candidate's Summary

.. i18n: Menus
.. i18n: -------
..

Menus
-------

.. i18n:  * Human Resources/Configuration/Candidate Categories
.. i18n:  * Human Resources/Interview
.. i18n:  * Human Resources/Interview/All Interviews
.. i18n:  * Human Resources/Interview/New Interview
.. i18n:  * Human Resources/Interview/All Interviews/Selected Candidates
.. i18n:  * Human Resources/Interview/All Interviews/Cancel Candidates
.. i18n:  * Human Resources/Interview/All Interviews/Rejected Candidates
.. i18n:  * Human Resources/Interview/All Interviews/Scheduled Candidates
.. i18n:  * Human Resources/Configuration/Candidate Experience
..

 * Human Resources/Configuration/Candidate Categories
 * Human Resources/Interview
 * Human Resources/Interview/All Interviews
 * Human Resources/Interview/New Interview
 * Human Resources/Interview/All Interviews/Selected Candidates
 * Human Resources/Interview/All Interviews/Cancel Candidates
 * Human Resources/Interview/All Interviews/Rejected Candidates
 * Human Resources/Interview/All Interviews/Scheduled Candidates
 * Human Resources/Configuration/Candidate Experience

.. i18n: Views
.. i18n: -----
..

Views
-----

.. i18n:  * cand.categ.search (form)
.. i18n:  * cand.categ.tree (tree)
.. i18n:  * hr.interview.tree (tree)
.. i18n:  * hr.interview.form (form)
.. i18n:  * technical.skill.form (form)
.. i18n:  * technical.skill.tree (tree)
.. i18n:  * candidate.experience.form (form)
.. i18n:  * candidate.experience.tree (tree)
.. i18n:  * category.question.form (form)
.. i18n:  * category.question.tree (tree)
.. i18n:  * hr.interview.log.form (form)
.. i18n:  * hr.interview.log.tree (tree)
..

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

.. i18n: Objects
.. i18n: -------
..

Objects
-------

.. i18n: Object: Category Of Candidate (candidate.category)
.. i18n: ##################################################
..

Object: Category Of Candidate (candidate.category)
##################################################

.. i18n: :code: Code, char, required
..

:code: Code, char, required

.. i18n: :question_ids: Question, one2many
..

:question_ids: Question, one2many

.. i18n: :name: Name, char, required
..

:name: Name, char, required

.. i18n: Object: Question Category (Question Belongs to Which Category) (category.question)
.. i18n: ##################################################################################
..

Object: Question Category (Question Belongs to Which Category) (category.question)
##################################################################################

.. i18n: :tot_marks: Total Marks, integer, required
..

:tot_marks: Total Marks, integer, required

.. i18n: :name: Question, char, required
..

:name: Question, char, required

.. i18n: :category_id: Category, many2one
..

:category_id: Category, many2one

.. i18n: Object: Candidate Experience (candidate.experience)
.. i18n: ###################################################
..

Object: Candidate Experience (candidate.experience)
###################################################

.. i18n: :code: Code, char, required
..

:code: Code, char, required

.. i18n: :name: Name, char, required
..

:name: Name, char, required

.. i18n: :special: Specialization, char
..

:special: Specialization, char

.. i18n: Object: Interview Evaluation (hr.interview)
.. i18n: ###########################################
..

Object: Interview Evaluation (hr.interview)
###########################################

.. i18n: :evaluator_ids: Evaluator, many2many
..

:evaluator_ids: Evaluator, many2many

.. i18n: :history_log_ids: Interview Logs, one2many, readonly
..

:history_log_ids: Interview Logs, one2many, readonly

.. i18n: :name: Candidate Name, char, required
..

:name: Candidate Name, char, required

.. i18n: :performance: Performance (%), float, readonly
..

:performance: Performance (%), float, readonly

.. i18n: :tech_skills_ids: Technology Skills, one2many
..

:tech_skills_ids: Technology Skills, one2many

.. i18n: :mobile_no: Mobile, char
..

:mobile_no: Mobile, char

.. i18n: :category_id: Category, many2one
..

:category_id: Category, many2one

.. i18n: :remarks: Remarks, text
..

:remarks: Remarks, text

.. i18n: :state: State, selection, readonly
..

:state: State, selection, readonly

.. i18n: :reference_id: Reference, many2one
..

:reference_id: Reference, many2one

.. i18n: :experience_id: Experience, many2one
..

:experience_id: Experience, many2one

.. i18n: :date: Scheduled Date, datetime
..

:date: Scheduled Date, datetime

.. i18n: :exam_date: Exam On, datetime
..

:exam_date: Exam On, datetime

.. i18n: :crm_case_id: Case, many2one
..

:crm_case_id: Case, many2one

.. i18n: :education: Education, selection
..

:education: Education, selection

.. i18n: :email: E-mail, char, required
..

:email: E-mail, char, required

.. i18n: :hr_id: Interview ID, char
..

:hr_id: Interview ID, char

.. i18n: Object: Technical Skill Of Candidate (technical.skill)
.. i18n: ######################################################
..

Object: Technical Skill Of Candidate (technical.skill)
######################################################

.. i18n: :remarks: Remarks, text
..

:remarks: Remarks, text

.. i18n: :obt_marks: Obtained Marks, float
..

:obt_marks: Obtained Marks, float

.. i18n: :tot_marks: Total Marks, float, required
..

:tot_marks: Total Marks, float, required

.. i18n: :candidate_id: Candidate ID, many2one
..

:candidate_id: Candidate ID, many2one

.. i18n: :name: Category, char, required
..

:name: Category, char, required

.. i18n: Object: HR interview log (hr.interview.log)
.. i18n: ###########################################
..

Object: HR interview log (hr.interview.log)
###########################################

.. i18n: :date: Date, datetime
..

:date: Date, datetime

.. i18n: :history_id: History ID, many2one
..

:history_id: History ID, many2one

.. i18n: :user_id: User Name, many2one
..

:user_id: User Name, many2one

.. i18n: :state: State, char
..

:state: State, char
