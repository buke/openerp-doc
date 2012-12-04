
.. index::
   single: recruitments
..

Talent Acquisition
==================

Using OpenERP, you can efficiently manage the process of hiring new people for your organization.
It is a well managed recruitment process from initial contact to hiring the applicant.

.. index::
   single: module; hr_recruitment

You need to install :mod:`hr_recruitment` module to efficiently manage the recruitment process.
The configuration wizard to install this module is shown below:

.. figure::  images/config_wiz_recruitment.png
   :scale: 75
   :align: center

   *Configuration wizard to install hr_recruitment module*

The :guilabel:`Applicants` form can be seen from the menu :menuselection:`Human Resources --> Recruitment --> Applicants`.

.. figure::  images/recruitment_applicant_form.png
   :scale: 75
   :align: center

   *Applicant recruitment form*

You can manage the following information using the Applicants form:

* :guilabel:`Applicant's Name`
* :guilabel:`Applied Job`
* :guilabel:`Department`
* :guilabel:`Stage`: can be ``Initial Job Demand``, ``Salary Negotiation``, ...
* :guilabel:`Responsible`: Responsible person who conducts the interview
* :guilabel:`Contact` information
* :guilabel:`Contract Data`: including Availability, Expected Salary, Proposed Salary
* :guilabel:`Qualification` of the applicant
* :guilabel:`State`: reflects the actual status of the recruitment process like ``New``, ``In Progress``, ``Pending``, ``Refused`` or ``Hired``

Initially, the applicant state is ``New``, after that it can be converted to ``In Progress``.
If the applicant is at one of the different stages like it may be in `Waiting for approval by human resource department` or `Waiting for offer acceptance by applicant`,
in these cases, the applicant state should be ``Pending``. When the status is ``Hired``, you can find that applicant's detail from the list of employees.

The information about the :guilabel:`Job Position` can be maintained by the menu :menuselection:`Human Resources --> Recruitment --> Job Positions`.

.. figure::  images/recruitment_job_position.png
   :scale: 75
   :align: center

   *Job Positions in the organization*

The key features of OpenERP for the process of hiring new people using :mod:`hr_recruitment` module are:

* It manages job positions and the recruitment process.
* It is integrated with the :mod:`survey` module to allow you to define interviews for different jobs.
* This module is integrated with the mail gateway to automatically track emails
  sent to jobs@yourcompany.com.
* It is also integrated with the document management system to store and search CVs in your CV base.

You can analyse data of recruitment process through the menu :menuselection:`Human Resources --> Reporting --> Recruitment Analysis`.

.. index::
   single: recruitments; create applicants from e-mail

Create applicants automatically based on incoming mail and keep track of attachments such as resumes and cover letters
----------------------------------------------------------------------------------------------------------------------

You have seen how to create new applicants from the `Applicants` form. You can also configure your email server in OpenERP to create new applicants based on incoming mails. For example, if you have an e-mail ID ``jobs@yourcompany.com``, you can configure it such that all emails received at this ID automatically generate new job applicants.

For this, you have to install the :mod:`fetchmail` module by using the :guilabel:`Reconfigure` wizard and configuring :guilabel:`Fetch Emails` for installation in the `CRM Application Configuration` section. 

Navigate to :menuselection:`Sales --> Configuration --> Emails --> Email Servers` and click :guilabel:`New`. Supply the following information in the `Email Servers` form:

* :guilabel:`Name` : A name for the server configuration.
* :guilabel:`Server Type` : Either ``POP Server`` or ``IMAP Server``.
* :guilabel:`Add Attachment` : Set to ``True``, to be able to retrieve attachments like CVs, cover letters, etc.
* :guilabel:`Server` : Server name.
* :guilabel:`Port` : Server port.
* :guilabel:`User Name` : The username on this e-mail server.
* :guilabel:`Password` : The password for access to this e-mail account.
* :guilabel:`Model` : The object model for which you wish to generate a record. Select ``Applicant`` (hr.applicant) in this case.

.. figure::  images/recruitment_config_server.png
   :scale: 75
   :align: center

   *Configuring an e-mail server*

After configuring your server, click the :guilabel:`Confirm` button to enable this configuration and start receiving e-mails.

Whenever you receive a new e-mail at the configured e-mail address, a new applicant record is created having the same subject name as the e-mail subject. The applicants e-mail details are stored too, for future correspondence. You can add more details to this job application. You can view these newly created applicants from :menuselection:`Human Resources --> Recruitment --> Applicants` and by clicking the :guilabel:`Clear` button to clear all filters. In the figure :ref:`ejob`, the top three applicants have been created automatically from received e-mails.

.. _ejob:

.. figure::  images/recruitment_from_email.png
   :scale: 70
   :align: center

   *Job applicants automatically created from e-mails*

Because you have configured your server to add attachments, if an incoming applicant e-mail contains attachments, it will be linked to the corresponding applicant record. You can find it in the :guilabel:`Attachments` section at the right of the applicant form. You can click on the attachment name to open it.

.. figure::  images/recruitment_email_attach.png
   :scale: 70
   :align: center

   *Applicant form with its corresponding attachments*

.. index::
   single: recruitments; stages

Define stages to track the progress in the recruitment process
--------------------------------------------------------------

Rarely will a recruitment process end after just a single meeting or a phone call. It is in fact a string of stages through which a recruitment progresses in order to bear a favourable outcome. You can define the stages which a recruitment process would undergo. Use the menu :menuselection:`Human Resources --> Configuration --> Recruitment --> Stages` to define various stages.

.. figure::  images/recruitment_stages.png
   :scale: 75
   :align: center

   *Defining recruitment stages*

You must give the stage a :guilabel:`Name`. Use the :guilabel:`Sequence` field to give a sequence order when displaying a list of stages. You may also associate the stage with a :guilabel:`Department`. The stages that you have defined then become available in the `Applicants` form's `Stage` field. Using this, you can qualify an ongoing recruitment process from one stage to another.

.. index::
   single: recruitments; next action

Define next action and next action dates
----------------------------------------

The :guilabel:`Next Action Date` and :guilabel:`Next Action` fields on the `Applicants` form let you define an action you would like to initiate on a given date. It serves as a reminder to the recruitment officer regarding what step he must take next and on which date.

.. index::
   single: recruitments; communication history

Track the history of the e-mail communication with the applicant
----------------------------------------------------------------

Using the :guilabel:`Communication & History` tab in the `Applicants` form, you can add notes for internal reference or send e-mails to the applicant. You can also view the history of communication and notes for a recruitment application in the `History` section. If you specify e-mail addresses in the :guilabel:`Global CC` field, these e-mail addresses will be added to the :guilabel:`CC` field of all inbound and outbound e-mails for this record before being sent. You can separate multiple e-mail addresses with a comma.

To create an internal note, click the :guilabel:`Add Internal Note` button. Add a note description in the popup that appears. You also have a choice to change the application state at this stage. Click :guilabel:`Add` to save the note and see it listed in the `History` section.

To send an e-mail to the applicant, click the :guilabel:`Send New Email` button. In the popup, you must enter the following:

* :guilabel:`From` : E-mail address used to send an e-mail.
* :guilabel:`Reply To` : E-mail address for receiving a reply.
* :guilabel:`To` : The applicants e-mail address
* :guilabel:`Subject` : Subject of the e-mail. By default, it takes the subject of the recruitment application.
* :guilabel:`Message` : The message to send in the e-mail.

.. figure::  images/recruitment_send_mail.png
   :scale: 75
   :align: center

   *Send an e-mail to the applicant*

Here too, you have a choice to change the application state. You may also add attachments through the :guilabel:`Attachments` tab in the popup. Click :guilabel:`Send` to send the e-mail. You can see a listing of the correspondence as shown in the figure below:

.. figure::  images/recruitment_comm_history.png
   :scale: 75
   :align: center

   *History of communication for the recruitment application*

.. index::
   single: recruitments; phone calls
   single: recruitments; appointments

Plan phone calls or appointments
--------------------------------

One of the advantages of using the :mod:`hr_recruitment` module is that you can plan and organise phone calls to and appointments with prospective employees. This is made possible due to its integration with :mod:`crm` module's Phone Calls and Meetings features.

You can schedule a phone call from the `Applicants` form by clicking the :guilabel:`Phone Call` button. This brings up a popup as shown below:

.. figure::  images/recruitment_sched_phone.png
   :scale: 75
   :align: center

   *Schedule an outbound phone call to an applicant*

You can enter the following details in the popup:

* :guilabel:`Assign To` : The user who is responsible for making the call.
* :guilabel:`Planned Date` : The scheduled date and time to make the call.
* :guilabel:`Goals` : The agenda of the phone call.
* :guilabel:`Category` : Whether the call is ``Outbound`` (default) or ``Inbound``.

You can then click the :guilabel:`Schedule Phone Call` button to create a plan for making the call. If the :guilabel:`Category` of your phone call is ``Outbound``, the `Outbound` form opens where you may add additional details. Once you have made the phone call, you can enter the :guilabel:`Duration` as well and click the :guilabel:`Held` button. You can track and evolve your plans of phone calls to an applicant from :menuselection:`Sales --> Phone Calls --> Outbound`.

.. figure::  images/recruitment_outbound_phone.png
   :scale: 75
   :align: center

   *Details of an outbound phone call to an applicant*

Just like you schedule phone calls, you can also schedule meetings with an applicant. To do this, click the :guilabel:`Meeting` button on the `Applicants` form. A calendar of meetings opens in the `Meetings` form. Here, you click an empty area on a date for which you wish to schedule the meeting. A popup appears as shown below:

.. figure::  images/recruitment_sched_meeting.png
   :scale: 75
   :align: center

   *Schedule a meeting with an applicant*

You can manage the following details from this form:

* :guilabel:`Summary` : Is the recruitment application subject by default, although you can change it.
* :guilabel:`Start Date` : The scheduled start date and time.
* :guilabel:`End Date` : The scheduled end date and time.
* :guilabel:`Duration` : The duration of the meeting in hours.
* :guilabel:`Location` : Location of the meeting.
* :guilabel:`Reminder` : If you want to be reminded about the meeting, you can select an alarm time before the event occurs.
* :guilabel:`Description` : You may specify the agenda of the meeting here.

On the :guilabel:`Invitation Detail` tab, you also have the choice to invite people for the meeting. Click :guilabel:`Save` once you have entered the necessary details. You can then see the meeting appear in the calendar as shown below:

.. figure::  images/recruitment_calendar_meeting.png
   :scale: 75
   :align: center

   *The scheduled meeting "Trainee - MCA" with the applicant as seen in the calendar*

You can track and edit your meetings with applicants from the menu :menuselection:`Sales --> Meetings --> Meetings`. By default, you will see the month-wise calendar view of meetings.

.. index::
   single: recruitments; questionnaires
   single: recruitments; survey

Fill questionnaires for each applicant (for instance preliminary questionnaires)
--------------------------------------------------------------------------------

You can use questionnaires as a tool to interview a job applicant. To be able to use questionnaires for a job applicant you must first define one through :menuselection:`Tools --> Surveys --> Define Surveys --> Survey`. Click :guilabel:`New` to open a new survey form. You may enter the :guilabel:`Survey Title` and the :guilabel:`Responsible` user for the survey.

.. figure::  images/recruitment_job_survey.png
   :scale: 75
   :align: center

   *The survey form*

A survey may have multiple pages. Each page may contain multiple questions and each question may have multiple answers. Different users may give different answers to the questions. You can define these in the :guilabel:`Survey` tab of the form. When you have entered the necessary details in the form, click :guilabel:`Save`. Since you will use this survey in a job interview, click the :guilabel:`Open` button to change the survey's state from ``Draft`` to ``Open``.

Then, go to :menuselection:`Human Resources --> Recruitment --> Job Positions` and select the job position that the applicant has applied for, or create a new job position. In the :guilabel:`Survey` field of the `Job Positions` form, enter the name of the survey you have just created, thus linking a questionnaire with this job profile and making it available for use during the interview.

You can now open the form of the applicant whose interview you wish to initiate. If an :guilabel:`Applied Job` is specified to which a survey is linked, the :guilabel:`Answer` button becomes accessible. Click it to initiate the survey, and fill in the applicant's response as you proceed. After the questionnaire has been completed, you can click the :guilabel:`Interview` button on the `Applicants` form to view the applicant's response in a PDF file.

.. figure::  images/recruitment_survey_answers.png
   :scale: 75
   :align: center

   *The applicant's response in a PDF file*

.. Copyright © Open Object Press. All rights reserved.

.. You may take electronic copy of this publication and distribute it if you don't
.. change the content. You can also print a copy to be read by yourself only.

.. We have contracts with different publishers in different countries to sell and
.. distribute paper or electronic based versions of this book (translated or not)
.. in bookstores. This helps to distribute and promote the OpenERP product. It
.. also helps us to create incentives to pay contributors and authors using author
.. rights of these sales.

.. Due to this, grants to translate, modify or sell this book are strictly
.. forbidden, unless Tiny SPRL (representing Open Object Press) gives you a
.. written authorisation for this.

.. Many of the designations used by manufacturers and suppliers to distinguish their
.. products are claimed as trademarks. Where those designations appear in this book,
.. and Open Object Press was aware of a trademark claim, the designations have been
.. printed in initial capitals.

.. While every precaution has been taken in the preparation of this book, the publisher
.. and the authors assume no responsibility for errors or omissions, or for damages
.. resulting from the use of the information contained herein.

.. Published by Open Object Press, Grand Rosière, Belgium
