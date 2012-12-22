.. i18n: ================
.. i18n: Build and deploy
.. i18n: ================
..

=================
构建安装程序包和安装
=================

.. i18n: This page describes how to build a custom version of OpenERP for Windows.
..

This page describes how to build a custom version of OpenERP for Windows.

.. i18n: Building
.. i18n: ========
..

构建
====

.. i18n: Dependencies
.. i18n: ------------
..

关联性
-----

.. i18n: The first step is to build the dependencies. To do so, grab the Windows installer branch::
.. i18n: 
.. i18n:     bzr branch lp:~openerp-groupes/openerp/win-installer-trunk
..

第一步是建立关联性。要建立关联性，要抓取 Windows 安装分支::

    bzr branch lp:~openerp-groupes/openerp/win-installer-trunk

.. i18n: and install the packages:
..

然后安装以下程序包:

.. i18n:     * 7z465.msi
.. i18n:     * python-2.5.2.msi
.. i18n:     * setuptools-0.6c9.win32-py2.5.exe
.. i18n:     * Beaker-1.4.1.tar.gz
.. i18n:     * Mako-0.2.4.tar.gz
.. i18n:     * pytz-2010l.win32.exe
..

    * 7z465.msi
    * python-2.5.2.msi
    * setuptools-0.6c9.win32-py2.5.exe
    * Beaker-1.4.1.tar.gz
    * Mako-0.2.4.tar.gz
    * pytz-2010l.win32.exe

.. i18n: Server
.. i18n: ++++++
..

服务器
+++++

.. i18n: Install the packages:
..

安装以下程序包:

.. i18n:     * lxml-2.1.2.win32-py2.5.exe
.. i18n:     * PIL-1.1.6.win32-py2.5.exe
.. i18n:     * psycopg2-2.2.2.win32-py2.5-pg9.0.1-release.exe
.. i18n:     * PyChart-1.39.win32.exe
.. i18n:     * pydot-1.0.2.win32.exe
.. i18n:     * python-dateutil-1.5.tar.gz
.. i18n:     * pywin32-212.win32-py2.5.exe
.. i18n:     * PyYAML-3.09.win32-py2.5.exe
.. i18n:     * ReportLab-2.2.win32-py2.5.exe
..

    * lxml-2.1.2.win32-py2.5.exe
    * PIL-1.1.6.win32-py2.5.exe
    * psycopg2-2.2.2.win32-py2.5-pg9.0.1-release.exe
    * PyChart-1.39.win32.exe
    * pydot-1.0.2.win32.exe
    * python-dateutil-1.5.tar.gz
    * pywin32-212.win32-py2.5.exe
    * PyYAML-3.09.win32-py2.5.exe
    * ReportLab-2.2.win32-py2.5.exe

.. i18n: Web
.. i18n: +++
..

网页
++++

.. i18n: Install the packages:
..

安装以下程序包:

.. i18n:     * Babel-0.9.4-py2.5.egg
.. i18n:     * CherryPy-3.1.2.win32.exe
.. i18n:     * FormEncode-1.2.2.tar.gz
.. i18n:     * simplejson-2.0.9-py2.5-win32.egg
.. i18n:     * xlwt-0.7.2.win32.exe
..

    * Babel-0.9.4-py2.5.egg
    * CherryPy-3.1.2.win32.exe
    * FormEncode-1.2.2.tar.gz
    * simplejson-2.0.9-py2.5-win32.egg
    * xlwt-0.7.2.win32.exe

.. i18n: Source distribution
.. i18n: -------------------
..

来源配置
-------

.. i18n: The second step is to build a source distribution on Linux.
..

第二步是在 Linux 上建构一个来源配置

.. i18n: Server
.. i18n: ++++++
..

服务器
+++++

.. i18n: Let's assume you work on your own server branch named **6.0** and you want to build a server with the following modules:
..

假设你是要用你自己的服务器建构，版本名称 **6.0** ，而且想用以下的模块建构服务器:

.. i18n:     * base_setup
.. i18n:     * base_tools
.. i18n:     * board
..

    * base_setup
    * base_tools
    * board

.. i18n: This implies that these modules have been linked in *bin/addons* by a command similar to::
.. i18n: 
.. i18n:     ln -s ~/openerp/addons/6.0/{base_setup,base_tools,board} .
..

这表示这些模块已经用类似以下的指令连结到 *bin/addons* ::

    ln -s ~/openerp/addons/6.0/{base_setup,base_tools,board} .

.. i18n: To build the server, go to the root directory and type::
.. i18n: 
.. i18n:     python setup.py sdist --format=zip
..

要建构服务器，到根目录输入::

    python setup.py sdist --format=zip

.. i18n: You now have a new file in the **dist** directory, called openerp-server-M.m.P.zip where:
.. i18n:     * **M** is the major version, example 6
.. i18n:     * **m** is the minor version, example 0
.. i18n:     * **p** is the patch version, example 1
..

现在在 **dist** 目录里新增了一个文件，名为 openerp-server-M.m.P.zip ，这里的:
    * **M** 是主版次编号，例如 6
    * **m** 是次要版次编号，例如 0
    * **p** 是补丁版次编号，例如 1

.. i18n: Web
.. i18n: +++
..

网页
++++

.. i18n: To build the web client, go to the root directory and type::
.. i18n: 
.. i18n:     python setup.py sdist --format=zip
..

要建构网页客户端，到根目录输入::

    python setup.py sdist --format=zip

.. i18n: You now have a new file in the **dist** directory, called openerp-web-M.m.P.zip where:
.. i18n:     * **M** is the major version, example 6
.. i18n:     * **m** is the minor version, example 0
.. i18n:     * **p** is the patch version, example 1
..

现在在 **dist** 目录里新增了一个文件，名为 openerp-web-M.m.P.zip ，这里的:
    * **M** 是主版次编号，例如 6
    * **m** 是次要版次编号，例如 0
    * **p** 是补丁版次编号，例如 1

.. i18n: Binary distribution
.. i18n: -------------------
..

Binary distribution
-------------------

.. i18n: The third step is to build a binary distribution on Windows.
..

第三步是建构一个 Windows 规格的安装程序包

.. i18n: Server
.. i18n: ++++++
..

服务器
+++++

.. i18n: Open a command prompt and unzip the file::
.. i18n: 
.. i18n:     7z x openerp-server-M.m.P.zip -oC:\openerp
..

开启一个指令提示行， 解压缩以下文件 ::

    7z x openerp-server-M.m.P.zip -oC:\openerp

.. i18n: Go to the **win32** directory::
.. i18n: 
.. i18n:     cd C:\openerp\openerp-server-M.m.P\win32
..

移到 **win32** 文件夹 ::

    cd C:\openerp\openerp-server-M.m.P\win32

.. i18n: Generate the service exe with::
.. i18n: 
.. i18n:     python setup.py py2exe
..

用以下指令建立一个服务程序 ::

    python setup.py py2exe

.. i18n: Go to the parent directory::
.. i18n: 
.. i18n:     cd ..
..

移到上一层文件夹 ::

    cd ..

.. i18n: Generate the server exe with::
.. i18n: 
.. i18n:     python setup.py py2exe
..

用以下指令建立一个服务程序 ::

    python setup.py py2exe

.. i18n: Build the Windows installer with::
.. i18n: 
.. i18n:     makensis setup.nsi
..

用以下指令建立一个 Windows 安装包 ::

    makensis setup.nsi

.. i18n: You now have a new file in the root directory, called openerp-server-setup-M.m.P.exe. This file is the installer that you can use the install a custom version of OpenERP.
..

现在在根文件夹有一个新文件，名为 openerp-server-setup-M.m.P.exe。 这个文件就是安装定制版本 OpenERP 的安装程序包。

.. i18n: Web
.. i18n: +++
..

网页
++++

.. i18n: Open a command prompt and unzip the file::
.. i18n: 
.. i18n:     7z x openerp-web-M.m.P.zip -oC:\openerp
..

开启一个指令提示行， 解压缩以下文件 ::

    7z x openerp-web-M.m.P.zip -oC:\openerp

.. i18n: Go to the **win32** directory::
.. i18n: 
.. i18n:     cd C:\openerp\openerp-web-M.m.P\win32
..

移到 **win32** 文件夹 ::

    cd C:\openerp\openerp-web-M.m.P\win32

.. i18n: Generate the service exe with::
.. i18n: 
.. i18n:     python setup.py py2exe
..

用以下指令建立一个服务程序 ::

    python setup.py py2exe

.. i18n: Go to the parent directory::
.. i18n: 
.. i18n:     cd ..
..

移到上一层文件夹 ::

    cd ..

.. i18n: Generate the web exe with::
.. i18n: 
.. i18n:     python setup.py py2exe
..

用以下指令建立一个网页程序 ::

    python setup.py py2exe

.. i18n: Build the Windows installer with::
.. i18n: 
.. i18n:     makensis setup.nsi
..

用以下指令建立一个 Windows 安装包 ::

    makensis setup.nsi

.. i18n: You now have a new file in the root directory, called openerp-web-setup-M.m.P.exe. This file is the installer that you can use the install a custom version of OpenERP.
..

现在在根文件夹有一个新文件，名为 openerp-web-setup-M.m.P.exe。 这个文件就是安装定制版本 OpenERP 的安装程序包。

.. i18n: Deploy
.. i18n: ======
..

安装
====

.. i18n: This page describes how to deploy a custom version of OpenERP on Windows.
..

这一页在说明如何是在 Windows 里安装定制版本的 OpenERP 。

.. i18n: Package script
.. i18n: --------------
..

安装包脚本
---------

.. i18n: The first step is to grab the package script branch::
.. i18n: 
.. i18n:     bzr branch lp:~openerp-groupes/openerp/package-script
..

第一步是要抓取安装包脚本分支 ::

    bzr branch lp:~openerp-groupes/openerp/package-script

.. i18n: Batch
.. i18n: -----
..

批次执行档
---------

.. i18n: Go to the *packaging* directory of the branch and copy the file *build.bat* to the *C:\\openerp* directory of your Windows machine.
..

移到这个分支的 *packaging* 文件夹，把 *build.bat* 复制到 Widnows 电脑的 *C:\\openerp* 文件夹里。

.. i18n: SSH server
.. i18n: ----------
..

SSH 服务器
----------

.. i18n: You need to install a SSH server on Windows. You can for example install `freeSSHd <http://www.freesshd.com/>`_.
..

你需要在 Windows 电脑上安装 SSH 服务器，例如 `freeSSHd <http://www.freesshd.com/>`_。

.. i18n: Fabric
.. i18n: ------
..

Fabric
------

.. i18n: You need to install the tool `Fabric <http://docs.fabfile.org/0.9.3/>`_ to run commands on Windows from Linux using SSH. Refer to your linux package manager to install it.
..

你需要安装 `Fabric <http://docs.fabfile.org/0.9.3/>`_ 这个工具，才能让 Linux 透过 SSH 连上这台电脑， 并且执行命令。参照你的 Linux 套装管理员进行安装。

.. i18n: Configure
.. i18n: +++++++++
..

设定
++++

.. i18n: Go to the *packaging* directory of the branch and edit the file fabfile.py. Change what need to be changed.
..

到分支里的 *packaging* 文件夹，依照需要修改 fabfile.py 文件。

.. i18n: Run
.. i18n: +++
..

运行
+++

.. i18n: run the command::
.. i18n: 
.. i18n:     fab -H host -u user server
..

输入以下指令 ::

    fab -H host -u user server

.. i18n: where:
.. i18n:     * *host* is the Windows host name
.. i18n:     * *user* is the Windows user name
..

这里的 :
    * *host* 是 Windows 主机名称
    * *user* 是 Windows 使用者名称
