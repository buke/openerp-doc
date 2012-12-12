.. index::
   single: planning
..

Planning to Improve Leadership
==============================

Planning in a company often takes the form of regular meetings between the different teams. Each
team has a certain number of projects and objectives that they must organize and establish
priorities for.

Ideally, these planning meetings should be short but regular and systematic. They can be weekly or
monthly depending on the type of activity. A planning meeting often runs in three phases:

	#. Minutes of the preceding period, and analysis of the work done compared to the planned work.

	#. Introduction of new projects.

	#. Planning the next period.

The planning function covers several objectives which will be described in this section:

* planning live projects against the commitments that have been made to clients,

* determining staffing (HR) requirements in the coming month,

* setting work for each employee or team for the periods to come,

* analyzing the work done in the preceding periods,

* passing the high-level objectives to lower levels in the company's hierarchy.

.. tip:: The Social Role of Planning

	Some project managers think that they can manage planning on their own.
	They are commonly overworked and think that meetings are a waste of time.

	Even if staff really can manage their work for themselves, you should recognize that this regular
	meeting is also aimed at reassurance.
	Without it you can get into unduly stressful situations from:

	* feelings of overwork because they have lost sight of their priorities,

	* lack of feedback and tracking of the work actually completed,

	* an impression of poor organization if that has not been made explicit.

	So the social role of planning should not be neglected. We have often experienced a background of
	stress in a company stemming from a lack of communication and planning.

.. index::
   single: tasks

Planning by Time or by Tasks?
-----------------------------

There are two major approaches to enterprise planning: planning by task and planning by time. You
can manage both with OpenERP.

In planning by task, the project manager assigns tasks from the different projects to each employee
over a given period. Employees then carry out precisely the work they have been assigned by the
project manager.

.. index::
   pair: time; allocation

Planning by time consists of allocating, for each employee, some time on each of the different
projects for the period concerned. The tasks for each project are ordered by priority and can be
directly assigned to a user or left unassigned. Each employee then chooses the task that he or she
will do next, based on the plans and the relative priorities of the tasks.

.. _fig-srvplantime:

.. figure::  images/service_planning_time.png
   :scale: 75
   :align: center

   *Monthly planning for work time of each employee*

The figure :ref:`fig-srvplantime` shows a monthly planning session where plans are being made for each employee to spend a
number of days' work on various different projects.

In this time-focused planning approach, clients' priorities do not feature in the planning any more,
but are explicit in the task list instead. So this approach helps you separate the planning of human
resources on projects from the task prioritization within a project.

.. note:: Comparing the Two Planning Methods

    To illustrate the difference between planning by time and planning by task, take the case of an
    IT project that is estimated to be around six months of work. This project is managed by iterative
    cycles of development of around a month, and a presentation is made to the client at the end of
    each cycle to track the progress of the project. At this meeting, you plan what must be carried
    out for the following month. At the end of the month, the account manager for the project invoices
    the client for the work done on the project.

    Suppose that the project encounters a delay because it is more complex than expected. There are
    two ways of resolving the delay if you have no further resources: you can be

    * late in your delivery of the planned functions, or 

    * on time, but with fewer functions than planned.

    If your planning is based on phases and tasks you will report at the client meeting that it will
    take several weeks to complete everything that was planned for the current phase. Conversely, if
    you are planning by time you will keep the meeting with the client to close the present development
    phase and plan the new one, but only be able to present part of the planned functionality.

    If the client is sensitive to delay, the first approach will cause acute unhappiness. You will have
    to re-plan the project and all of its future phases to take account of that delay. Some problems
    are also likely to occur later with invoicing, because it will be difficult for you to invoice
    any work that has been completed late but has not yet been shown to the client.

.. note:: Comparing the Two Planning Methods

    The second approach will require you to report on the functions that have not been completed, and
    on how they would fit into a future planning phase. That will not involve a break in the
    working time allocated to the project, however. 
    You would then generate two different lists: a staffing plan
    for the different projects, and the list of tasks prioritized for the client's project. This
    approach offers a number of advantages over the first one:

    * The client will have the choice of delaying the end of the project by planning an extra phase,
      or letting go of some minor functions to be able to deliver a final system more rapidly,

    * The client may re-plan the functions taking the new delay into account.

    * You will be able to make the client gradually aware of the fact that project progress has come
      under pressure and that work is perhaps more complex than had been estimated at the outset.

    * A delay in the delivery of several of the functions will not necessarily affect either monthly
      invoicing or project planning.

    Being able to separate human resource planning from task prioritization simplifies your
    management of complex issues, such as adjusting for employee holidays or handling the constantly
    changing priorities within projects.

.. index::
   single: planning; create plan
..

Plan your Time
--------------

Install the module :mod:`project_planning` to get additional functions
that help with both planning and reporting on projects. Start a plan by using the
menu :menuselection:`Project --> Long Term Planning --> Plannings`.

.. index::
   pair: time; allocation

On each planning line you should enter the user, the analytic account concerned, and the quantity of
time allocated. The quantity will be expressed in hours or in days depending on the unit of measure
used. For each line you can add a brief note about the work to be done.

Once the plan has been saved, use the other tabs of the planning form to check that the amount of
time allocated to the employees or to the projects is right. The time allocated should match
the employees' employment contracts, for example 37.5 hours per week. The forecast time for the
project should also match the commitments that you have made with client.

You should ideally complete all the planning for the current period. You can also complete some
lines in the planning of future months – reserving resources on different project in response to
your client commitments, for example. This enables you to manage your available human resources for
the months ahead.

.. index::
   single: module; board_project

Plans can be printed and/or sent to employees by email. 
Each employee can be given access to a dashboard that graphically shows the
time allocated to him or her on a project and the time that has been worked so far. So each employee
can decide which projects should be prioritized.

The employee then selects a task in the highest priority project. She ideally chooses either a task
that has been directly assigned to her, or one which is high on the priority list that she is capable
of completing, but is not yet directly assigned to anybody.

At the end of the period you can compare the duration of effective work on the different projects to
that of the initial estimate. Print the plan to obtain a comparison of the planned working time and
the real time worked.

.. figure::  images/planning_stat.png
   :scale: 75
   :align: center

   *Comparison of planned hours, worked hours and the productivity of employees by project*

You can also study several of your project's figures from the menus in :menuselection:`Project
--> Reporting`.

Planning at all Levels of the Hierarchy
---------------------------------------

.. index::
   single: module; report_analytic_planning_delegate

To put planning in place across the whole company you can use a system of planning delegation.

The planning entry form can reflect the hierarchical
structure of the company. To enter data into a plan line you can:

* assign time on a project to an employee,

* assign time on a project to a department manager for his whole team.

You can now allocate the working time on projects for the whole of a department, without having to
detail each employee's tasks. Then when a department manager creates his own plan, he will find
what is required of his group by his management at the bottom of the form. At the top of the form
there is a place for assigning project work in detail to each member of department.

If you do not have to plan time to work on a final draft you can do it on an analytic account that
relies on child accounts. This means that you can create plans to meet top-level objectives of the
senior management team and then cascade them down through the different departments to establish a
time budget for each employee. Each manager then uses his own plans for managing his level in the
hierarchy.


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

