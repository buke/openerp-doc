
.. i18n: .. index::
.. i18n:    single: HR; management
.. i18n:    single: employee
..

.. index::
   single: HR; management
   single: employee

.. i18n: Managing Human Resources
.. i18n: ========================
..

Managing Human Resources
========================

.. i18n: To establish a system that is integrated into the company's management, you need to start with a
.. i18n: current list of collaborators.
..

To establish a system that is integrated into the company's management, you need to start with a
current list of collaborators.

.. i18n: .. note:: Do not confuse employees and users
.. i18n: 
.. i18n: 	For OpenERP, “employee” represents all of the physical people who have a work contract with
.. i18n: 	the company. This includes all types of contracts: contracts with both fixed and indeterminate time
.. i18n: 	periods, and also independent and freelance service contracts.
.. i18n: 
.. i18n: 	A “user” is a physical person who is given access to the company's systems. Most employees are
.. i18n: 	users but some users are not employees: external partners can have access to parts of the system.
..

.. note:: Do not confuse employees and users

	For OpenERP, “employee” represents all of the physical people who have a work contract with
	the company. This includes all types of contracts: contracts with both fixed and indeterminate time
	periods, and also independent and freelance service contracts.

	A “user” is a physical person who is given access to the company's systems. Most employees are
	users but some users are not employees: external partners can have access to parts of the system.

.. i18n: Here are some examples of functions which depend on the accuracy of the employee list:
..

Here are some examples of functions which depend on the accuracy of the employee list:

.. i18n: * the cost of a service, which depends on the employee's working contract,
.. i18n: 
.. i18n: * project planning, which depends on the work pattern of the project contributors,
.. i18n: 
.. i18n: * the client billing rate, which probably depends on the employee's job function,
.. i18n: 
.. i18n: * the chain of command, or responsibilities, which is related to the hierarchical structure of the
.. i18n:   company.
..

* the cost of a service, which depends on the employee's working contract,

* project planning, which depends on the work pattern of the project contributors,

* the client billing rate, which probably depends on the employee's job function,

* the chain of command, or responsibilities, which is related to the hierarchical structure of the
  company.

.. i18n: Link employees and OpenERP users to facilitate the management of rights
.. i18n: -----------------------------------------------------------------------
..

Link employees and OpenERP users to facilitate the management of rights
-----------------------------------------------------------------------

.. i18n: To define a new employee in OpenERP, use the menu :menuselection:`Human Resources --> Employees`.
..

To define a new employee in OpenERP, use the menu :menuselection:`Human Resources --> Employees`.

.. i18n: .. figure::  images/service_employee_form.png
.. i18n:    :scale: 75
.. i18n:    :align: center
.. i18n: 
.. i18n:    *Form describing an employee*
..

.. figure::  images/service_employee_form.png
   :scale: 75
   :align: center

   *Form describing an employee*

.. i18n: Start by entering the employee's name in :guilabel:`Name` and the company that this employee works for
.. i18n: in :guilabel:`Company`. You can then create a new user of the OpenERP system linked to this
.. i18n: employee by filling in a new :guilabel:`User` form through the :guilabel:`User` field.
..

Start by entering the employee's name in :guilabel:`Name` and the company that this employee works for
in :guilabel:`Company`. You can then create a new user of the OpenERP system linked to this
employee by filling in a new :guilabel:`User` form through the :guilabel:`User` field.

.. i18n: Even if the employee is not a user, it is best if you
.. i18n: create a system access for most of your staff just so that you can control their access rights from
.. i18n: the outset (and you can do that through this field if you need to).
..

Even if the employee is not a user, it is best if you
create a system access for most of your staff just so that you can control their access rights from
the outset (and you can do that through this field if you need to).

.. i18n: .. tip:: Employee and User link.
.. i18n: 
.. i18n: 	If the employee has a user account on the system, you always link his or her user
.. i18n: 	account to the employee form.
.. i18n: 
.. i18n: 	Creating this link enables automatic completion to be done on the :guilabel:`Employee` field in the
.. i18n: 	relevant forms, such as services and expense records.
..

.. tip:: Employee and User link.

	If the employee has a user account on the system, you always link his or her user
	account to the employee form.

	Creating this link enables automatic completion to be done on the :guilabel:`Employee` field in the
	relevant forms, such as services and expense records.

.. i18n: Then enter the employee's address.
..

Then enter the employee's address.

.. i18n: .. todo:: We need to give better guidance about Partners vs Employees just here.
..

.. todo:: We need to give better guidance about Partners vs Employees just here.

.. i18n: This appears in the partner contact form in OpenERP. Since
.. i18n: employees are people that have contracts with your company, it is logical that they have entries
.. i18n: like any other partner in your database. So enter the name of the employee as a new partner Name and
.. i18n: the address in the Partner Contact section of the General tab.
.. i18n: Then all of the functions that apply to a partner can also be
.. i18n: applied to an employee. This is particularly useful for tracking debits and credits in
.. i18n: the accounts – so you can track salary payments, for example.
..

This appears in the partner contact form in OpenERP. Since
employees are people that have contracts with your company, it is logical that they have entries
like any other partner in your database. So enter the name of the employee as a new partner Name and
the address in the Partner Contact section of the General tab.
Then all of the functions that apply to a partner can also be
applied to an employee. This is particularly useful for tracking debits and credits in
the accounts – so you can track salary payments, for example.

.. i18n: To help employees encode and validate timesheets and attendances, you can install :mod:`hr_timesheet_sheet` by selecting :guilabel:`Timesheets` in the :guilabel:`Reconfigure` wizard.
.. i18n: You can then set both an analytic journal and a linked product to this employee
.. i18n: in the :guilabel:`Timesheets` tab. If
.. i18n: you do it that way, then this information can be used to track services. For now, just complete the
.. i18n: form with the following information:
..

To help employees encode and validate timesheets and attendances, you can install :mod:`hr_timesheet_sheet` by selecting :guilabel:`Timesheets` in the :guilabel:`Reconfigure` wizard.
You can then set both an analytic journal and a linked product to this employee
in the :guilabel:`Timesheets` tab. If
you do it that way, then this information can be used to track services. For now, just complete the
form with the following information:

.. i18n: *  :guilabel:`Analytic Journal` : usually a ``Timesheet Journal``,
.. i18n: 
.. i18n: *  :guilabel:`Product` : a service product that describes how this employee would be charged out,
.. i18n:    for example as ``Service on Timesheet``.
..

*  :guilabel:`Analytic Journal` : usually a ``Timesheet Journal``,

*  :guilabel:`Product` : a service product that describes how this employee would be charged out,
   for example as ``Service on Timesheet``.

.. i18n: .. index::
.. i18n:    single: employee; billing
..

.. index::
   single: employee; billing

.. i18n: Define employees' billing prices and costs
.. i18n: ------------------------------------------
..

Define employees' billing prices and costs
------------------------------------------

.. i18n: To be able to use the timesheets at all, you must first define those employees who are system users.
.. i18n: The employee definition forms contain the information necessary to use that sheet, such as the job
.. i18n: title, and hourly costs.
..

To be able to use the timesheets at all, you must first define those employees who are system users.
The employee definition forms contain the information necessary to use that sheet, such as the job
title, and hourly costs.

.. i18n: Two fields will be of particular interest to you for managing timesheets: the :guilabel:`Analytic
.. i18n: Journal` and the :guilabel:`Product`.
..

Two fields will be of particular interest to you for managing timesheets: the :guilabel:`Analytic
Journal` and the :guilabel:`Product`.

.. i18n: All the analytic entries about the costs of service times will be stored in the analytic journal.
.. i18n: These enable you to isolate the cost of service from other company costs, such as the purchase of raw
.. i18n: materials, expenses receipts and subcontracting. You can use different journals for each employee to
.. i18n: separate costs by department or by function.
..

All the analytic entries about the costs of service times will be stored in the analytic journal.
These enable you to isolate the cost of service from other company costs, such as the purchase of raw
materials, expenses receipts and subcontracting. You can use different journals for each employee to
separate costs by department or by function.

.. i18n: The employee is also associated with a product in your database in OpenERP. An employee is linked
.. i18n: with a product, so they can be 'bought' (subcontracting) or 'invoiced' (project management). You have
.. i18n: to create a product for each job type in your company.
..

The employee is also associated with a product in your database in OpenERP. An employee is linked
with a product, so they can be 'bought' (subcontracting) or 'invoiced' (project management). You have
to create a product for each job type in your company.

.. i18n: The following information is important in the product form:
..

The following information is important in the product form:

.. i18n: *  :guilabel:`Name` : \ ``Secretary`` \,  \ ``Salesperson`` \ or \ ``Project Manager``\
.. i18n: 
.. i18n: *  :guilabel:`Product Type` : \ ``Service``\
.. i18n: 
.. i18n: *  :guilabel:`Unit of Measure` : \ ``Hour`` \ or \ ``Day``\
.. i18n: 
.. i18n: *  :guilabel:`Cost Price`
.. i18n: 
.. i18n: *  :guilabel:`Sale Price`
.. i18n: 
.. i18n: *  :guilabel:`Costing Method` : either \ ``Standard Price``\  or  \ ``Average Price``\
..

*  :guilabel:`Name` : \ ``Secretary`` \,  \ ``Salesperson`` \ or \ ``Project Manager``\

*  :guilabel:`Product Type` : \ ``Service``\

*  :guilabel:`Unit of Measure` : \ ``Hour`` \ or \ ``Day``\

*  :guilabel:`Cost Price`

*  :guilabel:`Sale Price`

*  :guilabel:`Costing Method` : either \ ``Standard Price``\  or  \ ``Average Price``\

.. i18n: .. index::
.. i18n:    single: module; product_index
..

.. index::
   single: module; product_index

.. i18n: .. tip:: Price Indexation
.. i18n: 
.. i18n: 	When the `Costing Method` is `Average Price` in the `Product` form, you can have a button :guilabel:`Update`, beside the `Cost Price` field, that opens up a wizard for changing the cost price.
..

.. tip:: Price Indexation

	When the `Costing Method` is `Average Price` in the `Product` form, you can have a button :guilabel:`Update`, beside the `Cost Price` field, that opens up a wizard for changing the cost price.

.. i18n: In summary, each company employee corresponds, in most cases, to:
..

In summary, each company employee corresponds, in most cases, to:

.. i18n: * a :guilabel:`Partner`
.. i18n: 
.. i18n: * an :guilabel:`Employee` form,
.. i18n: 
.. i18n: * a :guilabel:`System User`.
..

* a :guilabel:`Partner`

* an :guilabel:`Employee` form,

* a :guilabel:`System User`.

.. i18n: And each company job position corresponds to a :guilabel:`Product`.
..

And each company job position corresponds to a :guilabel:`Product`.

.. i18n: .. index::
.. i18n:    single: module; hr_contract
..

.. index::
   single: module; hr_contract

.. i18n: .. note:: Time Charge Rates
.. i18n: 
.. i18n: 	By default, the hourly cost of an employee is given by the standard cost of the product linked to
.. i18n: 	that employee.
.. i18n: 	But if you install the :mod:`hr_contract` module, it is possible to manage contracts differently.
.. i18n: 	The hourly cost of the employee is then automatically calculated from their employment contract
.. i18n: 	when they enter their timesheet data.
.. i18n: 
.. i18n: 	To do this, the software uses a factor defined in the contract type
.. i18n: 	(for example, the gross monthly salary, calculated per day).
.. i18n: 	Ideally, this factor should take into account the salary costs, taxes, insurances and other
.. i18n: 	overheads associated with pay.
..

.. note:: Time Charge Rates

	By default, the hourly cost of an employee is given by the standard cost of the product linked to
	that employee.
	But if you install the :mod:`hr_contract` module, it is possible to manage contracts differently.
	The hourly cost of the employee is then automatically calculated from their employment contract
	when they enter their timesheet data.

	To do this, the software uses a factor defined in the contract type
	(for example, the gross monthly salary, calculated per day).
	Ideally, this factor should take into account the salary costs, taxes, insurances and other
	overheads associated with pay.

.. i18n: .. index::
.. i18n:    single: employee; categories
..

.. index::
   single: employee; categories

.. i18n: Define employee categories to assign different Holiday’s rights to different employee groups
.. i18n: --------------------------------------------------------------------------------------------
..

Define employee categories to assign different Holiday’s rights to different employee groups
--------------------------------------------------------------------------------------------

.. i18n: You must create and assign employee categories for employees in order to be able to assign and manage leave and allocation requests by category. You can define employee categories from :menuselection:`Human Resources --> Configuration --> Human Resources --> Employees --> Categories of Employee`. For a new category, define its name in :guilabel:`Category`. A category may also be assigned a :guilabel:`Parent Category`.
..

You must create and assign employee categories for employees in order to be able to assign and manage leave and allocation requests by category. You can define employee categories from :menuselection:`Human Resources --> Configuration --> Human Resources --> Employees --> Categories of Employee`. For a new category, define its name in :guilabel:`Category`. A category may also be assigned a :guilabel:`Parent Category`.

.. i18n: .. figure::  images/employee_categories.png
.. i18n:    :scale: 75
.. i18n:    :align: center
.. i18n: 
.. i18n:    *Example of categories defined for employees*
..

.. figure::  images/employee_categories.png
   :scale: 75
   :align: center

   *Example of categories defined for employees*

.. i18n: To link an employee to a category, open the employee form through :menuselection:`Human Resources --> Human Resources --> Employees`. In the :guilabel:`Categories` tab, you can assign more than one category to an employee by clicking :guilabel:`Add` and selecting a category.
..

To link an employee to a category, open the employee form through :menuselection:`Human Resources --> Human Resources --> Employees`. In the :guilabel:`Categories` tab, you can assign more than one category to an employee by clicking :guilabel:`Add` and selecting a category.

.. i18n: .. figure::  images/employee_assign_category.png
.. i18n:    :scale: 75
.. i18n:    :align: center
.. i18n: 
.. i18n:    *Assign categories to an employee in the Employee form*
..

.. figure::  images/employee_assign_category.png
   :scale: 75
   :align: center

   *Assign categories to an employee in the Employee form*

.. i18n: Now, when you create a new leave or allocation request from the menuitems under :menuselection:`Human Resources --> Holidays`, if your :guilabel:`Leave Category` or :guilabel:`Allocation Category` is ``By Employee Category``, then you must choose a pre-defined :guilabel:`Category`. The request will then be applicable to all those employees who belong to the category selected. For example, you can create an allocation request for employees belonging to the ``Trainee`` category, entitling them to fewer leaves than the rest of the employees.
..

Now, when you create a new leave or allocation request from the menuitems under :menuselection:`Human Resources --> Holidays`, if your :guilabel:`Leave Category` or :guilabel:`Allocation Category` is ``By Employee Category``, then you must choose a pre-defined :guilabel:`Category`. The request will then be applicable to all those employees who belong to the category selected. For example, you can create an allocation request for employees belonging to the ``Trainee`` category, entitling them to fewer leaves than the rest of the employees.

.. i18n: .. index::
.. i18n:    single: employee; contracts
..

.. index::
   single: employee; contracts

.. i18n: Define contract types and wage types with start and end dates for contracts as well as trial periods
.. i18n: ----------------------------------------------------------------------------------------------------
..

Define contract types and wage types with start and end dates for contracts as well as trial periods
----------------------------------------------------------------------------------------------------

.. i18n: If you install the :mod:`hr_contract` module you can link contract details to the employee record.
.. i18n: The configuration wizard to install this module is shown below.
..

If you install the :mod:`hr_contract` module you can link contract details to the employee record.
The configuration wizard to install this module is shown below.

.. i18n: .. figure::  images/config_wiz_contract.png
.. i18n:    :scale: 75
.. i18n:    :align: center
.. i18n: 
.. i18n:    *Configuration wizard to install hr_contract*
..

.. figure::  images/config_wiz_contract.png
   :scale: 75
   :align: center

   *Configuration wizard to install hr_contract*

.. i18n: Define new contract types at :menuselection:`Human Resources --> Configuration --> Human Resources --> Contract --> Contract Types`.
..

Define new contract types at :menuselection:`Human Resources --> Configuration --> Human Resources --> Contract --> Contract Types`.

.. i18n: .. figure::  images/hr_contract_type_list.png
.. i18n:    :scale: 75
.. i18n:    :align: center
.. i18n: 
.. i18n:    *Contract Types list*
..

.. figure::  images/hr_contract_type_list.png
   :scale: 75
   :align: center

   *Contract Types list*

.. i18n: You may similarly define wage types at :menuselection:`Human Resources --> Configuration --> Human Resources --> Contract --> Wage Type`. Enter the following details in the form:
..

You may similarly define wage types at :menuselection:`Human Resources --> Configuration --> Human Resources --> Contract --> Wage Type`. Enter the following details in the form:

.. i18n: *  :guilabel:`Wage Type Name` : A name for the wage type.
.. i18n: *  :guilabel:`Wage Period` : Select a pre-defined wage period. Wage periods are defined at :menuselection:`Human Resources --> Configuration --> Human Resources --> Contract --> Wage period`.
.. i18n: *  :guilabel:`Type` : Either ``Gross`` or ``Net``.
.. i18n: *  :guilabel:`Factor for hour cost` : Used by the timesheet system to compute the price of an hour of work based on the contract of an employee.
..

*  :guilabel:`Wage Type Name` : A name for the wage type.
*  :guilabel:`Wage Period` : Select a pre-defined wage period. Wage periods are defined at :menuselection:`Human Resources --> Configuration --> Human Resources --> Contract --> Wage period`.
*  :guilabel:`Type` : Either ``Gross`` or ``Net``.
*  :guilabel:`Factor for hour cost` : Used by the timesheet system to compute the price of an hour of work based on the contract of an employee.

.. i18n: .. figure::  images/hr_wage_type.png
.. i18n:    :scale: 75
.. i18n:    :align: center
.. i18n: 
.. i18n:    *Wage Type form*
..

.. figure::  images/hr_wage_type.png
   :scale: 75
   :align: center

   *Wage Type form*

.. i18n: Using :menuselection:`Human Resources --> Human Resources --> Contracts` you can create and edit contracts.
..

Using :menuselection:`Human Resources --> Human Resources --> Contracts` you can create and edit contracts.

.. i18n: .. figure::  images/service_hr_contract.png
.. i18n:    :scale: 75
.. i18n:    :align: center
.. i18n: 
.. i18n:    *Definition of a working contract for a given employee*
..

.. figure::  images/service_hr_contract.png
   :scale: 75
   :align: center

   *Definition of a working contract for a given employee*

.. i18n: You can enter information about the employment contract for the employee, such as:
..

You can enter information about the employment contract for the employee, such as:

.. i18n: *  :guilabel:`Contract Reference`
.. i18n: 
.. i18n: *  :guilabel:`Job Title`
.. i18n: 
.. i18n: *  :guilabel:`Working Schedule`
.. i18n: 
.. i18n: *  :guilabel:`Start Date`
.. i18n: 
.. i18n: *  :guilabel:`End Date`
.. i18n: 
.. i18n: *  :guilabel:`Wage Type` : Select one from pre-defined wage types.
.. i18n: 
.. i18n: *  :guilabel:`Contract Type` : Select one from pre-defined contract types.
.. i18n: 
.. i18n: *  :guilabel:`Trial Start Date` : Start date for the contract trial period, if any.
.. i18n: 
.. i18n: *  :guilabel:`Trial End Date` : End date for the contract trial period, if any.
..

*  :guilabel:`Contract Reference`

*  :guilabel:`Job Title`

*  :guilabel:`Working Schedule`

*  :guilabel:`Start Date`

*  :guilabel:`End Date`

*  :guilabel:`Wage Type` : Select one from pre-defined wage types.

*  :guilabel:`Contract Type` : Select one from pre-defined contract types.

*  :guilabel:`Trial Start Date` : Start date for the contract trial period, if any.

*  :guilabel:`Trial End Date` : End date for the contract trial period, if any.

.. i18n: .. index::
.. i18n:    single: employee; sign in / sign out
..

.. index::
   single: employee; sign in / sign out

.. i18n: Manage attendance (Sign in / Sign out)
.. i18n: --------------------------------------
..

Manage attendance (Sign in / Sign out)
--------------------------------------

.. i18n: In some companies, staff have to sign in when they arrive at work and sign out again at the end of
.. i18n: the day. If each employee has been linked to a system user, then they can sign into OpenERP by
.. i18n: using the menu :menuselection:`Human Resources --> Attendances --> Sign in / Sign out`.
..

In some companies, staff have to sign in when they arrive at work and sign out again at the end of
the day. If each employee has been linked to a system user, then they can sign into OpenERP by
using the menu :menuselection:`Human Resources --> Attendances --> Sign in / Sign out`.

.. i18n: If an employee has forgotten to sign out on leaving, the system proposes that they sign out manually
.. i18n: and type in the time that they left when they come in again the next day. This gives you a simple way
.. i18n: of managing forgotten sign-outs.
..

If an employee has forgotten to sign out on leaving, the system proposes that they sign out manually
and type in the time that they left when they come in again the next day. This gives you a simple way
of managing forgotten sign-outs.

.. i18n: Find employee attendance details from their forms in
.. i18n: :menuselection:`Human Resources --> Employees`.
..

Find employee attendance details from their forms in
:menuselection:`Human Resources --> Employees`.

.. i18n: To get the detail of attendances from an employee's form in OpenERP, you can use the
.. i18n: available reports:
..

To get the detail of attendances from an employee's form in OpenERP, you can use the
available reports:

.. i18n: *  :guilabel:`Attendances By Month`
.. i18n: 
.. i18n: *  :guilabel:`Attendances By Week`
.. i18n: 
.. i18n: *  :guilabel:`Attendance Error Report`
..

*  :guilabel:`Attendances By Month`

*  :guilabel:`Attendances By Week`

*  :guilabel:`Attendance Error Report`

.. i18n: The last report highlights errors in attendance data entry.
.. i18n: It shows you whether an employee has entered the time of
.. i18n: entry or exit manually and the differences between the actual and expected sign out time and the sign in time.
..

The last report highlights errors in attendance data entry.
It shows you whether an employee has entered the time of
entry or exit manually and the differences between the actual and expected sign out time and the sign in time.

.. i18n: The second report shows the attendance data for the selected month.
..

The second report shows the attendance data for the selected month.

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
