.. i18n: OpenERP Installation on Windows
.. i18n: ===============================
..

OpenERP 在Windows中的安装
===============================

.. i18n: In this chapter, you will see the installation of OpenERP 6.1 on a Windows system. This procedure is well-tested on Windows 7.
..

在本节中，你会看到OpenERP在Windows中的安装。本流程已在Windows 7中进行过很好的测试。

.. i18n: You have two options for the installation of OpenERP on a Windows system:
..

在Windows系统中安装OpenERP有2个选项：

.. i18n: * All-In-One Installation
.. i18n: 	This is the easiest and quickest way to install OpenERP. It installs all components (OpenERP Server and PostgreSQL database) pre-configured on one computer. This installation is recommended if you do not have any major customizations.
.. i18n: 
.. i18n: * Independent Installation
.. i18n: 	If you choose this mode of installation, all the components required to run OpenERP will have to be downloaded and installed separately. You will have to opt for an independent installation if you plan to install the components on separate machines. This mode is also practical if you are already working with, or plan to use, a different version of PostgreSQL than the one provided with the All-In-One installer.
..

* 一体化安装
	这是安装OpenERP最简单的方法。如果你没尝试过定制化安装，那么推荐你使用这种方法。

* 独立安装
	如果您选用该安装模式，所有运行OpenERP所必须的组件都需要单独下载安装。 如果您要把组件装在不同的机器上就需要使用这种方法。 如果您早已使用，或者计划使用不同版本的PostgreSQL，那么这种方法比一体式安装方法更实用。

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
