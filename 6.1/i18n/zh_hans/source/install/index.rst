.. i18n: .. _installation-link:
.. i18n: 
.. i18n: Installation
.. i18n: ============
..

.. _installation-link:

安装
============

.. i18n: .. index:: Installation
..

.. index:: 安装

.. i18n: This chapter contains the general installation procedure for deploying OpenERP on the main supported platforms.
..

本章讲述在主要支持平台上部署OpenERP时通常的安装过程。

.. i18n: For **OpenERP Online (SaaS mode)** the installation is as simple as creating a new account on https://www.openerp.com/online.
.. i18n: The first section in this chapter provides the answer to Frequently Asked Questions for SaaS usage.
..

对于 **OpenERP Online (SaaS mode)** 而言，安装过程简单到只需在 https://www.openerp.com/online 中创建一个新帐号。
本章的第一节，提供了SaaS使用的常见问题的答案。

.. i18n: For **OpenERP on-site**, the installation mainly consists of installing PostgreSQL (the database engine used by OpenERP), 
.. i18n: Python (built-in on most platforms) and then installing OpenERP itself, as an all-in-one package.
..
 
对于 **OpenERP on-site** 而言, 作为一个AllinOne的安装包，安装过程主要是 安装PostgreSQL (openerp使用的数据库引擎)、
Python (多数平台内置)以及之后的 OpenERP 自身的安装。

.. i18n: .. note:: For those familiar with earlier OpenERP versions, the 6.1 series has a different architecture, and only requires the installation of a single OpenERP package.
..

.. note:: 对于熟悉OpenERP早期版本的用户而言，6.1 系列有了一个不一样的框架，和只需要安装单个OpenERP安装包的安装过程。

.. i18n: .. toctree::
.. i18n:     :glob:
.. i18n: 
.. i18n:     saas/index
.. i18n:     linux/index
.. i18n:     windows/index
.. i18n:     migration/index
..

.. toctree::
    :glob:

    saas/index
    linux/index
    windows/index
    migration/index
    
