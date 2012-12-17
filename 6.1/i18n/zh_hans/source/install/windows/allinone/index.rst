.. i18n: .. index::
.. i18n:    single: Installation; OpenERP All-In-One (Windows)
.. i18n:    single: OpenERP All-In-One; Installation (Windows)
.. i18n: .. 
..

.. index::
   single: Installation; OpenERP All-In-One (Windows)
   single: OpenERP All-In-One; Installation (Windows)
.. 

.. i18n: .. windows-allinone-link:
..

.. windows-allinone-link:

.. i18n: OpenERP All-In-One Installation
.. i18n: ===============================
..

OpenERP完整（All-In-One）安装
===============================

.. i18n: Each time a new release of OpenERP is made, OpenERP supplies a complete Windows auto-installer for
.. i18n: it. This contains all of the components you need – the PostgreSQL database server, the OpenERP
.. i18n: application server and the GTK application client.
..

每当有新的版本的时候，OpenERP都会提供一个完整的Windows自动安装包。安装包包含你需要的所有组件 – PostgreSQL数据库服务器，OpenERP应用服务器，GTK应用客户端以及WEB客户端。

.. i18n: This auto-installer enables you to install the whole system in just a few mouse clicks. The initial
.. i18n: configuration is set up during installation, making it possible to start using it very quickly, as
.. i18n: long as you do not want to change the underlying code. It is aimed at the installation of everything
.. i18n: on a single PC, but you can later connect GTK clients from other PCs, Macs and Linux boxes to it as
.. i18n: well.
..

这个自动安装包能够让你仅仅点击几次鼠标就可以安装整个系统。在安装过程中完成初步配置，系统可以很快好用，无需改变底层代码。虽然安装包倾向于在单机上安装所有的东西，你还可以从其它的PC机、Mac机、Linux盒子连接GTK客户端。

.. i18n: Downloading OpenERP All-In-One
.. i18n: ------------------------------
..

下载OpenERP完整安装包
------------------------------

.. i18n: The first step is to download the OpenERP All-In-One installer. At this stage, you must choose which version
.. i18n: to install – the stable version or the development version. If you are planning to put it straight
.. i18n: into production we strongly advise you to choose the stable version.
..

第一步是下载OpenERP完整安装包。在这个阶段，必须选择哪个版本 – 稳定版或开发版。如果你想直接用于生产，那么我们强烈推荐你选择稳定版。

.. i18n: .. index::
.. i18n:    single: OpenERP versions
..

.. index::
   single: OpenERP versions

.. i18n: .. note::  Stable Versions and Development Versions
.. i18n: 
.. i18n: 	OpenERP development proceeds in two parallel tracks: stable versions and development versions.
.. i18n: 
.. i18n: 	New functionality is integrated into the development branch. This branch is more advanced than the
.. i18n: 	stable branch, but it can contain undiscovered and unfixed faults. A new development release is
.. i18n: 	made every month or so, and OpenERP has made the code repository available so you can download the
.. i18n: 	very latest revisions if you want.
.. i18n: 
.. i18n: 	The stable branch is designed for production environments. Here, releases of new functionality are
.. i18n: 	made only about once a year after a long period of testing and validation. Only bug fixes are
.. i18n: 	released through the year on the stable branch.
..

.. note::  稳定版和开发版

	OpenERP开发双轨平行进行有稳定版和开发版。

	新功能整合到开发分支。这个分支比稳定版分支先进，但是可能还有未发现和未解决的问题。开发版约每月发布一次，你可以从OpenERP代码库下载最新的版本。

	稳定版是为生产环境设计的。新功能版本要经过长期测试和验证后（大概）一年发布一次；  这个当中仅仅发布BUG补丁。

.. i18n: .. index::
.. i18n:    single: installation; Windows (all-in-one)
..

.. index::
   single: installation; Windows (all-in-one)

.. i18n: To download OpenERP for Windows, follow these steps:
..

按照以下步骤下载用于Windows的OpenERP：

.. i18n: #. Navigate to the site http://www.openerp.com.
.. i18n: 
.. i18n: #. Click the :menuselection:`Downloads` button at the right, then, under :guilabel:`Windows Auto-Installer`, select
.. i18n:    **All-In-One**.
.. i18n: 
.. i18n: #. Before you can proceed with the download, you will be asked to fill an online form with your contact and company details and information regarding your interest in OpenERP.
.. i18n: 
.. i18n: #. Once you submit the online form, the All-In-One Windows installer is automatically downloaded.
.. i18n: 
.. i18n: #. Save the file on your PC - it is quite a substantial size because it downloads everything including
.. i18n:    the PostgreSQL database system (version 8.3, at the time of writing), so it will take some time.
..

#. 访问站点：http://www.openerp.com。

#. 点击右边 :menuselection:`Downloads` 按钮，然后在 :guilabel:`Windows Auto-Installer`下面选择 **All-In-One**.

#. 在可以下载之前，你将被要求填写一个在线表格：你的联系方式和公司详情以及有关你对OpenERP兴趣的信息。

#. 提交在线表格之后，Windows完整安装包就可自动下载了。

#. 在你的PC上保存文件 – 因为要下载包含PostSQL数据库系统（撰写此文的时候版本是8.3）的所有东西，尺寸确实有些大，下载要费点时间。

.. i18n: .. index::
.. i18n:    single:  installation; administrator
..

.. index::
   single:  installation; administrator

.. i18n: Installing the OpenERP All-In-One
.. i18n: ---------------------------------
..

安装OpenERP完整包（All-In-One）
---------------------------------

.. i18n: To install OpenERP and its database, you must be signed in as an Administrator on your PC. 
..

要安装OpenERP及其数据库，你必须以管理员身份登录你的PC。 

.. i18n: If you have previously tried to install the All-In-One version of OpenERP, you will have to uninstall
.. i18n: that first, because various elements of a previous installation could interfere with your new installation.
.. i18n: Make sure that all Tiny ERP, OpenERP and PostgreSQL applications are removed:
.. i18n: you are likely to have to restart your PC to finish removing all traces of them.
..

如果你之前曾经安装过OpenERP完整版，你先需要卸载掉它，因为之前安装的各种元素可能会与新的安装冲突。确保所有Tiny ERP，OpenERP以及PostgreSQL应用已经移除：你极可能需要重启你的PC完成所有残余的移除。

.. i18n: Double-click the installer file to install OpenERP and accept the default parameters on each dialog box as you go.
.. i18n: The All-In-One installer is the simplest mode of installation and has the following steps:
..

双击安装文件安装OpenERP并接受接下来每个对话框的默认参数。完整安装包是最简单的安装模式，有如下步骤：

.. i18n: * 1. Select installation language
.. i18n: 	The default is ``English``. The other option is ``French``.
.. i18n: 
.. i18n: * 2. Welcome message
.. i18n: 	Carefully follow the recommendations given in this step.
..

* 1. 选择安装语言
	默认语言是英文；其他选项有法语。

* 2. 欢迎信息
	小心仔细遵循这步给出的推荐。

.. i18n:   .. figure:: ../../img/a2_welcome.png
.. i18n:         :scale: 50
.. i18n:         :align: center
.. i18n: 
.. i18n:         *Welcome to OpenERP*
..

  .. figure:: ../../img/a2_welcome.png
        :scale: 50
        :align: center

        *欢迎安装OpenERP*

.. i18n: * 3. Licence Agreement
.. i18n: 	It is important that you accept the GNU General Public License to proceed with installation.
.. i18n: 
.. i18n: * 4. Select components to install
.. i18n: 	You can proceed with the default install type ``All In One``, which will install the OpenERP Server, GTK Desktop Client and PostgreSQL Database (version 8.3, at the time of writing). Or, you may customize your installation by selecting only the components you require.
.. i18n:   
.. i18n:   .. figure:: ../../img/a4_components.png
.. i18n:         :scale: 50
.. i18n:         :align: center
.. i18n: 
.. i18n:         *Customize component installation*
.. i18n:   
.. i18n: * 5. Configure PostgreSQL connection
.. i18n: 	The installer will suggest default parameters to complete your PostgreSQL connection configuration. You may accept the defaults, or change it according to your requirement.
.. i18n: 
.. i18n:   .. figure:: ../../img/a6_config_postgres.png
.. i18n:         :scale: 50
.. i18n:         :align: center
.. i18n: 
.. i18n:         *PostgreSQL configuration*
.. i18n: 
.. i18n: * 6. Select folder for installation
.. i18n: 	By default, OpenERP is installed in ``C:\Program Files\OpenERP 6.0``. To install in a different folder, browse for a different location(folder) in this step.
.. i18n: 
.. i18n: * 7. Install
.. i18n: 	The automatic installation of OpenERP begins and you can view its progress.
.. i18n: 
.. i18n: * 8. Finish
.. i18n: 	On successful installation of OpenERP, you will get an appropriate confirmation. You can click `Finish` to close the setup wizard.
.. i18n: 
.. i18n:   .. figure:: ../../img/a9_finish.png
.. i18n:      :scale: 50
.. i18n:      :align: center
.. i18n: 
.. i18n:      *End of setup wizard*
..

* 3. 许可证协议
	你要接受GNU公共许可才能继续安装，这很重要。

* 4. 选择安装组件
	你可以以默认安装方式，完整安装OpenERP服务器，GTK桌面客户端，WEB客户端以及PostgreSQL数据库（撰写此书的时候版本是8.3）或者你可以定制安装你需要的组件。
  
  .. figure:: ../../img/a4_components.png
        :scale: 50
        :align: center

        *组件定制安装*
  
* 5. 配置PostgreSQL链接
	安装包将建议默认参数，完成你的PostgreSQL链接配置。你可以接受默认配置或者按照你的需要变更。

  .. figure:: ../../img/a6_config_postgres.png
        :scale: 50
        :align: center

        *PostgreSQL 配置*

* 6. 选择安装目录
	默认情况下，OpenERP安装在 ''C:\ProgramFiles\OpenERP 6.0''。要安装到不同的目录，在这步浏览不同的位置。

* 7. 安装
	OpenERP自动安装开始，你能看到安装进度。

* 8. 完成
	成功安装OpenERP，你会得到一个适当的确认。你可以点击完成结束安装向导。

  .. figure:: ../../img/a9_finish.png
     :scale: 50
     :align: center

     *结束安装向导*

.. i18n: Connecting to OpenERP
.. i18n: ---------------------
..

连接到 OpenERP
---------------------

.. i18n: You do not need to manually start the OpenERP Server, because it is installed as a Windows service and automatically started.
.. i18n: You may however access it from the shortcuts created in the `Start` menu for `OpenERP`, or simply by connecting with your
.. i18n: preferred browser to web interface, by default available on ``http://localhost:8069``
..

你不需要手工启动OpenERP服务器，OpenERP服务器安装为Windows服务，会自动启动。不过，你还可以开始菜单的OpenERP快捷方式进入，或者用你喜欢的浏览器连接web接口，默认情况下接口在``http://localhost:8069``。

.. i18n: Use the database list at the top-right corner to choose a database to connect to.
.. i18n: As this would be the first time you are using OpenERP since its installation, your database list will be empty.
.. i18n: You can create a new database through the ``Manage databases`` link on the login page.
..

用右上角的数据库列表选择要连接的数据库。如果你是安装后第一次使用的话，你的数据库列表是空的。你可以通过登录界面的 ''管理数据库'' 链接创建新的数据库。