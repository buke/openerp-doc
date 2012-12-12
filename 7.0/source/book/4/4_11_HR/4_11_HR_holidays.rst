
.. index::
   single: Human Resources; holidays
..

Holiday Management
==================

You can manage leaves taken by employees using the :mod:`hr_holidays`
module. The configuration wizard to install this module is shown below:

.. figure::  images/config_wiz_holidays.png
   :scale: 75
   :align: center

   *Configuration wizard to install hr_holidays module*

Using the menu :menuselection:`Human Resources --> Holidays --> Leave Requests` an employee can request a leave.

Leaves requests can be recorded by employees and validated by their managers.
Once a leave request is validated, it appears automatically in the agenda of the employee.
You can define several allocation types (paid holidays, sickness, etc.) and manage allocations
per type.

OpenERP can provide the following features for efficient holiday management process:

* It helps you to manage leaves and leave requests.
* Synchronisation with an internal agenda (use of :mod:`crm`) is possible:
  in order to automatically create a case when a holiday request is accepted,
  you have to link the holidays status to a case section.
* You can set up colour preferences according to your leave type, for example, `Sick Leave` should be red in reports.
* An employee can request for more days off, by making a new Allocation Request through :menuselection:`Human Resources --> Holidays --> Allocation Requests`.

The statistical report for leaves can be seen using the
:menuselection:`Human Resources --> Reporting --> Holidays --> Leaves Analysis` menu.

.. index::
   single: holidays; leave types

Define different leave types
----------------------------

You can define various leave types which can be availed of by an employee during a request for leave. To define a new leave type, navigate to :menuselection:`Human Resources --> Configuration --> Holidays --> Leave Type` and click :guilabel:`New`.

.. figure::  images/holidays_leave_type.png
   :scale: 80
   :align: center

   *Leave Type form*

You can configure the following information:

* :guilabel:`Leave Type` : A name for the leave type.
* :guilabel:`Colour in Report` : A colour that will be used in the leaves summary report.
* :guilabel:`Meeting` : If you select a meeting, once a leave is validated, an event will be created in the calendar.
* :guilabel:`Apply Double Validation` : If ``True``, then the request will require a second validator.
* :guilabel:`Allow to Override Limit` : If ``True``, the employee will be allowed to take more leaves than the maximum limit.

After entering the leave type information, click :guilabel:`Save`.

.. index::
   single: holidays; manage requests and approvals

Manage Holiday requests and approvals
-------------------------------------

An employee can request for leave from :menuselection:`Human Resources --> Holidays --> Leave Requests`. In a new :guilabel:`Leave Requests` form, you may enter the following:

* :guilabel:`Description` : Reason for leave.
* :guilabel:`Leave Category` : Either ``By Employee`` or ``By Employee Category``.
* :guilabel:`Employee` : If leave category is ``By Employee``, you must select an employee who places this request.
* :guilabel:`Category` : If leave category is ``By Employee Category``, you must select an employee category which places this request.
* :guilabel:`Leave Type`: Select a pre-defined type of leave.
* :guilabel:`Start Date` : Leave start date.
* :guilabel:`End Date` : Leave end date.
* :guilabel:`Number of Days` : It is calculated based on the :guilabel:`Start Date` and the :guilabel:`End Date`.

.. figure::  images/employee_leave_request_form.png
   :scale: 75
   :align: center

   *Leave Requests form*

The employee can click :guilabel:`Confirm` to make the leave request available to his manager for approval. The employee's manager can find leave requests awaiting approval by navigating to :menuselection:`Human Resources --> Holidays --> Leave Requests` and clicking :guilabel:`Clear` and :guilabel:`To Approve` filter button. The manager can select a pending request to open its form view and click :guilabel:`Refuse` to reject the request or :guilabel:`Approve` to accept the request. If the selected leave type has :guilabel:`Apply Double Validation` set to ``True``, then another action by a second manager will be required to give the request its final state, from ``Waiting Second Approval`` to either ``Approved`` or ``Refused``.

.. index::
   single: holidays; previous requests

Track previous Holiday requests
-------------------------------

Previous holidays can be tracked in a number of ways in OpenERP. You can get a report of leave requests by all users from :menuselection:`Human Resources --> Holidays --> Leave Requests`. Click :guilabel:`Clear` and then :guilabel:`Validated` to see a list of all approved leave requests. To see refused requests, click :guilabel:`Clear` and see the records marked with the colour red.

To see previous allocation requests, navigate to :menuselection:`Human Resources --> Holidays --> Allocation Requests` and follow the same procedure as above.

Through :menuselection:`Human Resources --> Holidays --> Leaves Summary`, you can track previous leaves as well as allocation requests in the same manner, but only for the currently logged in user. By default, you can see the requests grouped by leave type.

:menuselection:`Human Resources --> Reporting --> Holidays --> Leaves Analysis` will give you the statistical report of leaves and allocations grouped by employee and leave type. To see all requests without grouping, click :guilabel:`Clear`.

All the above statistical reports are enhanced by various filters and groupings to assist you in your search for required information. You can filter requests by their :guilabel:`State` (`Validated`, `To Confirm`, `To Approve`), :guilabel:`Employee`, :guilabel:`Department` and :guilabel:`Leave Type`. You can also view requests placed in :guilabel:`This Month`. You can group by :guilabel:`Employee`, :guilabel:`Manager`, :guilabel:`Department`, :guilabel:`Type` and :guilabel:`State`.

.. figure::  images/holidays_leaves_analysis.png
   :scale: 75
   :align: center

   *Leaves Analysis statistical report*

To get an overview of leaves by department, go to :menuselection:`Human Resource --> Reporting --> Holidays --> Leaves by Department`. You may select a :guilabel:`From` date, a :guilabel:`Leave Type` (``Validated``, ``Confirmed`` or ``Both Validated and Confirmed``) and select at least one department. Click :guilabel:`Print` to generate a PDF report based on your specifications.

.. figure::  images/holidays_dept_leaves.png
   :scale: 80
   :align: center

   *Leaves by Department PDF report*

.. index::
   single: holidays; allocation requests

Allow employees to enter their own allocation requests
------------------------------------------------------

To be able to request leaves at all, an employee must be allocated some leaves which he can avail of. Usually the management makes an allocation of leaves for its employees. But, for instance, when an employee has been working on an exceptional basis on weekends, he might be entitled to extra leaves. In such a case, the employee himself can be allowed to place a request for allocation, which can then be approved or rejected by his manager. If approved, the employee can request leaves based on the type and limit of this allocation too.

Leave allocations can be requested from :menuselection:`Human Resources --> Holidays --> Allocation Requests`. In its form view you can fill the following details:

* :guilabel:`Description` : A name for the request.
* :guilabel:`Allocation Category` : Either ``By Employee`` or ``By Employee Category``.
* :guilabel:`Employee` : If allocation category is ``By Employee``, you must select an employee for whom this allocation is made.
* :guilabel:`Category` : If allocation category is ``By Employee Category``, you must select an employee category for whom this allocation is made.
* :guilabel:`Leave Type` : Select a pre-defined leave type.
* :guilabel:`Number of Days` : The number of days requested for allocation.
* :guilabel:`Reasons` : Specify the reason of request.

The remaining fields are read-only and will acquire details once the request has been accepted or rejected. The employee can click :guilabel:`Confirm` to send the allocation request to his manager. The state of the request will now be ``Waiting Approval``.

.. figure::  images/holidays_allocation_request.png
   :scale: 75
   :align: center

   *Allocation Requests form*

The manager will then find this request in his list of allocation requests. He can then either click :guilabel:`Refuse` to reject the request or click :guilabel:`Approve` to accept the request.

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
