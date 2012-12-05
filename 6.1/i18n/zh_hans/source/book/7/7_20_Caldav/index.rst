.. i18n: .. _ch-sync:
.. i18n: 
.. i18n: Synchronizing your Calendars (CalDAV)
.. i18n: =====================================
..

.. _ch-sync:

同步日历(CalDAV)
=====================================

.. i18n: As from OpenERP Version 6.0, :mod:`document_webdav` v2.2, the iPhone has been thoroughly
.. i18n: tested and is now supported as a Calendaring client for the OpenERP CalDAV module.
.. i18n: The same applies to the Android phones, of course.
..

As from OpenERP Version 6.0, :mod:`document_webdav` v2.2, the iPhone has been thoroughly
tested and is now supported as a Calendaring client for the OpenERP CalDAV module.
The same applies to the Android phones, of course.

.. i18n: However, keep in mind that OpenERP is not a straightforward calendaring
.. i18n: server, but an ERP application (with more data + structure) which exposes
.. i18n: those data to calendar clients. That said, the full features that would be
.. i18n: accessible through the GTK or Web OpenERP clients cannot be included into Calendar clients (such as iPhone). 
..

However, keep in mind that OpenERP is not a straightforward calendaring
server, but an ERP application (with more data + structure) which exposes
those data to calendar clients. That said, the full features that would be
accessible through the GTK or Web OpenERP clients cannot be included into Calendar clients (such as iPhone). 

.. i18n: OpenERP Server Setup
.. i18n: --------------------
.. i18n: Some modules need to be installed on the OpenERP server. These are:
..

OpenERP Server 配置
--------------------
Some modules need to be installed on the OpenERP server. These are:

.. i18n:     - :mod:`caldav`: Required, has the reference setup and the necessary
.. i18n:             underlying code. Will also cause document & document_webdav
.. i18n:             to be installed.
.. i18n:     - :mod:`crm_caldav`: Optional, will export the CRM Meetings as a calendar.
.. i18n:     - :mod:`project_caldav`: Optional, will export project tasks as a calendar.
.. i18n:     - :mod:`http_well_known`: Optional, experimental. Will ease bootstrapping,
.. i18n:             but only when a DNS srv record is also used.
..

    - :mod:`caldav`: Required, has the reference setup and the necessary
            underlying code. Will also cause document & document_webdav
            to be installed.
    - :mod:`crm_caldav`: Optional, will export the CRM Meetings as a calendar.
    - :mod:`project_caldav`: Optional, will export project tasks as a calendar.
    - :mod:`http_well_known`: Optional, experimental. Will ease bootstrapping,
            but only when a DNS srv record is also used.

.. i18n: When you install the above module(s), a ready-to-go reference setup of the folders is provided.
.. i18n: The OpenERP administrator can add more calendars and (re)structure if needed.
..

When you install the above module(s), a ready-to-go reference setup of the folders is provided.
The OpenERP administrator can add more calendars and (re)structure if needed.

.. i18n: .. DNS Server Setup
.. i18n: .. ----------------
.. i18n: .. To be documented.
..

.. DNS Server 配置
.. ----------------
.. 相关配置文档筹备中.

.. i18n: SSL Setup
.. i18n: ---------
.. i18n: It is highly advisable that you also set up SSL to work for the OpenERP
.. i18n: server. HTTPS is a server-wide feature in OpenERP, which means a 
.. i18n: certificate will be set at the openerp-server.conf which will be the same
.. i18n: for XML-RPC, HTTP, WebDAV and CalDAV.
.. i18n: The iPhone also supports secure connections with SSL, although it does
.. i18n: not expect a self-signed certificate (or one that is not verified by
.. i18n: one of the "big" certificate authorities).
..

SSL 配置
---------
It is highly advisable that you also set up SSL to work for the OpenERP
server. HTTPS is a server-wide feature in OpenERP, which means a 
certificate will be set at the openerp-server.conf which will be the same
for XML-RPC, HTTP, WebDAV and CalDAV.
The iPhone also supports secure connections with SSL, although it does
not expect a self-signed certificate (or one that is not verified by
one of the "big" certificate authorities).

.. i18n: Calendars on iPhone
.. i18n: -------------------
..

iPhone 设备日历
-------------------

.. i18n: To set up the calendars, proceed as follows:
..

To set up the calendars, proceed as follows:

.. i18n: 1. Click ``Settings`` and go to the ``Mail, Contacts, Calendars`` page.
.. i18n: 
.. i18n: 2. Go to ``Add account...``
.. i18n: 
.. i18n: 3. Click ``Other``.
.. i18n: 
.. i18n: 4. From the ``Calendars`` group, select ``Add CalDAV Account``.
.. i18n: 
.. i18n: 5. Enter the host name.
.. i18n:    (e.g. if the URL is http://openerp.com:8069/webdav/db_1/calendars/ , openerp.com is the host)
..

1. Click ``Settings`` and go to the ``Mail, Contacts, Calendars`` page.

2. Go to ``Add account...``

3. Click ``Other``.

4. From the ``Calendars`` group, select ``Add CalDAV Account``.

5. Enter the host name.
   (e.g. if the URL is http://openerp.com:8069/webdav/db_1/calendars/ , openerp.com is the host)

.. i18n:       .. tip:: Go to :menuselection:`Sales --> Meetings --> Synchronize this Calendar` and select ``Iphone``. Then the Caldav server will be shown.
..

      .. tip:: Go to :menuselection:`Sales --> Meetings --> Synchronize this Calendar` and select ``Iphone``. Then the Caldav server will be shown.

.. i18n: 6. In ``Username`` and ``Password``, type your OpenERP login and password.
.. i18n: 
.. i18n: 7. As a description, you can either leave the server's name or
.. i18n:    something like "OpenERP calendars".
.. i18n: 
.. i18n: 8. If you are not using a SSL server, you will get an error, do not worry and push "Continue"
.. i18n: 
.. i18n: 9. Then click "Advanced Settings" to specify the correct ports and paths. 
.. i18n:     
.. i18n: 10. Specify the port for the OpenERP server: 8071 for SSL, 8069 without SSL.
.. i18n: 
.. i18n: 11. Set the ``Account URL`` to the right path of the OpenERP webdav:
.. i18n:     the URL given by the wizard (e.g. http://my.server.ip:8069/webdav/dbname/calendars/ )
.. i18n: 
.. i18n: 12. Click ``Done``. The phone will connect to the OpenERP server
.. i18n:     and verify whether the account can be used.
.. i18n: 
.. i18n: 13. Go to the main menu of the iPhone and open the Calendar application.
.. i18n:     Your OpenERP calendars will be visible inside the selection of the
.. i18n:     "Calendars" button.
.. i18n:     Note that when creating a new calendar entry, you will have to specify
.. i18n:     which calendar it should be saved to.
..

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

.. i18n: If you need *SSL* (and your certificate is not a verified one),
.. i18n: you will first need to let the iPhone trust the certificate. Follow these steps:
..

If you need *SSL* (and your certificate is not a verified one),
you will first need to let the iPhone trust the certificate. Follow these steps:

.. i18n: 1. Open Safari and enter the HTTPS location of the OpenERP server:
.. i18n:    https://my.server.ip:8071/
.. i18n:    (assuming you have the server at "my.server.ip" and the HTTPS port is the default 8071)
.. i18n: 
.. i18n: 2. Safari will try to connect and issue a warning about the certificate used. Inspect the certificate
.. i18n:    and click "Accept" so that iPhone now trusts it.
..

1. Open Safari and enter the HTTPS location of the OpenERP server:
   https://my.server.ip:8071/
   (assuming you have the server at "my.server.ip" and the HTTPS port is the default 8071)

2. Safari will try to connect and issue a warning about the certificate used. Inspect the certificate
   and click "Accept" so that iPhone now trusts it.

.. i18n: Calendars on Android
.. i18n: --------------------
..

Android 设备日历
--------------------

.. i18n: Prerequisites
.. i18n: *************
.. i18n: There is no built-in way to synchronize calendars with CalDAV.
.. i18n: So you need to install a third party software: Calendar (CalDav) Sync BETA 
.. i18n: from Hypermatix Software (for now, it is the only one).
..

使用条件
*************
There is no built-in way to synchronize calendars with CalDAV.
So you need to install a third party software: Calendar (CalDav) Sync BETA 
from Hypermatix Software (for now, it is the only one).

.. i18n: How to Configure?
.. i18n: *****************
..

配置步骤
*****************

.. i18n: 1. Open the ``Calendar Sync`` application.
.. i18n:    You get an interface with 2 tabs.
.. i18n:    
.. i18n: 2. On the `Connection` tab, in CalDAV Calendar URL, type a URL such as http://my.server.ip:8069/webdav/dbname/calendars/users/demo/c/Meetings.
..

1. 打开 ``Calendar Sync`` 应用.
   打开后，界面上应该会有两个页面.
   
2. 在 `Connection` 页面中, 找到 CalDAV 日历链接, 输入你的OpenERP 日历地址 "http://my.server.ip:8069/webdav/dbname/calendars/users/demo/c/Meetings" 。

.. i18n:    .. tip:: Go to :menuselection:`Sales --> Meetings --> Synchronize this Calendar` and select ``Android``. Then the Caldav server link will be shown. Make sure to use the correct XML-RPC port, it may differ from 8069.
..

   .. tip:: Go to :menuselection:`Sales --> Meetings --> Synchronize this Calendar` and select ``Android``. Then the Caldav server link will be shown. Make sure to use the correct XML-RPC port, it may differ from 8069.

.. i18n: 3. Type your OpenERP username and password.
.. i18n: 
.. i18n: 4. If your server does not use SSL, you will get a warning. Answer ``Yes``.
.. i18n: 
.. i18n: 5. Then you can synchronize manually or customize the settings (`Sync` tab) to synchronize every X minutes.
..

3. 输入你的OpenERP帐户及密码.

4. 如果你的OpenERP没有配置SSL，会接受一个关于SSL的警告，请选择 ``Yes``.

5. Then you can synchronize manually or customize the settings (`Sync` tab) to synchronize every X minutes.

.. i18n: Calendars in Evolution
.. i18n: ----------------------
..

Evolution 日历
----------------------

.. i18n: 1. Go to Calendar View.
.. i18n: 
.. i18n: 2. :menuselection:`File --> New --> Calendar`.
.. i18n: 
.. i18n: 3. Enter the data in the form:
.. i18n:  
.. i18n:     - Type : CalDav
.. i18n:     - Name : Whatever you want (e.g. Meeting)
.. i18n:     - URL : http://HOST:PORT/webdav/DB_NAME/calendars/users/USER/c/Meetings (e.g.
.. i18n:       http://localhost:8069/webdav/db_1/calendars/users/demo/c/Meetings) 
.. i18n:       the one given on top of this window
.. i18n:     - Uncheck "User SSL"
.. i18n:     - Username : Your username (e.g. Demo)
.. i18n:     - Refresh : every time you want Evolution to synchronize the data with the server
..

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

.. i18n:       .. tip:: Go to :menuselection:`Sales --> Meetings --> Synchronize this Calendar` and select ``Evolution``. Then the Caldav server will be shown.
..

      .. tip:: Go to :menuselection:`Sales --> Meetings --> Synchronize this Calendar` and select ``Evolution``. Then the Caldav server will be shown.

.. i18n: 4. Click OK and enter your OpenERP password.
.. i18n: 
.. i18n: 5. A new calendar with the name you entered should appear on the left side.
..

4. Click OK and enter your OpenERP password.

5. A new calendar with the name you entered should appear on the left side.

.. i18n: Calendars in Sunbird/Lightning
.. i18n: ------------------------------
..

Sunbird/Lightning 日历
------------------------------

.. i18n: Prerequisites
.. i18n: *************
.. i18n: If you are using Thunderbird, first install the Lightning module
.. i18n: http://www.mozilla.org/projects/calendar/lightning/
..

使用条件
*************
If you are using Thunderbird, first install the Lightning module
http://www.mozilla.org/projects/calendar/lightning/

.. i18n: Configuration
.. i18n: *************
..

配置
*************

.. i18n: 1. Go to Calendar View.
.. i18n: 
.. i18n: 2. :menuselection:`File --> New Calendar`.
.. i18n: 
.. i18n: 3. Choose ``On the Network``.
.. i18n: 
.. i18n: 4. As a format, select CalDav
.. i18n:    and as a location type the URL (e.g. http://host.com:8069/webdav/db/calendars/users/demo/c/Meetings).
..

1. Go to Calendar View.

2. :menuselection:`File --> New Calendar`.

3. Choose ``On the Network``.

4. As a format, select CalDav
   and as a location type the URL (e.g. http://host.com:8069/webdav/db/calendars/users/demo/c/Meetings).

.. i18n:       .. tip:: Go to :menuselection:`Sales --> Meetings --> Synchronize this Calendar` and select ``Sunbird/Lightning``. Then the Caldav server will be shown.)
.. i18n:   
.. i18n: 5. Choose a name and a colour for the Calendar, and we advice you to uncheck "alarm".
..

      .. tip:: Go to :menuselection:`Sales --> Meetings --> Synchronize this Calendar` and select ``Sunbird/Lightning``. Then the Caldav server will be shown.)
  
5. Choose a name and a colour for the Calendar, and we advice you to uncheck "alarm".

.. i18n: 6. Enter your OpenERP login and password (to give the password only once, check the box ``Use Password Manager to remember this password``).
.. i18n: 
.. i18n: 7. Then click Finish; your meetings should now appear in your Calendar view.
..

6. Enter your OpenERP login and password (to give the password only once, check the box ``Use Password Manager to remember this password``).

7. Then click Finish; your meetings should now appear in your Calendar view.

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
