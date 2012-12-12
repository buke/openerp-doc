
.. i18n: .. index::
.. i18n:    single: Installation; OpenERP All-In-One (Windows)
.. i18n:    single: OpenERP All-In-One; Installation (Windows)
.. i18n: .. 
..

.. index::
   single: Installation; OpenERP All-In-One (Windows)
   single: OpenERP All-In-One; Installation (Windows)
.. 

.. i18n: .. windows-allinone-link:
..

.. windows-allinone-link:

.. i18n: OpenERP All-In-One Installation
.. i18n: ===============================
..

OpenERP All-In-One Installation
===============================

.. i18n: Each time a new release of OpenERP is made, OpenERP supplies a complete Windows auto-installer for
.. i18n: it. This contains all of the components you need – the PostgreSQL database server, the OpenERP
.. i18n: application server, the GTK application client and the Web client.
..

Each time a new release of OpenERP is made, OpenERP supplies a complete Windows auto-installer for
it. This contains all of the components you need – the PostgreSQL database server, the OpenERP
application server, the GTK application client and the Web client.

.. i18n: This auto-installer enables you to install the whole system in just a few mouse clicks. The initial
.. i18n: configuration is set up during installation, making it possible to start using it very quickly, as
.. i18n: long as you do not want to change the underlying code. It is aimed at the installation of everything
.. i18n: on a single PC, but you can later connect GTK clients from other PCs, Macs and Linux boxes to it as
.. i18n: well.
..

This auto-installer enables you to install the whole system in just a few mouse clicks. The initial
configuration is set up during installation, making it possible to start using it very quickly, as
long as you do not want to change the underlying code. It is aimed at the installation of everything
on a single PC, but you can later connect GTK clients from other PCs, Macs and Linux boxes to it as
well.

.. i18n: Downloading OpenERP All-In-One
.. i18n: ------------------------------
..

Downloading OpenERP All-In-One
------------------------------

.. i18n: The first step is to download the OpenERP All-In-One installer. At this stage, you must choose which version
.. i18n: to install – the stable version or the development version. If you are planning to put it straight
.. i18n: into production we strongly advise you to choose the stable version.
..

The first step is to download the OpenERP All-In-One installer. At this stage, you must choose which version
to install – the stable version or the development version. If you are planning to put it straight
into production we strongly advise you to choose the stable version.

.. i18n: .. index::
.. i18n:    single: OpenERP versions
..

.. index::
   single: OpenERP versions

.. i18n: .. note::  Stable Versions and Development Versions
.. i18n: 
.. i18n: 	OpenERP development proceeds in two parallel tracks: stable versions and development versions.
.. i18n: 
.. i18n: 	New functionality is integrated into the development branch. This branch is more advanced than the
.. i18n: 	stable branch, but it can contain undiscovered and unfixed faults. A new development release is
.. i18n: 	made every month or so, and OpenERP has made the code repository available so you can download the
.. i18n: 	very latest revisions if you want.
.. i18n: 
.. i18n: 	The stable branch is designed for production environments. Here, releases of new functionality are
.. i18n: 	made only about once a year after a long period of testing and validation. Only bug fixes are
.. i18n: 	released through the year on the stable branch.
..

.. note::  Stable Versions and Development Versions

	OpenERP development proceeds in two parallel tracks: stable versions and development versions.

	New functionality is integrated into the development branch. This branch is more advanced than the
	stable branch, but it can contain undiscovered and unfixed faults. A new development release is
	made every month or so, and OpenERP has made the code repository available so you can download the
	very latest revisions if you want.

	The stable branch is designed for production environments. Here, releases of new functionality are
	made only about once a year after a long period of testing and validation. Only bug fixes are
	released through the year on the stable branch.

.. i18n: .. index::
.. i18n:    single: installation; Windows (all-in-one)
..

.. index::
   single: installation; Windows (all-in-one)

.. i18n: To download OpenERP for Windows, follow these steps:
..

To download OpenERP for Windows, follow these steps:

.. i18n: #. Navigate to the site http://www.openerp.com.
.. i18n: 
.. i18n: #. Click the :menuselection:`Downloads` button at the right, then, under :guilabel:`Windows Auto-Installer`, select
.. i18n:    **All-In-One**.
.. i18n: 
.. i18n: #. Before you can proceed with the download, you will be asked to fill an online form with your contact and company details and information regarding your interest in OpenERP.
.. i18n: 
.. i18n: #. Once you submit the online form, the All-In-One Windows installer is automatically downloaded.
.. i18n: 
.. i18n: #. Save the file on your PC - it is quite a substantial size because it downloads everything including
.. i18n:    the PostgreSQL database system (version 8.3, at the time of writing), so it will take some time.
..

#. Navigate to the site http://www.openerp.com.

#. Click the :menuselection:`Downloads` button at the right, then, under :guilabel:`Windows Auto-Installer`, select
   **All-In-One**.

#. Before you can proceed with the download, you will be asked to fill an online form with your contact and company details and information regarding your interest in OpenERP.

#. Once you submit the online form, the All-In-One Windows installer is automatically downloaded.

#. Save the file on your PC - it is quite a substantial size because it downloads everything including
   the PostgreSQL database system (version 8.3, at the time of writing), so it will take some time.

.. i18n: .. index::
.. i18n:    single:  installation; administrator
..

.. index::
   single:  installation; administrator

.. i18n: Installing the OpenERP All-In-One
.. i18n: ---------------------------------
..

Installing the OpenERP All-In-One
---------------------------------

.. i18n: To install OpenERP and its database, you must be signed in as an Administrator on your PC. 
..

To install OpenERP and its database, you must be signed in as an Administrator on your PC. 

.. i18n: If you have previously tried to install the All-In-One version of OpenERP, you will have to uninstall
.. i18n: that first, because various elements of a previous installation could interfere with your new installation.
.. i18n: Make sure that all Tiny ERP, OpenERP and PostgreSQL applications are removed:
.. i18n: you are likely to have to restart your PC to finish removing all traces of them.
..

If you have previously tried to install the All-In-One version of OpenERP, you will have to uninstall
that first, because various elements of a previous installation could interfere with your new installation.
Make sure that all Tiny ERP, OpenERP and PostgreSQL applications are removed:
you are likely to have to restart your PC to finish removing all traces of them.

.. i18n: Double-click the installer file to install OpenERP and accept the default parameters on each dialog box as you go.
.. i18n: The All-In-One installer is the simplest mode of installation and has the following steps:
..

Double-click the installer file to install OpenERP and accept the default parameters on each dialog box as you go.
The All-In-One installer is the simplest mode of installation and has the following steps:

.. i18n: * 1. Select installation language
.. i18n: 	The default is ``English``. The other option is ``French``.
.. i18n: 
.. i18n: * 2. Welcome message
.. i18n: 	Carefully follow the recommendations given in this step.
..

* 1. Select installation language
	The default is ``English``. The other option is ``French``.

* 2. Welcome message
	Carefully follow the recommendations given in this step.

.. i18n:   .. figure:: ../../img/a2_welcome.png
.. i18n:         :scale: 50
.. i18n:         :align: center
.. i18n: 
.. i18n:         *Welcome to OpenERP*
..

  .. figure:: ../../img/a2_welcome.png
        :scale: 50
        :align: center

        *Welcome to OpenERP*

.. i18n: * 3. Licence Agreement
.. i18n: 	It is important that you accept the GNU General Public License to proceed with installation.
.. i18n: 
.. i18n: * 4. Select components to install
.. i18n: 	You can proceed with the default install type ``All In One``, which will install the OpenERP Server, GTK Desktop Client, Web Client and PostgreSQL Database (version 8.3, at the time of writing). Or, you may customize your installation by selecting only the components you require.
.. i18n:   
.. i18n:   .. figure:: ../../img/a4_components.png
.. i18n:         :scale: 50
.. i18n:         :align: center
.. i18n: 
.. i18n:         *Customize component installation*
.. i18n:   
.. i18n: * 5. Configure PostgreSQL connection
.. i18n: 	The installer will suggest default parameters to complete your PostgreSQL connection configuration. You may accept the defaults, or change it according to your requirement.
.. i18n: 
.. i18n:   .. figure:: ../../img/a6_config_postgres.png
.. i18n:         :scale: 50
.. i18n:         :align: center
.. i18n: 
.. i18n:         *PostgreSQL configuration*
.. i18n: 
.. i18n: * 6. Select folder for installation
.. i18n: 	By default, OpenERP is installed in ``C:\Program Files\OpenERP 6.0``. To install in a different folder, browse for a different location(folder) in this step.
.. i18n: 
.. i18n: * 7. Install
.. i18n: 	The automatic installation of OpenERP begins and you can view its progress.
.. i18n: 
.. i18n: * 8. Finish
.. i18n: 	On successful installation of OpenERP, you will get an appropriate confirmation. You can click `Finish` to close the setup wizard.
.. i18n: 
.. i18n:   .. figure:: ../../img/a9_finish.png
.. i18n:      :scale: 50
.. i18n:      :align: center
.. i18n: 
.. i18n:      *End of setup wizard*
..

* 3. Licence Agreement
	It is important that you accept the GNU General Public License to proceed with installation.

* 4. Select components to install
	You can proceed with the default install type ``All In One``, which will install the OpenERP Server, GTK Desktop Client, Web Client and PostgreSQL Database (version 8.3, at the time of writing). Or, you may customize your installation by selecting only the components you require.
  
  .. figure:: ../../img/a4_components.png
        :scale: 50
        :align: center

        *Customize component installation*
  
* 5. Configure PostgreSQL connection
	The installer will suggest default parameters to complete your PostgreSQL connection configuration. You may accept the defaults, or change it according to your requirement.

  .. figure:: ../../img/a6_config_postgres.png
        :scale: 50
        :align: center

        *PostgreSQL configuration*

* 6. Select folder for installation
	By default, OpenERP is installed in ``C:\Program Files\OpenERP 6.0``. To install in a different folder, browse for a different location(folder) in this step.

* 7. Install
	The automatic installation of OpenERP begins and you can view its progress.

* 8. Finish
	On successful installation of OpenERP, you will get an appropriate confirmation. You can click `Finish` to close the setup wizard.

  .. figure:: ../../img/a9_finish.png
     :scale: 50
     :align: center

     *End of setup wizard*

.. i18n: Connecting to OpenERP
.. i18n: ---------------------
..

Connecting to OpenERP
---------------------

.. i18n: You do not need to manually start the OpenERP Server, because it is installed as a Windows service and automatically started.
.. i18n: You may however access it from the shortcuts created in the `Start` menu for `OpenERP`, or simply by connecting with your
.. i18n: preferred browser to web interface, by default available on ``http://localhost:8069``
..

You do not need to manually start the OpenERP Server, because it is installed as a Windows service and automatically started.
You may however access it from the shortcuts created in the `Start` menu for `OpenERP`, or simply by connecting with your
preferred browser to web interface, by default available on ``http://localhost:8069``

.. i18n: Use the database list at the top-right corner to choose a database to connect to.
.. i18n: As this would be the first time you are using OpenERP since its installation, your database list will be empty.
.. i18n: You can create a new database through the ``Manage databases`` link on the login page.
..

Use the database list at the top-right corner to choose a database to connect to.
As this would be the first time you are using OpenERP since its installation, your database list will be empty.
You can create a new database through the ``Manage databases`` link on the login page.
