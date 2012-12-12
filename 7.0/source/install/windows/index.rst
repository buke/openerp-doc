
OpenERP Installation on Windows
===============================

In this chapter, you will see the installation of OpenERP 6.1 on a Windows system. This procedure is well-tested on Windows 7.

You have two options for the installation of OpenERP on a Windows system:

* All-In-One Installation
	This is the easiest and quickest way to install OpenERP. It installs all components (OpenERP Server and PostgreSQL database) pre-configured on one computer. This installation is recommended if you do not have any major customizations.

* Independent Installation
	If you choose this mode of installation, all the components required to run OpenERP will have to be downloaded and installed separately. You will have to opt for an independent installation if you plan to install the components on separate machines. This mode is also practical if you are already working with or plan to use a different version of PostgreSQL than the one provided with the All-In-One installer.

.. toctree::
    :glob:

    allinone/index
    postgres/index
    server/index
    client/index
    web/index
    server/complementary_install_information
    updating
