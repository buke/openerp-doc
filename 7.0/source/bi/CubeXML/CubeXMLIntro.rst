XML in open object
==================

Introduction to the OpenObject Module
-------------------------------------

The :ref:`OLAP <olap-link>`  module is used to validate, run and format the output of *MDXExamples/MDX Queries*

The general flow is of :ref:`OLAP <olap-link>` module is shown in following diagram:

.. image::  images/Cube_olap_schema.png

Explanation of the components
-----------------------------

:Web-Services:

This is the layer provided by the base of OpenERP, protocols: NET-RPC (fast binary), XML-RPC, over HTTP or HTTPS

:Services:

Layer provided by OpenERP that provides: authentication (normal/ldap), user management, access rights, workflows, module management, ...

:MDX Parser:

It parses the MDX query and converts it to the form of python objects. It uses Python's pyparsing module to do this. It splits the query into form of objects of axis, level, sub level, slicer (if any) and measures. 


:MDX Validator:

Parses all the objects created and maps it to the browse object of OpenERP resource. For example, the axis object will receive a link to the OpenERP browse record on the related olap.axis object.

:MDX Runner:

It will run the query on the basis of objects using SQLAlchemy and return different subsets.
On the basis of it the cube is made in matrix form.
And it fills the cube by values using axis mapping

:RDBMS connectors:

The layer provided by SQL Alchemy, it supports: mysql, postgresql, oracle, ...

The schema definition is in the OpenERP database.

