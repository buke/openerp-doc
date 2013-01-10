.. i18n: .. index::
.. i18n:    single: Analytic Accounts
..

.. index::
   single: Analytic Accounts

.. i18n: .. _ch-accts:
.. i18n: 
.. i18n: *****************
.. i18n: Analytic Accounts
.. i18n: *****************
..

.. _ch-accts:

********
辅助核算
********

.. i18n:  *Sitting at the heart of your company's processes, analytic accounts (or cost accounts) are
.. i18n:  indispensable tools for managing your operations well. Unlike your financial accounts, they are for
.. i18n:  more than accountants - they are for general managers and project managers, too.*
..

 *作为公司流程的核心,分析会计（或成本会计）是您的操作管理的不可缺少的工具。与你的财务会计不同，他们为更多的会计
 师服务,同时也适用于老板和项目经理们。*

.. i18n: You need a common way of referring to each user, service, or document to integrate all your
.. i18n: company's processes effectively. Such a common basis is provided by analytic accounts (or management
.. i18n: accounts, or cost accounts, as they are also called) in OpenERP.
..

你需要一个通用的方法,将用户,服务和文档同公司的业务流程有效地整合到一起。在OpenERP里面,分析会计(也叫做管理会计或者
成本会计)提供这样一个通用的方法。

.. i18n: Analytic accounts are often presented as a foundation for strategic enterprise decisions. But
.. i18n: because of all the information they pull together, OpenERP's analytic accounts can be a useful
.. i18n: management tool, at the center of most system processes.
..

分析会计通常作为企业战略决策的基础。但因为这需要把所有信息集合到一起，在大多数系统的核心业务处理中，OpenERP的分析会计是一个有用的
管理工具。

.. i18n: There are several reasons for this:
..

这里有几点原因：

.. i18n: * they reflect your entire management activity,
.. i18n: 
.. i18n: * unlike the general accounts, the structure of the analytic accounts is not regulated by legal
.. i18n:   obligations, so each company can adapt it to its needs.
..

* 反映整个管理活动,

* 不同于财务会计，分析会计的结构不依据会计准则的规范制定，所以每个公司都可以调整适应自己的需要。

.. i18n: .. note:: Independence from General Accounts
.. i18n: 
.. i18n:         In some software packages, analytic accounts are managed as an extension of general accounts –
.. i18n:         for example, by using the two last digits of the account code to represent analytic accounts.
.. i18n: 
.. i18n:         In OpenERP, analytic accounts are linked to general accounts but are treated totally
.. i18n:         independently.
.. i18n:         So you can enter various different analytic operations that have no counterpart in the general
.. i18n:         financial accounts.
..

.. note:: 独立于财务会计

        在某些软件中，分析会计是财务会计的扩展 - 例如，通过使用帐户代码的最后两个数字来表示分析会计帐户。

        在OpenERP的中，分析会计被关联到财务会计，但是被完全独立的对待。
        所以，你可以使用各种不同的分析会计功能，不必在财务会计中有相应的分析会计科目。

.. i18n: While the structure of the general chart of accounts is imposed by law, the analytic chart of
.. i18n: accounts is built to fit a company's needs closely.
..

虽然法律规定了财务会计科目表的结构，但分析会计科目可以更好更紧密地适应一个公司的需求。

.. i18n: Just as in the general accounts, you will find accounting entries in the different analytic accounts.
.. i18n: Each analytic entry can be linked to a general account, or not, as you wish. Conversely, an entry in
.. i18n: a general account can be linked to one, several, or no corresponding analytic accounts.
..

正如在财务会计帐户，你会发现不同的分析会计科目产生各自的会计分录。每个会计分录可以关联到一个财务会计科目，正如你
所希望的。
相反，财务会计中的一个科目可以关联到一个，多个或没有相应的分析会计科目。

.. i18n: You will discover many advantages of this independent representation below. For the more impatient,
.. i18n: here are some of those advantages:
..

通过下面分析会计独立性的说明，你会发现它的许多优点。耐心点儿，这里是更多优势说明：

.. i18n: * you can manage many different analytic operations,
.. i18n: 
.. i18n: * you can modify an analytic plan on the fly, during the course of an activity, because of its
.. i18n:   independence,
.. i18n: 
.. i18n: * you can avoid an explosion in the number of general accounts,
.. i18n: 
.. i18n: * even those companies that do not use OpenERP's general accounts can use the analytic accounts for
.. i18n:   management.
..

* 你可以管理很多不同的分析操作，

* 因为它的独立性，在经营活动中，你可以在任何时候修改分析计划，

* 你能避免财务会计科目的爆炸行增长，

* 即使是那些不使用OpenERP的财务会计功能的公司也可以使用分析会计管理业务。

.. i18n: .. tip:: Who Benefits from Analytic Accounts?
.. i18n: 
.. i18n:         Unlike general accounts, analytic accounts in OpenERP are not so much an accounting tool for Accounts as a
.. i18n:         management tool for everyone in the company. (That is why they are also called management accounts.)
.. i18n: 
.. i18n:         The main users of analytic accounts should be the directors, general managers and project managers.
..

.. tip:: 谁受益于分析会计？

        不同于财务会计，OpenERP的分析会计不只是记账工具，可以作为公司里面任何一个人的管理工具。 （这就是为什么他们
        也被称为管理会计）。

        分析帐户的主要用户应该是公司董事，总经理和项目经理。

.. i18n: Analytic accounts make up a powerful tool that can be used in different ways. The trick is to create
.. i18n: your own analytic structure for a chart of accounts that closely matches your company's needs.
..

分析会计提供了一个能在很多情况下使用的强大工具。关键是要建立你自己的分析会计科目表，和自身的需求密切配合。

.. i18n: For this chapter, you should start with a fresh database that includes demo data,
.. i18n: with :mod:`sale` and its dependencies installed, and no particular chart of accounts configured.
..

在本章中，你应该使用一个包括了演示数据的全新数据库，安装`销售`及其依赖模块，并没有什么特别的会计科目配置

.. i18n: .. raw:: html
.. i18n: 
.. i18n:     <div class="all-toctree">
..

.. raw:: html

    <div class="all-toctree">

.. i18n: .. toctree::
.. i18n: 
.. i18n:     4_10_Accounts_analytic_chart
.. i18n:     4_10_Accounts_record
..

.. toctree::

    4_10_Accounts_analytic_chart
    4_10_Accounts_record

.. i18n: .. raw:: html
.. i18n: 
.. i18n:     </div>
..

.. raw:: html

    </div>

.. i18n: .. Copyright ? Open Object Press. All rights reserved.
..

.. Copyright ? Open Object Press. All rights reserved.

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
