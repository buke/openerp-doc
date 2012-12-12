
.. index:: GTD

The Art of Productivity without Stress
======================================

Now you can take a slight detour away from pure enterprise management by looking at some tools offered by
OpenERP to improve your own personal time management. It is not much of a detour because good
organization is the key to better productivity in your daily work.

.. index::
   single: module; project_gtd
   single: GTD
   single: Getting Things Done

OpenERP's :mod:`project_gtd` module was inspired by the work of two books focusing on efficient
time management:

* Getting Things Done – The Art of Stress-Free Productivity, by David Allen (2001), most often
  referred to by its initials **GTD** (trademark registered since 2005). This book is built around the
  principle that people should clearly write down all their outstanding tasks and store the details
  about these tasks in a trustworthy system.

  They then do not have to worry about holding all of this stuff in their head. Since they can be
  quite sure that it is recorded safely, they can allow themselves to relax and so have the energy
  and time to concentrate on handling the tasks themselves systematically.

.. index::
   simple: The 7 Habits of Highly Effective People

* The 7 Habits of Highly Effective People by Stephen R. Covey (1989) : the author advises
  organizations on the use of these practices, and reports on the productivity improvements in the
  organization that result.

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

The objective in this detour is not to detail the whole methodology, but to describe the supporting
tools provided by OpenERP's :mod:`project_gtd` module.

Not Everything that is Urgent is Necessarily Important
------------------------------------------------------

The first modification brought by the module to the basic OpenERP system is a separation of the
concepts of urgency and importance. Tasks are no longer classified by a single criterion, but by the
product of the two criteria, enabling you to prioritize matters that are both urgent and important
in a single list.

Many managers with a heavy workload use urgency as their sole method of prioritization. The
difficulty is then in working out how to plan for substantive tasks (like medium term objectives).
These are not urgent but are nevertheless very important.

.. note:: Example Distinction between Urgency and Importance

    If you are very well organized, urgent tasks can (and should often) be given lower precedence than
    important tasks. Take an example from daily life as an illustration: the case of having some time
    with your children.

    For most people, this task is important. But if you have a busy professional life, the days and
    weeks flow on with endless urgent tasks to be resolved. Even if you manage your time well, you
    could let several months pass without spending time with your children because the task of seeing
    them is never as urgent as your other work, despite its importance.

In OpenERP, urgency is given by the :guilabel:`Deadline` of the task, and importance by the :guilabel:`Priority`.
The classification of the tasks then results from the product of the two factors. The most important
tasks and the most urgent both appear at the top of the list.

Organizing your Life Systematically
-----------------------------------

A methodology of organizing yourself using the concepts of context and timebox is presented in this
section.

Context
^^^^^^^

The context is determined by the work environment you must be in to deal with certain tasks. For
example, you could define the following contexts:

*  *Office* : for tasks which have to be dealt with at your workplace (such as telephone a customer,
   or write a document),

*  *Car* : for tasks that you need to do on the move (such as going shopping, or going to
   the post office),

*  *Travel* : for tasks that you can handle on the plane or in the train while you are doing
   travelling on business (tasks such as writing an article, or analyzing a new product),

*  *Home* : for tasks which have to happen at your private address (such as finding a cleaning
   contractor, or mowing the lawn).

An employee / system user can create his or her own contexts using the menu
:menuselection:`Project --> Configuration --> Tasks --> Contexts`.

Timebox
^^^^^^^

You then have to define the timeboxes. You have to complete the tasks in the time interval specified
by a timebox. You usually define timeboxes with the following periods:

*  *Today* : for tasks which must be handled today,

*  *This Week* : for tasks that have to be dealt with this week,

*  *This Month* : for tasks which have to be completed within the month,

*  *Long Term* : for tasks that can be dealt with in more than one month.

A task can be put in one and only one timebox at a time.

You should distinguish between a timebox and the deadline for completing a task because the deadline
is usually fixed by the requirements of the project manager. A timebox, by contrast, is selected
with reference to what an individual can do.

To define timeboxes for your company, use the menu
:menuselection:`Project --> Configuration --> Tasks --> Timeboxes`.

.. index:: methodology; GTD

Methodology and Iterative Process
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

To organize your tasks efficiently, OpenERP uses a method based on the following systematic and
iterative process:

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

.. index:: agenda
.. index:: timebox

.. tip:: Do not confuse **Agenda** and **Timebox**

	The idea of timebox is independent from that of an agenda.
	Certain tasks, such as meetings, must be done on a precise date.
	So they cannot be managed by the timebox system but by an agenda.

	The ideal is to put the minimum of things on the agenda and to put there only tasks that have a
	fixed date.
	The timebox system is more flexible and more efficient for dealing with multiple tasks.

So start by entering all the tasks required by project.
These could have been entered by another user and assigned to you.
It is important to code in all of the tasks that are buzzing around in your head, just to get them
off your mind. A task could be:

* work to be done,

* a short objective, medium or long term,

* a complex project that has not yet been broken into tasks.

A project or an objective over several days can be summarized in a single task. You do not have to
detail each operation if the actions to be done are sufficiently clear to you.

You have to empty your Tasks periodically. To do that, use the menu :menuselection:`Project
--> Project --> Tasks`. Assign a timebox and a context to each task. This operation should
not take more than a few minutes, because you are not dealing with the tasks themselves, just
classifying them.

.. figure::  images/service_timebox_day.png
   :scale: 75
   :align: center

   *Timebox for tasks to be done today*

Then click on the button at the top right :guilabel:`Plannify Timebox`. This procedure lets you
select the tasks for the day from those in the timebox for the week. This operation gives you an
overview of the medium term tasks and objectives and makes you review them there at least once a
day. It is then that you would decide to allocate a part of your time that day to certain tasks based on
your priorities.

Since the tasks are sorted by priority, it is sufficient to take the first from the list, up to the
number of hours in your day. That will only take a minute, because the selection is not taken from
every task you know about in the future, but just from those selected for the current week.

Once the timebox has been completed you can start your daily work on the tasks. For each task, you
can start work on it, delegate it, close it, or cancel it.

At the end of the day, you empty the timebox using the button at the top right
:guilabel:`Empty Timebox`. All the tasks that have not been done are sent back
to the weekly timebox to sit in amongst the tasks that will be planned next morning.

Do the same each week and each month using the same principles, but just using the appropriate
timeboxes for those periods.

Some Convincing Results
^^^^^^^^^^^^^^^^^^^^^^^

After a few days of carefully practising this method, users have reported the following
improvements:

* a reduction in the number of tasks and objectives that were forgotten,

* a reduction in stress because people felt more in control of their situation,

* a change of the priorities in the types of tasks carried out daily,

* more notice taken of the urgency and importance of tasks and objectives in the long-term
  organization of time,

* better management of task delegation and the selection of which tasks were better to delegate,


Finally, it is important to note that this system is totally integrated with OpenERP's project
management function. Staff can use the system or not, depending on their own needs. The system is
complementary to the project management function that handles team organization and company-wide
planning.



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

