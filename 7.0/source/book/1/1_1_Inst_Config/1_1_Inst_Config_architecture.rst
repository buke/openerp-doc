
.. index::
   single: architecture; OpenERP

The Architecture of OpenERP
===========================

To access OpenERP you can:

* use a web browser pointed at the OpenERP client-web server, or

* use an application client (the GTK client) installed on each computer.

The two methods of access give very similar facilities, and you can use both on
the same server at the same time. It is best to use the web browser if the
OpenERP server is some distance away (such as on another continent) because
it is more tolerant of time delays between the two than the GTK client is. The
web client is also easier to maintain, because it is generally already installed
on users' computers.

Conversely you would be better off with the application client (called the GTK
client because of the technology it is built with) if you are using a local
server (such as in the same building). In this case the GTK client will be more
responsive, so more satisfying to use.

.. index::
   single: client; web (thin) and GTK (thick)
   single: client; caching

.. note::   Web Client and GTK Client

    There is little functional difference between the two OpenERP clients - the 
    web client and the GTK client at present. 
    The web client offers more functionality, for instance, the Corporate Intelligence feature, and the Gantt view.
    
    When you are changing the structure of your OpenERP installation (adding and
    removing modules, perhaps changing labels), you might find the web client to be
    irritating because of its use of **caching**. 
    
    Caching speeds it all up by keeping a copy of data somewhere between the server 
    and your client, which is usually good. But you may 
    have made changes to your installation that you cannot immediately see in
    your browser. Many apparent faults are caused by this! The workaround is 
    to use the GTK client during development and implementation where possible.

    The OpenERP company will continue to support two clients for the foreseeable
    future, so you can use whichever client you prefer.

An OpenERP system is formed from three main components:

* the PostgreSQL database server, which contains all of the databases, each of which contains all
  data and most elements of the OpenERP system configuration,

* the OpenERP application server, which contains all of the enterprise logic and ensures that
  OpenERP runs optimally,

* the web server, a separate application called the Open Object client-web, which enables you to
  connect to OpenERP from standard web browsers and is not needed when you connect using a GTK
  client.

.. figure:: images/terp_arch_1.png
   :align: center
   :scale: 90
   
   *The architecture of OpenERP*

.. note::   Terminology: Client-web – Server or Client?

    The client-web component can be thought of as a server or a client depending on
    your viewpoint.

    It acts as a web server to an end user connecting from a web browser, but
    it also acts as a client to the OpenERP application server just as a GTK
    application client does.

    So in this book its context will determine whether the client-web component is referred to as
    a server or a client.

.. index::
   pair: eTiny; client-web

.. note::   eTiny

    The web application used to be known as “eTiny”.
    Its name changed to “client-web” as Tiny ERP was renamed to OpenERP,
    but its characteristics have generally stayed the same.

.. index::
   single: PostgreSQL

.. note::   PostgreSQL, the relational and object database management system.

    It is a free and open-source high-performance system that compares well with other database
    management systems such as MySQL and FirebirdSQL (both free), Sybase, DB2
    and Microsoft SQL Server (all proprietary). It runs on all types of
    Operating System, from Unix/Linux to the various releases of Windows, via
    Mac OS X, Solaris, SunOS and BSD.

These three components can be installed on the same server or can be
distributed onto separate computer servers, if performance considerations
require it.

If you choose to run only with GTK clients, you will not need the third component –
the client-web server – at all. In this case, OpenERP's GTK client must be installed
on the workstation of each OpenERP user in the company.


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

