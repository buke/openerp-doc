MDXOverview
===========

MDX stands for Multidimensional Expressions. You use it to query OLAP databases. In a nutshell, MDX is to OLAP databases as SQL queries are to relational databases. 

OLAP databases primarily consist of OLAP cubes, which store fact tables, measures (such as sales, purchase, etc.) and dimensions/hierarchies. An OLAP database is often an aggregation of a relational database; as a result, you can write MDX queries to retrieve key calculations that measure company performance, often with less code than standard SQL. 

Because of the nature of OLAP databases, we need to write MDX code to retrieve data in far fewer lines of code than would be required using SQL. This is a segue into the role that OLAP databases and MDX play in the world of business intelligence. 

MDXAlchemy is developed taking care of all the aspects of becoming a complete OLAP Engine, to execute MDX query and fetch data efficiently. MDXAlchemy is a complete MDX engine that provides your database with full MDX capabilities. 

MDXAlchemy use the services of SQLAlchemy to provide some of the important features that makes MDXAlchemy a fully capable MDX Engine. The major is removing the clause of database dependency. 

The dimensional meta data facility addresses the issue that although the application stores dimensional data in relational tables (usually in the form of fact and dimension tables), the user does not have to be aware of the dimensionality, or OLAP semantics, of this data. It provides a comprehensive meta data facility to define these semantics and an XML capability to enable meta data interchange with other external OLAP products.

Independent yet Integrated to OpenERP
-------------------------------------

MDXAlchemy engine is totally independent of OpenERP and does not rely on OpenERP modules for its functionality. 
Yet being so diversified from OpenERP, it is fully integrated to OpenERP.

MDXAlchemy can be installed/integrated as an internal module of OpenERP and make itself available to assist OpenERP.

It is made of two major components, a cube engine and SQL Alchemy. It uses SQL Alchemy for connecting to the database while the cube engine processes the data to form the cube for the user.


Supported Databases
-------------------

OpenObject BI takes care of independent database functionality.

It supports connectivity with most of the leading Database programs.

Just a compatible Dialect and valid connection parameters are all that is needed to use a database.

The Dialect is used to describe how to talk to a specific kind of database. Dialects are included with SQLAlchemy for SQLite, Postgres, MySQL, MS-SQL, Firebird, Informix, and Oracle; these can be described as Python modules present in the sqlalchemy.databases package. Each dialect requires the appropriate DBAPI drivers to be installed separately.

Downloads for each DBAPI to connect to supported Databases are as follows:


* Postgres: psycopg2_

* SQLite  : pysqlite_

* MySQL   : MySQLDB_

* Oracle  : cx_Oracle_

* MS-SQL  : pyodbc_  (recommended) adodbapi pymssql

* Firebird:  kinterbasdb_

* Informix:  informixdb_



.. _psycopg2: http://www.initd.org/tracker/psycopg/wiki/PsycopgTwo

.. _pysqlite: http://initd.org/tracker/pysqlite

.. _MySQLDB: http://sourceforge.net/projects/mysql-python

.. _cx_Oracle: http://www.cxtools.net/default.aspx?nav=home

.. _pyodbc: http://pyodbc.sourceforge.net

.. _kinterbasdb: http://kinterbasdb.sourceforge.net/

.. _informixdb: http://informixdb.sourceforge.net/


