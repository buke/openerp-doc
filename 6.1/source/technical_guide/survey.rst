
.. i18n: .. module:: survey
.. i18n:     :synopsis: Survey Module 
.. i18n:     :noindex:
.. i18n: .. 
..

.. module:: survey
    :synopsis: Survey Module 
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
.. i18n:     <div class="js-kit-rating" title="" permalink="" standalone="yes" path="/survey"></div>
.. i18n:     <script src="http://js-kit.com/ratings.js"></script>
..

.. raw:: html

    <div class="js-kit-rating" title="" permalink="" standalone="yes" path="/survey"></div>
    <script src="http://js-kit.com/ratings.js"></script>

.. i18n: Survey Module (*survey*)
.. i18n: ========================
.. i18n: :Module: survey
.. i18n: :Name: Survey Module
.. i18n: :Version: 5.0.1.0
.. i18n: :Author: Tiny
.. i18n: :Directory: survey
.. i18n: :Web: 
.. i18n: :Official module: no
.. i18n: :Quality certified: no
..

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

.. i18n: Description
.. i18n: -----------
..

Description
-----------

.. i18n: ::
.. i18n: 
.. i18n:   This module is used for surveys. It depends on the answers or reviews of some questions by different users.
.. i18n:       A survey may have multiple pages. Each page may contain multiple questions and each question may have multiple answers.
.. i18n:       Different users may give different answers of question and according to that survey is done. 
.. i18n:       Partners are also sent mails with user name and password for the invitation of the survey
..

::

  This module is used for surveys. It depends on the answers or reviews of some questions by different users.
      A survey may have multiple pages. Each page may contain multiple questions and each question may have multiple answers.
      Different users may give different answers of question and according to that survey is done. 
      Partners are also sent mails with user name and password for the invitation of the survey

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

.. i18n:  * Survey Analysis Report1
..

 * Survey Analysis Report1

.. i18n: Menus
.. i18n: -------
..

Menus
-------

.. i18n:  * Survey Management
.. i18n:  * Survey Management/Configuration
.. i18n:  * Survey Management/Configuration/Surveys
.. i18n:  * Survey Management/Configuration/Surveys/New Survey
.. i18n:  * Survey Management/Configuration/Survey Pages
.. i18n:  * Survey Management/Configuration/Survey Pages/New Survey Page
.. i18n:  * Survey Management/Configuration/Survey Questions
.. i18n:  * Survey Management/Configuration/Survey Questions/New Survey Question
.. i18n:  * Survey Management/Give Survey Response
..

 * Survey Management
 * Survey Management/Configuration
 * Survey Management/Configuration/Surveys
 * Survey Management/Configuration/Surveys/New Survey
 * Survey Management/Configuration/Survey Pages
 * Survey Management/Configuration/Survey Pages/New Survey Page
 * Survey Management/Configuration/Survey Questions
 * Survey Management/Configuration/Survey Questions/New Survey Question
 * Survey Management/Give Survey Response

.. i18n: Views
.. i18n: -----
..

Views
-----

.. i18n:  * survey_form (form)
.. i18n:  * survey_tree (tree)
.. i18n:  * survey_page_form (form)
.. i18n:  * survey_page_tree (tree)
.. i18n:  * survey_question_form (form)
.. i18n:  * survey_question_tree (tree)
.. i18n:  * survey_answer_form (form)
.. i18n:  * survey_answer_tree (tree)
.. i18n:  * survey_response_form (form)
.. i18n:  * survey_response_tree (tree)
.. i18n:  * survey_response_answer_form (form)
.. i18n:  * survey_response_answer_tree (tree)
.. i18n:  * survey_question_column_heading_form (form)
.. i18n:  * survey_question_column_heading_tree (tree)
.. i18n:  * \* INHERIT view.res.users.form (form)
.. i18n:  * Survey Question (form)
.. i18n:  * Survey (form)
..

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

.. i18n: Objects
.. i18n: -------
..

Objects
-------

.. i18n: Object: Survey (survey)
.. i18n: #######################
..

Object: Survey (survey)
#######################

.. i18n: :users: Users, many2many
..

:users: Users, many2many

.. i18n: :date_open: Survey Open Date, datetime, readonly
..

:date_open: Survey Open Date, datetime, readonly

.. i18n: :title: Survey Title, char, required
..

:title: Survey Title, char, required

.. i18n: :responsible_id: Responsible, many2one
..

:responsible_id: Responsible, many2one

.. i18n: :page_ids: Page, one2many
..

:page_ids: Page, one2many

.. i18n: :tot_comp_survey: Total Completed Survey, integer, readonly
..

:tot_comp_survey: Total Completed Survey, integer, readonly

.. i18n: :date_close: Survey Close Date, datetime, readonly
..

:date_close: Survey Close Date, datetime, readonly

.. i18n: :note: Description, text
..

:note: Description, text

.. i18n: :state: Status, selection, readonly
..

:state: Status, selection, readonly

.. i18n: :max_response_limit: Maximum Response Limit, integer
..

:max_response_limit: Maximum Response Limit, integer

.. i18n: :tot_start_survey: Total Started Survey, integer, readonly
..

:tot_start_survey: Total Started Survey, integer, readonly

.. i18n: :response_user: Maximum Response per User, integer
..

:response_user: Maximum Response per User, integer

.. i18n:     *Set to one if  you require only one response per user*
..

    *Set to one if  you require only one response per user*

.. i18n: :history: History Lines, one2many, readonly
..

:history: History Lines, one2many, readonly

.. i18n: Object: Survey History (survey.history)
.. i18n: #######################################
..

Object: Survey History (survey.history)
#######################################

.. i18n: :date: Date started, datetime, readonly
..

:date: Date started, datetime, readonly

.. i18n: :survey_id: Survey, many2one
..

:survey_id: Survey, many2one

.. i18n: :user_id: User, many2one, readonly
..

:user_id: User, many2one, readonly

.. i18n: Object: Survey Pages (survey.page)
.. i18n: ##################################
..

Object: Survey Pages (survey.page)
##################################

.. i18n: :note: Description, text
..

:note: Description, text

.. i18n: :survey_id: Survey, many2one
..

:survey_id: Survey, many2one

.. i18n: :sequence: Sequence, integer
..

:sequence: Sequence, integer

.. i18n: :question_ids: Question, one2many
..

:question_ids: Question, one2many

.. i18n: :title: Page Title, char, required
..

:title: Page Title, char, required

.. i18n: Object: Survey Question (survey.question)
.. i18n: #########################################
..

Object: Survey Question (survey.question)
#########################################

.. i18n: :comment_maximum_float: Maximum decimal number, float
..

:comment_maximum_float: Maximum decimal number, float

.. i18n: :required_type: Respondent must answer, selection
..

:required_type: Respondent must answer, selection

.. i18n: :comment_valid_type: Text Validation, selection
..

:comment_valid_type: Text Validation, selection

.. i18n: :comment_maximum_date: Maximum date, date
..

:comment_maximum_date: Maximum date, date

.. i18n: :make_comment_field_err_msg: Error message, text
..

:make_comment_field_err_msg: Error message, text

.. i18n: :numeric_required_sum_err_msg: Error message, text
..

:numeric_required_sum_err_msg: Error message, text

.. i18n: :tot_resp: Total Response, float, readonly
..

:tot_resp: Total Response, float, readonly

.. i18n: :req_ans: #Required Answer, integer
..

:req_ans: #Required Answer, integer

.. i18n: :validation_valid_err_msg: Error message, text
..

:validation_valid_err_msg: Error message, text

.. i18n: :rating_allow_one_column_require: Allow Only One Response per Column (Forced Ranking), boolean
..

:rating_allow_one_column_require: Allow Only One Response per Column (Forced Ranking), boolean

.. i18n: :validation_minimum_date: Minimum date, date
..

:validation_minimum_date: Minimum date, date

.. i18n: :comment_minimum_date: Minimum date, date
..

:comment_minimum_date: Minimum date, date

.. i18n: :req_error_msg: Error Message, text
..

:req_error_msg: Error Message, text

.. i18n: :sequence: Sequence, integer
..

:sequence: Sequence, integer

.. i18n: :question: Question, char, required
..

:question: Question, char, required

.. i18n: :validation_maximum_date: Maximum date, date
..

:validation_maximum_date: Maximum date, date

.. i18n: :comment_field_type: Comment Field Type, selection
..

:comment_field_type: Comment Field Type, selection

.. i18n: :is_require_answer: Required Answer, boolean
..

:is_require_answer: Required Answer, boolean

.. i18n: :comment_minimum_no: Minimum number, integer
..

:comment_minimum_no: Minimum number, integer

.. i18n: :validation_maximum_no: Maximum number, integer
..

:validation_maximum_no: Maximum number, integer

.. i18n: :make_comment_field: Make Comment Field an Answer Choice, boolean
..

:make_comment_field: Make Comment Field an Answer Choice, boolean

.. i18n: :type: Question Type, selection, required
..

:type: Question Type, selection, required

.. i18n: :column_heading_ids:  Column heading, one2many
..

:column_heading_ids:  Column heading, one2many

.. i18n: :response_ids: Response, one2many, readonly
..

:response_ids: Response, one2many, readonly

.. i18n: :minimum_req_ans: Minimum Required Answer, integer
..

:minimum_req_ans: Minimum Required Answer, integer

.. i18n: :comment_minimum_float: Minimum decimal number, float
..

:comment_minimum_float: Minimum decimal number, float

.. i18n: :comment_valid_err_msg: Error message, text
..

:comment_valid_err_msg: Error message, text

.. i18n: :in_visible_single_text: Is Single Text Invisible?, boolean
..

:in_visible_single_text: Is Single Text Invisible?, boolean

.. i18n: :validation_maximum_float: Maximum decimal number, float
..

:validation_maximum_float: Maximum decimal number, float

.. i18n: :validation_minimum_no: Minimum number, integer
..

:validation_minimum_no: Minimum number, integer

.. i18n: :answer_choice_ids: Answer, one2many
..

:answer_choice_ids: Answer, one2many

.. i18n: :descriptive_text: Descriptive Text, text
..

:descriptive_text: Descriptive Text, text

.. i18n: :maximum_req_ans: Maximum Required Answer, integer
..

:maximum_req_ans: Maximum Required Answer, integer

.. i18n: :comment_maximum_no: Maximum number, integer
..

:comment_maximum_no: Maximum number, integer

.. i18n: :numeric_required_sum: Sum of all choices, integer
..

:numeric_required_sum: Sum of all choices, integer

.. i18n: :in_visible_menu_choice: Is Menu Choice Invisible?, boolean
..

:in_visible_menu_choice: Is Menu Choice Invisible?, boolean

.. i18n: :validation_minimum_float: Minimum decimal number, float
..

:validation_minimum_float: Minimum decimal number, float

.. i18n: :page_id: Survey Page, many2one, required
..

:page_id: Survey Page, many2one, required

.. i18n: :validation_type: Text Validation, selection
..

:validation_type: Text Validation, selection

.. i18n: :comment_label: Field Label, char
..

:comment_label: Field Label, char

.. i18n: :survey: Survey, many2one
..

:survey: Survey, many2one

.. i18n: :in_visible_rating_weight: Is Rating Scale Invisible?, boolean
..

:in_visible_rating_weight: Is Rating Scale Invisible?, boolean

.. i18n: :allow_comment: Allow Comment Field, boolean
..

:allow_comment: Allow Comment Field, boolean

.. i18n: Object: Survey Question Column Heading (survey.question.column.heading)
.. i18n: #######################################################################
..

Object: Survey Question Column Heading (survey.question.column.heading)
#######################################################################

.. i18n: :in_visible_menu_choice: Is Menu Choice Invisible??, boolean
..

:in_visible_menu_choice: Is Menu Choice Invisible??, boolean

.. i18n: :title: Column Heading, char, required
..

:title: Column Heading, char, required

.. i18n: :rating_weight: Weight, integer
..

:rating_weight: Weight, integer

.. i18n: :in_visible_rating_weight: Is Rating Scale Invisible ??, boolean
..

:in_visible_rating_weight: Is Rating Scale Invisible ??, boolean

.. i18n: :menu_choice: Menu Choice, text
..

:menu_choice: Menu Choice, text

.. i18n: :question_id: Question, many2one
..

:question_id: Question, many2one

.. i18n: Object: Survey Answer (survey.answer)
.. i18n: #####################################
..

Object: Survey Answer (survey.answer)
#####################################

.. i18n: :answer: Answer, char, required
..

:answer: Answer, char, required

.. i18n: :average: #Avg, float, readonly
..

:average: #Avg, float, readonly

.. i18n: :sequence: Sequence, integer
..

:sequence: Sequence, integer

.. i18n: :response: #Response, float, readonly
..

:response: #Response, float, readonly

.. i18n: :question_id: Question, many2one
..

:question_id: Question, many2one

.. i18n: Object: Survey Response (survey.response)
.. i18n: #########################################
..

Object: Survey Response (survey.response)
#########################################

.. i18n: :comment: Notes, text
..

:comment: Notes, text

.. i18n: :response_answer_ids: Response Answer, one2many
..

:response_answer_ids: Response Answer, one2many

.. i18n: :single_text: Text, char
..

:single_text: Text, char

.. i18n: :in_visible_single_text: Is Single Text Invisible??, boolean
..

:in_visible_single_text: Is Single Text Invisible??, boolean

.. i18n: :date_create: Create Date, datetime, required
..

:date_create: Create Date, datetime, required

.. i18n: :state: Status, selection, readonly
..

:state: Status, selection, readonly

.. i18n: :response_id: User, many2one
..

:response_id: User, many2one

.. i18n: :response_type: Response Type, selection
..

:response_type: Response Type, selection

.. i18n: :question_id: Question, many2one
..

:question_id: Question, many2one

.. i18n: Object: Survey Response Answer (survey.response.answer)
.. i18n: #######################################################
..

Object: Survey Response Answer (survey.response.answer)
#######################################################

.. i18n: :answer: Value, char
..

:answer: Value, char

.. i18n: :comment: Notes, text
..

:comment: Notes, text

.. i18n: :value_choice: Value Choice, char
..

:value_choice: Value Choice, char

.. i18n: :response_id: Response, many2one
..

:response_id: Response, many2one

.. i18n: :answer_id: Answer, many2one, required
..

:answer_id: Answer, many2one, required

.. i18n: Object: survey.name.wiz (survey.name.wiz)
.. i18n: #########################################
..

Object: survey.name.wiz (survey.name.wiz)
#########################################

.. i18n: :transfer: Page Transfer, boolean
..

:transfer: Page Transfer, boolean

.. i18n: :note: Description, text
..

:note: Description, text

.. i18n: :store_ans: Store Answer, text
..

:store_ans: Store Answer, text

.. i18n: :survey_id: Survey, selection, required
..

:survey_id: Survey, selection, required

.. i18n: :page: Page Position, char
..

:page: Page Position, char

.. i18n: :page_no: Page Number, integer
..

:page_no: Page Number, integer

.. i18n: Object: survey.question.wiz (survey.question.wiz)
.. i18n: #################################################
..

Object: survey.question.wiz (survey.question.wiz)
#################################################

.. i18n: :name: Number, integer
..

:name: Number, integer
