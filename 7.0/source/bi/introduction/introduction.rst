
What is for User?
=================

The Open Object Business Intelligence system aims to be a full featured open source Business Intelligence system written in Python. It implements a HOLAP (Hybrid OLAP = ROLAP + MOLAP) cube and a MDX query engine based on SQLAlchemy.

Comparing to most current business intelligence software in the market, our goal is to produce a BI for the mid market. It has to be:

For the end-user:
-----------------

* Easy and fast to use: a simple web-interface that has no dependencies and can be integrated in proprietary
  software. It should have an OpenOffice interface for complex dashboards creation.
* Easy to install: auto-installation on Windows and Linux, with few dependencies.
* Integrated and independent from OpenERP. 

For the administrator user:
---------------------------

* A cube designer within OpenERP (application and web-client)
* Easy to configure: Automatic cube definition (5 clicks, using introspection on database),
* Easy to maintain: The application must be sufficiently intelligent that it requires no fine tuning in cube definition,
  runs well on bad indices, with no need for explicitly defined aggregated tables, or defined axes.
* No intervention from developers: everything achievable through interfaces for end-user.

For the developer:
------------------

* Everything (dimensions, ) must be object oriented with a module system to allow to add your own code to extend the software, like in OpenERP.
* It must support main database engine and aggregation of multiple database: PostgreSQL, MySQL, Oracle, MSSQL etc... to do reporting for any application.


.. Copyright © Open Object Press. All rights reserved.

.. You may take electronic copy of this publication and distribute it if you don't
.. change the content. You can also print a copy to be read by yourself only.

.. We have contracts with different publishers in different countries to sell and
.. distribute paper or electronic based versions of this book (translated or not)
.. in bookstores. This helps to distribute and promote the OpenERP product. It
.. also helps us to create incentives to pay contributors and authors using author
.. rights of these sales.

.. Due to this, grants to translate, modify or sell this book are strictly
.. forbidden, unless Open  SPRL (representing Open Object Presses) gives you a
.. written authorisation for this.

.. Many of the designations used by manufacturers and suppliers to distinguish their
.. products are claimed as trademarks. Where those designations appear in this book,
.. and OpenERP Press was aware of a trademark claim, the designations have been
.. printed in initial capitals.

.. While every precaution has been taken in the preparation of this book, the publisher
.. and the authors assume no responsibility for errors or omissions, or for damages
.. resulting from the use of the information contained herein.

.. Published by OpenERP Press, Grand Rosière, Belgium


