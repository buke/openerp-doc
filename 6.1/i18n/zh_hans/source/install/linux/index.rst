.. i18n: OpenERP Installation on Linux
.. i18n: =============================
..

OpenERP 在 Linux 的安装
=============================

.. i18n: The installation procedure for OpenERP 6.1 under Linux is explained in this chapter. This procedure is well tested on Ubuntu
.. i18n: version 10.04 LTS. For those familiar with earlier OpenERP versions, the 6.1 series has a different architecture:
..

这章介绍了 OpenERP 6.1 在 Linux 下的安装过程。这个过程是在 Ubuntu version 10.04 LTS 测试的. 对于熟悉 OpenERP 早期版本的用户， 6.1 系列有一下不一样的架构:

.. i18n: * The web client is now embedded in the main OpenERP Server, and does not require separate deployment
.. i18n: * The native GTK client is preserved as a legacy component, but the recommended way to use OpenERP is
.. i18n:   the web interface, as for all modern applications. There is usually no need to install the GTK client
.. i18n:   at all.
..

* web 客户端已经内置在 OpenERP 服务器中，不再要求单独安装。
* 原生 GTK 客户端保存为遗留组件，但是使用 OpenERP 的建议方法是 web 界面 , 就像所有的现代应用程序. 通常，完全不需要安装GTK 客户端。

.. i18n: For **Debian-based distributions**, OpenERP is available as an All-In-One application package (``.deb``), that
.. i18n: can be installed with a simple click. The package is available on the `OpenERP website's download page <http://www.openerp.com/downloads>`_ 
..

对于**基于 Debian 发行版**，OpenERP已经有了All-In-One应用程序包(``.deb``)，能够简单地一键安装。该包可在 OpenERP 站点的 `下载页 <http://www.openerp.com/downloads>`_ 找到。

.. i18n: For **RedHat-based platforms**, an experimental RPM distribution is available in our nightly builds. See the `downloads page <http://www.openerp.com/downloads>`_ for more details. 
..

对于**基于 RedHat 的平台**，有个试验性的 RPM 发布在 nightly builds. 看 `下载页 <http://www.openerp.com/downloads>`_ 获取更多信息. 



.. i18n: For **other Linux distributions** and for those who prefer a **manual installation**, there are only two steps
.. i18n: to deploy OpenERP under Linux: install PostgreSQL, the database engine used by OpenERP, then install OpenERP
.. i18n: itself. These steps are described in the following sections:
..

对于**其它的 Linux 发行版** ，已经那些更喜欢**手工安装的**的人,在linux下面部署Openerp 有两个步骤 : 安装 Openerp使用的数据库引擎, 然后安装 OpenERP 自身. 这些步骤在下列章节描述:

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
