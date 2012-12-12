
The Installation of OpenERP
===========================

Whether you are from a small company investigating how OpenERP works, or you are part of the IT staff of a
larger organization and have been asked to assess OpenERP's capabilities, your first requirement
is to install it or to find a working installation.

The table below summarizes the various installation methods that will be described in the following
sections.

.. csv-table:: Comparison of the different methods of installation on Windows or Linux
   :header: "Method","Average Time","Level of Complexity","Notes"
   :widths: 20,15,15,30

   "OpenERP Demo","No installation","Simple","Very useful for quick evaluations because no need to install anything."
   "All-in-one Windows Installer","A few minutes","Simple","Very useful for quick evaluations because it installs all of the components pre-configured on one computer (using the GTK client)."
   "Independent installation on Windows","Half an hour","Medium","Enables you to install the components on different computers. Can be put into production use."
   "Ubuntu Linux packages","A few minutes","Simple","Simple and quick but the Ubuntu packages are not always up to date."
   "From source, for all Linux systems","More than half an hour","Medium to slightly difficult","This is the method recommended for production environments because it is easy to keep it up to date."

Each time a new release of OpenERP is made, OpenERP supplies a complete Windows auto-installer for
it. This contains all of the components you need – the PostgreSQL database server, the OpenERP
application server and the GTK application client.

This auto-installer enables you to install the whole system in just a few mouse clicks. The initial
configuration is set up during installation, making it possible to start using it very quickly as
long as you do not want to change the underlying code. It is aimed at the installation of everything
on a single PC, but you can later connect GTK clients from other PCs, Macs and Linux boxes to it as
well.

The first step is to download the OpenERP installer. At this stage you must choose which version
to install – the stable version or the development version. If you are planning to put it straight
into production we strongly advise you to choose the stable version.

.. index::
   single: stable versions

.. note::  Stable Versions and Development Versions

	OpenERP development proceeds in two parallel tracks: stable versions and development versions.

	New functionality is integrated into the development branch. This branch is more advanced than the
	stable branch, but it can contain undiscovered and unfixed faults. A new development release is
	made every month or so, and OpenERP has made the code repository available so you can download the
	very latest revisions if you want.

	The stable branch is designed for production environments. Releases of new functionality there are
	made only about once a year after a long period of testing and validation. Only bug fixes are
	released through the year on the stable branch.

.. index::
   single: installation; Windows (all-in-one)

To download the version of OpenERP for Windows, follow these steps:

#. Navigate to the site http://openerp.com.

#. Click the :menuselection:`Downloads` button at the right, then, under :guilabel:`Windows Auto-Installer`, select
   :menuselection:`All-in-One`.

#. This brings up the demonstration version Windows installer, 
   currently :program:`openerp-allinone-setup-6.0.0`.

#. Save the file on your PC - it is quite a substantial size because it downloads everything including
   the PostgreSQL database system, so it will take some time.

.. index::
   single:  installation; administrator

To install OpenERP and its database, you must be signed in as an Administrator on your PC. Double-
click the installer file to install it and accept the default parameters on each dialog box as you go. 

If you had previously tried to install the all-in-one version of OpenERP, you will have to uninstall
that first, because various elements of a previous installation could interfere with your new installation.
Make sure that all Tiny ERP, OpenERP and PostgreSQL applications are removed:
you are likely to have to restart your PC to finish removing all traces of them.

The OpenERP client can be opened, ready to use the OpenERP system, once you have completed 
the all-in-one installation. The next step consists
of setting up the database, and is covered in the final section of this chapter :ref:`sect-creatingdb`.

.. index::
   single: installation; Windows (independent)

Independent Installation on Windows
-----------------------------------

System administrators can have very good reasons for wanting to install the various components of a
Windows installation separately. For example, your company may not support the version of PostgreSQL
or Python that is installed automatically, or you may already have PostgreSQL installed on the server
you are using, or you may want to install the database server, application server and web server on
separate hardware units.

For this situation, you can get separate installers for the OpenERP server and client from the same
location as the all-in-one auto-installer. You will also have to download and install a suitable
version of PostgreSQL independently.

You must install PostgreSQL before the OpenERP server, and you must also set it up with a user
and password so that the OpenERP server can connect to it. OpenERP's web-based documentation gives
full and current details.

Connecting Users on Other PCs to the OpenERP Server
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

To connect other computers to the OpenERP server, you must set the server up so that it is
visible to the other PCs, and install a GTK client on each of those PCs:

#. Make your OpenERP server visible to other PCs by opening the Windows Firewall in the Control
   Panel, then ask the firewall to make an exception of the OpenERP server. In the
   :guilabel:`Exceptions` tab of Windows Firewall click :guilabel:`Add a program...` and choose
   :guilabel:`OpenERP Server` in the list provided. This step enables other computers to see the
   OpenERP application on this server.

#. Install the OpenERP client (:program:`openerp-client-6.X.exe`), which you can download in the
   same way as you downloaded the other OpenERP software, onto the other PCs.

.. tip:: Version Matching

	You must make sure that the version of the client matches that of the server. The version number is
	given as part of the name of the downloaded file. Although it is possible that some different
	revisions of client and server will function together, there is no certainty about that.

.. index::
   single:  administrator

To run the client installer on every other PC you will need to have administrator rights there. The
installation is automated, so you just need follow the different installation steps.

To test your installation, start by connecting through the OpenERP client on the server machine
while you are still logged in as administrator.

.. note:: Why sign in as a PC Administrator?

	You would not usually be signed in as a PC administrator when you are just running the OpenERP client,
	but if there have been problems in the installation it is easier to remain as an administrator after
	the installation so that you can make any necessary fixes than to switch users as you alternate
	between roles as a tester and a software installer.

Start the GTK client on the server through the Windows Start menu there. The main client window
appears, identifying the server you are connected to (which is \ ``localhost``\   – your own server
PC – by default). If the message :guilabel:`No database found, you must create one` appears then
you have **successfully connected** to an OpenERP server containing, as yet, no databases.

.. figure:: images/new_login_dlg.png
   :align: center
   :scale: 75

   *Dialog box on connecting a GTK client to a new OpenERP server*

.. index::
   single: protocol; XML-RPC
   single: protocol; NET-RPC
   single: XML-RPC
   single: NET-RPC

.. note:: Connection Modes

	In its default configuration at the time of writing, 
	the OpenERP client connects to port 8069 on the server using the
	XML-RPC protocol (from Linux) or port 8070 using the NET-RPC protocol instead (from Windows).
	You can use any protocol from either operating system.
	NET-RPC is quite a bit quicker, although you may not notice that on the GTK client in normal use.
	OpenERP can run XML-RPC, but not NET-RPC, as a secure connection.
	
Resolving Errors with a Windows Installation
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

If you cannot get OpenERP to work after installing your Windows system you will find some ideas for
resolving this below:

#. Is the OpenERP Server working? Signed in to the server as an administrator, stop and
   restart the service using :guilabel:`Stop Service` and :guilabel:`Start Service` from the menu
   :menuselection:`Start --> Programs --> OpenERP Server` .

#. Is the OpenERP Server set up correctly? Signed in to the server as
   Administrator, open the file \ ``openerp-server.conf``\  in \
   ``C:\Program Files\OpenERP AllInOne``\  and check its content. This file is generated during
   installation with information derived from the database. If you see something strange it is best to
   entirely reinstall the server from the demonstration installer rather than try to work out what is
   happening.

	.. figure:: images/terp_server_conf.png
	   :align: center
	   :scale: 80
	          
	   *Typical OpenERP configuration file*

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
   \ ``openerp-server.log``\  in \ ``C:\Program Files\OpenERP AllInOne``\  
   (which you can only do when the server is stopped) and scan through the
   history for ideas. If something looks strange there, contributors to the OpenERP forums can often
   help identify the reason.

.. index::
   single: installation; Linux (Ubuntu)

Installation on Linux (Ubuntu)
------------------------------

This section guides you through installing the OpenERP server and client on Ubuntu, one of the
most popular Linux distributions. It assumes that you are using a recent release of Desktop Ubuntu
with its graphical user interface on a desktop or laptop PC.

.. note:: Other Linux Distributions

	Installation on other distributions of Linux is fairly similar to installation on Ubuntu. Read this
	section of the book so that you understand the principles, then use the online documentation and
	the forums for your specific needs on another distribution.

For information about installation on other distributions, visit the documentation section by
following :menuselection:`Services --> Documentation` on http://www.openerp.com. Detailed instructions
are given there for different distributions and releases, and you should also check if there are
more up to date instructions for the Ubuntu distribution as well.

.. To Check

.. _installation-ubuntu-9.04:

Technical Procedure: Initial Installation and Configuration
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Upgrade of Ubuntu packages and installation of OpenERP and pgadmin::

    $ sudo apt-get update

    $ sudo apt-get upgrade

    $ sudo apt-get install openerp-server openerp-client pgadmin3

To avoid having some of the labels untranslated in the GTK client, install the language-pack-gnome-YOURLANG-base package. The following command installs the Spanish language pack::

    $ sudo apt-get install language-pack-gnome-es-base

PostgreSQL version 8.4 has been used at the time of writing. You may have to replace the version number in the
commands below with your own PostgreSQL version number if it differs. Postgres Database configuration::

    $ sudo vi /etc/postgresql/8.4/main/pg_hba.conf

Replace the following line::

    # “local” is for Unix domain socket connections only
    local all all ident

with::

    #”local” is for Unix domain socket connections only
    local all all md5

Restart Postgres::

    $ sudo /etc/init.d/postgresql-8.4 restart

    * Restarting PostgreSQL 8.4 database server [ OK ]

The following two commands will avoid problems with /etc/init.d/openerp-web INIT script::

    $ sudo mkdir /home/openerp

    $ sudo chown openerp.nogroup /home/openerp

Create a user account called openerp with password “openerp” and with privileges to create Postgres databases::

    $ sudo su postgres

    $ createuser openerp -P

    Enter password for new role: (openerp)

    Enter it again:

    Shall the new role be a superuser? (y/n) n

    Shall the new role be allowed to create databases? (y/n) y

    Shall the new role be allowed to create more new roles? (y/n) n

Quit from user postgres::

    $ exit

    exit

Edit OpenERP configuration file::

    $ sudo vi /etc/openerp-server.conf

Replace the following two lines (we don’t force to use a specific database and we add the required password to gain access to postgres)::

    db_name =

    db_user = openerp

    db_password = openerp

We can now restart openerp-server::

    $ sudo /etc/init.d/openerp-server restart

    Restarting openerp-server: openerp-server.

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

OpenERP is now up and running, connected to Postgres database on port 5432 and listening on ports 8069 and 8070

::

    $ ps uaxww | grep -i openerp

    openerp      5686  0.0  1.2  84688 26584 pts/7    Sl+  12:36   0:03 /usr/bin/python ./openerp-server.py

::

    $ sudo lsof -i :8069

    COMMAND  PID USER    FD   TYPE DEVICE SIZE/OFF NODE NAME
    
    python  5686 openerp 3u  IPv4 116555      0t0  TCP *:8069 (LISTEN)


::

    $ sudo lsof -i :8070

    COMMAND  PID USER    FD   TYPE DEVICE SIZE/OFF NODE NAME
    
    python  5686 openerp 5u  IPv4 116563      0t0  TCP *:8070 (LISTEN)

Start the OpenERP GTK client by clicking its icon in the :menuselection:`Applications --> Internet
--> OpenERP Client`  menu,
or by opening a terminal window and typing \ ``openerp-client``\  . The OpenERP login dialog box
should open and show the message :guilabel:`No database found you must create one!`.

Although this installation method is simple and therefore an attractive option, it is better to
install OpenERP using a version downloaded from http://openerp.com. The downloaded revision is
likely to be far more up to date than that available from a Linux distribution.

.. note:: Package Versions

	Maintaining packages is a process of development, testing and publication that takes time. The
	releases in OpenERP packages are therefore not always the latest available. Check
	the version number from the information on the website before installing a package. If only the
	third digit group differs (for example 6.0.1 instead of 6.0.2) then you may decide to install it because
	the differences may be minor – bug fixes rather than functionality changes between the package
	and the latest version.
	
	
Manual Installation of the OpenERP Server
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

In this section you will see how to install OpenERP by downloading it from the site
http://openerp.com, and how to install the libraries and packages that OpenERP depends on, onto a
desktop version of Ubuntu. Here is a summary of the procedure:

#. Navigate to the page http://openerp.com with your web browser,

#. Click the :menuselection:`Download` button on the right side,

#. Download the client and server files from the *Sources* section into your home directory
   (or some other location if you have defined a different download area).

To download the PostgreSQL database and all of the other dependencies for OpenERP from packages:

#. Start Synaptic Package Manager, and enter the root password as required.

#. Check that the repositories \ ``main`` \, \ ``universe`` \ and \ ``restricted`` \  are enabled.

#. Search for a recent version of PostgreSQL (such as \ ``postgresql-8.4``\   then select it for
   installation along with its dependencies.

#. Select all of OpenERP's dependencies, an up-to-date list of which should be
   found in the installation documents on OpenERP's website,
   then click :guilabel:`Apply` to install them.

.. index::
   single: Python

.. note::  Python Programming Language

	Python is the programming language that has been used to develop OpenERP. It is a dynamic, non-typed
	language that is object-oriented, procedural and functional. It comes with numerous libraries that
	provide interfaces to other languages and has the great advantage that it can be learnt in only a
	few days. It is the language of choice for large parts of NASA's, Google's and many other
	enterprises' code.

	For more information on Python, explore http://www.python.org.

Once all these dependencies and the database are installed, install the server itself using the
instructions on the website.

Open a terminal window to start the server with the command :command:`openerp-server`, which
should result in a series of log messages as the server starts up. If the server
is correctly installed, the message :guilabel:`[...] waiting for connections...` should show within 30
seconds or so, which indicates that the server is waiting for a client to connect to it.

.. figure:: images/terps_startup_log.png
   :align: center
   :scale: 75
   
   *OpenERP startup log in the console*

.. index::
   single: client; GTK
   single: installation; GTK client

Manual Installation of OpenERP GTK Clients
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

To install an OpenERP GTK client, follow the steps outlined in the website installation document for
your particular operating system.

.. figure:: images/terp_client_startup.png
   :align: center
   :scale: 75
   
   *OpenERP client at startup*

Open a terminal window to start the client using the command :command:`openerp-client`. When you start the
client on the same Linux PC as the server you will find that the default connection parameters will
just work without needing any change. The message :guilabel:`No database found, you must create
one!`  shows you that the connection to the server has been successful and you need to create a
database on the server.

Creating the Database
^^^^^^^^^^^^^^^^^^^^^

You can connect other GTK clients over the network to your Linux server. Before you leave your
server, make sure you know its network address – either by its name (such as \
``mycomputer.mycompany.net``\  ) or its IP address (such as \ ``192.168.0.123``\  ).

.. index::
   single: port (network)

.. note:: Different Networks

	Communications between an OpenERP client and server are based on standard protocols. You can
	connect Windows clients to a Linux server, or vice versa, without problems. It is the same for Mac
	versions of OpenERP – you can connect Windows and Linux clients and servers to them.

To install an OpenERP client on a computer under Linux, repeat the procedure shown earlier in this
section. You can connect different clients to the OpenERP server by modifying the connection
parameters on each client. To do that, click the :guilabel:`Change` button in the connection dialog
and set the following fields as needed:

*  :guilabel:`Server` : \ ``name``\   or  \ ``IP address``\   of the server over the network,

*  :guilabel:`Port` : the port, whose default is \ ``8069``\   or  \ ``8070``\ ,

*  :guilabel:`Connection protocol` : \ ``XML-RPC``\   or  \ ``NET-RPC``\  .


.. figure:: images/terp_client_server.png
   :align: center
   :scale: 75

   *Dialog box for defining connection parameters to the server*

It is possible to connect the server to the client using a secure protocol to prevent other network
users from listening in, but the installation described here is for direct unencrypted connection.

If your Linux server is protected by a firewall you will have to provide access to port 
 \ ``8069`` \ or \ ``8070`` \ for users on other computers with OpenERP GTK clients.

.. index::
   single: installation; eTiny web server
   single: installation; OpenERP client-web server

Installation of an OpenERP Web Server
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Just as you installed a GTK client on a Linux server, you can also install the OpenERP client-web
server.
You can install it from sources after installing its dependencies from packages as you did
with the OpenERP server,
but OpenERP has provided a simpler way to do this for the web client – using a system known as ez_setup.

Before proceeding, confirm that your OpenERP installation is functioning correctly with a GTK
client.
If it is not, you will need to go back now and fix it, because you need to be able to fully use it for
the next stages.

To install client-web follow the up-to-date instructions in the installation document on the website.

.. note:: Ez Tool

	Ez is the packaging system used by Python. It enables the installation of programs as required just
	like the packages used by a Linux distribution. The software is downloaded across the network and
	installed on your computer by ez_install.

	:program:`ez_setup` is a small program that installs ez_install automatically.

The OpenERP Web server connects to the OpenERP server in the same way as an OpenERP client
using the NET-RPC protocol. Its default setup corresponds to that of the OpenERP server
you have just installed, so should connect directly at startup.

#.	At the same console as you've just been using, go to the OpenERP web directory by typing
	:command:`cd openerp-web-6.X`.

#. 	At a terminal window type :command:`openerp-web` to start the OpenERP Web server.

.. _fig-webwel:

.. figure:: images/web_welcome.png
   :scale: 70
   :align: center

   *OpenERP web client at startup*
   
You can verify the installation by opening a web browser on the server and navigating to
http://localhost:8080 to connect to the OpenERP web version as shown in the figure :ref:`fig-webwel`. 
You can also test this from
another computer connected to the same network if you know the name or IP address of the server over
the network – your browser should be set to http://<server_address>:8080 for this.

Verifying your Linux Installation
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. index::
   single: pgAdmin III

You have used default parameters so far during the installation of the various components.
If you have had problems, or you just want to set this up differently,
the following points provide some indicators about how you can set up your installation.

.. tip:: **psql** and **pgAdmin** tools

	psql is a simple client, executed from the command line, that is delivered with PostgreSQL. It
	enables you to execute SQL commands on your OpenERP database.

	If you prefer a graphical utility to manipulate your database directly you can install pgAdmin III
	(it is commonly installed automatically with PostgreSQL on a windowing system, but can also be
	found at \ ``http://www.pgadmin.org/`` \ ).

.. To check pts 4 and 7

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

.. 	hint:: One Server for Several Companies

	You can start several OpenERP application servers on one physical computer server by using
	different ports. If you have defined multiple database roles in PostgreSQL, each connected through
	an OpenERP instance to a different port, you can simultaneously serve many companies from one
	physical server at one time.

.. Copyright © Open Object Press. All rights reserved.

.. You may take electronic copy of this publication and distribute it if you don't
.. change the content. You can also print a copy to be read by yourself only.

.. We have contracts with different publishers in different countries to sell and
.. distribute paper or electronic based versions of this book (translated or not)
.. in bookstores. This helps to distribute and promote the OpenERP product. It
.. also helps us to create incentives to pay contributors and authors using author
.. rights of these sales.

.. Due to this, grants to translate, modify or sell this book are strictly
.. forbidden, unless Tiny SPRL (representing Open Object Press) gives you a
.. written authorisation for this.

.. Many of the designations used by manufacturers and suppliers to distinguish their
.. products are claimed as trademarks. Where those designations appear in this book,
.. and Open Object Press was aware of a trademark claim, the designations have been
.. printed in initial capitals.

.. While every precaution has been taken in the preparation of this book, the publisher
.. and the authors assume no responsibility for errors or omissions, or for damages
.. resulting from the use of the information contained herein.

.. Published by Open Object Press, Grand Rosière, Belgium

