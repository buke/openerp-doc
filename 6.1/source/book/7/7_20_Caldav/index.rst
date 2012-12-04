.. _ch-sync:

Synchronizing your Calendars (CalDAV)
=====================================

As from OpenERP Version 6.0, :mod:`document_webdav` v2.2, the iPhone has been thoroughly
tested and is now supported as a Calendaring client for the OpenERP CalDAV module.
The same applies to the Android phones, of course.

However, keep in mind that OpenERP is not a straightforward calendaring
server, but an ERP application (with more data + structure) which exposes
those data to calendar clients. That said, the full features that would be
accessible through the GTK or Web OpenERP clients cannot be included into Calendar clients (such as iPhone). 

OpenERP Server Setup
--------------------
Some modules need to be installed on the OpenERP server. These are:

    - :mod:`caldav`: Required, has the reference setup and the necessary
            underlying code. Will also cause document & document_webdav
            to be installed.
    - :mod:`crm_caldav`: Optional, will export the CRM Meetings as a calendar.
    - :mod:`project_caldav`: Optional, will export project tasks as a calendar.
    - :mod:`http_well_known`: Optional, experimental. Will ease bootstrapping,
            but only when a DNS srv record is also used.

When you install the above module(s), a ready-to-go reference setup of the folders is provided.
The OpenERP administrator can add more calendars and (re)structure if needed.

.. DNS Server Setup
.. ----------------
.. To be documented.

SSL Setup
---------
It is highly advisable that you also set up SSL to work for the OpenERP
server. HTTPS is a server-wide feature in OpenERP, which means a 
certificate will be set at the openerp-server.conf which will be the same
for XML-RPC, HTTP, WebDAV and CalDAV.
The iPhone also supports secure connections with SSL, although it does
not expect a self-signed certificate (or one that is not verified by
one of the "big" certificate authorities).

Calendars on iPhone
-------------------

To set up the calendars, proceed as follows:

1. Click ``Settings`` and go to the ``Mail, Contacts, Calendars`` page.

2. Go to ``Add account...``

3. Click ``Other``.

4. From the ``Calendars`` group, select ``Add CalDAV Account``.

5. Enter the host name.
   (e.g. if the URL is http://openerp.com:8069/webdav/db_1/calendars/ , openerp.com is the host)

      .. tip:: Go to :menuselection:`Sales --> Meetings --> Synchronize this Calendar` and select ``Iphone``. Then the Caldav server will be shown.

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
--------------------

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

   .. tip:: Go to :menuselection:`Sales --> Meetings --> Synchronize this Calendar` and select ``Android``. Then the Caldav server link will be shown. Make sure to use the correct XML-RPC port, it may differ from 8069.

3. Type your OpenERP username and password.

4. If your server does not use SSL, you will get a warning. Answer ``Yes``.

5. Then you can synchronize manually or customize the settings (`Sync` tab) to synchronize every X minutes.

Calendars in Evolution
----------------------

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

      .. tip:: Go to :menuselection:`Sales --> Meetings --> Synchronize this Calendar` and select ``Evolution``. Then the Caldav server will be shown.

4. Click OK and enter your OpenERP password.

5. A new calendar with the name you entered should appear on the left side.

Calendars in Sunbird/Lightning
------------------------------

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

      .. tip:: Go to :menuselection:`Sales --> Meetings --> Synchronize this Calendar` and select ``Sunbird/Lightning``. Then the Caldav server will be shown.)
  
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

