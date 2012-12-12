
.. _part2-crm-communicate:

.. index::
   single: module; outlook, thunderbird
   single: module; fetchmail
   single: gateway

Connecting with your Email and Accessing from your Mobile Device
================================================================

 *OpenERP provides all the information you need to pursue your company's business opportunities
 effectively. But to stay productive with all the information you have to handle, it is essential 
 that you can keep using your normal communication tools by interfacing them with OpenERP, 
 and that you are not limited just to OpenERP's interface.*

Often your sales persons are already used to working with standard email clients to manage their business. OpenERP allows you to perfectly integrate their knowledge with the use of OpenERP. 

OpenERP offers this flexibility to those who need to continue using their traditional email programs to maintain their
efficiency: OpenERP can be connected to Outlook and Thunderbird. Your users can participate in many OpenERP-maintained processes without ever leaving their familiar environment, and can avoid double data entry, yet easily link information to OpenERP's database automatically.

With the Outlook and Thunderbird plug-ins, you can create and/or open contacts directly from your email client in OpenERP without effort.
You can also link emails (with attachments) to OpenERP, to avoid information getting lost.
Both plug-ins enable you for instance to create leads based on exchanges you have with the customer.

The email gateway functionality enables you to use OpenERP’s CRM without necessarily using the OpenERP interface. Up-to-date leads can automatically be stored in OpenERP just by sending and receiving emails through a specific email address. You can even answer such mails from your own mailbox.

And of course, you can link the OpenERP meeting calendar to your mobile device.

.. _ch-crm-fetchmail:

Communication Tools
-------------------

.. index:: fetchmail

The *Fetchmail / Mailgateway* functionality lets you interface the CRM with incoming and outgoing emails. So you can receive mails in OpenERP and answer them directly from OpenERP.
You can install it when you configure the CRM, through the `Reconfigure` wizard, `Fetch Emails`, or by installing the :mod:`fetchmail` module from the list of modules.
Thanks to this feature, each email you receive on the specified email address may automatically create a lead, a contact or an other object in OpenERP, while keeping track of email attachments. This is an easy way to ensure that no crucial sales information gets lost.

You set the generic email address you want to use, such as sales@mycompany.com, and then you tell OpenERP that every incoming email for this address should automatically be created as a lead.

.. tip:: Objects

       You can use this feature for any object in OpenERP, so for instance also to keep track of your helpdesk or job applications.

To use the email gateway, you should install the `Fetchmail` module. You might need a system administrator to carry out this work.

If you followed the steps in the previous chapters, you should have the `Fetchmail` module installed. If not, you can install the `Fetchmail` module from the Configuration Wizard (CRM Configuration Wizard, Synchronization, Fetch Emails), or from the modules list.

.. note:: Scheduled Action

       Click the ``Fetch email`` button to get the emails directly. OpenERP also automatically creates a **Scheduled Action** to fetch the mails every 5 minutes.

*Step 1*

You can configure your incoming mail account(s) from the :menuselection:`Sales --> Configuration --> Emails --> Email Servers`.

.. figure::  images/email_server_config.jpeg
   :scale: 80
   :align: center

   *How to Configure your Email Server for Incoming Mails?*

Go to :menuselection:`Tools --> Configuration --> Email Template --> Email Accounts` to define the email smtp settings.

In the ``Description`` field, type the visible name you would like to use for the account.

In ``Server``, type the mail server, i.e. smtp.googlemail.com.

Type the SMTP port (e.g. 587), configure the other settings according to the specifications of your server.

Add the User Information, such as email address for which the mails will enter OpenERP, i.e. support@mycompany.com, the user name and the password. Configure the other settings to your needs.

Save and click the ``Test Outgoing Connection`` button to check whether the settings are correct.

When everything is correctly configured, `Approve` the account. OpenERP will automatically create a Scheduler for the mails. You can also send/receive mails manually by clicking the ``Send/Receive`` button.

*Step 2*

You can configure your outgoing mail account(s) from the :menuselection:`Tools --> Configuration --> Email Template --> Email Accounts`.

.. figure::  images/outgoing_server_config.jpeg
   :scale: 80
   :align: center

   *How to Configure your Email Server for Outgoing Mails?*

Go to Sales > Configuration > Emails > Email Servers to define the email server settings.

Assign a ``Name`` and select the ``Server Type``, i.e. IMAP Server.

Click ``Add Attachments`` if you want to include attachments for the mails received / sent.

Enter the Server Information, check SSL if necessary, i.e. imap.googlemail.com and the Login Information.

You can also choose to send an automatic reply on receipt of the mail. You can configure the mail here from the ``Email Server Action`` field.

Assign the ``Model`` to use when a new email arrives, i.e. choose Lead (crm.leads) if you want every new email that arrives to be created as a lead. 

Click `Confirm` to confirm the account settings.

.. note:: Server Configuration

       You will also need your administrator to configure your server settings to allow for an email gateway. This will not be explained
       in this book.

.. index:: Outlook (Microsoft)

.. _outl:

Managing your CRM from Microsoft Outlook
----------------------------------------

The Microsoft Outlook plug-in enables you to carry out a series of OpenERP operations quickly and directly
from the Outlook email client:

* create a contact or partner from an email,

* open a partner from an email,

* save an email and its attachments in OpenERP from your mailbox,

* send any attachment to an OpenERP document (such as opportunities, customers).

Thanks to the plug-in, you can effortlessly link emails and attachments to the corresponding opportunity in OpenERP, or link an attached product folder to a customer, for instance.

.. tip:: Outlook Versions

	The Microsoft Outlook plug-in works with Microsoft Outlook 2003 and 2007, but not with Outlook Express.

In this chapter, only the actual possibilities of the plug-in will be discussed. For more information about how to install and configure the Outlook plug-in, please refer to the chapter :ref:`outlook`.

From the Outlook toolbar, have a look at the :menuselection:`Tools` menu.

The `Push` option allows you to archive emails to OpenERP, either to new document types or to existing ones (such as Leads). It also allows you to create a new contact.

The `Partner` option allows you to open the Partner in OpenERP according to the email (i.e. contact email address) selected. 

With `Document`, you can open the document (i.e. a customer, an opportunity) concerned in OpenERP. Make sure your web server is running to use this functionality. 

.. figure::  images/outlook_config2.png
   :scale: 100
   :align: center

   *How to Access OpenERP from Outlook?*

* Link an email to an existing document in OpenERP

To archive an email in OpenERP from Outlook, select the email and click the `Push` button. Alternatively you can open the menu :menuselection:`Tools --> Push`: the ``Push to OpenERP`` screen will open.

In the ``Link to an Existing Document`` section, check *Partner*. Then select the customer you want to attach the selected mail to.
The plug-in also allows you to select several customers at once, simply by selecting a customer and pressing the ``ctrl`` button while selecting the next one.

Suppose you decide to no longer link the selected email to a customer, but instead to an opportunity. Then you have to click the ``Search`` button to refresh the `Documents` list to display your opportunities.    

From the list of available documents, you can select any document type you defined in the ``Document Settings`` section. 

* Create a New Document

This feature can be used to create any of the configured document types in the ``Document Settings`` tab.
Suppose you would like to create a new lead from an email. In the ``Create a New Document`` section, select ``CRM Lead``, then click the ``Create`` button. A new lead will be created in OpenERP from the selected email.

* Create a New Contact / Partner

If the partner or contact from your email does not exist in OpenERP yet, the Outlook plug-in allows you to
create one on the fly simply by using the information contained in the email.

Select the email from which you want to create a new contact, then click the ``Push`` button.
In the ``Create a New Contact`` section, click the ``New Contact`` button. This option offers two possibilities:
either you just create a contact (address), or you create a partner with the contact linked to it.

	- When you just want to create a new contact, complete the address data in the dialog box and click the ``Save`` button.
	  The contact will then be created in OpenERP.

	- When you also want to create a new partner, complete the contact data.
	  Then click the ``Create Partner`` button, add the partner's name and click the ``Save`` button.

	- You can also add a new contact to an existing partner. Click the ``Search`` button next to the Partner field
	  and select the corresponding partner from the list. Then complete the contact data and click the ``Save`` button.

.. figure::  images/outlook_creation.png
   :scale: 100
   :align: center

   *Creating a Contact on the Fly from Outlook*

* Open the Document created in OpenERP

From your mailbox, simply by clicking an email, you can directly access the corresponding data in OpenERP. Go to the menu :menuselection:`Tools --> Document` which will open the corresponding document (e.g. a lead) in OpenERP, directly from the email you selected.

.. tip:: Knowledge Management

	The Outlook plug-in is compatible with OpenERP's Knowledge (i.e. Document) Management. If you install the
	Knowledge application you will be able to:

	* search through the content of your company's documents (those that have the type .doc, .pdf, .sxw
	  and .odt) and also in archived emails,

	* have a shared file system that is connected to various OpenERP documents to share information and
	  access it with your favorite browser,

	* organize and structure your documents (such as projects, partners and users) in OpenERP's
	  system.

* Step 1: Install the Outlook plugin in OpenERP

Use the OpenERP Configuration Wizard and install the ``Customer Relationship Management`` application. In the *CRM Application Configuration* dialog under Plug-In, select `MS-Outlook`.
Then the *Outlook Plug-In* wizard appears. Next to the ``Outlook Plug-in`` field, click the ``Save As`` button to save the plugin to your desktop (or any other location on your computer).

You can also download the installation manual by clicking the green arrow next to ``Installation Manual``.  

Another way to use the Outlook plugin, is by installing the OpenERP module \
``outlook``\. When you install this module, the same Configuration Wizard as explained before will be displayed. Follow the same instructions.


* Step 2: Prerequisites (for more details, please refer to the online documentation)

  1. Install Python 2.6+

  2. Python for Windows extensions - PyWin32, this module for python must be installed for the appropriate version of Python.

  3. Specify the python folder in the system path (typically with this installer C:\Python26)

  *How to set the path in Windows XP*
  For Windows XP: http://www.computerhope.com/issues/ch000549.htm
    
  *How to set the path in Windows 7*
  To change the system environment variables, follow the steps below. 

   - From the Windows button, select ``Control Panel``, then click ``System``. 
   - Click ``Remote Settings`` to open the System Properties window.
   - In the System Properties window, click the Advanced tab. 
   - In the Advanced section, click the ``Environment Variables`` button. 
   - Finally, in the Environment Variables window (as shown below) under System Variables, highlight the Path directory,
     click Edit and add ;C:\Python26.

  4. If you are using MS Outlook 2007 then you are required to install "Microsoft Exchange Server MAPI Client and Collaboration
  Data Objects 1.2.1 (CDO 1.21)"
  Double-click Exchange CDO to install it.

  5. If you are using MS Outlook 2003, be sure to install the built-in CDO component.


* Step 3: Install the OpenERP extension in Outlook.

	#. Double-click the file \``OpenERP-Outlook-addin.exe``\ that you saved on your desktop. Confirm the default settings.

	#. Double-click the file \``Register plugin``\ in the OpenERP Outlook Addin folder (typically in C:\Program Files).

	#. Start Outlook.

When you have executed Installation Step 1, Step 2 and Step 3, the first thing to do is connect Outlook to OpenERP.
A little configuration needs to be done.

.. tip:: Toolbars 

      If you want the OpenERP connection to be shown as a separate toolbar, go to the menu :menuselection:`View --> Toolbars`. Select ``OpenERP``.

* Go to the menu :menuselection:`Tools` and select `Configuration`. If this raises an error, make sure to check the access rights to that particular folder.

A configuration window appears enabling you to enter configuration data about your OpenERP server.

.. figure::  images/outlook_menu2.png
   :scale: 75
   :align: center

   *How to Connect to the Server*

	#. On the ``Configuration Settings`` tab, under *Connection Parameters* click the `Change` button
	   and type your server settings and XML-RPC port, e.g. ``http://127.0.0.1:8069``,

	#. Select the database you want to connect to, and type the user and the password required to log in to the database,

	#. Click the `Connect` button,

	#. On the ``Configuration Settings`` tab, under *Webserver Parameters* click the `Change` button
	   and type your web server settings, e.g. ``http://localhost:8080``,

	#. Click the `Open` button to test the connection.

When your connection has succeeded, you would typically want to configure Outlook to fit your needs.

To define extra document types, go to the `Document Settings` tab. This is the place where you can add objects from OpenERP that you wish to link mails to. The default installation comes with a number of predefined documents, such as Partners, Leads and Sales Orders.

Here is an example of how to configure extra document types. Suppose you would like to link mails to a meeting:

	#. In the `Title`, type ``Meeting``,

	#. In the `Document`, type the object from OpenERP, in this example ``crm.meeting``,

	#. In the `Image`, select an icon you would like to use,

	#. Click the `Add` button to actually create the document type.

.. note:: A Word about Objects

       To find the object you need in OpenERP, go to the menu :menuselection:`Administration --> Customization --> Database Structure -->
       Objects`. OpenERP will only show objects for which the corresponding Business Applications / Modules have been installed.
       You can only add objects to Outlook that are available in the selected database.

.. index::
   single: Thunderbird (Mozilla)

.. _thunder:

Managing your CRM from Mozilla Thunderbird
------------------------------------------

With the Mozilla Thunderbird plug-in you can carry out a series of OpenERP operations directly from Thunderbird, such as:

* create a contact or partner from an email,

* open a partner from an email,

* save an email and its attachments in OpenERP,

* send any attachment to an OpenERP document (such as opportunities, customers).

Thanks to the plug-in, you can effortlessly link emails and attachments to the corresponding opportunity in OpenERP, or link an attached product folder to a customer, for instance.

In this chapter, only the actual possibilities of the plug-in will be discussed. For more information about how to install and configure the Thunderbird plug-in, please refer to the chapter :ref:`thunderbird`.

From the Thunderbird toolbar, have a look at the :menuselection:`OpenERP` menu.

The `Push` option allows you to archive emails to OpenERP, either to new document types or to existing ones. It also allows you to create a new contact.

The `Partner` allows you to open the Partner in OpenERP according to the email (i.e. contact email address) selected. 

With `Document`, you can open the document (i.e. a customer, an opportunity) concerned in OpenERP. Make sure your web server is running to use this functionality. You have to open the mail to use this feature. 

* Link an email to an existing document in OpenERP

.. figure::  images/thunderbird_selection.png
   :scale: 100
   :align: center

   *How to Access OpenERP from Thunderbird?*

To archive an email in OpenERP from Thunderbird, select the email and click the `Push` button. Alternatively you can open the menu :menuselection:`OpenERP --> Push`: the ``Push to OpenERP`` screen will open.

In the ``Link to an Existing Document`` section, check *Partner*. Then select the customer you want to attach the selected mail to.
The plug-in also allows you to select several customers at once, simply by selecting a customer and pressing the ``ctrl`` button while selecting the next one.

Suppose you decide to no longer link the selected email to a customer, but instead to an opportunity. Then you have to click the ``Search`` button to refresh the `Documents` list to display your opportunities.    

From the list of available documents, you can select any document type you defined in the ``Document Settings`` section. 

* Create a New Document

This feature can be used to create any of the configured document types in the ``Document Settings`` tab.
Suppose you would like to create a new lead from an email. In the ``Create a New Document`` section, select ``CRM Lead``, then click the ``Create`` button. A new lead will be created in OpenERP from the selected email.

* Create a New Contact / Partner

If the partner or contact from your email does not exist in OpenERP yet, the Thunderbird plug-in allows you to
create one on the fly simply by using the information contained in the email.

Select the email from which you want to create a new contact, then click the ``Push`` button.
In the ``Create a New Contact`` section, click the ``New Contact`` button. This option offers two possibilities:
either you just create a contact (address), or you create a partner with the contact linked to it.

	- When you just want to create a new contact, complete the address data in the dialog box and click the ``Save`` button.
	  The contact will then be created in OpenERP.

	- When you also want to create a new partner, complete the contact data.
	  Then click the ``Create Partner`` button, add the partner's name and click the ``Save`` button.

	- You can also add a new contact to an existing partner. Click the ``Search`` button next to the Partner field
	  and select the corresponding partner from the list. Then complete the contact data and click the ``Save`` button.

.. figure::  images/thunderbird_creation.png
   :scale: 75
   :align: center

   *Creating a Contact on the Fly from Thunderbird*

* Open the Document created in OpenERP

From your mailbox, simply by clicking an email, you can directly access the corresponding data in OpenERP. Go to the menu :menuselection:`Tools --> Document` which will open the corresponding document (e.g. a lead) in OpenERP, directly from the email you selected.

.. tip:: Knowledge Management

	The Thunderbird plug-in is compatible with OpenERP's Knowledge (i.e. Document) Management. If you install the
	Knowledge application you will be able to:

	* search through the content of your company's documents (those that have the type .doc, .pdf, .sxw
	  and .odt) and also in archived emails,

	* have a shared file system that is connected to various OpenERP documents to share information and
	  access it with your favorite browser,

* Step 1: Install the Thunderbird plugin in OpenERP

Use the OpenERP Configuration Wizard and install the ``Customer Relationship Management`` application. In the *CRM Application Configuration* dialog under Plug-In, select `Thunderbird`.
Then the *Thunderbird Plug-In* wizard appears. Next to the ``Thunderbird Plug-in`` field, click the ``Save As`` button to save the plugin to your desktop (or any other location on your computer).

You can also download the installation manual by clicking the orange arrow next to ``Installation Manual``.  

Another way to use the Thunderbird plugin, is by installing the OpenERP module \
``thunderbird``\. When you install this module, the same Configuration Wizard as explained before will be displayed. Follow the same instructions.

* Step 2: Install the OpenERP extension in Thunderbird.

To do that, use the file \``openerp_plugin.xpi``\ that you saved on your desktop. 

Then proceed as follows:

	#. From Thunderbird, open the menu :menuselection:`Tools --> Add-ons`.

	#. Click Extensions, then click the `Install` button.

	#. Go to your desktop and select the file \ ``openerp_plugin.xpi``\. Click Open.

	#. Click `Install Now` then restart Thunderbird.

Once the extension has been installed, a new ``OpenERP`` menu item is added to your Thunderbird menubar. 

.. tip::  Thunderbird Version

	The OpenERP plugin for Thunderbird works as from Thunderbird version 2.0.

	So check your Thunderbird version before installing, and download the latest version that you need
	from the following address: http://www.mozilla.org/products/thunderbird/

When you have executed Installation Step 1 and Step 2, the first thing to do is connect Thunderbird to OpenERP.
A little configuration needs to be done.

.. note:: Before starting the configuration, make sure your GTK server and web server are running (XML-RPC should be allowed).

Go to the ``OpenERP`` menubar and select ` Configuration`.

A configuration window appears enabling you to enter configuration data about your OpenERP server.

.. figure::  images/thunderbird_config.png
   :scale: 75
   :align: center

   *How to Connect to the Server*

	#. On the ``Configuration Settings`` tab, under *Connection Parameters* click the `Change` button
	   and type your server settings and XML-RPC port, e.g. ``http://127.0.0.1:8069``,

	#. Select the database you want to connect to, and type the user and the password required to log in to the database,

	#. Click the `Connect` button,

	#. On the ``Configuration Settings`` tab, under *Webserver Parameters* click the `Change` button
	   and type your web server settings, e.g. ``http://localhost:8080``,

	#. Click the `Open` button to test the connection.

When your connection has succeeded, you would typically want to configure Thunderbird to fit your needs.

To define extra document types, go to the `Document Settings` tab. This is the place where you can add objects from OpenERP that you wish to link mails to. The default installation comes with a number of predefined documents, such as Partners, Leads and Sales Orders.

Here is an example of how to configure extra document types. Suppose you would like to link mails to a purchase order.

	#. In the `Title`, type ``Purchase Order``,

	#. In the `Document`, type the object from OpenERP, in this example ``purchase.order``,

	#. In the `Image`, select an icon you would like to use,

	#. Click the `Add` button to actually create the document type.

.. note:: A Word about Objects 

       To find the object you need in OpenERP, go to the menu :menuselection:`Administration --> Customization --> Database Structure -->
       Objects`. OpenERP will only show objects for which the corresponding Business Applications / Modules have been installed.
       You can only add objects to Thunderbird that are available in the selected database.

.. figure::  images/thunderbird_document.png
   :scale: 75
   :align: center

   *How to Add Extra OpenERP Document Types to Thunderbird?*
   * organize and structure your documents (such as projects, partners and users) in OpenERP's system.

.. _ch-sync1:

Synchronizing your CRM with Mobile Devices
------------------------------------------

Synchronize your OpenERP calendars with your mobile device and know which meeting to go to from wherever you are!

Make your OpenERP even more efficient and let your sales synchronize their meetings with their mobile devices.
Anywhere your sales people are, they can easily check their planning and confirm new meetings with customers on the spot.

You can synchronize your calendars with iPhone and Android phones, and also with tools such as Evolution and Sunbird/Lightning.

.. note:: Installation and Configuration

       Please note that setting this up requires some technical knowledge, and probably the assistance of IT staff.

.. index::
   single: mobile; caldav; Android; iPhone; Sunbird; Evolution; Lightning

.. _mobile:

OpenERP Server and SSL Setup
++++++++++++++++++++++++++++
Some modules need to be installed on the OpenERP server (or may already be installed). These are:

    - :mod:`caldav`: Required, has the reference setup and the necessary
            underlying code. Will also cause document & document_webdav
            to be installed.
    - :mod:`crm_caldav`: Optional, will export the CRM Meetings as a calendar.
    - :mod:`project_caldav`: Optional, will export project tasks as a calendar.
    - :mod:`http_well_known`: Optional, experimental. Will ease bootstrapping,
            but only when a DNS srv record is also used.

When you install the above module(s), a ready-to-go reference setup of the folders is provided.
The OpenERP administrator can add more calendars and (re)structure if needed.

It is highly advisable that you also set up SSL to work for the OpenERP server. HTTPS is a server-wide feature in OpenERP, which means a 
certificate will be set at the openerp-server.conf which will be the same for XML-RPC, HTTP, WebDAV and CalDAV.
The iPhone also supports secure connections with SSL, although it does not expect a self-signed certificate (or one that is not verified by
one of the "big" certificate authorities).

Calendars on iPhone
+++++++++++++++++++

To set up the calendars, proceed as follows:

1. Click ``Settings`` and go to the ``Mail, Contacts, Calendars`` page.

2. Go to ``Add account...``

3. Click ``Other``.

4. From the ``Calendars`` group, select ``Add CalDAV Account``.

5. Enter the host name.
   (e.g. if the URL is http://openerp.com:8069/webdav/db_1/calendars/ , openerp.com is the host)

.. tip:: Synchronize this Calendar 

      Go to :menuselection:`Sales --> Meetings --> Synchronize this Calendar` and select ``Iphone``. Then the Caldav server will be shown.

6. In ``Username`` and ``Password``, type your OpenERP login and password.

7. As a description, you can either leave the server's name or
   something like "OpenERP calendars".

8. If you are not using a SSL server, you will get an error, do not worry and push "Continue"

9. Then click "Advanced Settings" to specify the correct ports and paths. 
    
10. Specify the port for the OpenERP server: 8071 for SSL, 8069 without SSL.

11. Set the ``Account URL`` to the right path of the OpenERP webdav:
    the URL given by the wizard (e.g. http://my.server.ip:8069/webdav/dbname/calendars/ )

12. Click ``Done``. The phone will connect to the OpenERP server
    and verify whether the account can be used.

13. Go to the main menu of the iPhone and open the Calendar application.
    Your OpenERP calendars will be visible inside the selection of the
    "Calendars" button.
    Note that when creating a new calendar entry, you will have to specify
    which calendar it should be saved to.

If you need *SSL* (and your certificate is not a verified one),
you will first need to let the iPhone trust the certificate. Follow these steps:

1. Open Safari and enter the HTTPS location of the OpenERP server:
   https://my.server.ip:8071/
   (assuming you have the server at "my.server.ip" and the HTTPS port is the default 8071)

2. Safari will try to connect and issue a warning about the certificate used. Inspect the certificate
   and click "Accept" so that iPhone now trusts it.

Calendars on Android
++++++++++++++++++++

Prerequisites
*************
There is no built-in way to synchronize calendars with CalDAV.
So you need to install a third party software: Calendar (CalDav) Sync BETA 
from Hypermatix Software (for now, it is the only one).

How to Configure?
*****************

1. Open the ``Calendar Sync`` application.
   You get an interface with 2 tabs.
   
2. On the `Connection` tab, in CalDAV Calendar URL, type a URL such as http://my.server.ip:8069/webdav/dbname/calendars/users/demo/c/Meetings.

.. tip:: Synchronize this Calendar

      Go to :menuselection:`Sales --> Meetings --> Synchronize this Calendar` and select ``Android``. Then the Caldav server link will be shown. Make sure to use the correct XML-RPC port, it may differ from 8069.

3. Type your OpenERP username and password.

4. If your server does not use SSL, you will get a warning. Answer ``Yes``.

5. Then you can synchronize manually or customize the settings (`Sync` tab) to synchronize every X minutes.

Calendars in Evolution
++++++++++++++++++++++

1. Go to Calendar View.

2. :menuselection:`File --> New --> Calendar`.

3. Enter the data in the form:
 
    - Type : CalDav
    - Name : Whatever you want (e.g. Meeting)
    - URL : http://HOST:PORT/webdav/DB_NAME/calendars/users/USER/c/Meetings (e.g.
      http://localhost:8069/webdav/db_1/calendars/users/demo/c/Meetings) 
      the one given on top of this window
    - Uncheck "User SSL"
    - Username : Your username (e.g. Demo)
    - Refresh : every time you want Evolution to synchronize the data with the server

.. tip:: Synchronize this Calendar

       Go to :menuselection:`Sales --> Meetings --> Synchronize this Calendar` and select ``Evolution``. Then the Caldav server will be shown.

4. Click OK and enter your OpenERP password.

5. A new calendar with the name you entered should appear on the left side.

Calendars in Sunbird/Lightning
++++++++++++++++++++++++++++++

Prerequisites
*************
If you are using Thunderbird, first install the Lightning module
http://www.mozilla.org/projects/calendar/lightning/

Configuration
*************

1. Go to Calendar View.

2. :menuselection:`File --> New Calendar`.

3. Choose ``On the Network``.

4. As a format, select CalDav
   and as a location type the URL (e.g. http://host.com:8069/webdav/db/calendars/users/demo/c/Meetings).

.. tip:: Synchronize this Calendar

      Go to :menuselection:`Sales --> Meetings --> Synchronize this Calendar` and select ``Sunbird/Lightning``. Then the Caldav server will be shown.
  
5. Choose a name and a colour for the Calendar, and we advice you to uncheck "alarm".

6. Enter your OpenERP login and password (to give the password only once, check the box ``Use Password Manager to remember this password``).

7. Then click Finish; your meetings should now appear in your Calendar view.


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



