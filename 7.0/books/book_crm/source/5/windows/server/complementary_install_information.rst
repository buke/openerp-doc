
.. index::
   single: Installation; Windows installation quirks
.. 

.. _troubleshooting-and-windows-complementary-install-information:

Troubleshooting and Windows Complementary Install Information
=============================================================

*PostgreSQL Administration*

OpenERP Server Connection Error with PostgreSQL

If you are initializing a database from the command-line with a custom username/role (-r) and password (-w), ensure that you have created a corresponding PostgreSQL user for the same. Else, you may encounter error messages as shown below:

.. image:: ../../img/user_fail.png

*User authentication failure*

You may also face another problem similar to this situation:

.. image:: ../../img/101_erp2pgsql_conn_fail.png

*Database connection failure*

In this case, you should have a look if the service ``postgresql-9.0 - PostgreSQL Server 9.0`` is running in the Services Manager (:menuselection:`Control Panel --> System and Security --> Administrative Tools --> Services`).

.. image:: ../../img/Pgsql_51_service_status.png

*PostgreSQL 9.0 in the Services list*

You can edit the service configuration to have PostgreSQL start as a service at system boot. This is usually a default.

.. image:: ../../img/Pgsql_53_service_start_mode.png

*Configure PostgreSQL 9.0 service*

If your PostgreSQL service is running, but you get connection errors, you can restart the service.

.. image:: ../../img/Pgsql_52_service_restart.png

*Restarting the service*

