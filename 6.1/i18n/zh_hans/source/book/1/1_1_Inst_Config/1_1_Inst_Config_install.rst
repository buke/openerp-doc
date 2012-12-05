
.. i18n: The Installation of OpenERP
.. i18n: ===========================
..

安装 OpenERP
===========================

.. i18n: Whether you are from a small company investigating how OpenERP works, or you are part of the IT staff of a
.. i18n: larger organization and have been asked to assess OpenERP's capabilities, your first requirement
.. i18n: is to install it or to find a working installation.
..

Whether you are from a small company investigating how OpenERP works, or you are part of the IT staff of a
larger organization and have been asked to assess OpenERP's capabilities, your first requirement
is to install it or to find a working installation.

.. i18n: The table below summarizes the various installation methods that will be described in the following
.. i18n: sections.
..

The table below summarizes the various installation methods that will be described in the following
sections.

.. i18n: .. csv-table:: Comparison of the different methods of installation on Windows or Linux
.. i18n:    :header: "Method","Average Time","Level of Complexity","Notes"
.. i18n:    :widths: 20,15,15,30
.. i18n: 
.. i18n:    "OpenERP Demo","No installation","Simple","Very useful for quick evaluations because no need to install anything."
.. i18n:    "All-in-one Windows Installer","A few minutes","Simple","Very useful for quick evaluations because it installs all of the components pre-configured on one computer (using the GTK client)."
.. i18n:    "Independent installation on Windows","Half an hour","Medium","Enables you to install the components on different computers. Can be put into production use."
.. i18n:    "Ubuntu Linux packages","A few minutes","Simple","Simple and quick but the Ubuntu packages are not always up to date."
.. i18n:    "From source, for all Linux systems","More than half an hour","Medium to slightly difficult","This is the method recommended for production environments because it is easy to keep it up to date."
..

.. csv-table:: Comparison of the different methods of installation on Windows or Linux
   :header: "Method","Average Time","Level of Complexity","Notes"
   :widths: 20,15,15,30

   "OpenERP Demo","No installation","Simple","Very useful for quick evaluations because no need to install anything."
   "All-in-one Windows Installer","A few minutes","Simple","Very useful for quick evaluations because it installs all of the components pre-configured on one computer (using the GTK client)."
   "Independent installation on Windows","Half an hour","Medium","Enables you to install the components on different computers. Can be put into production use."
   "Ubuntu Linux packages","A few minutes","Simple","Simple and quick but the Ubuntu packages are not always up to date."
   "From source, for all Linux systems","More than half an hour","Medium to slightly difficult","This is the method recommended for production environments because it is easy to keep it up to date."

.. i18n: Each time a new release of OpenERP is made, OpenERP supplies a complete Windows auto-installer for
.. i18n: it. This contains all of the components you need – the PostgreSQL database server, the OpenERP
.. i18n: application server and the GTK application client.
..

Each time a new release of OpenERP is made, OpenERP supplies a complete Windows auto-installer for
it. This contains all of the components you need – the PostgreSQL database server, the OpenERP
application server and the GTK application client.

.. i18n: This auto-installer enables you to install the whole system in just a few mouse clicks. The initial
.. i18n: configuration is set up during installation, making it possible to start using it very quickly as
.. i18n: long as you do not want to change the underlying code. It is aimed at the installation of everything
.. i18n: on a single PC, but you can later connect GTK clients from other PCs, Macs and Linux boxes to it as
.. i18n: well.
..

This auto-installer enables you to install the whole system in just a few mouse clicks. The initial
configuration is set up during installation, making it possible to start using it very quickly as
long as you do not want to change the underlying code. It is aimed at the installation of everything
on a single PC, but you can later connect GTK clients from other PCs, Macs and Linux boxes to it as
well.

.. i18n: The first step is to download the OpenERP installer. At this stage you must choose which version
.. i18n: to install – the stable version or the development version. If you are planning to put it straight
.. i18n: into production we strongly advise you to choose the stable version.
..

The first step is to download the OpenERP installer. At this stage you must choose which version
to install – the stable version or the development version. If you are planning to put it straight
into production we strongly advise you to choose the stable version.

.. i18n: .. index::
.. i18n:    single: stable versions
..

.. index::
   single: stable versions

.. i18n: .. note::  Stable Versions and Development Versions
.. i18n: 
.. i18n: 	OpenERP development proceeds in two parallel tracks: stable versions and development versions.
.. i18n: 
.. i18n: 	New functionality is integrated into the development branch. This branch is more advanced than the
.. i18n: 	stable branch, but it can contain undiscovered and unfixed faults. A new development release is
.. i18n: 	made every month or so, and OpenERP has made the code repository available so you can download the
.. i18n: 	very latest revisions if you want.
.. i18n: 
.. i18n: 	The stable branch is designed for production environments. Releases of new functionality there are
.. i18n: 	made only about once a year after a long period of testing and validation. Only bug fixes are
.. i18n: 	released through the year on the stable branch.
..

.. note::  Stable Versions and Development Versions

	OpenERP development proceeds in two parallel tracks: stable versions and development versions.

	New functionality is integrated into the development branch. This branch is more advanced than the
	stable branch, but it can contain undiscovered and unfixed faults. A new development release is
	made every month or so, and OpenERP has made the code repository available so you can download the
	very latest revisions if you want.

	The stable branch is designed for production environments. Releases of new functionality there are
	made only about once a year after a long period of testing and validation. Only bug fixes are
	released through the year on the stable branch.

.. i18n: .. index::
.. i18n:    single: installation; Windows (all-in-one)
..

.. index::
   single: installation; Windows (all-in-one)

.. i18n: To download the version of OpenERP for Windows, follow these steps:
..

To download the version of OpenERP for Windows, follow these steps:

.. i18n: #. Navigate to the site http://openerp.com.
.. i18n: 
.. i18n: #. Click the :menuselection:`Downloads` button at the right, then, under :guilabel:`Windows Auto-Installer`, select
.. i18n:    :menuselection:`All-in-One`.
.. i18n: 
.. i18n: #. This brings up the demonstration version Windows installer, 
.. i18n:    currently :program:`openerp-allinone-setup-6.0.0`.
.. i18n: 
.. i18n: #. Save the file on your PC - it is quite a substantial size because it downloads everything including
.. i18n:    the PostgreSQL database system, so it will take some time.
..

#. Navigate to the site http://openerp.com.

#. Click the :menuselection:`Downloads` button at the right, then, under :guilabel:`Windows Auto-Installer`, select
   :menuselection:`All-in-One`.

#. This brings up the demonstration version Windows installer, 
   currently :program:`openerp-allinone-setup-6.0.0`.

#. Save the file on your PC - it is quite a substantial size because it downloads everything including
   the PostgreSQL database system, so it will take some time.

.. i18n: .. index::
.. i18n:    single:  installation; administrator
..

.. index::
   single:  installation; administrator

.. i18n: To install OpenERP and its database, you must be signed in as an Administrator on your PC. Double-
.. i18n: click the installer file to install it and accept the default parameters on each dialog box as you go. 
..

To install OpenERP and its database, you must be signed in as an Administrator on your PC. Double-
click the installer file to install it and accept the default parameters on each dialog box as you go. 

.. i18n: If you had previously tried to install the all-in-one version of OpenERP, you will have to uninstall
.. i18n: that first, because various elements of a previous installation could interfere with your new installation.
.. i18n: Make sure that all Tiny ERP, OpenERP and PostgreSQL applications are removed:
.. i18n: you are likely to have to restart your PC to finish removing all traces of them.
..

If you had previously tried to install the all-in-one version of OpenERP, you will have to uninstall
that first, because various elements of a previous installation could interfere with your new installation.
Make sure that all Tiny ERP, OpenERP and PostgreSQL applications are removed:
you are likely to have to restart your PC to finish removing all traces of them.

.. i18n: The OpenERP client can be opened, ready to use the OpenERP system, once you have completed 
.. i18n: the all-in-one installation. The next step consists
.. i18n: of setting up the database, and is covered in the final section of this chapter :ref:`sect-creatingdb`.
..

The OpenERP client can be opened, ready to use the OpenERP system, once you have completed 
the all-in-one installation. The next step consists
of setting up the database, and is covered in the final section of this chapter :ref:`sect-creatingdb`.

.. i18n: .. index::
.. i18n:    single: installation; Windows (independent)
..

.. index::
   single: installation; Windows (independent)

.. i18n: Independent Installation on Windows
.. i18n: -----------------------------------
..

Windows 独立安装
-----------------------------------

.. i18n: System administrators can have very good reasons for wanting to install the various components of a
.. i18n: Windows installation separately. For example, your company may not support the version of PostgreSQL
.. i18n: or Python that is installed automatically, or you may already have PostgreSQL installed on the server
.. i18n: you are using, or you may want to install the database server and application server on
.. i18n: separate hardware units.
..

System administrators can have very good reasons for wanting to install the various components of a
Windows installation separately. For example, your company may not support the version of PostgreSQL
or Python that is installed automatically, or you may already have PostgreSQL installed on the server
you are using, or you may want to install the database server and application server on
separate hardware units.

.. i18n: For this situation, you can get a separate installer for the OpenERP server from the same
.. i18n: location as the all-in-one auto-installer. You will also have to download and install a suitable
.. i18n: version of PostgreSQL independently.
..

For this situation, you can get a separate installer for the OpenERP server from the same
location as the all-in-one auto-installer. You will also have to download and install a suitable
version of PostgreSQL independently.

.. i18n: You must install PostgreSQL before the OpenERP server, and you must also set it up with a user
.. i18n: and password so that the OpenERP server can connect to it. OpenERP's web-based documentation gives
.. i18n: full and current details.
..

You must install PostgreSQL before the OpenERP server, and you must also set it up with a user
and password so that the OpenERP server can connect to it. OpenERP's web-based documentation gives
full and current details.

.. i18n: Connecting Users on Other PCs to the OpenERP Server
.. i18n: ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
..

从其它计算机访问 OpenERP Server
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. i18n: To connect other computers to the OpenERP server, you must set the server up so that it is
.. i18n: visible to the other PCs, and install a GTK client on each of those PCs:
..

To connect other computers to the OpenERP server, you must set the server up so that it is
visible to the other PCs, and install a GTK client on each of those PCs:

.. i18n: #. Make your OpenERP server visible to other PCs by opening the Windows Firewall in the Control
.. i18n:    Panel, then ask the firewall to make an exception of the OpenERP server. In the
.. i18n:    :guilabel:`Exceptions` tab of Windows Firewall click :guilabel:`Add a program...` and choose
.. i18n:    :guilabel:`OpenERP Server` in the list provided. This step enables other computers to see the
.. i18n:    OpenERP application on this server.
.. i18n: 
.. i18n: #. Install the OpenERP client (:program:`openerp-client-6.X.exe`), which you can download in the
.. i18n:    same way as you downloaded the other OpenERP software, onto the other PCs.
..

#. Make your OpenERP server visible to other PCs by opening the Windows Firewall in the Control
   Panel, then ask the firewall to make an exception of the OpenERP server. In the
   :guilabel:`Exceptions` tab of Windows Firewall click :guilabel:`Add a program...` and choose
   :guilabel:`OpenERP Server` in the list provided. This step enables other computers to see the
   OpenERP application on this server.

#. Install the OpenERP client (:program:`openerp-client-6.X.exe`), which you can download in the
   same way as you downloaded the other OpenERP software, onto the other PCs.

.. i18n: .. tip:: Version Matching
.. i18n: 
.. i18n: 	You must make sure that the version of the client matches that of the server. The version number is
.. i18n: 	given as part of the name of the downloaded file. Although it is possible that some different
.. i18n: 	revisions of client and server will function together, there is no certainty about that.
..

.. tip:: Version Matching

	You must make sure that the version of the client matches that of the server. The version number is
	given as part of the name of the downloaded file. Although it is possible that some different
	revisions of client and server will function together, there is no certainty about that.

.. i18n: .. index::
.. i18n:    single:  administrator
..

.. index::
   single:  administrator

.. i18n: To run the client installer on every other PC you will need to have administrator rights there. The
.. i18n: installation is automated, so you just need follow the different installation steps.
..

To run the client installer on every other PC you will need to have administrator rights there. The
installation is automated, so you just need follow the different installation steps.

.. i18n: To test your installation, start by connecting through the OpenERP client on the server machine
.. i18n: while you are still logged in as administrator.
..

To test your installation, start by connecting through the OpenERP client on the server machine
while you are still logged in as administrator.

.. i18n: .. note:: Why sign in as a PC Administrator?
.. i18n: 
.. i18n: 	You would not usually be signed in as a PC administrator when you are just running the OpenERP client,
.. i18n: 	but if there have been problems in the installation it is easier to remain as an administrator after
.. i18n: 	the installation so that you can make any necessary fixes than to switch users as you alternate
.. i18n: 	between roles as a tester and a software installer.
..

.. note:: Why sign in as a PC Administrator?

	You would not usually be signed in as a PC administrator when you are just running the OpenERP client,
	but if there have been problems in the installation it is easier to remain as an administrator after
	the installation so that you can make any necessary fixes than to switch users as you alternate
	between roles as a tester and a software installer.

.. i18n: Start the GTK client on the server through the Windows Start menu there. The main client window
.. i18n: appears, identifying the server you are connected to (which is \ ``localhost``\   – your own server
.. i18n: PC – by default). If the message :guilabel:`No database found, you must create one` appears then
.. i18n: you have **successfully connected** to an OpenERP server containing, as yet, no databases.
..

Start the GTK client on the server through the Windows Start menu there. The main client window
appears, identifying the server you are connected to (which is \ ``localhost``\   – your own server
PC – by default). If the message :guilabel:`No database found, you must create one` appears then
you have **successfully connected** to an OpenERP server containing, as yet, no databases.

.. i18n: .. figure:: images/new_login_dlg.png
.. i18n:    :align: center
.. i18n:    :scale: 75
.. i18n: 
.. i18n:    *Dialog box on connecting a GTK client to a new OpenERP server*
..

.. figure:: images/new_login_dlg.png
   :align: center
   :scale: 75

   *Dialog box on connecting a GTK client to a new OpenERP server*

.. i18n: .. index::
.. i18n:    single: protocol; XML-RPC
.. i18n:    single: protocol; NET-RPC
.. i18n:    single: XML-RPC
.. i18n:    single: NET-RPC
..

.. index::
   single: protocol; XML-RPC
   single: protocol; NET-RPC
   single: XML-RPC
   single: NET-RPC

.. i18n: .. note:: Connection Modes
.. i18n: 
.. i18n: 	In its default configuration at the time of writing, 
.. i18n: 	the OpenERP client connects to port 8069 on the server using the
.. i18n: 	XML-RPC protocol (from Linux) or port 8070 using the NET-RPC protocol instead (from Windows).
.. i18n: 	You can use any protocol from either operating system.
.. i18n: 	NET-RPC is quite a bit quicker, although you may not notice that on the GTK client in normal use.
.. i18n: 	OpenERP can run XML-RPC, but not NET-RPC, as a secure connection.
.. i18n: 	
.. i18n: Resolving Errors with a Windows Installation
.. i18n: ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
..

.. note:: Connection Modes

	In its default configuration at the time of writing, 
	the OpenERP client connects to port 8069 on the server using the
	XML-RPC protocol (from Linux) or port 8070 using the NET-RPC protocol instead (from Windows).
	You can use any protocol from either operating system.
	NET-RPC is quite a bit quicker, although you may not notice that on the GTK client in normal use.
	OpenERP can run XML-RPC, but not NET-RPC, as a secure connection.
	
解决 Windows 安装中的错误
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. i18n: If you cannot get OpenERP to work after installing your Windows system you will find some ideas for
.. i18n: resolving this below:
..

If you cannot get OpenERP to work after installing your Windows system you will find some ideas for
resolving this below:

.. i18n: #. Is the OpenERP Server working? Signed in to the server as an administrator, stop and
.. i18n:    restart the service using :guilabel:`Stop Service` and :guilabel:`Start Service` from the menu
.. i18n:    :menuselection:`Start --> Programs --> OpenERP Server` .
.. i18n: 
.. i18n: #. Is the OpenERP Server set up correctly? Signed in to the server as
.. i18n:    Administrator, open the file \ ``openerp-server.conf``\  in \
.. i18n:    ``C:\Program Files\OpenERP AllInOne``\  and check its content. This file is generated during
.. i18n:    installation with information derived from the database. If you see something strange it is best to
.. i18n:    entirely reinstall the server from the demonstration installer rather than try to work out what is
.. i18n:    happening.
..

#. Is the OpenERP Server working? Signed in to the server as an administrator, stop and
   restart the service using :guilabel:`Stop Service` and :guilabel:`Start Service` from the menu
   :menuselection:`Start --> Programs --> OpenERP Server` .

#. Is the OpenERP Server set up correctly? Signed in to the server as
   Administrator, open the file \ ``openerp-server.conf``\  in \
   ``C:\Program Files\OpenERP AllInOne``\  and check its content. This file is generated during
   installation with information derived from the database. If you see something strange it is best to
   entirely reinstall the server from the demonstration installer rather than try to work out what is
   happening.

.. i18n: 	.. figure:: images/terp_server_conf.png
.. i18n: 	   :align: center
.. i18n: 	   :scale: 80
.. i18n: 	          
.. i18n: 	   *Typical OpenERP configuration file*
..

	.. figure:: images/terp_server_conf.png
	   :align: center
	   :scale: 80
	          
	   *Typical OpenERP configuration file*

.. i18n: #. Is your PostgreSQL running? Signed in as administrator, select :guilabel:`Stop Service`
.. i18n:    from the menu :menuselection:`Start --> Programs --> PostgreSQL`.  If after a couple of seconds,
.. i18n:    you read :guilabel:`The PostgreSQL4OpenERP service has stopped` then you can be reasonably sure
.. i18n:    that the database server was working. Restart PostgreSQL.
.. i18n: 	   
.. i18n: #. Is the database accessible? Still in the PostgreSQL menu, start
.. i18n:    the pgAdmin III application which you can use to explore the database. Double-click the \
.. i18n:    ``PostgreSQL4OpenERP``\  connection. 
.. i18n:    You can find the password in the OpenERP server configuration file.
.. i18n:    If the database server is accessible
.. i18n:    you will be able to see some information about the empty database. If it is not, an error message
.. i18n:    will appear.
.. i18n: 
.. i18n: #. Are your client programs correctly installed? If your OpenERP GTK clients have not started,
.. i18n:    the swiftest approach is to reinstall them.
.. i18n: 
.. i18n: #. Can remote client computers see the server computer at all? Check this by opening a command prompt
.. i18n:    window (enter \ ``cmd``\  in the window :menuselection:`Start --> Run...` ) and enter \ ``ping
.. i18n:    <address of server>``\  there (where \ ``<address of server>``\  represents the IP address of the
.. i18n:    server). The server should respond with a reply. 
.. i18n: 
.. i18n: #. Have you changed any of the server's parameters? At this point in the installation the port
.. i18n:    number of the server must be 8069 using the protocol XML-RPC.
.. i18n: 
.. i18n: #. Is there anything else in the server's history that can help you identify the problem? Open the file
.. i18n:    \ ``openerp-server.log``\  in \ ``C:\Program Files\OpenERP AllInOne``\  
.. i18n:    (which you can only do when the server is stopped) and scan through the
.. i18n:    history for ideas. If something looks strange there, contributors to the OpenERP forums can often
.. i18n:    help identify the reason.
..

#. Is your PostgreSQL running? Signed in as administrator, select :guilabel:`Stop Service`
   from the menu :menuselection:`Start --> Programs --> PostgreSQL`.  If after a couple of seconds,
   you read :guilabel:`The PostgreSQL4OpenERP service has stopped` then you can be reasonably sure
   that the database server was working. Restart PostgreSQL.
	   
#. Is the database accessible? Still in the PostgreSQL menu, start
   the pgAdmin III application which you can use to explore the database. Double-click the \
   ``PostgreSQL4OpenERP``\  connection. 
   You can find the password in the OpenERP server configuration file.
   If the database server is accessible
   you will be able to see some information about the empty database. If it is not, an error message
   will appear.

#. Are your client programs correctly installed? If your OpenERP GTK clients have not started,
   the swiftest approach is to reinstall them.

#. Can remote client computers see the server computer at all? Check this by opening a command prompt
   window (enter \ ``cmd``\  in the window :menuselection:`Start --> Run...` ) and enter \ ``ping
   <address of server>``\  there (where \ ``<address of server>``\  represents the IP address of the
   server). The server should respond with a reply. 

#. Have you changed any of the server's parameters? At this point in the installation the port
   number of the server must be 8069 using the protocol XML-RPC.

#. Is there anything else in the server's history that can help you identify the problem? Open the file
   \ ``openerp-server.log``\  in \ ``C:\Program Files\OpenERP AllInOne``\  
   (which you can only do when the server is stopped) and scan through the
   history for ideas. If something looks strange there, contributors to the OpenERP forums can often
   help identify the reason.

.. i18n: .. index::
.. i18n:    single: installation; Linux (Ubuntu)
..

.. index::
   single: installation; Linux (Ubuntu)

.. i18n: Installation on Linux (Ubuntu)
.. i18n: ------------------------------
..

Linux (Ubuntu) 安装
------------------------------

.. i18n: This section guides you through installing the OpenERP server and client on Ubuntu, one of the
.. i18n: most popular Linux distributions. It assumes that you are using a recent release of Desktop Ubuntu
.. i18n: with its graphical user interface on a desktop or laptop PC.
..

This section guides you through installing the OpenERP server and client on Ubuntu, one of the
most popular Linux distributions. It assumes that you are using a recent release of Desktop Ubuntu
with its graphical user interface on a desktop or laptop PC.

.. i18n: .. note:: Other Linux Distributions
.. i18n: 
.. i18n: 	Installation on other distributions of Linux is fairly similar to installation on Ubuntu. Read this
.. i18n: 	section of the book so that you understand the principles, then use the online documentation and
.. i18n: 	the forums for your specific needs on another distribution.
..

.. note:: Other Linux Distributions

	Installation on other distributions of Linux is fairly similar to installation on Ubuntu. Read this
	section of the book so that you understand the principles, then use the online documentation and
	the forums for your specific needs on another distribution.

.. i18n: For information about installation on other distributions, visit the documentation section by
.. i18n: following :menuselection:`Services --> Documentation` on http://www.openerp.com. Detailed instructions
.. i18n: are given there for different distributions and releases, and you should also check if there are
.. i18n: more up to date instructions for the Ubuntu distribution as well.
..

For information about installation on other distributions, visit the documentation section by
following :menuselection:`Services --> Documentation` on http://www.openerp.com. Detailed instructions
are given there for different distributions and releases, and you should also check if there are
more up to date instructions for the Ubuntu distribution as well.

.. i18n: .. To Check
..

.. To Check

.. i18n: .. _installation-ubuntu-9.04:
..

.. _installation-ubuntu-9.04:

.. i18n: Technical Procedure: Initial Installation and Configuration
.. i18n: ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
..

技术过程: 初始化安装和配置
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. i18n: Upgrade of Ubuntu packages and installation of OpenERP and pgadmin::
.. i18n: 
.. i18n:     $ sudo apt-get update
.. i18n: 
.. i18n:     $ sudo apt-get upgrade
.. i18n: 
.. i18n:     $ sudo apt-get install openerp-server openerp-client pgadmin3
..

Upgrade of Ubuntu packages and installation of OpenERP and pgadmin::

    $ sudo apt-get update

    $ sudo apt-get upgrade

    $ sudo apt-get install openerp-server openerp-client pgadmin3

.. i18n: To avoid having some of the labels untranslated in the GTK client, install the language-pack-gnome-YOURLANG-base package. The following command installs the Spanish language pack::
.. i18n: 
.. i18n:     $ sudo apt-get install language-pack-gnome-es-base
..

To avoid having some of the labels untranslated in the GTK client, install the language-pack-gnome-YOURLANG-base package. The following command installs the Spanish language pack::

    $ sudo apt-get install language-pack-gnome-es-base

.. i18n: PostgreSQL version 8.4 has been used at the time of writing. You may have to replace the version number in the
.. i18n: commands below with your own PostgreSQL version number if it differs. Postgres Database configuration::
.. i18n: 
.. i18n:     $ sudo vi /etc/postgresql/8.4/main/pg_hba.conf
..

PostgreSQL version 8.4 has been used at the time of writing. You may have to replace the version number in the
commands below with your own PostgreSQL version number if it differs. Postgres Database configuration::

    $ sudo vi /etc/postgresql/8.4/main/pg_hba.conf

.. i18n: Replace the following line::
.. i18n: 
.. i18n:     # “local” is for Unix domain socket connections only
.. i18n:     local all all ident
..

Replace the following line::

    # “local” is for Unix domain socket connections only
    local all all ident

.. i18n: with::
.. i18n: 
.. i18n:     #”local” is for Unix domain socket connections only
.. i18n:     local all all md5
..

with::

    #”local” is for Unix domain socket connections only
    local all all md5

.. i18n: Restart Postgres::
.. i18n: 
.. i18n:     $ sudo /etc/init.d/postgresql-8.4 restart
.. i18n: 
.. i18n:     * Restarting PostgreSQL 8.4 database server [ OK ]
..

Restart Postgres::

    $ sudo /etc/init.d/postgresql-8.4 restart

    * Restarting PostgreSQL 8.4 database server [ OK ]

.. i18n: The following two commands will avoid problems with /etc/init.d/openerp-web INIT script::
.. i18n: 
.. i18n:     $ sudo mkdir /home/openerp
.. i18n: 
.. i18n:     $ sudo chown openerp.nogroup /home/openerp
..

The following two commands will avoid problems with /etc/init.d/openerp-web INIT script::

    $ sudo mkdir /home/openerp

    $ sudo chown openerp.nogroup /home/openerp

.. i18n: Create a user account called openerp with password “openerp” and with privileges to create Postgres databases::
.. i18n: 
.. i18n:     $ sudo su postgres
.. i18n: 
.. i18n:     $ createuser openerp -P
.. i18n: 
.. i18n:     Enter password for new role: (openerp)
.. i18n: 
.. i18n:     Enter it again:
.. i18n: 
.. i18n:     Shall the new role be a superuser? (y/n) n
.. i18n: 
.. i18n:     Shall the new role be allowed to create databases? (y/n) y
.. i18n: 
.. i18n:     Shall the new role be allowed to create more new roles? (y/n) n
..

Create a user account called openerp with password “openerp” and with privileges to create Postgres databases::

    $ sudo su postgres

    $ createuser openerp -P

    Enter password for new role: (openerp)

    Enter it again:

    Shall the new role be a superuser? (y/n) n

    Shall the new role be allowed to create databases? (y/n) y

    Shall the new role be allowed to create more new roles? (y/n) n

.. i18n: Quit from user postgres::
.. i18n: 
.. i18n:     $ exit
.. i18n: 
.. i18n:     exit
..

Quit from user postgres::

    $ exit

    exit

.. i18n: Edit OpenERP configuration file::
.. i18n: 
.. i18n:     $ sudo vi /etc/openerp-server.conf
..

Edit OpenERP configuration file::

    $ sudo vi /etc/openerp-server.conf

.. i18n: Replace the following two lines (we don’t force to use a specific database and we add the required password to gain access to postgres)::
.. i18n: 
.. i18n:     db_name =
.. i18n: 
.. i18n:     db_user = openerp
.. i18n: 
.. i18n:     db_password = openerp
..

Replace the following two lines (we don’t force to use a specific database and we add the required password to gain access to postgres)::

    db_name =

    db_user = openerp

    db_password = openerp

.. i18n: We can now restart openerp-server::
.. i18n: 
.. i18n:     $ sudo /etc/init.d/openerp-server restart
.. i18n: 
.. i18n:     Restarting openerp-server: openerp-server.
..

We can now restart openerp-server::

    $ sudo /etc/init.d/openerp-server restart

    Restarting openerp-server: openerp-server.

.. i18n: Check out the logs::
.. i18n: 
.. i18n:     $ sudo cat /var/log/openerp.log
.. i18n: 
.. i18n:     [2009-06-14 21:06:39,314] INFO:server:version – 6.0.0
.. i18n: 
.. i18n:     [2009-06-14 21:06:39,314] INFO:server:addons_path – /usr/lib/openerp-server/addons
.. i18n: 
.. i18n:     [2009-06-14 21:06:39,314] INFO:server:database hostname – localhost
.. i18n: 
.. i18n:     [2009-06-14 21:06:39,315] INFO:server:database port – 5432
.. i18n: 
.. i18n:     [2009-06-14 21:06:39,315] INFO:server:database user – openerp
.. i18n: 
.. i18n:     [2009-06-14 21:06:39,315] INFO:objects:initialising distributed objects services
.. i18n: 
.. i18n:     [2009-06-14 21:06:39,502] INFO:web-services:starting XML-RPC services, port 8069
.. i18n: 
.. i18n:     [2009-06-14 21:06:39,502] INFO:web-services:starting NET-RPC service, port 8070
.. i18n: 
.. i18n:     [2009-06-14 21:06:39,502] INFO:web-services:the server is running, waiting for connections…
..

Check out the logs::

    $ sudo cat /var/log/openerp.log

    [2009-06-14 21:06:39,314] INFO:server:version – 6.0.0

    [2009-06-14 21:06:39,314] INFO:server:addons_path – /usr/lib/openerp-server/addons

    [2009-06-14 21:06:39,314] INFO:server:database hostname – localhost

    [2009-06-14 21:06:39,315] INFO:server:database port – 5432

    [2009-06-14 21:06:39,315] INFO:server:database user – openerp

    [2009-06-14 21:06:39,315] INFO:objects:initialising distributed objects services

    [2009-06-14 21:06:39,502] INFO:web-services:starting XML-RPC services, port 8069

    [2009-06-14 21:06:39,502] INFO:web-services:starting NET-RPC service, port 8070

    [2009-06-14 21:06:39,502] INFO:web-services:the server is running, waiting for connections…

.. i18n: OpenERP is now up and running, connected to Postgres database on port 5432 and listening on ports 8069 and 8070
..

OpenERP is now up and running, connected to Postgres database on port 5432 and listening on ports 8069 and 8070

.. i18n: ::
.. i18n: 
.. i18n:     $ ps uaxww | grep -i openerp
.. i18n: 
.. i18n:     openerp      5686  0.0  1.2  84688 26584 pts/7    Sl+  12:36   0:03 /usr/bin/python ./openerp-server.py
..

::

    $ ps uaxww | grep -i openerp

    openerp      5686  0.0  1.2  84688 26584 pts/7    Sl+  12:36   0:03 /usr/bin/python ./openerp-server.py

.. i18n: ::
.. i18n: 
.. i18n:     $ sudo lsof -i :8069
.. i18n: 
.. i18n:     COMMAND  PID USER    FD   TYPE DEVICE SIZE/OFF NODE NAME
.. i18n:     
.. i18n:     python  5686 openerp 3u  IPv4 116555      0t0  TCP *:8069 (LISTEN)
..

::

    $ sudo lsof -i :8069

    COMMAND  PID USER    FD   TYPE DEVICE SIZE/OFF NODE NAME
    
    python  5686 openerp 3u  IPv4 116555      0t0  TCP *:8069 (LISTEN)

.. i18n: ::
.. i18n: 
.. i18n:     $ sudo lsof -i :8070
.. i18n: 
.. i18n:     COMMAND  PID USER    FD   TYPE DEVICE SIZE/OFF NODE NAME
.. i18n:     
.. i18n:     python  5686 openerp 5u  IPv4 116563      0t0  TCP *:8070 (LISTEN)
..

::

    $ sudo lsof -i :8070

    COMMAND  PID USER    FD   TYPE DEVICE SIZE/OFF NODE NAME
    
    python  5686 openerp 5u  IPv4 116563      0t0  TCP *:8070 (LISTEN)

.. i18n: Start the OpenERP GTK client by clicking its icon in the :menuselection:`Applications --> Internet
.. i18n: --> OpenERP Client`  menu,
.. i18n: or by opening a terminal window and typing \ ``openerp-client``\  . The OpenERP login dialog box
.. i18n: should open and show the message :guilabel:`No database found you must create one!`.
..

Start the OpenERP GTK client by clicking its icon in the :menuselection:`Applications --> Internet
--> OpenERP Client`  menu,
or by opening a terminal window and typing \ ``openerp-client``\  . The OpenERP login dialog box
should open and show the message :guilabel:`No database found you must create one!`.

.. i18n: Although this installation method is simple and therefore an attractive option, it is better to
.. i18n: install OpenERP using a version downloaded from http://openerp.com. The downloaded revision is
.. i18n: likely to be far more up to date than that available from a Linux distribution.
..

Although this installation method is simple and therefore an attractive option, it is better to
install OpenERP using a version downloaded from http://openerp.com. The downloaded revision is
likely to be far more up to date than that available from a Linux distribution.

.. i18n: .. note:: Package Versions
.. i18n: 
.. i18n: 	Maintaining packages is a process of development, testing and publication that takes time. The
.. i18n: 	releases in OpenERP packages are therefore not always the latest available. Check
.. i18n: 	the version number from the information on the website before installing a package. If only the
.. i18n: 	third digit group differs (for example 6.0.1 instead of 6.0.2) then you may decide to install it because
.. i18n: 	the differences may be minor – bug fixes rather than functionality changes between the package
.. i18n: 	and the latest version.
.. i18n: 	
.. i18n: 	
.. i18n: Manual Installation of the OpenERP Server
.. i18n: ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
..

.. note:: Package Versions

	Maintaining packages is a process of development, testing and publication that takes time. The
	releases in OpenERP packages are therefore not always the latest available. Check
	the version number from the information on the website before installing a package. If only the
	third digit group differs (for example 6.0.1 instead of 6.0.2) then you may decide to install it because
	the differences may be minor – bug fixes rather than functionality changes between the package
	and the latest version.
	
	
手动安装 OpenERP Server
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. i18n: In this section you will see how to install OpenERP by downloading it from the site
.. i18n: http://openerp.com, and how to install the libraries and packages that OpenERP depends on, onto a
.. i18n: desktop version of Ubuntu. Here is a summary of the procedure:
..

In this section you will see how to install OpenERP by downloading it from the site
http://openerp.com, and how to install the libraries and packages that OpenERP depends on, onto a
desktop version of Ubuntu. Here is a summary of the procedure:

.. i18n: #. Navigate to the page http://openerp.com with your web browser,
.. i18n: 
.. i18n: #. Click the :menuselection:`Download` button on the right side,
.. i18n: 
.. i18n: #. Download the client and server files from the *Sources* section into your home directory
.. i18n:    (or some other location if you have defined a different download area).
..

#. Navigate to the page http://openerp.com with your web browser,

#. Click the :menuselection:`Download` button on the right side,

#. Download the client and server files from the *Sources* section into your home directory
   (or some other location if you have defined a different download area).

.. i18n: To download the PostgreSQL database and all of the other dependencies for OpenERP from packages:
..

To download the PostgreSQL database and all of the other dependencies for OpenERP from packages:

.. i18n: #. Start Synaptic Package Manager, and enter the root password as required.
.. i18n: 
.. i18n: #. Check that the repositories \ ``main`` \, \ ``universe`` \ and \ ``restricted`` \  are enabled.
.. i18n: 
.. i18n: #. Search for a recent version of PostgreSQL (such as \ ``postgresql-8.4``\   then select it for
.. i18n:    installation along with its dependencies.
.. i18n: 
.. i18n: #. Select all of OpenERP's dependencies, an up-to-date list of which should be
.. i18n:    found in the installation documents on OpenERP's website,
.. i18n:    then click :guilabel:`Apply` to install them.
..

#. Start Synaptic Package Manager, and enter the root password as required.

#. Check that the repositories \ ``main`` \, \ ``universe`` \ and \ ``restricted`` \  are enabled.

#. Search for a recent version of PostgreSQL (such as \ ``postgresql-8.4``\   then select it for
   installation along with its dependencies.

#. Select all of OpenERP's dependencies, an up-to-date list of which should be
   found in the installation documents on OpenERP's website,
   then click :guilabel:`Apply` to install them.

.. i18n: .. index::
.. i18n:    single: Python
..

.. index::
   single: Python

.. i18n: .. note::  Python Programming Language
.. i18n: 
.. i18n: 	Python is the programming language that has been used to develop OpenERP. It is a dynamic, non-typed
.. i18n: 	language that is object-oriented, procedural and functional. It comes with numerous libraries that
.. i18n: 	provide interfaces to other languages and has the great advantage that it can be learnt in only a
.. i18n: 	few days. It is the language of choice for large parts of NASA's, Google's and many other
.. i18n: 	enterprises' code.
.. i18n: 
.. i18n: 	For more information on Python, explore http://www.python.org.
..

.. note::  Python Programming Language

	Python is the programming language that has been used to develop OpenERP. It is a dynamic, non-typed
	language that is object-oriented, procedural and functional. It comes with numerous libraries that
	provide interfaces to other languages and has the great advantage that it can be learnt in only a
	few days. It is the language of choice for large parts of NASA's, Google's and many other
	enterprises' code.

	For more information on Python, explore http://www.python.org.

.. i18n: Once all these dependencies and the database are installed, install the server itself using the
.. i18n: instructions on the website.
..

Once all these dependencies and the database are installed, install the server itself using the
instructions on the website.

.. i18n: Open a terminal window to start the server with the command :command:`openerp-server`, which
.. i18n: should result in a series of log messages as the server starts up. If the server
.. i18n: is correctly installed, the message :guilabel:`[...] waiting for connections...` should show within 30
.. i18n: seconds or so, which indicates that the server is waiting for a client to connect to it.
..

Open a terminal window to start the server with the command :command:`openerp-server`, which
should result in a series of log messages as the server starts up. If the server
is correctly installed, the message :guilabel:`[...] waiting for connections...` should show within 30
seconds or so, which indicates that the server is waiting for a client to connect to it.

.. i18n: .. figure:: images/terps_startup_log.png
.. i18n:    :align: center
.. i18n:    :scale: 75
.. i18n:    
.. i18n:    *OpenERP startup log in the console*
..

.. figure:: images/terps_startup_log.png
   :align: center
   :scale: 75
   
   *OpenERP startup log in the console*

.. i18n: .. index::
.. i18n:    single: client; GTK
.. i18n:    single: installation; GTK client
..

.. index::
   single: client; GTK
   single: installation; GTK client

.. i18n: Manual Installation of OpenERP GTK Clients
.. i18n: ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
..

手动安装 OpenERP GTK 客户端
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. i18n: To install an OpenERP GTK client, follow the steps outlined in the website installation document for
.. i18n: your particular operating system.
..

To install an OpenERP GTK client, follow the steps outlined in the website installation document for
your particular operating system.

.. i18n: .. figure:: images/terp_client_startup.png
.. i18n:    :align: center
.. i18n:    :scale: 75
.. i18n:    
.. i18n:    *OpenERP client at startup*
..

.. figure:: images/terp_client_startup.png
   :align: center
   :scale: 75
   
   *OpenERP client at startup*

.. i18n: Open a terminal window to start the client using the command :command:`openerp-client`. When you start the
.. i18n: client on the same Linux PC as the server you will find that the default connection parameters will
.. i18n: just work without needing any change. The message :guilabel:`No database found, you must create
.. i18n: one!`  shows you that the connection to the server has been successful and you need to create a
.. i18n: database on the server.
..

Open a terminal window to start the client using the command :command:`openerp-client`. When you start the
client on the same Linux PC as the server you will find that the default connection parameters will
just work without needing any change. The message :guilabel:`No database found, you must create
one!`  shows you that the connection to the server has been successful and you need to create a
database on the server.

.. i18n: Creating the Database
.. i18n: ^^^^^^^^^^^^^^^^^^^^^
..

创建数据库
^^^^^^^^^^^^^^^^^^^^^

.. i18n: You can connect other GTK clients over the network to your Linux server. Before you leave your
.. i18n: server, make sure you know its network address – either by its name (such as \
.. i18n: ``mycomputer.mycompany.net``\  ) or its IP address (such as \ ``192.168.0.123``\  ).
..

You can connect other GTK clients over the network to your Linux server. Before you leave your
server, make sure you know its network address – either by its name (such as \
``mycomputer.mycompany.net``\  ) or its IP address (such as \ ``192.168.0.123``\  ).

.. i18n: .. index::
.. i18n:    single: port (network)
..

.. index::
   single: port (network)

.. i18n: .. note:: Different Networks
.. i18n: 
.. i18n: 	Communications between an OpenERP client and server are based on standard protocols. You can
.. i18n: 	connect Windows clients to a Linux server, or vice versa, without problems. It is the same for Mac
.. i18n: 	versions of OpenERP – you can connect Windows and Linux clients and servers to them.
..

.. note:: Different Networks

	Communications between an OpenERP client and server are based on standard protocols. You can
	connect Windows clients to a Linux server, or vice versa, without problems. It is the same for Mac
	versions of OpenERP – you can connect Windows and Linux clients and servers to them.

.. i18n: To install an OpenERP client on a computer under Linux, repeat the procedure shown earlier in this
.. i18n: section. You can connect different clients to the OpenERP server by modifying the connection
.. i18n: parameters on each client. To do that, click the :guilabel:`Change` button in the connection dialog
.. i18n: and set the following fields as needed:
..

To install an OpenERP client on a computer under Linux, repeat the procedure shown earlier in this
section. You can connect different clients to the OpenERP server by modifying the connection
parameters on each client. To do that, click the :guilabel:`Change` button in the connection dialog
and set the following fields as needed:

.. i18n: *  :guilabel:`Server` : \ ``name``\   or  \ ``IP address``\   of the server over the network,
.. i18n: 
.. i18n: *  :guilabel:`Port` : the port, whose default is \ ``8069``\   or  \ ``8070``\ ,
.. i18n: 
.. i18n: *  :guilabel:`Connection protocol` : \ ``XML-RPC``\   or  \ ``NET-RPC``\  .
..

*  :guilabel:`Server` : \ ``name``\   or  \ ``IP address``\   of the server over the network,

*  :guilabel:`Port` : the port, whose default is \ ``8069``\   or  \ ``8070``\ ,

*  :guilabel:`Connection protocol` : \ ``XML-RPC``\   or  \ ``NET-RPC``\  .

.. i18n: .. figure:: images/terp_client_server.png
.. i18n:    :align: center
.. i18n:    :scale: 75
.. i18n: 
.. i18n:    *Dialog box for defining connection parameters to the server*
..

.. figure:: images/terp_client_server.png
   :align: center
   :scale: 75

   *Dialog box for defining connection parameters to the server*

.. i18n: It is possible to connect the server to the client using a secure protocol to prevent other network
.. i18n: users from listening in, but the installation described here is for direct unencrypted connection.
..

It is possible to connect the server to the client using a secure protocol to prevent other network
users from listening in, but the installation described here is for direct unencrypted connection.

.. i18n: If your Linux server is protected by a firewall you will have to provide access to port 
.. i18n:  \ ``8069`` \ or \ ``8070`` \ for users on other computers with OpenERP GTK clients.
..

If your Linux server is protected by a firewall you will have to provide access to port 
 \ ``8069`` \ or \ ``8070`` \ for users on other computers with OpenERP GTK clients.

.. i18n: .. _fig-webwel:
.. i18n: 
.. i18n: .. figure:: images/web_welcome.png
.. i18n:    :scale: 70
.. i18n:    :align: center
.. i18n: 
.. i18n:    *OpenERP web client at startup*
..

.. _fig-webwel:

.. figure:: images/web_welcome.png
   :scale: 70
   :align: center

   *OpenERP web client at startup*

.. i18n: You can verify the installation by opening a web browser on the server and navigating to
.. i18n: http://localhost:8069 to connect to the OpenERP web version as shown in the figure :ref:`fig-webwel`. 
.. i18n: You can also test this from
.. i18n: another computer connected to the same network if you know the name or IP address of the server over
.. i18n: the network – your browser should be set to http://<server_address>:8069 for this.
..

You can verify the installation by opening a web browser on the server and navigating to
http://localhost:8069 to connect to the OpenERP web version as shown in the figure :ref:`fig-webwel`. 
You can also test this from
another computer connected to the same network if you know the name or IP address of the server over
the network – your browser should be set to http://<server_address>:8069 for this.

.. i18n: Verifying your Linux Installation
.. i18n: ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
..

检查您的 Linux 安装
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. i18n: .. index::
.. i18n:    single: pgAdmin III
..

.. index::
   single: pgAdmin III

.. i18n: You have used default parameters so far during the installation of the various components.
.. i18n: If you have had problems, or you just want to set this up differently,
.. i18n: the following points provide some indicators about how you can set up your installation.
..

You have used default parameters so far during the installation of the various components.
If you have had problems, or you just want to set this up differently,
the following points provide some indicators about how you can set up your installation.

.. i18n: .. tip:: **psql** and **pgAdmin** tools
.. i18n: 
.. i18n: 	psql is a simple client, executed from the command line, that is delivered with PostgreSQL. It
.. i18n: 	enables you to execute SQL commands on your OpenERP database.
.. i18n: 
.. i18n: 	If you prefer a graphical utility to manipulate your database directly you can install pgAdmin III
.. i18n: 	(it is commonly installed automatically with PostgreSQL on a windowing system, but can also be
.. i18n: 	found at \ ``http://www.pgadmin.org/`` \ ).
..

.. tip:: **psql** and **pgAdmin** tools

	psql is a simple client, executed from the command line, that is delivered with PostgreSQL. It
	enables you to execute SQL commands on your OpenERP database.

	If you prefer a graphical utility to manipulate your database directly you can install pgAdmin III
	(it is commonly installed automatically with PostgreSQL on a windowing system, but can also be
	found at \ ``http://www.pgadmin.org/`` \ ).

.. i18n: .. To check pts 4 and 7
..

.. To check pts 4 and 7

.. i18n: #.	The PostgreSQL database starts automatically and listens locally on port 5432 as standard: check
.. i18n: 	this by entering \ ``sudo netstat -anpt``\  at a terminal to see if port 5432 is visible there.
.. i18n: 
.. i18n: #.	The database system has a default role of \ ``postgres``\   accessible by running under the Linux
.. i18n: 	postgres user: check this by entering \ ``sudo su postgres -c psql``\  at a terminal to see the psql
.. i18n: 	startup message – then type \ ``\q``\  to quit the program.
.. i18n: 
.. i18n: #.	If you try to start the OpenERP server from a terminal but get the message ``socket.error: (98,
.. i18n: 	'Address already in use')`` then you might be trying to start OpenERP while an instance of
.. i18n: 	OpenERP is already running and using the sockets that you have defined (by default 8069 and 8070).
.. i18n: 	If that is a surprise to you then you may be coming up against a previous installation of OpenERP
.. i18n: 	or Tiny ERP, or something else using one or both of those ports. 
.. i18n: 	
.. i18n: 	Type \ ``sudo netstat -anpt``\  to
.. i18n: 	discover what is running there, and record the PID. You can check that the PID corresponds to a
.. i18n: 	program you can dispense with by typing \ ``ps aux | grep <PID>``\   and you can then stop the
.. i18n: 	program from running by typing \ ``sudo kill <PID>``\ .  You need additional measures to stop it from
.. i18n: 	restarting when you restart the server.
.. i18n: 
.. i18n: #.	The OpenERP server has a large number of configuration options. You can see what they are by
.. i18n: 	starting the server with the argument \ ``–help``\ .   By default the server configuration is stored
.. i18n: 	in the file \ ``.terp_serverrc``\  in the user's home directory (and for the postgres user that
.. i18n: 	directory is \ ``/var/lib/postgresql``\  .
.. i18n: 
.. i18n: #.	You can delete the configuration file to be quite sure that the OpenERP server is starting with
.. i18n: 	just the default options. It is quite common for an upgraded system to behave badly because a new
.. i18n: 	version server cannot work with options from a previous version. When the server starts without a
.. i18n: 	configuration file it will write a new one once there is something non-default to write to it – it
.. i18n: 	will operate using defaults until then.
.. i18n: 
.. i18n: #.	To verify that the system works, without becoming entangled in firewall problems, you can start
.. i18n: 	the OpenERP client from a second terminal window on the server computer (which does not pass
.. i18n: 	through the firewall). Connect using the XML-RPC protocol on port 8069 or NET-RPC on port 8070. The
.. i18n: 	server can use both ports simultaneously. The window displays the log file when the client is
.. i18n: 	started this way.
.. i18n: 
.. i18n: #.	The client setup is stored in the file \ ``.terprc``\  in the user's home directory.
.. i18n: 	Since a GTK client can be started by any user, each user would have their setup defined in a
.. i18n: 	configuration file in their own home directory.
.. i18n: 
.. i18n: #.	You can delete the configuration file to be quite sure that the OpenERP client is starting with
.. i18n: 	just the default options. When the client starts without a configuration file it will write a new
.. i18n: 	one for itself.
.. i18n: 
.. i18n: #.	The web server uses the NET-RPC protocol. If a GTK client works but the web server does not, then the
.. i18n: 	problem is either with the NET-RPC port or with the web server itself, and not with the OpenERP server.
..

#.	The PostgreSQL database starts automatically and listens locally on port 5432 as standard: check
	this by entering \ ``sudo netstat -anpt``\  at a terminal to see if port 5432 is visible there.

#.	The database system has a default role of \ ``postgres``\   accessible by running under the Linux
	postgres user: check this by entering \ ``sudo su postgres -c psql``\  at a terminal to see the psql
	startup message – then type \ ``\q``\  to quit the program.

#.	If you try to start the OpenERP server from a terminal but get the message ``socket.error: (98,
	'Address already in use')`` then you might be trying to start OpenERP while an instance of
	OpenERP is already running and using the sockets that you have defined (by default 8069 and 8070).
	If that is a surprise to you then you may be coming up against a previous installation of OpenERP
	or Tiny ERP, or something else using one or both of those ports. 
	
	Type \ ``sudo netstat -anpt``\  to
	discover what is running there, and record the PID. You can check that the PID corresponds to a
	program you can dispense with by typing \ ``ps aux | grep <PID>``\   and you can then stop the
	program from running by typing \ ``sudo kill <PID>``\ .  You need additional measures to stop it from
	restarting when you restart the server.

#.	The OpenERP server has a large number of configuration options. You can see what they are by
	starting the server with the argument \ ``–help``\ .   By default the server configuration is stored
	in the file \ ``.terp_serverrc``\  in the user's home directory (and for the postgres user that
	directory is \ ``/var/lib/postgresql``\  .

#.	You can delete the configuration file to be quite sure that the OpenERP server is starting with
	just the default options. It is quite common for an upgraded system to behave badly because a new
	version server cannot work with options from a previous version. When the server starts without a
	configuration file it will write a new one once there is something non-default to write to it – it
	will operate using defaults until then.

#.	To verify that the system works, without becoming entangled in firewall problems, you can start
	the OpenERP client from a second terminal window on the server computer (which does not pass
	through the firewall). Connect using the XML-RPC protocol on port 8069 or NET-RPC on port 8070. The
	server can use both ports simultaneously. The window displays the log file when the client is
	started this way.

#.	The client setup is stored in the file \ ``.terprc``\  in the user's home directory.
	Since a GTK client can be started by any user, each user would have their setup defined in a
	configuration file in their own home directory.

#.	You can delete the configuration file to be quite sure that the OpenERP client is starting with
	just the default options. When the client starts without a configuration file it will write a new
	one for itself.

#.	The web server uses the NET-RPC protocol. If a GTK client works but the web server does not, then the
	problem is either with the NET-RPC port or with the web server itself, and not with the OpenERP server.

.. i18n: .. 	hint:: One Server for Several Companies
.. i18n: 
.. i18n: 	You can start several OpenERP application servers on one physical computer server by using
.. i18n: 	different ports. If you have defined multiple database roles in PostgreSQL, each connected through
.. i18n: 	an OpenERP instance to a different port, you can simultaneously serve many companies from one
.. i18n: 	physical server at one time.
..

.. 	hint:: One Server for Several Companies

	You can start several OpenERP application servers on one physical computer server by using
	different ports. If you have defined multiple database roles in PostgreSQL, each connected through
	an OpenERP instance to a different port, you can simultaneously serve many companies from one
	physical server at one time.

.. i18n: .. Copyright © Open Object Press. All rights reserved.
..

.. Copyright © Open Object Press. All rights reserved.

.. i18n: .. You may take electronic copy of this publication and distribute it if you don't
.. i18n: .. change the content. You can also print a copy to be read by yourself only.
..

.. You may take electronic copy of this publication and distribute it if you don't
.. change the content. You can also print a copy to be read by yourself only.

.. i18n: .. We have contracts with different publishers in different countries to sell and
.. i18n: .. distribute paper or electronic based versions of this book (translated or not)
.. i18n: .. in bookstores. This helps to distribute and promote the OpenERP product. It
.. i18n: .. also helps us to create incentives to pay contributors and authors using author
.. i18n: .. rights of these sales.
..

.. We have contracts with different publishers in different countries to sell and
.. distribute paper or electronic based versions of this book (translated or not)
.. in bookstores. This helps to distribute and promote the OpenERP product. It
.. also helps us to create incentives to pay contributors and authors using author
.. rights of these sales.

.. i18n: .. Due to this, grants to translate, modify or sell this book are strictly
.. i18n: .. forbidden, unless Tiny SPRL (representing Open Object Press) gives you a
.. i18n: .. written authorisation for this.
..

.. Due to this, grants to translate, modify or sell this book are strictly
.. forbidden, unless Tiny SPRL (representing Open Object Press) gives you a
.. written authorisation for this.

.. i18n: .. Many of the designations used by manufacturers and suppliers to distinguish their
.. i18n: .. products are claimed as trademarks. Where those designations appear in this book,
.. i18n: .. and Open Object Press was aware of a trademark claim, the designations have been
.. i18n: .. printed in initial capitals.
..

.. Many of the designations used by manufacturers and suppliers to distinguish their
.. products are claimed as trademarks. Where those designations appear in this book,
.. and Open Object Press was aware of a trademark claim, the designations have been
.. printed in initial capitals.

.. i18n: .. While every precaution has been taken in the preparation of this book, the publisher
.. i18n: .. and the authors assume no responsibility for errors or omissions, or for damages
.. i18n: .. resulting from the use of the information contained herein.
..

.. While every precaution has been taken in the preparation of this book, the publisher
.. and the authors assume no responsibility for errors or omissions, or for damages
.. resulting from the use of the information contained herein.

.. i18n: .. Published by Open Object Press, Grand Rosière, Belgium
..

.. Published by Open Object Press, Grand Rosière, Belgium
