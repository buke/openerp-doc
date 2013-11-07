.. i18n: OpenERP Installation on Linux
.. i18n: =============================
..

在 Linux 上安装 OpenERP 
=============================

.. i18n: The installation procedure for OpenERP 6.1 under Linux is explained in this chapter. This procedure is well tested on Ubuntu
.. i18n: version 10.04 LTS. For those familiar with earlier OpenERP versions, the 6.1 series has a different architecture:
..

本章介绍在 Linux 上安装OpenERP 6.1 的过程。此过程已在 Ubuntu version 10.04 LTS 严格测试过。 对于熟悉 OpenERP 早期版本的用户而言， 6.1 系列有一个不一样的架构:

.. i18n: * The web client is now embedded in the main OpenERP Server, and does not require separate deployment
.. i18n: * The native GTK client is preserved as a legacy component, but the recommended way to use OpenERP is
.. i18n:   the web interface, as for all modern applications. There is usually no need to install the GTK client
.. i18n:   at all.
..

* web 客户端已经内置在 OpenERP 服务器中，再不需要单独安装。
* 原生的 GTK 客户端作为历史遗留组件仍将保留，但是就像对所有现代应用一样，更推荐以 web 界面来使用 OpenERP 。通常情况下，完全没必要安装GTK 客户端。

.. i18n: For **Debian-based distributions**, OpenERP is available as an All-In-One application package (``.deb``), that
.. i18n: can be installed with a simple click. The package is available on the `OpenERP website's download page <http://www.openerp.com/downloads>`_ 
..

对于**基于 Debian 发行版**，OpenERP已经有了All-In-One应用程序包(``.deb``)，能够简单地一键安装。该包可在 OpenERP 站点的 `下载页 <http://www.openerp.com/downloads>`_ 中找到。

.. i18n: For **RedHat-based platforms**, an experimental RPM distribution is available in our nightly builds. See the `downloads page <http://www.openerp.com/downloads>`_ for more details. 
..

对于**基于 RedHat 的平台**，在 nightly builds 上有个试验性的 RPM 发布包。 查看 `下载页 <http://www.openerp.com/downloads>`_ 以获取更多信息。 



.. i18n: For **other Linux distributions** and for those who prefer a **manual installation**, there are only two steps
.. i18n: to deploy OpenERP under Linux: install PostgreSQL, the database engine used by OpenERP, then install OpenERP
.. i18n: itself. These steps are described in the following sections:
..

对于**其它的 Linux 发行版** ，以及那些更喜欢**手工安装**的人们，在linux上面部署Openerp 也只需两个步骤：安装 OpenERP 使用的数据库引擎PostgreSQL， 然后安装 OpenERP 自身。 接下来的章节中将介绍这些步骤:

.. i18n: .. toctree::
.. i18n:     :glob:
.. i18n: 
.. i18n:     postgres/index
.. i18n:     server/index
.. i18n:     client/index
.. i18n:     web/index
.. i18n:     updating
..

.. toctree::
    :glob:

    postgres/index
    server/index
    client/index
    web/index
    updating
    
