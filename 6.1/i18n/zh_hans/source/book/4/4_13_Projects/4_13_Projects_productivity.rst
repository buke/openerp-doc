
.. i18n: .. index:: GTD
..

.. index:: GTD

.. i18n: The Art of Productivity without Stress
.. i18n: ======================================
..

The Art of Productivity without Stress
======================================

.. i18n: Now you can take a slight detour away from pure enterprise management by looking at some tools offered by
.. i18n: OpenERP to improve your own personal time management. It is not much of a detour because good
.. i18n: organization is the key to better productivity in your daily work.
..

Now you can take a slight detour away from pure enterprise management by looking at some tools offered by
OpenERP to improve your own personal time management. It is not much of a detour because good
organization is the key to better productivity in your daily work.

.. i18n: .. index::
.. i18n:    single: module; project_gtd
.. i18n:    single: GTD
.. i18n:    single: Getting Things Done
..

.. index::
   single: module; project_gtd
   single: GTD
   single: Getting Things Done

.. i18n: OpenERP's :mod:`project_gtd` module was inspired by the work of two books focusing on efficient
.. i18n: time management:
..

OpenERP's :mod:`project_gtd` module was inspired by the work of two books focusing on efficient
time management:

.. i18n: * Getting Things Done – The Art of Stress-Free Productivity, by David Allen (2001), most often
.. i18n:   referred to by its initials **GTD** (trademark registered since 2005). This book is built around the
.. i18n:   principle that people should clearly write down all their outstanding tasks and store the details
.. i18n:   about these tasks in a trustworthy system.
..

* Getting Things Done – The Art of Stress-Free Productivity, by David Allen (2001), most often
  referred to by its initials **GTD** (trademark registered since 2005). This book is built around the
  principle that people should clearly write down all their outstanding tasks and store the details
  about these tasks in a trustworthy system.

.. i18n:   They then do not have to worry about holding all of this stuff in their head. Since they can be
.. i18n:   quite sure that it is recorded safely, they can allow themselves to relax and so have the energy
.. i18n:   and time to concentrate on handling the tasks themselves systematically.
..

  They then do not have to worry about holding all of this stuff in their head. Since they can be
  quite sure that it is recorded safely, they can allow themselves to relax and so have the energy
  and time to concentrate on handling the tasks themselves systematically.

.. i18n: .. index::
.. i18n:    simple: The 7 Habits of Highly Effective People
..

.. index::
   simple: The 7 Habits of Highly Effective People

.. i18n: * The 7 Habits of Highly Effective People by Stephen R. Covey (1989) : the author advises
.. i18n:   organizations on the use of these practices, and reports on the productivity improvements in the
.. i18n:   organization that result.
..

* The 7 Habits of Highly Effective People by Stephen R. Covey (1989) : the author advises
  organizations on the use of these practices, and reports on the productivity improvements in the
  organization that result.

.. i18n:   .. note:: Managing Time Efficiently
.. i18n: 
.. i18n:      David Allen, Getting Things Done, Penguin Books, New York, 2001, 267 pages. (ISBN :
.. i18n:      978-0142000281). Also see the site: http://davidco.com
.. i18n: 
.. i18n:      Stephen R. Covey, The 7 Habits of Highly Effective People, Free Press, 1989, 15th Anniversary
.. i18n:      Edition : 2004, 384 pages. (ISBN : 978-0743269513).
.. i18n: 
.. i18n:   .. tip:: De-stress Yourself!
.. i18n: 
.. i18n: 	 Clear the tasks that clutter your thoughts by registering them in an organized system.
.. i18n: 	 This immediately helps you to de-stress yourself and organize your work in the best possible way.
.. i18n: 
.. i18n: 	 If you feel stressed by too much work, do the following exercise to convince yourself about the
.. i18n: 	 benefits.
.. i18n: 	 Take some sheets of blank paper and write down everything that passes through your head about the
.. i18n: 	 things you need to do.
.. i18n: 	 For each task, note the next action to do on an adjacent line, and rank it by the date that you will
.. i18n: 	 commit yourself to doing it.
.. i18n: 
.. i18n: 	 At the end of the exercise you will feel better organized, considerably de-stressed and remarkably
.. i18n: 	 free of worries !
..

  .. note:: Managing Time Efficiently

     David Allen, Getting Things Done, Penguin Books, New York, 2001, 267 pages. (ISBN :
     978-0142000281). Also see the site: http://davidco.com

     Stephen R. Covey, The 7 Habits of Highly Effective People, Free Press, 1989, 15th Anniversary
     Edition : 2004, 384 pages. (ISBN : 978-0743269513).

  .. tip:: De-stress Yourself!

	 Clear the tasks that clutter your thoughts by registering them in an organized system.
	 This immediately helps you to de-stress yourself and organize your work in the best possible way.

	 If you feel stressed by too much work, do the following exercise to convince yourself about the
	 benefits.
	 Take some sheets of blank paper and write down everything that passes through your head about the
	 things you need to do.
	 For each task, note the next action to do on an adjacent line, and rank it by the date that you will
	 commit yourself to doing it.

	 At the end of the exercise you will feel better organized, considerably de-stressed and remarkably
	 free of worries !

.. i18n: The objective in this detour is not to detail the whole methodology, but to describe the supporting
.. i18n: tools provided by OpenERP's :mod:`project_gtd` module.
..

The objective in this detour is not to detail the whole methodology, but to describe the supporting
tools provided by OpenERP's :mod:`project_gtd` module.

.. i18n: Not Everything that is Urgent is Necessarily Important
.. i18n: ------------------------------------------------------
..

Not Everything that is Urgent is Necessarily Important
------------------------------------------------------

.. i18n: The first modification brought by the module to the basic OpenERP system is a separation of the
.. i18n: concepts of urgency and importance. Tasks are no longer classified by a single criterion, but by the
.. i18n: product of the two criteria, enabling you to prioritize matters that are both urgent and important
.. i18n: in a single list.
..

The first modification brought by the module to the basic OpenERP system is a separation of the
concepts of urgency and importance. Tasks are no longer classified by a single criterion, but by the
product of the two criteria, enabling you to prioritize matters that are both urgent and important
in a single list.

.. i18n: Many managers with a heavy workload use urgency as their sole method of prioritization. The
.. i18n: difficulty is then in working out how to plan for substantive tasks (like medium term objectives).
.. i18n: These are not urgent but are nevertheless very important.
..

Many managers with a heavy workload use urgency as their sole method of prioritization. The
difficulty is then in working out how to plan for substantive tasks (like medium term objectives).
These are not urgent but are nevertheless very important.

.. i18n: .. note:: Example Distinction between Urgency and Importance
.. i18n: 
.. i18n:     If you are very well organized, urgent tasks can (and should often) be given lower precedence than
.. i18n:     important tasks. Take an example from daily life as an illustration: the case of having some time
.. i18n:     with your children.
.. i18n: 
.. i18n:     For most people, this task is important. But if you have a busy professional life, the days and
.. i18n:     weeks flow on with endless urgent tasks to be resolved. Even if you manage your time well, you
.. i18n:     could let several months pass without spending time with your children because the task of seeing
.. i18n:     them is never as urgent as your other work, despite its importance.
..

.. note:: Example Distinction between Urgency and Importance

    If you are very well organized, urgent tasks can (and should often) be given lower precedence than
    important tasks. Take an example from daily life as an illustration: the case of having some time
    with your children.

    For most people, this task is important. But if you have a busy professional life, the days and
    weeks flow on with endless urgent tasks to be resolved. Even if you manage your time well, you
    could let several months pass without spending time with your children because the task of seeing
    them is never as urgent as your other work, despite its importance.

.. i18n: In OpenERP, urgency is given by the :guilabel:`Deadline` of the task, and importance by the :guilabel:`Priority`.
.. i18n: The classification of the tasks then results from the product of the two factors. The most important
.. i18n: tasks and the most urgent both appear at the top of the list.
..

In OpenERP, urgency is given by the :guilabel:`Deadline` of the task, and importance by the :guilabel:`Priority`.
The classification of the tasks then results from the product of the two factors. The most important
tasks and the most urgent both appear at the top of the list.

.. i18n: Organizing your Life Systematically
.. i18n: -----------------------------------
..

Organizing your Life Systematically
-----------------------------------

.. i18n: A methodology of organizing yourself using the concepts of context and timebox is presented in this
.. i18n: section.
..

A methodology of organizing yourself using the concepts of context and timebox is presented in this
section.

.. i18n: Context
.. i18n: ^^^^^^^
..

Context
^^^^^^^

.. i18n: The context is determined by the work environment you must be in to deal with certain tasks. For
.. i18n: example, you could define the following contexts:
..

The context is determined by the work environment you must be in to deal with certain tasks. For
example, you could define the following contexts:

.. i18n: *  *Office* : for tasks which have to be dealt with at your workplace (such as telephone a customer,
.. i18n:    or write a document),
.. i18n: 
.. i18n: *  *Car* : for tasks that you need to do on the move (such as going shopping, or going to
.. i18n:    the post office),
.. i18n: 
.. i18n: *  *Travel* : for tasks that you can handle on the plane or in the train while you are doing
.. i18n:    travelling on business (tasks such as writing an article, or analyzing a new product),
.. i18n: 
.. i18n: *  *Home* : for tasks which have to happen at your private address (such as finding a cleaning
.. i18n:    contractor, or mowing the lawn).
..

*  *Office* : for tasks which have to be dealt with at your workplace (such as telephone a customer,
   or write a document),

*  *Car* : for tasks that you need to do on the move (such as going shopping, or going to
   the post office),

*  *Travel* : for tasks that you can handle on the plane or in the train while you are doing
   travelling on business (tasks such as writing an article, or analyzing a new product),

*  *Home* : for tasks which have to happen at your private address (such as finding a cleaning
   contractor, or mowing the lawn).

.. i18n: An employee / system user can create his or her own contexts using the menu
.. i18n: :menuselection:`Project --> Configuration --> Tasks --> Contexts`.
..

An employee / system user can create his or her own contexts using the menu
:menuselection:`Project --> Configuration --> Tasks --> Contexts`.

.. i18n: Timebox
.. i18n: ^^^^^^^
..

Timebox
^^^^^^^

.. i18n: You then have to define the timeboxes. You have to complete the tasks in the time interval specified
.. i18n: by a timebox. You usually define timeboxes with the following periods:
..

You then have to define the timeboxes. You have to complete the tasks in the time interval specified
by a timebox. You usually define timeboxes with the following periods:

.. i18n: *  *Today* : for tasks which must be handled today,
.. i18n: 
.. i18n: *  *This Week* : for tasks that have to be dealt with this week,
.. i18n: 
.. i18n: *  *This Month* : for tasks which have to be completed within the month,
.. i18n: 
.. i18n: *  *Long Term* : for tasks that can be dealt with in more than one month.
..

*  *Today* : for tasks which must be handled today,

*  *This Week* : for tasks that have to be dealt with this week,

*  *This Month* : for tasks which have to be completed within the month,

*  *Long Term* : for tasks that can be dealt with in more than one month.

.. i18n: A task can be put in one and only one timebox at a time.
..

A task can be put in one and only one timebox at a time.

.. i18n: You should distinguish between a timebox and the deadline for completing a task because the deadline
.. i18n: is usually fixed by the requirements of the project manager. A timebox, by contrast, is selected
.. i18n: with reference to what an individual can do.
..

You should distinguish between a timebox and the deadline for completing a task because the deadline
is usually fixed by the requirements of the project manager. A timebox, by contrast, is selected
with reference to what an individual can do.

.. i18n: To define timeboxes for your company, use the menu
.. i18n: :menuselection:`Project --> Configuration --> Tasks --> Timeboxes`.
..

To define timeboxes for your company, use the menu
:menuselection:`Project --> Configuration --> Tasks --> Timeboxes`.

.. i18n: .. index:: methodology; GTD
..

.. index:: methodology; GTD

.. i18n: Methodology and Iterative Process
.. i18n: ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
..

Methodology and Iterative Process
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. i18n: To organize your tasks efficiently, OpenERP uses a method based on the following systematic and
.. i18n: iterative process:
..

To organize your tasks efficiently, OpenERP uses a method based on the following systematic and
iterative process:

.. i18n: 	#. Identify all the tasks that you have to deal with, including everything that keeps you awake at
.. i18n: 	   night, and enter them in Tasks, which you will find in the menu
.. i18n: 	   :menuselection:`Project --> Project --> Tasks`.
.. i18n: 
.. i18n: 	#. Classify the tasks periodically, assigning them a context and a timebox. This
.. i18n: 	   indicates both when and where the task should be handled. If a task takes less than 10 minutes, then
.. i18n: 	   maybe it could be handled immediately.
.. i18n: 
.. i18n: 	#. Every day, carry out the following process:
.. i18n: 
.. i18n: 		* First thing in the morning, select those tasks contained in the current week's timebox that you
.. i18n: 		  want to deal with today. These are presented in order of importance and urgency, so you should
.. i18n: 		  select the tasks closest to the top of the list.
.. i18n: 
.. i18n: 		* Carry out each task, that is to say either work on the task yourself or delegate it to another
.. i18n: 		  user,
.. i18n: 
.. i18n: 		* Last thing, at the end of the day's work, empty that day's timebox and return all unclosed tasks
.. i18n: 		  into the week's timebox.
.. i18n: 
.. i18n: 	#. Repeat the same process each week and each month for the respective timeboxes.
..

	#. Identify all the tasks that you have to deal with, including everything that keeps you awake at
	   night, and enter them in Tasks, which you will find in the menu
	   :menuselection:`Project --> Project --> Tasks`.

	#. Classify the tasks periodically, assigning them a context and a timebox. This
	   indicates both when and where the task should be handled. If a task takes less than 10 minutes, then
	   maybe it could be handled immediately.

	#. Every day, carry out the following process:

		* First thing in the morning, select those tasks contained in the current week's timebox that you
		  want to deal with today. These are presented in order of importance and urgency, so you should
		  select the tasks closest to the top of the list.

		* Carry out each task, that is to say either work on the task yourself or delegate it to another
		  user,

		* Last thing, at the end of the day's work, empty that day's timebox and return all unclosed tasks
		  into the week's timebox.

	#. Repeat the same process each week and each month for the respective timeboxes.

.. i18n: .. index:: agenda
.. i18n: .. index:: timebox
..

.. index:: agenda
.. index:: timebox

.. i18n: .. tip:: Do not confuse **Agenda** and **Timebox**
.. i18n: 
.. i18n: 	The idea of timebox is independent from that of an agenda.
.. i18n: 	Certain tasks, such as meetings, must be done on a precise date.
.. i18n: 	So they cannot be managed by the timebox system but by an agenda.
.. i18n: 
.. i18n: 	The ideal is to put the minimum of things on the agenda and to put there only tasks that have a
.. i18n: 	fixed date.
.. i18n: 	The timebox system is more flexible and more efficient for dealing with multiple tasks.
..

.. tip:: Do not confuse **Agenda** and **Timebox**

	The idea of timebox is independent from that of an agenda.
	Certain tasks, such as meetings, must be done on a precise date.
	So they cannot be managed by the timebox system but by an agenda.

	The ideal is to put the minimum of things on the agenda and to put there only tasks that have a
	fixed date.
	The timebox system is more flexible and more efficient for dealing with multiple tasks.

.. i18n: So start by entering all the tasks required by project.
.. i18n: These could have been entered by another user and assigned to you.
.. i18n: It is important to code in all of the tasks that are buzzing around in your head, just to get them
.. i18n: off your mind. A task could be:
..

So start by entering all the tasks required by project.
These could have been entered by another user and assigned to you.
It is important to code in all of the tasks that are buzzing around in your head, just to get them
off your mind. A task could be:

.. i18n: * work to be done,
.. i18n: 
.. i18n: * a short objective, medium or long term,
.. i18n: 
.. i18n: * a complex project that has not yet been broken into tasks.
..

* work to be done,

* a short objective, medium or long term,

* a complex project that has not yet been broken into tasks.

.. i18n: A project or an objective over several days can be summarized in a single task. You do not have to
.. i18n: detail each operation if the actions to be done are sufficiently clear to you.
..

A project or an objective over several days can be summarized in a single task. You do not have to
detail each operation if the actions to be done are sufficiently clear to you.

.. i18n: You have to empty your Tasks periodically. To do that, use the menu :menuselection:`Project
.. i18n: --> Project --> Tasks`. Assign a timebox and a context to each task. This operation should
.. i18n: not take more than a few minutes, because you are not dealing with the tasks themselves, just
.. i18n: classifying them.
..

You have to empty your Tasks periodically. To do that, use the menu :menuselection:`Project
--> Project --> Tasks`. Assign a timebox and a context to each task. This operation should
not take more than a few minutes, because you are not dealing with the tasks themselves, just
classifying them.

.. i18n: .. figure::  images/service_timebox_day.png
.. i18n:    :scale: 75
.. i18n:    :align: center
.. i18n: 
.. i18n:    *Timebox for tasks to be done today*
..

.. figure::  images/service_timebox_day.png
   :scale: 75
   :align: center

   *Timebox for tasks to be done today*

.. i18n: Then click on the button at the top right :guilabel:`Plannify Timebox`. This procedure lets you
.. i18n: select the tasks for the day from those in the timebox for the week. This operation gives you an
.. i18n: overview of the medium term tasks and objectives and makes you review them there at least once a
.. i18n: day. It is then that you would decide to allocate a part of your time that day to certain tasks based on
.. i18n: your priorities.
..

Then click on the button at the top right :guilabel:`Plannify Timebox`. This procedure lets you
select the tasks for the day from those in the timebox for the week. This operation gives you an
overview of the medium term tasks and objectives and makes you review them there at least once a
day. It is then that you would decide to allocate a part of your time that day to certain tasks based on
your priorities.

.. i18n: Since the tasks are sorted by priority, it is sufficient to take the first from the list, up to the
.. i18n: number of hours in your day. That will only take a minute, because the selection is not taken from
.. i18n: every task you know about in the future, but just from those selected for the current week.
..

Since the tasks are sorted by priority, it is sufficient to take the first from the list, up to the
number of hours in your day. That will only take a minute, because the selection is not taken from
every task you know about in the future, but just from those selected for the current week.

.. i18n: Once the timebox has been completed you can start your daily work on the tasks. For each task, you
.. i18n: can start work on it, delegate it, close it, or cancel it.
..

Once the timebox has been completed you can start your daily work on the tasks. For each task, you
can start work on it, delegate it, close it, or cancel it.

.. i18n: At the end of the day, you empty the timebox using the button at the top right
.. i18n: :guilabel:`Empty Timebox`. All the tasks that have not been done are sent back
.. i18n: to the weekly timebox to sit in amongst the tasks that will be planned next morning.
..

At the end of the day, you empty the timebox using the button at the top right
:guilabel:`Empty Timebox`. All the tasks that have not been done are sent back
to the weekly timebox to sit in amongst the tasks that will be planned next morning.

.. i18n: Do the same each week and each month using the same principles, but just using the appropriate
.. i18n: timeboxes for those periods.
..

Do the same each week and each month using the same principles, but just using the appropriate
timeboxes for those periods.

.. i18n: Some Convincing Results
.. i18n: ^^^^^^^^^^^^^^^^^^^^^^^
..

Some Convincing Results
^^^^^^^^^^^^^^^^^^^^^^^

.. i18n: After a few days of carefully practising this method, users have reported the following
.. i18n: improvements:
..

After a few days of carefully practising this method, users have reported the following
improvements:

.. i18n: * a reduction in the number of tasks and objectives that were forgotten,
.. i18n: 
.. i18n: * a reduction in stress because people felt more in control of their situation,
.. i18n: 
.. i18n: * a change of the priorities in the types of tasks carried out daily,
.. i18n: 
.. i18n: * more notice taken of the urgency and importance of tasks and objectives in the long-term
.. i18n:   organization of time,
.. i18n: 
.. i18n: * better management of task delegation and the selection of which tasks were better to delegate,
..

* a reduction in the number of tasks and objectives that were forgotten,

* a reduction in stress because people felt more in control of their situation,

* a change of the priorities in the types of tasks carried out daily,

* more notice taken of the urgency and importance of tasks and objectives in the long-term
  organization of time,

* better management of task delegation and the selection of which tasks were better to delegate,

.. i18n: Finally, it is important to note that this system is totally integrated with OpenERP's project
.. i18n: management function. Staff can use the system or not, depending on their own needs. The system is
.. i18n: complementary to the project management function that handles team organization and company-wide
.. i18n: planning.
..

Finally, it is important to note that this system is totally integrated with OpenERP's project
management function. Staff can use the system or not, depending on their own needs. The system is
complementary to the project management function that handles team organization and company-wide
planning.

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
