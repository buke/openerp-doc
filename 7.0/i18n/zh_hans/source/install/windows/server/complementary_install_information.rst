
.. i18n: .. index::
.. i18n:    single: Installation; Windows installation quirks
.. i18n: .. 
..

.. index::
   single: Installation; Windows installation quirks
.. 

.. i18n: .. _troubleshooting-and-windows-complementary-install-information:
.. i18n: 
.. i18n: Troubleshooting and Windows Complementary Install Information
.. i18n: =============================================================
..

.. _troubleshooting-and-windows-complementary-install-information:

Troubleshooting and Windows Complementary Install Information
=============================================================

.. i18n: PostgreSQL Administration
.. i18n: +++++++++++++++++++++++++
..

PostgreSQL Administration
+++++++++++++++++++++++++

.. i18n: OpenERP Server Connection Error with PostgreSQL
.. i18n: """""""""""""""""""""""""""""""""""""""""""""""
..

OpenERP Server Connection Error with PostgreSQL
"""""""""""""""""""""""""""""""""""""""""""""""

.. i18n: If you are initializing a database from the command-line with a custom username/role (-r) and password (-w), ensure that you have created a corresponding PostgreSQL user for the same.
.. i18n: Otherwise you may encounter error messages as shown below:
..

If you are initializing a database from the command-line with a custom username/role (-r) and password (-w), ensure that you have created a corresponding PostgreSQL user for the same.
Otherwise you may encounter error messages as shown below:

.. i18n: .. figure:: ../../img/user_fail.png
.. i18n:    :scale: 50
.. i18n:    :align: center
..

.. figure:: ../../img/user_fail.png
   :scale: 50
   :align: center

.. i18n: *User authentication failure*
..

*User authentication failure*

.. i18n: You may also face another problem similar to this situation:
..

You may also face another problem similar to this situation:

.. i18n: .. figure:: ../../img/101_erp2pgsql_conn_fail.png
.. i18n:    :scale: 50
.. i18n:    :align: center
..

.. figure:: ../../img/101_erp2pgsql_conn_fail.png
   :scale: 50
   :align: center

.. i18n: *Database connection failure*
..

*Database connection failure*

.. i18n: In this case, check if the service ``postgresql-9.0 - PostgreSQL Server 9.0`` is running in the Services Manager (:menuselection:`Control Panel --> System and Security --> Administrative Tools --> Services`).
..

In this case, check if the service ``postgresql-9.0 - PostgreSQL Server 9.0`` is running in the Services Manager (:menuselection:`Control Panel --> System and Security --> Administrative Tools --> Services`).

.. i18n: .. figure:: ../../img/Pgsql_51_service_status.png
.. i18n:    :scale: 50
.. i18n:    :align: center
..

.. figure:: ../../img/Pgsql_51_service_status.png
   :scale: 50
   :align: center

.. i18n: *PostgreSQL 9.0 in the Services list*
..

*PostgreSQL 9.0 in the Services list*

.. i18n: You can edit the service configuration to start PostgreSQL as a service on system boot. This is usually the default.
..

You can edit the service configuration to start PostgreSQL as a service on system boot. This is usually the default.

.. i18n: .. figure:: ../../img/Pgsql_53_service_start_mode.png
.. i18n:    :scale: 50
.. i18n:    :align: center
..

.. figure:: ../../img/Pgsql_53_service_start_mode.png
   :scale: 50
   :align: center

.. i18n: *Configure PostgreSQL 9.0 service*
..

*Configure PostgreSQL 9.0 service*

.. i18n: If your PostgreSQL service is running, but you get connection errors, you can restart the service.
..

If your PostgreSQL service is running, but you get connection errors, you can restart the service.

.. i18n: .. figure:: ../../img/Pgsql_52_service_restart.png
.. i18n:    :scale: 50
.. i18n:    :align: center
..

.. figure:: ../../img/Pgsql_52_service_restart.png
   :scale: 50
   :align: center

.. i18n: *Restarting the service*
..

*Restarting the service*
