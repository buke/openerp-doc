.. index::
   single: Long Term
..

Long Term Project Planning
==========================

You can plan your projects with Long Term Planning. To do this, use the :guilabel:`Reconfigure` wizard and in the
:guilabel:`Project Application Configuration` section, select \ ``Long Term Planning`` \ and click :guilabel:`Configure`. This installs the :mod:`project_long_term` module. By using this feature, you can link tasks to your planning to have a great view of who will do what at a specific time.

The traditional phased approach identifies the sequence of steps to be completed. `Faces <http://faces.homeip.net/>`_ library is used for scheduling phases and tasks based on calendar resources. So resource availability or resource leaves are tracked using this tool. The Gantt chart allows you to easily manage your resources and plans by mere drag & drop. The Calendar view also helps you map your deadlines and tasks needing attention.

Project Phases
--------------

You can subdivide your larger projects into several phases.
To define a new phase, go to :menuselection:`Project --> Project --> Project Phases` and click :guilabel:`New`. You must link your phase to a project through the :guilabel:`Project` field. For each phase, you can define your resources allocation (human or machine), describe the different tasks and link your phase to previous and following ones. You can also add constraints linked with dates and scheduling. A Gantt view of your project is available from this menu, which you may alternatively open through the :menuselection:`Project --> Long Term Planning --> Project Phases` menu.

.. _fig-project_phase:

.. figure::  images/project_phase.png
   :scale: 75
   :align: center

   *Form View of Project Phase*

Scheduling
----------

You need to define a working schedule and leaves, since the project scheduler will use these to calculate the project dates.
Ensure that you have entered a working schedule for your project in the :guilabel:`Working Time` field in the :guilabel:`Administration` tab of the :guilabel:`Project` form. This is useful to generate accurate Gantt charts for your project.

If you have tasks related to a phase, you can see them in the :guilabel:`Tasks Details` tab of your phase form. Schedule them by clicking the :guilabel:`Schedule Tasks` button. All the tasks which are in draft, pending and open state are scheduled and their dates are calculated based on the starting date of the phase.

.. _fig-schedule_tasks:

.. figure::  images/schedule_tasks.png
   :scale: 75
   :align: center

   *Schedule Related Unclosed Tasks*

You can similarly derive the Gantt charts for Project Phases and Resources Allocation in the following ways:

Compute Phase Scheduling
^^^^^^^^^^^^^^^^^^^^^^^^

Obtain the Gantt chart for Project Phases through the menu :menuselection:`Project --> Scheduling --> Compute Phase Scheduling`. A dialog box will appear, allowing you to select all projects or a single project.
It will compute the start date and end date of the phases which are in draft, open and pending state of the given project. Click :guilabel:`Compute` to open Gantt view.

.. _fig-gc_project_phases:

.. figure::  images/gc_project_phases.png
   :scale: 75
   :align: center

   *Gantt Chart for Project Phases*

Compute Tasks Scheduling
^^^^^^^^^^^^^^^^^^^^^^^^

This feature has the same purpose as the previous one and is used only for projects that are not cut in phases, but only consist of a list of tasks. To access it, go to :menuselection:`Project --> Scheduling --> Compute Task Scheduling`. You must and can select only a single project for computation. It shows the Gantt chart for Resources Allocation.

.. _fig-gc_resources_allocation:

.. figure::  images/gc_resources_allocation.png
   :scale: 75
   :align: center

   *Gantt Chart for Resources Allocation*


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

