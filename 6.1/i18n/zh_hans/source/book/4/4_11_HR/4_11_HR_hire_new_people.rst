
.. i18n: .. index::
.. i18n:    single: recruitments
.. i18n: ..
..

.. index::
   single: recruitments
..

.. i18n: Talent Acquisition
.. i18n: ==================
..

Talent Acquisition
==================

.. i18n: Using OpenERP, you can efficiently manage the process of hiring new people for your organization.
.. i18n: It is a well managed recruitment process from initial contact to hiring the applicant.
..

Using OpenERP, you can efficiently manage the process of hiring new people for your organization.
It is a well managed recruitment process from initial contact to hiring the applicant.

.. i18n: .. index::
.. i18n:    single: module; hr_recruitment
..

.. index::
   single: module; hr_recruitment

.. i18n: You need to install :mod:`hr_recruitment` module to efficiently manage the recruitment process.
.. i18n: The configuration wizard to install this module is shown below:
..

You need to install :mod:`hr_recruitment` module to efficiently manage the recruitment process.
The configuration wizard to install this module is shown below:

.. i18n: .. figure::  images/config_wiz_recruitment.png
.. i18n:    :scale: 75
.. i18n:    :align: center
.. i18n: 
.. i18n:    *Configuration wizard to install hr_recruitment module*
..

.. figure::  images/config_wiz_recruitment.png
   :scale: 75
   :align: center

   *Configuration wizard to install hr_recruitment module*

.. i18n: The :guilabel:`Applicants` form can be seen from the menu :menuselection:`Human Resources --> Recruitment --> Applicants`.
..

The :guilabel:`Applicants` form can be seen from the menu :menuselection:`Human Resources --> Recruitment --> Applicants`.

.. i18n: .. figure::  images/recruitment_applicant_form.png
.. i18n:    :scale: 75
.. i18n:    :align: center
.. i18n: 
.. i18n:    *Applicant recruitment form*
..

.. figure::  images/recruitment_applicant_form.png
   :scale: 75
   :align: center

   *Applicant recruitment form*

.. i18n: You can manage the following information using the Applicants form:
..

You can manage the following information using the Applicants form:

.. i18n: * :guilabel:`Applicant's Name`
.. i18n: * :guilabel:`Applied Job`
.. i18n: * :guilabel:`Department`
.. i18n: * :guilabel:`Stage`: can be ``Initial Job Demand``, ``Salary Negotiation``, ...
.. i18n: * :guilabel:`Responsible`: Responsible person who conducts the interview
.. i18n: * :guilabel:`Contact` information
.. i18n: * :guilabel:`Contract Data`: including Availability, Expected Salary, Proposed Salary
.. i18n: * :guilabel:`Qualification` of the applicant
.. i18n: * :guilabel:`State`: reflects the actual status of the recruitment process like ``New``, ``In Progress``, ``Pending``, ``Refused`` or ``Hired``
..

* :guilabel:`Applicant's Name`
* :guilabel:`Applied Job`
* :guilabel:`Department`
* :guilabel:`Stage`: can be ``Initial Job Demand``, ``Salary Negotiation``, ...
* :guilabel:`Responsible`: Responsible person who conducts the interview
* :guilabel:`Contact` information
* :guilabel:`Contract Data`: including Availability, Expected Salary, Proposed Salary
* :guilabel:`Qualification` of the applicant
* :guilabel:`State`: reflects the actual status of the recruitment process like ``New``, ``In Progress``, ``Pending``, ``Refused`` or ``Hired``

.. i18n: Initially, the applicant state is ``New``, after that it can be converted to ``In Progress``.
.. i18n: If the applicant is at one of the different stages like it may be in `Waiting for approval by human resource department` or `Waiting for offer acceptance by applicant`,
.. i18n: in these cases, the applicant state should be ``Pending``. When the status is ``Hired``, you can find that applicant's detail from the list of employees.
..

Initially, the applicant state is ``New``, after that it can be converted to ``In Progress``.
If the applicant is at one of the different stages like it may be in `Waiting for approval by human resource department` or `Waiting for offer acceptance by applicant`,
in these cases, the applicant state should be ``Pending``. When the status is ``Hired``, you can find that applicant's detail from the list of employees.

.. i18n: The information about the :guilabel:`Job Position` can be maintained by the menu :menuselection:`Human Resources --> Recruitment --> Job Positions`.
..

The information about the :guilabel:`Job Position` can be maintained by the menu :menuselection:`Human Resources --> Recruitment --> Job Positions`.

.. i18n: .. figure::  images/recruitment_job_position.png
.. i18n:    :scale: 75
.. i18n:    :align: center
.. i18n: 
.. i18n:    *Job Positions in the organization*
..

.. figure::  images/recruitment_job_position.png
   :scale: 75
   :align: center

   *Job Positions in the organization*

.. i18n: The key features of OpenERP for the process of hiring new people using :mod:`hr_recruitment` module are:
..

The key features of OpenERP for the process of hiring new people using :mod:`hr_recruitment` module are:

.. i18n: * It manages job positions and the recruitment process.
.. i18n: * It is integrated with the :mod:`survey` module to allow you to define interviews for different jobs.
.. i18n: * This module is integrated with the mail gateway to automatically track emails
.. i18n:   sent to jobs@yourcompany.com.
.. i18n: * It is also integrated with the document management system to store and search CVs in your CV base.
..

* It manages job positions and the recruitment process.
* It is integrated with the :mod:`survey` module to allow you to define interviews for different jobs.
* This module is integrated with the mail gateway to automatically track emails
  sent to jobs@yourcompany.com.
* It is also integrated with the document management system to store and search CVs in your CV base.

.. i18n: You can analyse data of recruitment process through the menu :menuselection:`Human Resources --> Reporting --> Recruitment Analysis`.
..

You can analyse data of recruitment process through the menu :menuselection:`Human Resources --> Reporting --> Recruitment Analysis`.

.. i18n: .. index::
.. i18n:    single: recruitments; create applicants from e-mail
..

.. index::
   single: recruitments; create applicants from e-mail

.. i18n: Create applicants automatically based on incoming mail and keep track of attachments such as resumes and cover letters
.. i18n: ----------------------------------------------------------------------------------------------------------------------
..

Create applicants automatically based on incoming mail and keep track of attachments such as resumes and cover letters
----------------------------------------------------------------------------------------------------------------------

.. i18n: You have seen how to create new applicants from the `Applicants` form. You can also configure your email server in OpenERP to create new applicants based on incoming mails. For example, if you have an e-mail ID ``jobs@yourcompany.com``, you can configure it such that all emails received at this ID automatically generate new job applicants.
..

You have seen how to create new applicants from the `Applicants` form. You can also configure your email server in OpenERP to create new applicants based on incoming mails. For example, if you have an e-mail ID ``jobs@yourcompany.com``, you can configure it such that all emails received at this ID automatically generate new job applicants.

.. i18n: For this, you have to install the :mod:`fetchmail` module by using the :guilabel:`Reconfigure` wizard and configuring :guilabel:`Fetch Emails` for installation in the `CRM Application Configuration` section. 
..

For this, you have to install the :mod:`fetchmail` module by using the :guilabel:`Reconfigure` wizard and configuring :guilabel:`Fetch Emails` for installation in the `CRM Application Configuration` section. 

.. i18n: Navigate to :menuselection:`Sales --> Configuration --> Emails --> Email Servers` and click :guilabel:`New`. Supply the following information in the `Email Servers` form:
..

Navigate to :menuselection:`Sales --> Configuration --> Emails --> Email Servers` and click :guilabel:`New`. Supply the following information in the `Email Servers` form:

.. i18n: * :guilabel:`Name` : A name for the server configuration.
.. i18n: * :guilabel:`Server Type` : Either ``POP Server`` or ``IMAP Server``.
.. i18n: * :guilabel:`Add Attachment` : Set to ``True``, to be able to retrieve attachments like CVs, cover letters, etc.
.. i18n: * :guilabel:`Server` : Server name.
.. i18n: * :guilabel:`Port` : Server port.
.. i18n: * :guilabel:`User Name` : The username on this e-mail server.
.. i18n: * :guilabel:`Password` : The password for access to this e-mail account.
.. i18n: * :guilabel:`Model` : The object model for which you wish to generate a record. Select ``Applicant`` (hr.applicant) in this case.
..

* :guilabel:`Name` : A name for the server configuration.
* :guilabel:`Server Type` : Either ``POP Server`` or ``IMAP Server``.
* :guilabel:`Add Attachment` : Set to ``True``, to be able to retrieve attachments like CVs, cover letters, etc.
* :guilabel:`Server` : Server name.
* :guilabel:`Port` : Server port.
* :guilabel:`User Name` : The username on this e-mail server.
* :guilabel:`Password` : The password for access to this e-mail account.
* :guilabel:`Model` : The object model for which you wish to generate a record. Select ``Applicant`` (hr.applicant) in this case.

.. i18n: .. figure::  images/recruitment_config_server.png
.. i18n:    :scale: 75
.. i18n:    :align: center
.. i18n: 
.. i18n:    *Configuring an e-mail server*
..

.. figure::  images/recruitment_config_server.png
   :scale: 75
   :align: center

   *Configuring an e-mail server*

.. i18n: After configuring your server, click the :guilabel:`Confirm` button to enable this configuration and start receiving e-mails.
..

After configuring your server, click the :guilabel:`Confirm` button to enable this configuration and start receiving e-mails.

.. i18n: Whenever you receive a new e-mail at the configured e-mail address, a new applicant record is created having the same subject name as the e-mail subject. The applicants e-mail details are stored too, for future correspondence. You can add more details to this job application. You can view these newly created applicants from :menuselection:`Human Resources --> Recruitment --> Applicants` and by clicking the :guilabel:`Clear` button to clear all filters. In the figure :ref:`ejob`, the top three applicants have been created automatically from received e-mails.
..

Whenever you receive a new e-mail at the configured e-mail address, a new applicant record is created having the same subject name as the e-mail subject. The applicants e-mail details are stored too, for future correspondence. You can add more details to this job application. You can view these newly created applicants from :menuselection:`Human Resources --> Recruitment --> Applicants` and by clicking the :guilabel:`Clear` button to clear all filters. In the figure :ref:`ejob`, the top three applicants have been created automatically from received e-mails.

.. i18n: .. _ejob:
.. i18n: 
.. i18n: .. figure::  images/recruitment_from_email.png
.. i18n:    :scale: 70
.. i18n:    :align: center
.. i18n: 
.. i18n:    *Job applicants automatically created from e-mails*
..

.. _ejob:

.. figure::  images/recruitment_from_email.png
   :scale: 70
   :align: center

   *Job applicants automatically created from e-mails*

.. i18n: Because you have configured your server to add attachments, if an incoming applicant e-mail contains attachments, it will be linked to the corresponding applicant record. You can find it in the :guilabel:`Attachments` section at the right of the applicant form. You can click on the attachment name to open it.
..

Because you have configured your server to add attachments, if an incoming applicant e-mail contains attachments, it will be linked to the corresponding applicant record. You can find it in the :guilabel:`Attachments` section at the right of the applicant form. You can click on the attachment name to open it.

.. i18n: .. figure::  images/recruitment_email_attach.png
.. i18n:    :scale: 70
.. i18n:    :align: center
.. i18n: 
.. i18n:    *Applicant form with its corresponding attachments*
..

.. figure::  images/recruitment_email_attach.png
   :scale: 70
   :align: center

   *Applicant form with its corresponding attachments*

.. i18n: .. index::
.. i18n:    single: recruitments; stages
..

.. index::
   single: recruitments; stages

.. i18n: Define stages to track the progress in the recruitment process
.. i18n: --------------------------------------------------------------
..

Define stages to track the progress in the recruitment process
--------------------------------------------------------------

.. i18n: Rarely will a recruitment process end after just a single meeting or a phone call. It is in fact a string of stages through which a recruitment progresses in order to bear a favourable outcome. You can define the stages which a recruitment process would undergo. Use the menu :menuselection:`Human Resources --> Configuration --> Recruitment --> Stages` to define various stages.
..

Rarely will a recruitment process end after just a single meeting or a phone call. It is in fact a string of stages through which a recruitment progresses in order to bear a favourable outcome. You can define the stages which a recruitment process would undergo. Use the menu :menuselection:`Human Resources --> Configuration --> Recruitment --> Stages` to define various stages.

.. i18n: .. figure::  images/recruitment_stages.png
.. i18n:    :scale: 75
.. i18n:    :align: center
.. i18n: 
.. i18n:    *Defining recruitment stages*
..

.. figure::  images/recruitment_stages.png
   :scale: 75
   :align: center

   *Defining recruitment stages*

.. i18n: You must give the stage a :guilabel:`Name`. Use the :guilabel:`Sequence` field to give a sequence order when displaying a list of stages. You may also associate the stage with a :guilabel:`Department`. The stages that you have defined then become available in the `Applicants` form's `Stage` field. Using this, you can qualify an ongoing recruitment process from one stage to another.
..

You must give the stage a :guilabel:`Name`. Use the :guilabel:`Sequence` field to give a sequence order when displaying a list of stages. You may also associate the stage with a :guilabel:`Department`. The stages that you have defined then become available in the `Applicants` form's `Stage` field. Using this, you can qualify an ongoing recruitment process from one stage to another.

.. i18n: .. index::
.. i18n:    single: recruitments; next action
..

.. index::
   single: recruitments; next action

.. i18n: Define next action and next action dates
.. i18n: ----------------------------------------
..

Define next action and next action dates
----------------------------------------

.. i18n: The :guilabel:`Next Action Date` and :guilabel:`Next Action` fields on the `Applicants` form let you define an action you would like to initiate on a given date. It serves as a reminder to the recruitment officer regarding what step he must take next and on which date.
..

The :guilabel:`Next Action Date` and :guilabel:`Next Action` fields on the `Applicants` form let you define an action you would like to initiate on a given date. It serves as a reminder to the recruitment officer regarding what step he must take next and on which date.

.. i18n: .. index::
.. i18n:    single: recruitments; communication history
..

.. index::
   single: recruitments; communication history

.. i18n: Track the history of the e-mail communication with the applicant
.. i18n: ----------------------------------------------------------------
..

Track the history of the e-mail communication with the applicant
----------------------------------------------------------------

.. i18n: Using the :guilabel:`Communication & History` tab in the `Applicants` form, you can add notes for internal reference or send e-mails to the applicant. You can also view the history of communication and notes for a recruitment application in the `History` section. If you specify e-mail addresses in the :guilabel:`Global CC` field, these e-mail addresses will be added to the :guilabel:`CC` field of all inbound and outbound e-mails for this record before being sent. You can separate multiple e-mail addresses with a comma.
..

Using the :guilabel:`Communication & History` tab in the `Applicants` form, you can add notes for internal reference or send e-mails to the applicant. You can also view the history of communication and notes for a recruitment application in the `History` section. If you specify e-mail addresses in the :guilabel:`Global CC` field, these e-mail addresses will be added to the :guilabel:`CC` field of all inbound and outbound e-mails for this record before being sent. You can separate multiple e-mail addresses with a comma.

.. i18n: To create an internal note, click the :guilabel:`Add Internal Note` button. Add a note description in the popup that appears. You also have a choice to change the application state at this stage. Click :guilabel:`Add` to save the note and see it listed in the `History` section.
..

To create an internal note, click the :guilabel:`Add Internal Note` button. Add a note description in the popup that appears. You also have a choice to change the application state at this stage. Click :guilabel:`Add` to save the note and see it listed in the `History` section.

.. i18n: To send an e-mail to the applicant, click the :guilabel:`Send New Email` button. In the popup, you must enter the following:
..

To send an e-mail to the applicant, click the :guilabel:`Send New Email` button. In the popup, you must enter the following:

.. i18n: * :guilabel:`From` : E-mail address used to send an e-mail.
.. i18n: * :guilabel:`Reply To` : E-mail address for receiving a reply.
.. i18n: * :guilabel:`To` : The applicants e-mail address
.. i18n: * :guilabel:`Subject` : Subject of the e-mail. By default, it takes the subject of the recruitment application.
.. i18n: * :guilabel:`Message` : The message to send in the e-mail.
..

* :guilabel:`From` : E-mail address used to send an e-mail.
* :guilabel:`Reply To` : E-mail address for receiving a reply.
* :guilabel:`To` : The applicants e-mail address
* :guilabel:`Subject` : Subject of the e-mail. By default, it takes the subject of the recruitment application.
* :guilabel:`Message` : The message to send in the e-mail.

.. i18n: .. figure::  images/recruitment_send_mail.png
.. i18n:    :scale: 75
.. i18n:    :align: center
.. i18n: 
.. i18n:    *Send an e-mail to the applicant*
..

.. figure::  images/recruitment_send_mail.png
   :scale: 75
   :align: center

   *Send an e-mail to the applicant*

.. i18n: Here too, you have a choice to change the application state. You may also add attachments through the :guilabel:`Attachments` tab in the popup. Click :guilabel:`Send` to send the e-mail. You can see a listing of the correspondence as shown in the figure below:
..

Here too, you have a choice to change the application state. You may also add attachments through the :guilabel:`Attachments` tab in the popup. Click :guilabel:`Send` to send the e-mail. You can see a listing of the correspondence as shown in the figure below:

.. i18n: .. figure::  images/recruitment_comm_history.png
.. i18n:    :scale: 75
.. i18n:    :align: center
.. i18n: 
.. i18n:    *History of communication for the recruitment application*
..

.. figure::  images/recruitment_comm_history.png
   :scale: 75
   :align: center

   *History of communication for the recruitment application*

.. i18n: .. index::
.. i18n:    single: recruitments; phone calls
.. i18n:    single: recruitments; appointments
..

.. index::
   single: recruitments; phone calls
   single: recruitments; appointments

.. i18n: Plan phone calls or appointments
.. i18n: --------------------------------
..

Plan phone calls or appointments
--------------------------------

.. i18n: One of the advantages of using the :mod:`hr_recruitment` module is that you can plan and organise phone calls to and appointments with prospective employees. This is made possible due to its integration with :mod:`crm` module's Phone Calls and Meetings features.
..

One of the advantages of using the :mod:`hr_recruitment` module is that you can plan and organise phone calls to and appointments with prospective employees. This is made possible due to its integration with :mod:`crm` module's Phone Calls and Meetings features.

.. i18n: You can schedule a phone call from the `Applicants` form by clicking the :guilabel:`Phone Call` button. This brings up a popup as shown below:
..

You can schedule a phone call from the `Applicants` form by clicking the :guilabel:`Phone Call` button. This brings up a popup as shown below:

.. i18n: .. figure::  images/recruitment_sched_phone.png
.. i18n:    :scale: 75
.. i18n:    :align: center
.. i18n: 
.. i18n:    *Schedule an outbound phone call to an applicant*
..

.. figure::  images/recruitment_sched_phone.png
   :scale: 75
   :align: center

   *Schedule an outbound phone call to an applicant*

.. i18n: You can enter the following details in the popup:
..

You can enter the following details in the popup:

.. i18n: * :guilabel:`Assign To` : The user who is responsible for making the call.
.. i18n: * :guilabel:`Planned Date` : The scheduled date and time to make the call.
.. i18n: * :guilabel:`Goals` : The agenda of the phone call.
.. i18n: * :guilabel:`Category` : Whether the call is ``Outbound`` (default) or ``Inbound``.
..

* :guilabel:`Assign To` : The user who is responsible for making the call.
* :guilabel:`Planned Date` : The scheduled date and time to make the call.
* :guilabel:`Goals` : The agenda of the phone call.
* :guilabel:`Category` : Whether the call is ``Outbound`` (default) or ``Inbound``.

.. i18n: You can then click the :guilabel:`Schedule Phone Call` button to create a plan for making the call. If the :guilabel:`Category` of your phone call is ``Outbound``, the `Outbound` form opens where you may add additional details. Once you have made the phone call, you can enter the :guilabel:`Duration` as well and click the :guilabel:`Held` button. You can track and evolve your plans of phone calls to an applicant from :menuselection:`Sales --> Phone Calls --> Outbound`.
..

You can then click the :guilabel:`Schedule Phone Call` button to create a plan for making the call. If the :guilabel:`Category` of your phone call is ``Outbound``, the `Outbound` form opens where you may add additional details. Once you have made the phone call, you can enter the :guilabel:`Duration` as well and click the :guilabel:`Held` button. You can track and evolve your plans of phone calls to an applicant from :menuselection:`Sales --> Phone Calls --> Outbound`.

.. i18n: .. figure::  images/recruitment_outbound_phone.png
.. i18n:    :scale: 75
.. i18n:    :align: center
.. i18n: 
.. i18n:    *Details of an outbound phone call to an applicant*
..

.. figure::  images/recruitment_outbound_phone.png
   :scale: 75
   :align: center

   *Details of an outbound phone call to an applicant*

.. i18n: Just like you schedule phone calls, you can also schedule meetings with an applicant. To do this, click the :guilabel:`Meeting` button on the `Applicants` form. A calendar of meetings opens in the `Meetings` form. Here, you click an empty area on a date for which you wish to schedule the meeting. A popup appears as shown below:
..

Just like you schedule phone calls, you can also schedule meetings with an applicant. To do this, click the :guilabel:`Meeting` button on the `Applicants` form. A calendar of meetings opens in the `Meetings` form. Here, you click an empty area on a date for which you wish to schedule the meeting. A popup appears as shown below:

.. i18n: .. figure::  images/recruitment_sched_meeting.png
.. i18n:    :scale: 75
.. i18n:    :align: center
.. i18n: 
.. i18n:    *Schedule a meeting with an applicant*
..

.. figure::  images/recruitment_sched_meeting.png
   :scale: 75
   :align: center

   *Schedule a meeting with an applicant*

.. i18n: You can manage the following details from this form:
..

You can manage the following details from this form:

.. i18n: * :guilabel:`Summary` : Is the recruitment application subject by default, although you can change it.
.. i18n: * :guilabel:`Start Date` : The scheduled start date and time.
.. i18n: * :guilabel:`End Date` : The scheduled end date and time.
.. i18n: * :guilabel:`Duration` : The duration of the meeting in hours.
.. i18n: * :guilabel:`Location` : Location of the meeting.
.. i18n: * :guilabel:`Reminder` : If you want to be reminded about the meeting, you can select an alarm time before the event occurs.
.. i18n: * :guilabel:`Description` : You may specify the agenda of the meeting here.
..

* :guilabel:`Summary` : Is the recruitment application subject by default, although you can change it.
* :guilabel:`Start Date` : The scheduled start date and time.
* :guilabel:`End Date` : The scheduled end date and time.
* :guilabel:`Duration` : The duration of the meeting in hours.
* :guilabel:`Location` : Location of the meeting.
* :guilabel:`Reminder` : If you want to be reminded about the meeting, you can select an alarm time before the event occurs.
* :guilabel:`Description` : You may specify the agenda of the meeting here.

.. i18n: On the :guilabel:`Invitation Detail` tab, you also have the choice to invite people for the meeting. Click :guilabel:`Save` once you have entered the necessary details. You can then see the meeting appear in the calendar as shown below:
..

On the :guilabel:`Invitation Detail` tab, you also have the choice to invite people for the meeting. Click :guilabel:`Save` once you have entered the necessary details. You can then see the meeting appear in the calendar as shown below:

.. i18n: .. figure::  images/recruitment_calendar_meeting.png
.. i18n:    :scale: 75
.. i18n:    :align: center
.. i18n: 
.. i18n:    *The scheduled meeting "Trainee - MCA" with the applicant as seen in the calendar*
..

.. figure::  images/recruitment_calendar_meeting.png
   :scale: 75
   :align: center

   *The scheduled meeting "Trainee - MCA" with the applicant as seen in the calendar*

.. i18n: You can track and edit your meetings with applicants from the menu :menuselection:`Sales --> Meetings --> Meetings`. By default, you will see the month-wise calendar view of meetings.
..

You can track and edit your meetings with applicants from the menu :menuselection:`Sales --> Meetings --> Meetings`. By default, you will see the month-wise calendar view of meetings.

.. i18n: .. index::
.. i18n:    single: recruitments; questionnaires
.. i18n:    single: recruitments; survey
..

.. index::
   single: recruitments; questionnaires
   single: recruitments; survey

.. i18n: Fill questionnaires for each applicant (for instance preliminary questionnaires)
.. i18n: --------------------------------------------------------------------------------
..

Fill questionnaires for each applicant (for instance preliminary questionnaires)
--------------------------------------------------------------------------------

.. i18n: You can use questionnaires as a tool to interview a job applicant. To be able to use questionnaires for a job applicant you must first define one through :menuselection:`Tools --> Surveys --> Define Surveys --> Survey`. Click :guilabel:`New` to open a new survey form. You may enter the :guilabel:`Survey Title` and the :guilabel:`Responsible` user for the survey.
..

You can use questionnaires as a tool to interview a job applicant. To be able to use questionnaires for a job applicant you must first define one through :menuselection:`Tools --> Surveys --> Define Surveys --> Survey`. Click :guilabel:`New` to open a new survey form. You may enter the :guilabel:`Survey Title` and the :guilabel:`Responsible` user for the survey.

.. i18n: .. figure::  images/recruitment_job_survey.png
.. i18n:    :scale: 75
.. i18n:    :align: center
.. i18n: 
.. i18n:    *The survey form*
..

.. figure::  images/recruitment_job_survey.png
   :scale: 75
   :align: center

   *The survey form*

.. i18n: A survey may have multiple pages. Each page may contain multiple questions and each question may have multiple answers. Different users may give different answers to the questions. You can define these in the :guilabel:`Survey` tab of the form. When you have entered the necessary details in the form, click :guilabel:`Save`. Since you will use this survey in a job interview, click the :guilabel:`Open` button to change the survey's state from ``Draft`` to ``Open``.
..

A survey may have multiple pages. Each page may contain multiple questions and each question may have multiple answers. Different users may give different answers to the questions. You can define these in the :guilabel:`Survey` tab of the form. When you have entered the necessary details in the form, click :guilabel:`Save`. Since you will use this survey in a job interview, click the :guilabel:`Open` button to change the survey's state from ``Draft`` to ``Open``.

.. i18n: Then, go to :menuselection:`Human Resources --> Recruitment --> Job Positions` and select the job position that the applicant has applied for, or create a new job position. In the :guilabel:`Survey` field of the `Job Positions` form, enter the name of the survey you have just created, thus linking a questionnaire with this job profile and making it available for use during the interview.
..

Then, go to :menuselection:`Human Resources --> Recruitment --> Job Positions` and select the job position that the applicant has applied for, or create a new job position. In the :guilabel:`Survey` field of the `Job Positions` form, enter the name of the survey you have just created, thus linking a questionnaire with this job profile and making it available for use during the interview.

.. i18n: You can now open the form of the applicant whose interview you wish to initiate. If an :guilabel:`Applied Job` is specified to which a survey is linked, the :guilabel:`Answer` button becomes accessible. Click it to initiate the survey, and fill in the applicant's response as you proceed. After the questionnaire has been completed, you can click the :guilabel:`Interview` button on the `Applicants` form to view the applicant's response in a PDF file.
..

You can now open the form of the applicant whose interview you wish to initiate. If an :guilabel:`Applied Job` is specified to which a survey is linked, the :guilabel:`Answer` button becomes accessible. Click it to initiate the survey, and fill in the applicant's response as you proceed. After the questionnaire has been completed, you can click the :guilabel:`Interview` button on the `Applicants` form to view the applicant's response in a PDF file.

.. i18n: .. figure::  images/recruitment_survey_answers.png
.. i18n:    :scale: 75
.. i18n:    :align: center
.. i18n: 
.. i18n:    *The applicant's response in a PDF file*
..

.. figure::  images/recruitment_survey_answers.png
   :scale: 75
   :align: center

   *The applicant's response in a PDF file*

.. i18n: .. Copyright © Open Object Press. All rights reserved.
..

.. Copyright © Open Object Press. All rights reserved.

.. i18n: .. You may take electronic copy of this publication and distribute it if you don't
.. i18n: .. change the content. You can also print a copy to be read by yourself only.
..

.. You may take electronic copy of this publication and distribute it if you don't
.. change the content. You can also print a copy to be read by yourself only.

.. i18n: .. We have contracts with different publishers in different countries to sell and
.. i18n: .. distribute paper or electronic based versions of this book (translated or not)
.. i18n: .. in bookstores. This helps to distribute and promote the OpenERP product. It
.. i18n: .. also helps us to create incentives to pay contributors and authors using author
.. i18n: .. rights of these sales.
..

.. We have contracts with different publishers in different countries to sell and
.. distribute paper or electronic based versions of this book (translated or not)
.. in bookstores. This helps to distribute and promote the OpenERP product. It
.. also helps us to create incentives to pay contributors and authors using author
.. rights of these sales.

.. i18n: .. Due to this, grants to translate, modify or sell this book are strictly
.. i18n: .. forbidden, unless Tiny SPRL (representing Open Object Press) gives you a
.. i18n: .. written authorisation for this.
..

.. Due to this, grants to translate, modify or sell this book are strictly
.. forbidden, unless Tiny SPRL (representing Open Object Press) gives you a
.. written authorisation for this.

.. i18n: .. Many of the designations used by manufacturers and suppliers to distinguish their
.. i18n: .. products are claimed as trademarks. Where those designations appear in this book,
.. i18n: .. and Open Object Press was aware of a trademark claim, the designations have been
.. i18n: .. printed in initial capitals.
..

.. Many of the designations used by manufacturers and suppliers to distinguish their
.. products are claimed as trademarks. Where those designations appear in this book,
.. and Open Object Press was aware of a trademark claim, the designations have been
.. printed in initial capitals.

.. i18n: .. While every precaution has been taken in the preparation of this book, the publisher
.. i18n: .. and the authors assume no responsibility for errors or omissions, or for damages
.. i18n: .. resulting from the use of the information contained herein.
..

.. While every precaution has been taken in the preparation of this book, the publisher
.. and the authors assume no responsibility for errors or omissions, or for damages
.. resulting from the use of the information contained herein.

.. i18n: .. Published by Open Object Press, Grand Rosière, Belgium
..

.. Published by Open Object Press, Grand Rosière, Belgium
