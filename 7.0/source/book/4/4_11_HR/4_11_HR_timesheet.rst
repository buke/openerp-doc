
.. index::
   single: attendance
   single: timesheet
..

Attendances and Timesheet Management
====================================

In most service companies where OpenERP has been integrated, service sheets, or timesheets, have
revolutionized management practices. These service sheets are produced by each employee as they work
on the different cases or projects that are running. Each of these is represented by an analytic
account in the system.

Throughout the day, when employees work on one project or another, they add a line to the timesheets
with details of the time used on each project. At the end of the day, each employee must mark all
the time worked on client or internal projects to make up the full number of hours worked in the
day. If an account is not in the system, then the time is added to the hours that have not been
assigned for the day.

.. _fig-servtimlis:

.. figure::  images/service_timesheet_list.png
   :scale: 65
   :align: center

   *Timesheet for a working day*

The figure :ref:`fig-servtimlis` gives an example of a timesheet for an employee.

.. index::
   pair: cost; allocation

.. note:: Do not confuse timesheets and attendance compliance

	The timesheet system is not intended to be a disguised attendance form. There is no control over the
	service times and the employee is free to encode 8 or 9 hours or more of services each day if they
	want.

	If you decide to put such a system into place, it is important to clarify this point with your
	staff. The objective here is not to control hours, because the employees decide for themselves what
	they will be entering – but to track the tasks running and the allocation of costs between them is the
	responsibility of the management.

To enable your system with all the features related to `Timesheet`, your configuration wizard should be like this.

.. figure::  images/config_wiz_timesheets.png
   :scale: 75
   :align: center

   *Configuration wizard for Timesheet*

Amongst the many uses of such a timesheet system for a company, here are some of the most important:

* enabling tracking of the true costs of a project by accounting for the time used on it,

* tracking the services provided by different employees,

* comparing the hours really used on a project with the initial planning estimates,

* automatically invoicing based on the service hours provided,

* obtaining a list of the service hours for a given client,

* knowing the costs needed to run the company, such as the marketing costs, the training costs for a
  new employee, and the invoicing rates for a client.

**Timesheet Categories**

You will need to install the :guilabel:`Manufacturing` application (:mod:`mrp`) in order to access timesheet categories.
The different timesheet categories (working time sessions) can be defined through the menu
:menuselection:`Manufacturing --> Configuration --> Resources --> Working Period` and selecting
one of the groups there such as :guilabel:`38 Hours/Week`.

.. figure::  images/service_timesheet_def.png
   :scale: 75
   :align: center

   *Timesheet category for full time 38 hours per week*


.. index::
   single: timesheet; entering data
..

**Entering Timesheet Data**

.. index::
   single: module; hr_timesheet

To be able to use timesheets fully, install the module :mod:`hr_timesheet_sheet` through the :guilabel:`Reconfigure` wizard by selecting :guilabel:`Timesheets` and clicking :guilabel:`Configure`. Once this module
has been installed and the employees configured, the different system users can enter their
timesheet data in the menu
:menuselection:`Human Resources --> Time Tracking --> Working Hours`,
then click :guilabel:`New`.

.. tip:: Shortcut to Timesheets

	It is a good idea if all employees who use timesheets place this menu in their shortcuts.
	That is because they will need to return to them several times each day.

For a new entry:

	#.	The :guilabel:`User` : proposed by default, but you can change it if you are encoding the first timesheet
		for another company employee.

	#.	The :guilabel:`Date` : automatically proposed as today's date, but it is possible to change it if you are
		encoding the timesheet for a prior day.

	#.	:guilabel:`Analytic Account` : for the project you have been working on - obviously it should be predefined.

	#. 	:guilabel:`Description` : a free text description of the work done in the time.

	#. 	:guilabel:`Quantity` : number of units of time (the units are defined as part of the product).

The other fields are automatically completed, but can be modified: the :guilabel:`Product`
which is the service product such as consultancy, the
:guilabel:`Unit of Measure` (predefined, and could perhaps be minutes, hours or days),
the :guilabel:`Cost` of the service (which is calculated by default),
and the associated :guilabel:`General Account`.

The hours are then encoded throughout the day by each employee. It helps to revisit the list at the
end of the day to verify that the number of hours of attendance in the company has been properly
accounted for. The total entered is shown at the bottom right of the list of service hours.

.. tip:: Hiding Service Costs

	By default, OpenERP is configured to show the cost of each service when an employee encodes the
	number of hours per project.
	You can modify this field by adding the attribute ``invisible=True`` in the timesheet view.

	(And the way to do that is either to modify the view on the file system, or
	to use the web client to modify the view in the current database.
	For the latter, there is a pale grey :guilabel:`[Customize]` label
	to the bottom left of each form that gives you access to the
	:guilabel:`Manage Views` option.
	If you have sufficient permissions, you can edit the XML that defines the current view.)

	The value in the cost field shows employees the cost of their time used in the company, so masking this
	field might not always be the best option.

The accuracy of the services entered is crucial for calculating the profitability of the different
jobs and the recharging of services. Different reports are therefore available for verifying
employees' data entry. Employees can verify their own timesheet using the following reports:

* Printing the particular employee's timesheet, using the menu :menuselection:`Human Resources --> Reporting
  --> Timesheet --> Employee Timesheet`.

* Printing more than one employees' timesheet, using the menu :menuselection:`Human Resources --> Reporting
  --> Timesheet --> Employees Timesheet`.You can print a summary in the form of a table per user and per day.

.. figure::  images/service_timesheet_all.png
   :scale: 65
   :align: center

   *Employees' monthly summary timesheet*

* Reviewing profit of timesheet, using the menu :menuselection:`Human Resources --> Reporting --> Timesheets
  --> Timesheet Profit`.

* You can then use the statistical reports to analyze your services by period, by product
  or by account using the menu :menuselection:`Human Resources --> Reporting --> Timesheets
  --> Timesheet Analysis` and :menuselection:`Human Resources --> Reporting --> Timesheets
  --> Timesheet Sheet Analysis`.

.. figure::  images/service_timesheet_graph.png
   :scale: 75
   :align: center

   *Chart of timesheet by account*

The data making up these list views can be varied using the filters available in the upper part of the
screen. If you want to see more detail, switch to the graph view.

.. index::
   single: timesheet; evaluation
..

**Evaluation of Service Costs**

You already know that timesheets are closely linked with analytic accounts. The different projects
reported on the timesheets correspond to analytic accounts. The timesheet entries themselves are
analytic entries.

These entries comprise various analytic operations that do not correspond to any of
the general accounts. Therefore all operations that modify and create timesheet lines automatically
impact the corresponding analytic line and, conversely are automatically modified by changes in that
line.

.. note:: Timesheets and Analytical Data

	The implementation of timesheets in OpenERP relating to analytic entries is managed by an
	inheritance mechanism:
	the timesheet object inherits the analytic entry object.

	The information is therefore not encoded into the database as two separate events, which avoids
	many synchronization problems.
	They are stored in two different tables, however, because a service is an analytical entry, but an
	analytical entry is not necessarily a service.

This is not a classical approach, but it is logical and pragmatic. Employee timesheets are a good
indication of how the costs of a service enterprise are spread across different cases, as reported in
the analytic accounts.

.. index::
   single: benefits

An analytic account should be reflected in the general accounts, but there is no direct counterpart
of these analytic accounts in the general accounts. Instead, if the hourly costs of the employees
are correctly accounted for, the month's timesheet entries should be balanced by the salary +
benefits package paid out to all the employees at the end of the month.

Despite all this, it is quite difficult to work out the average hourly cost of an employee precisely,
because it depends on:

* the extra hours that they have worked,

* holidays and sickness,

* salary variations and all the linked costs, such as social insurance charges.

The reports that enable you to relate general accounts to analytic accounts are valuable tools for
improving your evaluation of different hourly costs of employees. The difference between product
balances in the analytic account and in the general accounts, divided by the total number of hours
worked, can then be applied to the cost of the product. Some companies adjust for that difference by
carrying out another analytic operation at the end of the month in an account created for that
purpose. This analytic account should have a balance that tends towards zero.

Because you have got a system with integrated timesheets, you can then:

* track the profitability of projects in the analytic accounts,

* look at the history of timesheet entries by project and by employee,

* regularly adjust hourly costs by comparing your rates with reality,

.. important:: Project Cost Control

	Controlling the costs and the profitability of projects precisely is very important.

	It enables you to make good estimates and to track budgets allocated to different services and
	their projects, such as sales and, R&D costs.
	You can also refine your arguments on the basis of clear facts rather than guesses if you have
	to renegotiate a contract with a customer following a project slippage.

The analyses of profitability by project and by employee are available from the analytic accounts.
They take all of the invoices into account, and also take into account the cost of the time spent on
each project.

.. index::
   single: attendance; sign in / sign out

Manage attendance through Sign in / Sign out
--------------------------------------------

In some companies, staff have to sign in when they arrive at work and sign out again at the end of
the day. If each employee has been linked to a system user, then they can sign in on OpenERP by
using the menu :menuselection:`Human Resources --> Attendances --> Sign in / Sign out`.

If an employee has forgotten to sign out on leaving, the system proposes that they sign out manually
and type in the time that they left when they come in again the next day. This gives you a simple way
of managing forgotten sign-outs.

Find employee attendance details from their forms in
:menuselection:`Human Resources --> Employees`.

To get the detail of attendance from an employee's form in OpenERP, you can use the
available reports:

*  :guilabel:`Attendances By Month`

*  :guilabel:`Attendances By Week`

*  :guilabel:`Attendance Error Report`

The last report highlights errors in attendance data entry.
It shows you whether an employee has entered the time of
entry or exit manually and the differences between the actual and expected sign out time and the time.


.. index::
   single: attendance; differences

Keep track of differences between timesheets and attendance
-----------------------------------------------------------

When they are used properly, timesheets can be a good control tool for project managers and can
provide awareness of costs and times.

When employee teams are important, a control system must be implemented. All employees should
complete their timesheets correctly because this forms the basis of planning control, and the
financial management and invoicing of projects

You will see in :ref:`ch-services` that you can automatically invoice services at the end of
the month based on the timesheet. But at the same time, some contracts are limited to prepaid hours.
These hours and their deduction from the original limit are also managed by these timesheets.

.. index::
   single: module; hr_timesheet_sheet

In such a situation, hours that are not coded into the timesheets represent lost money for the
company. So it is important to establish effective follow-up of the services timesheets and their
encoding. To set up a structure for control using timesheets you should install the module
:mod:`hr_timesheet_sheet` (:guilabel:`Timesheets` in the :guilabel:`Reconfigure` wizard).

.. figure::  images/timesheet_flow.png
   :scale: 75
   :align: center

   *Process of approving a timesheet*

This module supplies a new screen enabling you to manage timesheets by period. Timesheet entries are
made by employees each day. At the end of the week, employees validate their week's sheet and it is
then passed to the services manager, who must approve his team's entries. Periods are defined in the
company forms, and you can set them to run monthly or weekly.

To enter timesheet data each employee uses the menu :menuselection:`Human Resources --> Time Tracking
--> My Timesheet`.

.. figure::  images/service_timesheet_sheet_form.png
   :scale: 75
   :align: center

   *Form for entering timesheet data*

In the upper part of the screen, the user starts with the sign-in and sign-out times. The system
enables the control of attendance day by day. The two buttons :guilabel:`Sign In` and :guilabel:`Sign Out` enable the
automatic completion of hours in the area to the left. These hours can be modified by employee, so
it is not a true management control system.

The area to the bottom of the screen represents a sheet of the employee's time entries for the
selected day. In total, this should comprise the number of hours worked in the company each day.
This provides a simple verification that the whole day's attendance time has been entered properly.

The second tab of the timesheet, :guilabel:`By Day`, gives the number of hours worked on the different
projects. When there is a gap between the attendance and the timesheet entries, you can use the
second tab to detect the days or the entries that have not been correctly entered.

.. figure::  images/timesheet_sheet_hours.png
   :scale: 75
   :align: center

   *Detail of hours worked by day for an employee*

The action :guilabel:`Timesheet by Account` shows the time worked on all the different projects. That enables you
to step back to see an overview of the time an employee has worked spread over different projects.

At the end of the week or the month, the employee confirms his timesheet. If the attendance time in
the company corresponds to the encoded entries, the whole timesheet is then confirmed and sent to
his department manager, who is then responsible for approving it or asking for corrections.

Each manager can then look at a list of his department's timesheets waiting for approval using the
menu :menuselection:`Human Resource --> Reporting  --> Timesheet --> Timesheet Sheet Analysis` by applying the proper filters. He then has to approve them or return them to their initial state.

To define the departmental structure, use the menu :menuselection:`Human Resources --> Configuration -->
Human Resources --> Departments`.

.. tip:: Timesheet Approval

	At first sight, the approval of timesheets by a department manager can seem a bureaucratic
	hindrance.
	This operation is crucial for effective management, however.
	We have too frequently seen companies in the situation where managers are so overworked that they
	do not know what their employees are doing.

	So this approval process supplies the manager with an outline of each employee's work at least once
	a week.
	And this is carried out for the hours worked on all the different projects.

Once the timesheets have been approved, you can then use them for cost control and for invoicing
hours to clients.

Contracts and their rates, planning, and methods of invoicing are the object of the following
chapter, :ref:`ch-services`.


.. Copyright © Open Object Press. All rights reserved.

.. You may take electronic copy of this publication and distribute it if you do not
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

