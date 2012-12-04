.. i18n: .. index::
.. i18n:    single: Update; Upgrade; OpenERP (Linux)
..

.. index::
   single: Update; Upgrade; OpenERP (Linux)

.. i18n: .. _updating-linux-link:
.. i18n: 
.. i18n: ===============================================================================
.. i18n: Updating your OpenERP Installation
.. i18n: ===============================================================================
..

.. _updating-linux-link:

===============================================================================
更新你的 OpenERP 安装
===============================================================================

.. i18n: Going to a Newer Minor/Patch Release
.. i18n: ++++++++++++++++++++++++++++++++++++
..

更新Minor/补丁发行版
++++++++++++++++++++++++++++++++++++

.. i18n: OpenERP's release policy states that minor/patch releases of the stable
.. i18n: versions are usually published every month. These are recommended for
.. i18n: production deployment, as they include the latest security updates and bugfixes,
.. i18n: and do not require any migration process.
..

OpenERP的发布策略是 通常每个月发布稳定版本的Minor/补丁。 这些建议部署在生产环
境,因为它们包括最新的安全更新和错误修正,并且需要任何迁移过程。 

.. i18n: Of course you should always test these updates on a staging environment
.. i18n: (copy of your production environment) before applying them on the real
.. i18n: production systems.
..

当然，当然,你总是应该在应用到实际生产环境之前，在一个模拟环境（生成环境的
拷贝）中测试这些更新。

.. i18n: Minor/patch releases of OpenERP are identified by an increasing 3rd release
.. i18n: number, for example, v6.0.15 would be the 15th patch release of OpenERP v6.0.
..

OpenERP的小版本/补丁发行版用增加第3个发行号来标识，例如 v6.0.5是  OpenERP v6.0 的第15个补丁发行.

.. i18n: For more details regarding the release cycle, have a look at the section
.. i18n: :ref:`release_cycle`.
..

关于发行周期的更多信息，参阅 :ref:`release_cycle` 。

.. i18n: .. note:: Minor Versions
.. i18n: 
.. i18n:         You can skip minor versions, for example, you do not need to install all the intermediary versions between 6.0.6 and 6.0.15 if you need to upgrade an outdated installation, as long as you stay in the same version line (6.0 in this example).
..

.. note:: Minor

        你能跳过 minor 版本, 例如,如果你要升级一个已经过时的版本，只要你还停留在同一个版本线中，你不必安装从 6.0.6 到 6.0.15 的所有发行版（例如：例子中的6.0），

.. i18n: Updating an existing OpenERP installation to a newer patch release boils down
.. i18n: to 2 operations:
..

升级一个已有的 OpenERP 安装到较新的补丁发行版，归结为两个操作:

.. i18n:     * Install the new code over the existing one
.. i18n:     * Synchronize each existing database with the new code
..

    * 安装新的代码覆盖已有的一个
    * 用新的代码同步每个已有的数据库

.. i18n: In order to accomplish this, the following step-by-step procedure should give you
.. i18n: the best results:
..

为了实现这些，下面的步骤将给你一个最好的结果 :

.. i18n:     #. Make a fresh backup of all existing databases, as well as a backup of the files 
.. i18n:        of your OpenERP installation (server and addons), just in case.
.. i18n:     #. Locate the executable file to start the Server, it should be named
.. i18n:        ``openerp-server.py``. You may want to have a look at the running processes
.. i18n:        to find out the command-line parameters that are passed to the server (needed below).
.. i18n:     #. Stop the OpenERP server.
.. i18n:     #. Update the source files to the latest release, or simply install the new releases
.. i18n:        over the previous ones.
.. i18n:     #. Start the server manually (directly call the executable you located above), with
.. i18n:        the following additional parameters, to trigger an update of all module data and
.. i18n:        views in the database, based on the new source files (include your usual startup
.. i18n:        parameters, if any, and replace ``DB_NAME`` with the name of the OpenERP database you wish
.. i18n:        to update)::
.. i18n: 
.. i18n:          openerp-server.py -d DB_NAME -u all
.. i18n: 
.. i18n:     #. Let the server complete its startup (watch the log for the final message that says
.. i18n:        ``OpenERP server is running, waiting for connections`` or wait until you can connect
.. i18n:        to that database with a GTK client), then stop the server with :kbd:`Ctrl+C` and repeat the
.. i18n:        previous step for each database on this OpenERP installation (any database not updated
.. i18n:        will use the latest business logic but might have errors or missing improvements in
.. i18n:        the views until you update it using this procedure).
.. i18n:     #. Stop the server again with :kbd:`Ctrl+C` and restart it normally (no extra parameters anymore).
.. i18n:     #. You can now proceed with the update of the GTK clients,
.. i18n:        by simply reinstalling the latest version over the previous one.
..

    #. 为所有数据库制作一个新的备份, 而且要备份你的Openerp安装的全部文件（服务器和addons），以防万一。
    #. 找到启动服务器的执行文件,通常是``openerp-server.py``。 你可能要看一下运行过程，找出传递给服务器的命
       令行参数(下面需要).
    #. 停止 OpenERP 服务器.
    #. 升级最新发布的源文件e,或者简单地按一个新的发布覆盖以前的一个。
    #. 用下来附加参数手动启动服务器 (直接调用上面找到的执行文件), 基于新的源文件，升级数据库中所有 
       模块数据和视图 (包括你常用的启动参数,并且用你要升级的数据库名称替换 ``DB_NAME``)::

         openerp-server.py -d DB_NAME -u all

    #. 让服务器完成他的启动 (查看日志的最后一条消息： ``OpenERP server is running, waiting for connections`` 或者
       等到你能用GTK客户端连接到数据库 ), 然后用 :kbd:`Ctrl+C` 停止服务器 ，并且为OpenERP安装的每个数据库重复上述
       步骤 (任何数据库没有更新，将使用最新的业务逻辑，但是可能有错误或者在视图中丢失改进的东西，直到你用这个步骤更新).
    #. 再次用 :kbd:`Ctrl+C` 停止服务器 并且正常重启(不需要额外参数).
    #. 现在可以更新 GTK 客户端，简单地重新安装一个最新版覆盖前面版本即可。

.. i18n: .. note:: Server
.. i18n: 
.. i18n:         As an alternative to restarting the server in update mode for each database, as described above, you may try to start the server normally, and then connect to each database as the *Administrator* user, open the list of modules and manually trigger an update of the *base* module. Because all modules depend on *base* they will be updated too. However this requires the *Administrator* password of each database and may not work for some updates, specifically when the update prevents you from logging into the system.
..

.. note:: 服务器

        作为一个选中，在更新模式为每个数据重启服务器，如上面所述，你可以横穿启动服务器，然后作为*Administrator* 用户连接到每个数据库, 打开模块列表，手工触发 *base* 模块的升级.因为所有的模块依赖于 *base*，他们也将被升级。然而这要求每个数据库的 *Administrator* 密码，特别是当这些更新阻止你的系统.

.. i18n: .. tip:: Developer Book
.. i18n: 
.. i18n:         For more technical details on the actual operations accomplished by the server during such an update, you may refer to the corresponding section in the Developer Book: :ref:`technical_update_procedure`.
..

.. tip:: 开发指南

        为了更多在真实的譬如完成服务器升级的技术信息, 你参考开发指南的相关章节: :ref:`technical_update_procedure`.

.. i18n: Going to a Newer Major Release
.. i18n: ++++++++++++++++++++++++++++++
..

更新到一个新的主发行版
++++++++++++++++++++++++++++++

.. i18n: The frequency of major stable releases has fluctuated in the past, but the current policy is to release a new stable version every 6 months on average, with one out of three stable versions being a Long Term Support (LTS) version. An LTS version is a normal stable version, but one that is supported for an extended time under the OpenERP Publisher’s Warranty (OPW). Stable versions are labelled as a decimal number with 2 components (e.g. 6.1), where the leftmost part indicates the corresponding Long Term Support (LTS) version, and the second digit indicates successive stable releases between two LTS versions.
..

在过去，主要的稳定发行版的频率是波动的, 但是当前策略是平均每6个月发布一个新的稳定版本, 三个稳定版之间有个一个是长期支持版（LTS）.一个LTS版本通常是正常稳定的版, 是在 OpenERP Publisher’s Warranty (OPW)下面支持长时间。稳定版用两个部件标记为一个小数(例如 6.1),在最左边的部分显示相应的长期支持(LTS)版本,第二个数字指示了在两个LTS版之间的连续稳定版本。

.. i18n: Transitioning to the next major release implies a lot more changes than jumping to another minor release.
.. i18n: As the underlying OpenERP data structures usually evolve quite a bit from one major release to the next, a full migration of the existing data is needed.
.. i18n: Each major release will be published with specific recommendations and procedures for upgrading an existing OpenERP system to the next major version.
..

过渡到下个主发行版意味着比小发行版多得多的变化。从主发行版到下一个，因为基础的Openerp数据结构的演进非常大,对已有的数据，需要一个完整的迁移。
每个主发行版，将发布具体建议和过程，以升级一个已有的Openerp系统到下一个主版本。
