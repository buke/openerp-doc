.. include:: <isonum.txt>

.. index::
   single: Process
   single: workflow

.. _ch-process:

*******
Process
*******

 *If you have reached this far in the book, your mind may well be reeling with the number
 of new documents (based on business objects) and processes that you need to encounter to
 model and manage your business.*
 
 *OpenERP's process module, which is installed automatically when a process-aware module
 is installed, shows you cross-functional processes and technical workflows for those
 nodes in the process that have them. This visualization is invaluable for documentation - 
 but it also goes a step further. You can modify processes and workflows and even generate
 entirely new processes and workflows for your various document types.*
 
 *If your starting point is a specific document, such as
 an invoice or order, then you will also be shown the exact position of that document on 
 its process and workflow diagrams.*

.. index::
   single: module; sale
   single: modules; hr_
   single: module; hr_attendance
   single: module; hr_contract
   single: module; hr_holidays
   single: module; hr_holidays_request

For this chapter you should start with a fresh database that includes demonstration data,
with :mod:`sale` and its dependencies installed and no particular chart of accounts configured. 
:mod:`process` is one of those dependencies. Also install some of the :mod:`hr` modules for
the second example in this chapter, such as :mod:`hr_attendance`, :mod:`hr_contract`,
and :mod:`hr_holidays`.

.. raw:: html

    <div class="all-toctree">

.. toctree::

   7_18_Process_integ
   7_18_Process_workflow

.. raw:: html

    </div>

The organization and quality of a company is typically related to its maturity. A mature
company is one where processes are well established, and where staff do not
waste much time searching for documents or trying to find out how to do their
different tasks.

From this need for effective organization and explicit quality improvement,
have appeared numerous tools:

* The ISO9001 quality standard,

* Business Process Management (BPM) tools,

* Use Case workflows, and formalized standards such as UML,

* The company Quality Manual.

The problem is that these tools are usually quite separate from your management
system and often reserved for the use of just a few specific people in your
company. They are treated separately rather than put at the heart of your
management system. When you ask company staff about ISO9001 they usually see it
as a constraint rather than a helpful daily management tool.

To help the company meet its quality requirements and to form these processes
into assistance integrated with everyday work, OpenERP supplies a Corporate
Intelligence\ |reg| tool that enables you to put company processes at the heart
of your management system.

The system enables:

* new employees to learn how to use the software by graphically and dynamically, discovering how each
  document and action works,

* easy access to the all the links to a document and everything that is attached to it,

* people to see both a high-level map and the detail of all the company's processes,

* access to a graphical model and integrated quality manual for rapid access that depends on the
  work context,

* use of a knowledge base and capitalization of that knowledge for all of the company's actions in
  the form of interactive processes,

* an employee to become more aware of his role in the whole environment.

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
