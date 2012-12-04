在Windows上安装OpenERP
======================

在本章，你将看到OpenERP v6.1在Windows系统上的安装。这个流程在Windows 7上很好地测过。

在Windows系统上安装OpenERP有两个选择：

* 完整（All-In-One）安装
	这是安装OpenERP最便捷的方式。在计算机上安装并配置所有的组件（OpenERP服务器，客户端，WEB以及PostgreSQL数据库）。如果没有很大的系统定制，推荐这种安装方式。

* 独立安装
	如果选择这种安装模式，运行OpenERP所需的组件需要分别下载和安装。如果计划在不同机器上安装这些组件，须选择独立安装方式。如果已经在用或者计划使用不同于完整安装版本的PostgreSQL，这个模式也比较可行。

.. toctree::
    :glob:

    allinone/index
    postgres/index
    server/index
    client/index
    web/index
    server/complementary_install_information
    updating
