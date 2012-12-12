.. index::
   single: process integration
   
Process Integration in the Management System
============================================

Processes are at the heart of a company: they form a structure for all
activities that enable the company to function effectively. A company's human
dimension is often disconnected from its processes at the moment, preventing
individual employees' aspirations from being directed towards a collective
objective.

From a mapping process, integrating management and the changing needs of each
employee becomes very useful for the fulfilment of each. Based on that, each
employee becomes aware of his own personal contribution to the company's value
chain. This representation also helps an employee's own personal management
because it shows his place and his role in the overall process, very often over
several departments.

The system of 'Corporate Intelligence' will also be highly useful to system
implementers who, after studying the requirements, have to formalize a
company's processes to put them into operation in OpenERP.

Examples of Process
-------------------

To understand the aims of the system of Corporate Intelligence (process)
better, you will now see an overview of the functions available to you in a the study of
two processes:

* A customer order quotation,

* The engagement of a new employee.

.. index::
   single: process; customer order

Following a Customer Sales Order
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The example :ref:`fig-procquot` shows the process for handling a customer sales order. Use
the menu :menuselection:`Sales --> Sales --> Sales Orders` to list all orders, then choose
Order SO001 – you can either check the checkbox to its left, or you can open
the order itself by clicking the row containing the order.

To view the process for that specific order, click the :guilabel:`Corporate Intelligence`
button (displayed as a question mark) at the
top right of the title of the list or form. The process for this order is shown in the
window, and the current state of this document can be seen by looking for the
node whose left edge is colored maroon rather than grey.

.. _fig-procquot:

.. figure:: images/process_quotation_flow.png
   :scale: 75
   :align: center

   *Example of a process handling a customer order quotation*

This order is in the ``Quotation`` state. The whole of some nodes is greyed out
because the selected document will never enter into that state, such as
invoicing based on deliveries (the order is in an invoicing mode that is based
on orders, not deliveries).

The process is completely dynamic and based on that specific sale order
document. You can click each of the process nodes (:guilabel:`Quotation`, :guilabel:`Sale Order`,
:guilabel:`Procurement`, :guilabel:`Draft Invoice`, :guilabel:`Outgoing Products`) using one of the
links or icons on it:

* Obtaining the documentation and the corresponding process in the quality manual, using the
  :guilabel:`Help` (or :guilabel:`Information`) icon,

* Obtaining the documents that an employee needs to carry out the process by clicking the green
  arrow icon,

* Seeing the menu that OpenERP uses to get the document by hovering over the green arrow icon.

.. index::
   single: process; new employee

New Employee Induction
^^^^^^^^^^^^^^^^^^^^^^

Open the employee form for Fabien Pinckaers from the menu
:menuselection:`Human Resources --> Human Resources --> Employees`.
Click the :guilabel:`Corporate Intelligence` button to open the detailed
process of engagement.

.. figure:: images/process_employee_flow.png
   :scale: 75
   :align: center

   *Example of a process engaging a new employee*

You can immediately see things that might interest the HR manager. On a single
screen she has all of the documents about the selected employee. She can then
zoom into each document to look at associated documents or
the user account in the system.

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
