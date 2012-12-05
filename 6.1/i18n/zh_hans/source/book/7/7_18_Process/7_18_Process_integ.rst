
.. i18n: .. index::
.. i18n:    single: process integration
.. i18n:    
.. i18n: Process Integration in the Management System
.. i18n: ============================================
..

.. index::
   single: process integration
   
Process Integration in the Management System
============================================

.. i18n: Processes are at the heart of a company: they form a structure for all
.. i18n: activities that enable the company to function effectively. A company's human
.. i18n: dimension is often disconnected from its processes at the moment, preventing
.. i18n: individual employees' aspirations from being directed towards a collective
.. i18n: objective.
..

Processes are at the heart of a company: they form a structure for all
activities that enable the company to function effectively. A company's human
dimension is often disconnected from its processes at the moment, preventing
individual employees' aspirations from being directed towards a collective
objective.

.. i18n: From a mapping process, integrating management and the changing needs of each
.. i18n: employee becomes very useful for the fulfilment of each. Based on that, each
.. i18n: employee becomes aware of his own personal contribution to the company's value
.. i18n: chain. This representation also helps an employee's own personal management
.. i18n: because it shows his place and his role in the overall process, very often over
.. i18n: several departments.
..

From a mapping process, integrating management and the changing needs of each
employee becomes very useful for the fulfilment of each. Based on that, each
employee becomes aware of his own personal contribution to the company's value
chain. This representation also helps an employee's own personal management
because it shows his place and his role in the overall process, very often over
several departments.

.. i18n: The system of 'Corporate Intelligence' will also be highly useful to system
.. i18n: implementers who, after studying the requirements, have to formalize a
.. i18n: company's processes to put them into operation in OpenERP.
..

The system of 'Corporate Intelligence' will also be highly useful to system
implementers who, after studying the requirements, have to formalize a
company's processes to put them into operation in OpenERP.

.. i18n: Examples of Process
.. i18n: -------------------
..

Examples of Process
-------------------

.. i18n: To understand the aims of the system of Corporate Intelligence (process)
.. i18n: better, you will now see an overview of the functions available to you in a the study of
.. i18n: two processes:
..

To understand the aims of the system of Corporate Intelligence (process)
better, you will now see an overview of the functions available to you in a the study of
two processes:

.. i18n: * A customer order quotation,
.. i18n: 
.. i18n: * The engagement of a new employee.
..

* A customer order quotation,

* The engagement of a new employee.

.. i18n: .. index::
.. i18n:    single: process; customer order
..

.. index::
   single: process; customer order

.. i18n: Following a Customer Sales Order
.. i18n: ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
..

Following a Customer Sales Order
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. i18n: The example :ref:`fig-procquot` shows the process for handling a customer sales order. Use
.. i18n: the menu :menuselection:`Sales --> Sales --> Sales Orders` to list all orders, then choose
.. i18n: Order SO001 – you can either check the checkbox to its left, or you can open
.. i18n: the order itself by clicking the row containing the order.
..

The example :ref:`fig-procquot` shows the process for handling a customer sales order. Use
the menu :menuselection:`Sales --> Sales --> Sales Orders` to list all orders, then choose
Order SO001 – you can either check the checkbox to its left, or you can open
the order itself by clicking the row containing the order.

.. i18n: To view the process for that specific order, click the :guilabel:`Corporate Intelligence`
.. i18n: button (displayed as a question mark) at the
.. i18n: top right of the title of the list or form. The process for this order is shown in the
.. i18n: window, and the current state of this document can be seen by looking for the
.. i18n: node whose left edge is colored maroon rather than grey.
..

To view the process for that specific order, click the :guilabel:`Corporate Intelligence`
button (displayed as a question mark) at the
top right of the title of the list or form. The process for this order is shown in the
window, and the current state of this document can be seen by looking for the
node whose left edge is colored maroon rather than grey.

.. i18n: .. _fig-procquot:
.. i18n: 
.. i18n: .. figure:: images/process_quotation_flow.png
.. i18n:    :scale: 75
.. i18n:    :align: center
.. i18n: 
.. i18n:    *Example of a process handling a customer order quotation*
..

.. _fig-procquot:

.. figure:: images/process_quotation_flow.png
   :scale: 75
   :align: center

   *Example of a process handling a customer order quotation*

.. i18n: This order is in the ``Quotation`` state. The whole of some nodes is greyed out
.. i18n: because the selected document will never enter into that state, such as
.. i18n: invoicing based on deliveries (the order is in an invoicing mode that is based
.. i18n: on orders, not deliveries).
..

This order is in the ``Quotation`` state. The whole of some nodes is greyed out
because the selected document will never enter into that state, such as
invoicing based on deliveries (the order is in an invoicing mode that is based
on orders, not deliveries).

.. i18n: The process is completely dynamic and based on that specific sale order
.. i18n: document. You can click each of the process nodes (:guilabel:`Quotation`, :guilabel:`Sale Order`,
.. i18n: :guilabel:`Procurement`, :guilabel:`Draft Invoice`, :guilabel:`Outgoing Products`) using one of the
.. i18n: links or icons on it:
..

The process is completely dynamic and based on that specific sale order
document. You can click each of the process nodes (:guilabel:`Quotation`, :guilabel:`Sale Order`,
:guilabel:`Procurement`, :guilabel:`Draft Invoice`, :guilabel:`Outgoing Products`) using one of the
links or icons on it:

.. i18n: * Obtaining the documentation and the corresponding process in the quality manual, using the
.. i18n:   :guilabel:`Help` (or :guilabel:`Information`) icon,
.. i18n: 
.. i18n: * Obtaining the documents that an employee needs to carry out the process by clicking the green
.. i18n:   arrow icon,
.. i18n: 
.. i18n: * Seeing the menu that OpenERP uses to get the document by hovering over the green arrow icon.
..

* Obtaining the documentation and the corresponding process in the quality manual, using the
  :guilabel:`Help` (or :guilabel:`Information`) icon,

* Obtaining the documents that an employee needs to carry out the process by clicking the green
  arrow icon,

* Seeing the menu that OpenERP uses to get the document by hovering over the green arrow icon.

.. i18n: .. index::
.. i18n:    single: process; new employee
..

.. index::
   single: process; new employee

.. i18n: New Employee Induction
.. i18n: ^^^^^^^^^^^^^^^^^^^^^^
..

New Employee Induction
^^^^^^^^^^^^^^^^^^^^^^

.. i18n: Open the employee form for Fabien Pinckaers from the menu
.. i18n: :menuselection:`Human Resources --> Human Resources --> Employees`.
.. i18n: Click the :guilabel:`Corporate Intelligence` button to open the detailed
.. i18n: process of engagement.
..

Open the employee form for Fabien Pinckaers from the menu
:menuselection:`Human Resources --> Human Resources --> Employees`.
Click the :guilabel:`Corporate Intelligence` button to open the detailed
process of engagement.

.. i18n: .. figure:: images/process_employee_flow.png
.. i18n:    :scale: 75
.. i18n:    :align: center
.. i18n: 
.. i18n:    *Example of a process engaging a new employee*
..

.. figure:: images/process_employee_flow.png
   :scale: 75
   :align: center

   *Example of a process engaging a new employee*

.. i18n: You can immediately see things that might interest the HR manager. On a single
.. i18n: screen she has all of the documents about the selected employee. She can then
.. i18n: zoom into each document to look at associated documents or
.. i18n: the user account in the system.
..

You can immediately see things that might interest the HR manager. On a single
screen she has all of the documents about the selected employee. She can then
zoom into each document to look at associated documents or
the user account in the system.

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
