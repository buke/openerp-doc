.. i18n: OpenERP Installation on Windows
.. i18n: ===============================
..

在Windows上安装OpenERP
======================

.. i18n: In this chapter, you will see the installation of OpenERP 6.1 on a Windows system. This procedure is well-tested on Windows 7.
..

在本章，你将看到OpenERP v6.1在Windows系统上的安装。这个流程在Windows 7上很好地测过。

.. i18n: You have two options for the installation of OpenERP on a Windows system:
..

在Windows系统上安装OpenERP有两个选择：

.. i18n: * All-In-One Installation
.. i18n: 	This is the easiest and quickest way to install OpenERP. It installs all components (OpenERP Server and PostgreSQL database) pre-configured on one computer. This installation is recommended if you do not have any major customizations.
.. i18n: 
.. i18n: * Independent Installation
.. i18n: 	If you choose this mode of installation, all the components required to run OpenERP will have to be downloaded and installed separately. You will have to opt for an independent installation if you plan to install the components on separate machines. This mode is also practical if you are already working with, or plan to use, a different version of PostgreSQL than the one provided with the All-In-One installer.
..

* All-In-One 安装
	这是安装OpenERP最快捷的方式。在计算机上安装并配置所有的组件（OpenERP服务器，客户端，WEB以及PostgreSQL数据库）。如果没有很大的系统定制，推荐这种安装方式。
 
* 独立安装
	如果选择这种安装模式，运行OpenERP所需的组件需要分别下载和安装。如果计划在不同机器上安装这些组件，须选择独立安装方式。如果已经在用或者计划使用不同于完整安装版本的PostgreSQL，这个模式也比较可行。

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
