
.. index::
   single: Installation; OpenERP All-In-One (Windows)
   single: OpenERP All-In-One; Installation (Windows)
.. 

.. windows-allinone-link:

OpenERP All-In-One Installation
===============================

Each time a new release of OpenERP is made, OpenERP supplies a complete Windows auto-installer for
it. This contains all of the components you need – the PostgreSQL database server, the OpenERP
application server, the GTK application client and the Web client.

This auto-installer enables you to install the whole system in just a few mouse clicks. The initial
configuration is set up during installation, making it possible to start using it very quickly, as
long as you do not want to change the underlying code. It is aimed at the installation of everything
on a single PC, but you can later connect GTK clients from other PCs, Macs and Linux boxes to it as
well.

Downloading OpenERP All-In-One
------------------------------

The first step is to download the OpenERP All-In-One installer. At this stage, you must choose which version
to install – the stable version or the development version. If you are planning to put it straight
into production we strongly advise you to choose the stable version.

.. index::
   single: OpenERP versions

.. note::  Stable Versions and Development Versions

	OpenERP development proceeds in two parallel tracks: stable versions and development versions.

	New functionality is integrated into the development branch. This branch is more advanced than the
	stable branch, but it can contain undiscovered and unfixed faults. A new development release is
	made every month or so, and OpenERP has made the code repository available so you can download the
	very latest revisions if you want.

	The stable branch is designed for production environments. Here, releases of new functionality are
	made only about once a year after a long period of testing and validation. Only bug fixes are
	released through the year on the stable branch.

.. index::
   single: installation; Windows (all-in-one)

To download OpenERP for Windows, follow these steps:

#. Navigate to the site http://www.openerp.com.

#. Click the :menuselection:`Downloads` button at the right, then, under :guilabel:`Windows Auto-Installer`, select
   **All-In-One**.

#. Before you can proceed with the download, you will be asked to fill an online form with your contact and company details and information regarding your interest in OpenERP.

#. Once you submit the online form, the All-In-One Windows installer (currently :program:`openerp-allinone-setup-6.0.2.exe`) becomes available for download.

#. Save the file on your PC - it is quite a substantial size because it downloads everything including
   the PostgreSQL database system (version 8.3, at the time of writing), so it will take some time.

.. index::
   single:  installation; administrator

Installing the OpenERP All-In-One
---------------------------------

To install OpenERP and its database, you must be signed in as an Administrator on your PC. 

If you have previously tried to install the All-In-One version of OpenERP, you will have to uninstall
that first, because various elements of a previous installation could interfere with your new installation.
Make sure that all Tiny ERP, OpenERP and PostgreSQL applications are removed:
you are likely to have to restart your PC to finish removing all traces of them.

Double-click the installer file to install OpenERP and accept the default parameters on each dialog box as you go.
The All-In-One installer is the simplest mode of installation and has the following steps:

* 1. Select installation language
	The default is ``English``. The other option is ``French``.

* 2. Welcome message
	Carefully follow the recommendations given in this step.

  .. figure:: ../../img/a2_welcome.png
        :scale: 50
        :align: center

        *Welcome to OpenERP*

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

Starting the OpenERP Client
---------------------------

You do not need to manually start the OpenERP Server, because it is installed as a Windows service. But you may trigger various actions from the shortcuts created in the `Start` menu for `OpenERP GTK Client 6.0`, `OpenERP Server 6.0` and `PostgreSQL 8.3`. The OpenERP Client can be opened, ready to use the OpenERP system, once you have completed the All-In-One installation.

You will find the `OpenERP Client` icon on your desktop, which you double-click to access the OpenERP client interface. Use the menu :menuselection:`File --> Connect...` to connect to a database. As this would be the first time you are using OpenERP since its installation, your database will be empty. You can create a new database through :menuselection:`File --> Databases --> New database`.

.. figure:: ../../img/a10_start_client.png
   :scale: 50
   :align: center

   *Database on first run*

