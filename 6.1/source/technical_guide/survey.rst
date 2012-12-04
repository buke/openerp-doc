
.. module:: survey
    :synopsis: Survey Module 
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

    <div class="js-kit-rating" title="" permalink="" standalone="yes" path="/survey"></div>
    <script src="http://js-kit.com/ratings.js"></script>

Survey Module (*survey*)
========================
:Module: survey
:Name: Survey Module
:Version: 5.0.1.0
:Author: Tiny
:Directory: survey
:Web: 
:Official module: no
:Quality certified: no

Description
-----------

::

  This module is used for surveys. It depends on the answers or reviews of some questions by different users.
      A survey may have multiple pages. Each page may contain multiple questions and each question may have multiple answers.
      Different users may give different answers of question and according to that survey is done. 
      Partners are also sent mails with user name and password for the invitation of the survey

Download links
--------------

You can download this module as a zip file in the following version:

(No download links available)


Dependencies
------------

 * :mod:`base`

Reports
-------

 * Survey Analysis Report1

Menus
-------

 * Survey Management
 * Survey Management/Configuration
 * Survey Management/Configuration/Surveys
 * Survey Management/Configuration/Surveys/New Survey
 * Survey Management/Configuration/Survey Pages
 * Survey Management/Configuration/Survey Pages/New Survey Page
 * Survey Management/Configuration/Survey Questions
 * Survey Management/Configuration/Survey Questions/New Survey Question
 * Survey Management/Give Survey Response

Views
-----

 * survey_form (form)
 * survey_tree (tree)
 * survey_page_form (form)
 * survey_page_tree (tree)
 * survey_question_form (form)
 * survey_question_tree (tree)
 * survey_answer_form (form)
 * survey_answer_tree (tree)
 * survey_response_form (form)
 * survey_response_tree (tree)
 * survey_response_answer_form (form)
 * survey_response_answer_tree (tree)
 * survey_question_column_heading_form (form)
 * survey_question_column_heading_tree (tree)
 * \* INHERIT view.res.users.form (form)
 * Survey Question (form)
 * Survey (form)


Objects
-------

Object: Survey (survey)
#######################



:users: Users, many2many





:date_open: Survey Open Date, datetime, readonly





:title: Survey Title, char, required





:responsible_id: Responsible, many2one





:page_ids: Page, one2many





:tot_comp_survey: Total Completed Survey, integer, readonly





:date_close: Survey Close Date, datetime, readonly





:note: Description, text





:state: Status, selection, readonly





:max_response_limit: Maximum Response Limit, integer





:tot_start_survey: Total Started Survey, integer, readonly





:response_user: Maximum Response per User, integer

    *Set to one if  you require only one response per user*



:history: History Lines, one2many, readonly




Object: Survey History (survey.history)
#######################################



:date: Date started, datetime, readonly





:survey_id: Survey, many2one





:user_id: User, many2one, readonly




Object: Survey Pages (survey.page)
##################################



:note: Description, text





:survey_id: Survey, many2one





:sequence: Sequence, integer





:question_ids: Question, one2many





:title: Page Title, char, required




Object: Survey Question (survey.question)
#########################################



:comment_maximum_float: Maximum decimal number, float





:required_type: Respondent must answer, selection





:comment_valid_type: Text Validation, selection





:comment_maximum_date: Maximum date, date





:make_comment_field_err_msg: Error message, text





:numeric_required_sum_err_msg: Error message, text





:tot_resp: Total Response, float, readonly





:req_ans: #Required Answer, integer





:validation_valid_err_msg: Error message, text





:rating_allow_one_column_require: Allow Only One Response per Column (Forced Ranking), boolean





:validation_minimum_date: Minimum date, date





:comment_minimum_date: Minimum date, date





:req_error_msg: Error Message, text





:sequence: Sequence, integer





:question: Question, char, required





:validation_maximum_date: Maximum date, date





:comment_field_type: Comment Field Type, selection





:is_require_answer: Required Answer, boolean





:comment_minimum_no: Minimum number, integer





:validation_maximum_no: Maximum number, integer





:make_comment_field: Make Comment Field an Answer Choice, boolean





:type: Question Type, selection, required





:column_heading_ids:  Column heading, one2many





:response_ids: Response, one2many, readonly





:minimum_req_ans: Minimum Required Answer, integer





:comment_minimum_float: Minimum decimal number, float





:comment_valid_err_msg: Error message, text





:in_visible_single_text: Is Single Text Invisible?, boolean





:validation_maximum_float: Maximum decimal number, float





:validation_minimum_no: Minimum number, integer





:answer_choice_ids: Answer, one2many





:descriptive_text: Descriptive Text, text





:maximum_req_ans: Maximum Required Answer, integer





:comment_maximum_no: Maximum number, integer





:numeric_required_sum: Sum of all choices, integer





:in_visible_menu_choice: Is Menu Choice Invisible?, boolean





:validation_minimum_float: Minimum decimal number, float





:page_id: Survey Page, many2one, required





:validation_type: Text Validation, selection





:comment_label: Field Label, char





:survey: Survey, many2one





:in_visible_rating_weight: Is Rating Scale Invisible?, boolean





:allow_comment: Allow Comment Field, boolean




Object: Survey Question Column Heading (survey.question.column.heading)
#######################################################################



:in_visible_menu_choice: Is Menu Choice Invisible??, boolean





:title: Column Heading, char, required





:rating_weight: Weight, integer





:in_visible_rating_weight: Is Rating Scale Invisible ??, boolean





:menu_choice: Menu Choice, text





:question_id: Question, many2one




Object: Survey Answer (survey.answer)
#####################################



:answer: Answer, char, required





:average: #Avg, float, readonly





:sequence: Sequence, integer





:response: #Response, float, readonly





:question_id: Question, many2one




Object: Survey Response (survey.response)
#########################################



:comment: Notes, text





:response_answer_ids: Response Answer, one2many





:single_text: Text, char





:in_visible_single_text: Is Single Text Invisible??, boolean





:date_create: Create Date, datetime, required





:state: Status, selection, readonly





:response_id: User, many2one





:response_type: Response Type, selection





:question_id: Question, many2one




Object: Survey Response Answer (survey.response.answer)
#######################################################



:answer: Value, char





:comment: Notes, text





:value_choice: Value Choice, char





:response_id: Response, many2one





:answer_id: Answer, many2one, required




Object: survey.name.wiz (survey.name.wiz)
#########################################



:transfer: Page Transfer, boolean





:note: Description, text





:store_ans: Store Answer, text





:survey_id: Survey, selection, required





:page: Page Position, char





:page_no: Page Number, integer




Object: survey.question.wiz (survey.question.wiz)
#################################################



:name: Number, integer


