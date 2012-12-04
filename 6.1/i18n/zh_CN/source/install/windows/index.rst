.. i18n: OpenERP Installation on Windows
.. i18n: ===============================
..

在Windows操作系统下安装OpenERP
===============================

.. i18n: In this chapter, you will see the installation of OpenERP 6.1 on a Windows system. This procedure is well-tested on Windows 7.
..

本节会引导你在 Windows 系统下安装OpenERP 6.1。并且同样适用于Windows 7。

.. i18n: You have two options for the installation of OpenERP on a Windows system:
..

在Windows下面，你可以有两种方式进行安装:

.. i18n: * All-In-One Installation
.. i18n: 	This is the easiest and quickest way to install OpenERP. It installs all components (OpenERP Server and PostgreSQL database) pre-configured on one computer. This installation is recommended if you do not have any major customizations.
.. i18n: 
.. i18n: * Independent Installation
.. i18n: 	If you choose this mode of installation, all the components required to run OpenERP will have to be downloaded and installed separately. You will have to opt for an independent installation if you plan to install the components on separate machines. This mode is also practical if you are already working with, or plan to use, a different version of PostgreSQL than the one provided with the All-In-One installer.
..

* All-In-One 安装
	这种安装最方便快捷。会自动安装OpenERP6.1需要的(OpenERP Server 以及 PostgreSQL数据库)并做一些简单配置。如果你没有进行一些特殊的要求，推荐使用这种方式进行安装。
 
* 各部分独立安装
	If you choose this mode of installation, all the components required to run OpenERP will have to be downloaded and installed separately. You will have to opt for an independent installation if you plan to install the components on separate machines. This mode is also practical if you are already working with, or plan to use, a different version of PostgreSQL than the one provided with the All-In-One installer.

.. i18n: .. toctree::
.. i18n:     :glob:
.. i18n: 
.. i18n:     allinone/index
.. i18n:     postgres/index
.. i18n:     server/index
.. i18n:     client/index
.. i18n:     web/index
.. i18n:     server/complementary_install_information
.. i18n:     updating
..

.. toctree::
    :glob:

    allinone/index
    postgres/index
    server/index
    client/index
    web/index
    server/complementary_install_information
    updating
