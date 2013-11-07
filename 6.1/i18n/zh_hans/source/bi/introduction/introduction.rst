.. i18n: What is for User?
.. i18n: =================
..

对用户意味什么?
=================

.. i18n: The Open Object Business Intelligence system aims to be a full featured open source Business Intelligence system written in Python. It implements a HOLAP (Hybrid OLAP = ROLAP + MOLAP) cube and a MDX query engine based on SQLAlchemy.
..

Open Object Business Intelligence系统的目标是成为一个全功能的用Python编写的开源商业智能系统。 It implements a HOLAP (Hybrid OLAP = ROLAP + MOLAP) cube and a MDX query engine based on SQLAlchemy.

.. i18n: Comparing to most current business intelligence software in the market, our goal is to produce a BI for the mid market. It has to be:
..

相对当前市面上大多数的business intelligence 软件, 我们的目的是生产一个针对中端市场的BI。 它意味着:

.. i18n: For the end-user:
.. i18n: -----------------
..

对最终用户而言:
-----------------

.. i18n: * Easy and fast to use: a simple web-interface that has no dependencies and can be integrated in proprietary
.. i18n:   software. It should have an OpenOffice interface for complex dashboards creation.
.. i18n: * Easy to install: auto-installation on Windows and Linux, with few dependencies.
.. i18n: * Integrated and independent from OpenERP. 
..

* 使用起来方便及快捷: 简单的web界面，不需依赖其它软件，并且可以集成到所有软件中。它应该保留一个OpenOffice接口以创建复杂的报表。
* 容易安装: 在Windows和Linux中都可自动化安装，极少依赖其它软件。
* 在OpenERP中集成，但并不被依赖。

.. i18n: For the administrator user:
.. i18n: ---------------------------
..

对管理员用户而言:
---------------------------

.. i18n: * A cube designer within OpenERP
.. i18n: * Easy to configure: Automatic cube definition (5 clicks, using introspection on database),
.. i18n: * Easy to maintain: The application must be sufficiently intelligent that it requires no fine tuning in cube definition,
.. i18n:   runs well on bad indices, with no need for explicitly defined aggregated tables, or defined axes.
.. i18n: * No intervention from developers: everything achievable through interfaces for end-user.
..

* OpenERP内部的全方面设计器
* 容易配置: Automatic cube definition (5 clicks, using introspection on database),
* 容易维护: The application must be sufficiently intelligent that it requires no fine tuning in cube definition,
  runs well on bad indices, with no need for explicitly defined aggregated tables, or defined axes.
* 无需开发者干预: 最终用户可以通过界面完成所有事情。

.. i18n: For the developer:
.. i18n: ------------------
..

对开发者而言:
------------------

.. i18n: * Everything (dimensions, ) must be object oriented with a module system to allow to add your own code to extend the software, like in OpenERP.
.. i18n: * It must support main database engine and aggregation of multiple database: PostgreSQL, MySQL, Oracle, MSSQL etc... to do reporting for any application.
..

* 就像OpenERP一样，所有东西 (dimensions, ) 必须是一个模块中面向对象的，允许你自己增加代码来扩展软件。
* 它必须支持主流的数据库引擎并且可集合多个数据库: PostgreSQL, MySQL, Oracle, MSSQL 等等... 使任意应用都能取得数据以生成报表。

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
.. i18n: .. forbidden, unless Open  SPRL (representing Open Object Presses) gives you a
.. i18n: .. written authorisation for this.
..

.. Due to this, grants to translate, modify or sell this book are strictly
.. forbidden, unless Open  SPRL (representing Open Object Presses) gives you a
.. written authorisation for this.

.. i18n: .. Many of the designations used by manufacturers and suppliers to distinguish their
.. i18n: .. products are claimed as trademarks. Where those designations appear in this book,
.. i18n: .. and OpenERP Press was aware of a trademark claim, the designations have been
.. i18n: .. printed in initial capitals.
..

.. Many of the designations used by manufacturers and suppliers to distinguish their
.. products are claimed as trademarks. Where those designations appear in this book,
.. and OpenERP Press was aware of a trademark claim, the designations have been
.. printed in initial capitals.

.. i18n: .. While every precaution has been taken in the preparation of this book, the publisher
.. i18n: .. and the authors assume no responsibility for errors or omissions, or for damages
.. i18n: .. resulting from the use of the information contained herein.
..

.. While every precaution has been taken in the preparation of this book, the publisher
.. and the authors assume no responsibility for errors or omissions, or for damages
.. resulting from the use of the information contained herein.

.. i18n: .. Published by OpenERP Press, Grand Rosière, Belgium
..

.. Published by OpenERP Press, Grand Rosière, Belgium

