.. i18n: .. include:: <isonum.txt>
..

.. include:: <isonum.txt>

.. i18n: .. index::
.. i18n:    single: Process
.. i18n:    single: workflow
..

.. index::
   single: Process
   single: workflow

.. i18n: .. _ch-process:
.. i18n: 
.. i18n: *******
.. i18n: Process
.. i18n: *******
..

.. _ch-process:

*******
流程
*******

.. i18n:  *If you have reached this far in the book, your mind may well be reeling with the number
.. i18n:  of new documents (based on business objects) and processes that you need to encounter to
.. i18n:  model and manage your business.*
.. i18n:  
.. i18n:  *OpenERP's process module, which is installed automatically when a process-aware module
.. i18n:  is installed, shows you cross-functional processes and technical workflows for those
.. i18n:  nodes in the process that have them. This visualization is invaluable for documentation - 
.. i18n:  but it also goes a step further. You can modify processes and workflows and even generate
.. i18n:  entirely new processes and workflows for your various document types.*
.. i18n:  
.. i18n:  *If your starting point is a specific document, such as
.. i18n:  an invoice or order, then you will also be shown the exact position of that document on 
.. i18n:  its process and workflow diagrams.*
..

 *在学习流程之前,你可能不是很清楚哪些带编号的业务对象,更没有头绪如何去实现模型和业务之间的流程.*
 
 *在安装有流程功能的模块时,OpenERP的流程模块会被自动安装，流程里的各节点之间的跨职能的流程和工作流技术细节会被很好地展示。这种可视化对流程规范来说是非常重要- 甚至还可以更深一步。你可以修改已有的流程和工作流，甚至可以根据不同的单据类型重新产生新的流程和工作流.*
 
 *如果你从发票或订单这类特定的单据进入,那你可以看到这个单据在工作流程图上的确切位置*

.. i18n: .. index::
.. i18n:    single: module; sale
.. i18n:    single: modules; hr_
.. i18n:    single: module; hr_attendance
.. i18n:    single: module; hr_contract
.. i18n:    single: module; hr_holidays
.. i18n:    single: module; hr_holidays_request
..

.. index::
   single: module; sale
   single: modules; hr_
   single: module; hr_attendance
   single: module; hr_contract
   single: module; hr_holidays
   single: module; hr_holidays_request

.. i18n: For this chapter you should start with a fresh database that includes demonstration data,
.. i18n: with :mod:`sale` and its dependencies installed and no particular chart of accounts configured. 
.. i18n: :mod:`process` is one of those dependencies. Also install some of the :mod:`hr` modules for
.. i18n: the second example in this chapter, such as :mod:`hr_attendance`, :mod:`hr_contract`,
.. i18n: and :mod:`hr_holidays`.
..

在本章，你有一个包含销售模块(:mod:`sale`)且带演示数据的新数据库就可以开始，跟销售关联的模块都会被自动安装，流程模块(:mod:'process')是其中之一，也不必去配置好科目表.
对于本章的第二个例子，你还需要安装一些诸如(:mod:`hr_attendance`)，(:mod:`hr_contract`)和(:mod:`hr_holidays`)一些相关的人事模块(:mod:`hr`).

.. i18n: .. raw:: html
.. i18n: 
.. i18n:     <div class="all-toctree">
..

.. raw:: html

    <div class="all-toctree">

.. i18n: .. toctree::
.. i18n: 
.. i18n:    7_18_Process_integ
.. i18n:    7_18_Process_workflow
..

.. toctree::

   7_18_Process_integ
   7_18_Process_workflow

.. i18n: .. raw:: html
.. i18n: 
.. i18n:     </div>
..

.. raw:: html

    </div>

.. i18n: The organization and quality of a company is typically related to its maturity. A mature
.. i18n: company is one where processes are well established, and where staff do not
.. i18n: waste much time searching for documents or trying to find out how to do their
.. i18n: different tasks.
..

一个公司组织结构的优劣通常要看这个公司的是否成熟。一个成熟的公司需要有一个完善的流程，员工能够根据流程快速找到所需文档,知道如何去完成各种任务.

.. i18n: From this need for effective organization and explicit quality improvement,
.. i18n: have appeared numerous tools:
..

有很多现成的工具可以满足建立有效的组织结构或提高组织结构品质的需求:

.. i18n: * The ISO9001 quality standard,
.. i18n: 
.. i18n: * Business Process Management (BPM) tools,
.. i18n: 
.. i18n: * Use Case workflows, and formalized standards such as UML,
.. i18n: 
.. i18n: * The company Quality Manual.
..

* ISO9001 质量标准,

* 业务流程管理工具(BPM),

* 类似统一建模语言(UML)的用例工作流或正式标准规范,

* 公司质量手册.

.. i18n: The problem is that these tools are usually quite separate from your management
.. i18n: system and often reserved for the use of just a few specific people in your
.. i18n: company. They are treated separately rather than put at the heart of your
.. i18n: management system. When you ask company staff about ISO9001 they usually see it
.. i18n: as a constraint rather than a helpful daily management tool.
..

问题是这些工具通常跟管理系统是分开的，只是被公司里的个别人所使用。它们往往不是放在在管理系统之中处理而是分开处理。当你问公司员工关于ISO9001时,你会发现它只是被看作一个规约，而不是一个非常有用的日常管理工具。

.. i18n: To help the company meet its quality requirements and to form these processes
.. i18n: into assistance integrated with everyday work, OpenERP supplies a Corporate
.. i18n: Intelligence\ |reg| tool that enables you to put company processes at the heart
.. i18n: of your management system.
..

To help the company meet its quality requirements and to form these processes
into assistance integrated with everyday work, OpenERP supplies a Corporate
Intelligence\ |reg| tool that enables you to put company processes at the heart
of your management system.

.. i18n: The system enables:
..

The system enables:

.. i18n: * new employees to learn how to use the software by graphically and dynamically, discovering how each
.. i18n:   document and action works,
.. i18n: 
.. i18n: * easy access to the all the links to a document and everything that is attached to it,
.. i18n: 
.. i18n: * people to see both a high-level map and the detail of all the company's processes,
.. i18n: 
.. i18n: * access to a graphical model and integrated quality manual for rapid access that depends on the
.. i18n:   work context,
.. i18n: 
.. i18n: * use of a knowledge base and capitalization of that knowledge for all of the company's actions in
.. i18n:   the form of interactive processes,
.. i18n: 
.. i18n: * an employee to become more aware of his role in the whole environment.
..

* new employees to learn how to use the software by graphically and dynamically, discovering how each
  document and action works,

* easy access to the all the links to a document and everything that is attached to it,

* people to see both a high-level map and the detail of all the company's processes,

* access to a graphical model and integrated quality manual for rapid access that depends on the
  work context,

* use of a knowledge base and capitalization of that knowledge for all of the company's actions in
  the form of interactive processes,

* an employee to become more aware of his role in the whole environment.

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
