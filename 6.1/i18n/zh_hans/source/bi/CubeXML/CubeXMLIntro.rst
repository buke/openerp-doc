
.. i18n: XML in open object
.. i18n: ==================
..

XML in open object
==================

.. i18n: Introduction to the OpenObject Module
.. i18n: -------------------------------------
..

Introduction to the OpenObject Module
-------------------------------------

.. i18n: The :ref:`OLAP <olap-link>`  module is used to validate, run and format the output of *MDXExamples/MDX Queries*
..

The :ref:`OLAP <olap-link>`  module is used to validate, run and format the output of *MDXExamples/MDX Queries*

.. i18n: The general flow is of :ref:`OLAP <olap-link>` module is shown in following diagram:
..

The general flow is of :ref:`OLAP <olap-link>` module is shown in following diagram:

.. i18n: .. image::  images/Cube_olap_schema.png
..

.. image::  images/Cube_olap_schema.png

.. i18n: Explanation of the components
.. i18n: -----------------------------
..

Explanation of the components
-----------------------------

.. i18n: :Web-Services:
..

:Web-Services:

.. i18n: This is the layer provided by the base of OpenERP, protocols: NET-RPC (fast binary), XML-RPC, over HTTP or HTTPS
..

This is the layer provided by the base of OpenERP, protocols: NET-RPC (fast binary), XML-RPC, over HTTP or HTTPS

.. i18n: :Services:
..

:Services:

.. i18n: Layer provided by OpenERP that provides: authentication (normal/ldap), user management, access rights, workflows, module management, ...
..

Layer provided by OpenERP that provides: authentication (normal/ldap), user management, access rights, workflows, module management, ...

.. i18n: :MDX Parser:
..

:MDX Parser:

.. i18n: It parses the MDX query and converts it to the form of python objects. It uses Python's pyparsing module to do this. It splits the query into form of objects of axis, level, sub level, slicer (if any) and measures. 
..

It parses the MDX query and converts it to the form of python objects. It uses Python's pyparsing module to do this. It splits the query into form of objects of axis, level, sub level, slicer (if any) and measures. 

.. i18n: :MDX Validator:
..

:MDX Validator:

.. i18n: Parses all the objects created and maps it to the browse object of OpenERP resource. For example, the axis object will receive a link to the OpenERP browse record on the related olap.axis object.
..

Parses all the objects created and maps it to the browse object of OpenERP resource. For example, the axis object will receive a link to the OpenERP browse record on the related olap.axis object.

.. i18n: :MDX Runner:
..

:MDX Runner:

.. i18n: It will run the query on the basis of objects using SQLAlchemy and return different subsets.
.. i18n: On the basis of it the cube is made in matrix form.
.. i18n: And it fills the cube by values using axis mapping
..

It will run the query on the basis of objects using SQLAlchemy and return different subsets.
On the basis of it the cube is made in matrix form.
And it fills the cube by values using axis mapping

.. i18n: :RDBMS connectors:
..

:RDBMS connectors:

.. i18n: The layer provided by SQL Alchemy, it supports: mysql, postgresql, oracle, ...
..

The layer provided by SQL Alchemy, it supports: mysql, postgresql, oracle, ...

.. i18n: The schema definition is in the OpenERP database.
..

The schema definition is in the OpenERP database.
