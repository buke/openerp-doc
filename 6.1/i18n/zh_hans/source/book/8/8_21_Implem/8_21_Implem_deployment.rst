.. i18n: .. index::
.. i18n:    single: deployment
..

.. index::
   single: deployment

.. i18n: Deployment
.. i18n: ==========
..

系统部署
==========

.. i18n: As you have seen, the complete architecture of OpenERP includes the following elements:
..

As you have seen, the complete architecture of OpenERP includes the following elements:

.. i18n: * a database server,
.. i18n: 
.. i18n: * an OpenERP application server,
.. i18n: 
.. i18n: * an OpenERP client-web server,
.. i18n: 
.. i18n: * several clients that access the OpenERP server: they can either be web clients if the client-web
.. i18n:   server is installed, or GTK clients.
..

* a database server,

* an OpenERP application server,

* an OpenERP client-web server,

* several clients that access the OpenERP server: they can either be web clients if the client-web
  server is installed, or GTK clients.

.. i18n: .. index::
.. i18n:    single: deployment
..

.. index::
   single: deployment

.. i18n: .. note:: Deployment
.. i18n: 
.. i18n: 	Deployment is the process of putting an OpenERP database into a production-ready state,
.. i18n: 	where it can be used by everyone in your business for their daily work.
.. i18n: 	You would usually configure OpenERP and load data into it on one development system,
.. i18n: 	train staff on that or another training system and
.. i18n: 	deploy it onto a production system that has better protection against failure, better security and
.. i18n: 	more performance.
..

.. note:: Deployment

	Deployment is the process of putting an OpenERP database into a production-ready state,
	where it can be used by everyone in your business for their daily work.
	You would usually configure OpenERP and load data into it on one development system,
	train staff on that or another training system and
	deploy it onto a production system that has better protection against failure, better security and
	more performance.

.. i18n: Deployment Options
.. i18n: ------------------
..

部署环境
------------------

.. i18n: To deploy OpenERP in your company, several options are available to you:
..

To deploy OpenERP in your company, several options are available to you:

.. i18n: * a SaaS (Software as a Service) or On-Demand offer, which includes the equipment, the hosting, the
.. i18n:   maintenance and the support on a system configured to your needs in advance,
.. i18n: 
.. i18n: * an internal installation, that you manage yourselves or have managed by an IT services company
.. i18n:   such as an OpenERP partner,
.. i18n: 
.. i18n: * hosting by a server supplier on which OpenERP is installed, which enables you to proceed to add
.. i18n:   adaptations on your server.
..

* a SaaS (Software as a Service) or On-Demand offer, which includes the equipment, the hosting, the
  maintenance and the support on a system configured to your needs in advance,

* an internal installation, that you manage yourselves or have managed by an IT services company
  such as an OpenERP partner,

* hosting by a server supplier on which OpenERP is installed, which enables you to proceed to add
  adaptations on your server.

.. i18n: The first two approaches are the most commonly used.
..

The first two approaches are the most commonly used.

.. i18n: .. index::
.. i18n:    single: SaaS
.. i18n:    single: Software as a Service
.. i18n:    single: On-Demand
..

.. index::
   single: SaaS
   single: Software as a Service
   single: On-Demand

.. i18n: The SaaS (Software as a Service) Offer
.. i18n: ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
..

以SaaS(Software as a Service)方式部署
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. i18n: SaaS is a complete package hosted at a supplier, that includes the following services: server
.. i18n: hardware, hosting of the generic solution, installation and initial configuration, redundancy of the
.. i18n: architecture, backups, system maintenance and support. It is also known as :guilabel:`On-Demand`.
..

SaaS is a complete package hosted at a supplier, that includes the following services: server
hardware, hosting of the generic solution, installation and initial configuration, redundancy of the
architecture, backups, system maintenance and support. It is also known as :guilabel:`On-Demand`.

.. i18n: It is provided in the form of a monthly subscription with a fixed price per user. You can find the
.. i18n: detail of Tiny's SaaS packages at http://ondemand.openerp.com/.
..

It is provided in the form of a monthly subscription with a fixed price per user. You can find the
detail of Tiny's SaaS packages at http://ondemand.openerp.com/.

.. i18n: SaaS packages do not permit you to develop specific modules to your needs. On the contrary, they
.. i18n: offer a service at a set price based on standard software modules that contain few migration risks.
.. i18n: SaaS suppliers are limited generally to the modules certified and validated by the original author
.. i18n: and project manager, Tiny.
..

SaaS packages do not permit you to develop specific modules to your needs. On the contrary, they
offer a service at a set price based on standard software modules that contain few migration risks.
SaaS suppliers are limited generally to the modules certified and validated by the original author
and project manager, Tiny.

.. i18n: Here are the main advantages of an OpenERP SaaS solution:
..

Here are the main advantages of an OpenERP SaaS solution:

.. i18n: * an unbeatable return on investment (cost of implementation: 0, cost of licenses: 0),
.. i18n: 
.. i18n: * costs that are controlled and without surprises (the offer includes maintenance, frequent
.. i18n:   migrations and support),
.. i18n: 
.. i18n: * a turnkey solution, installed in less than twenty-four hours,
.. i18n: 
.. i18n: * packages adapted and preconfigured for different sectors of activity,
.. i18n: 
.. i18n: * a very robust architecture guaranteed to have constant and permanent access, reachable from
.. i18n:   anywhere.
..

* an unbeatable return on investment (cost of implementation: 0, cost of licenses: 0),

* costs that are controlled and without surprises (the offer includes maintenance, frequent
  migrations and support),

* a turnkey solution, installed in less than twenty-four hours,

* packages adapted and preconfigured for different sectors of activity,

* a very robust architecture guaranteed to have constant and permanent access, reachable from
  anywhere.

.. i18n: So this server is recommended for small companies with fewer than about fifteen employees.
..

So this server is recommended for small companies with fewer than about fifteen employees.

.. i18n: .. index::
.. i18n:    single: hosting
..

.. index::
   single: hosting

.. i18n: Hosting by a Supplier
.. i18n: ^^^^^^^^^^^^^^^^^^^^^
..

服务器托管
^^^^^^^^^^^^^^^^^^^^^

.. i18n: At first sight, a hosted OpenERP system appears similar to SaaS: it provides OpenERP from a
.. i18n: remote installation through a web browser. But in general, the similarities stop there.
..

At first sight, a hosted OpenERP system appears similar to SaaS: it provides OpenERP from a
remote installation through a web browser. But in general, the similarities stop there.

.. i18n: To compare it with an SaaS package, you should check if the hosting offer properly includes the
.. i18n: following elements:
..

To compare it with an SaaS package, you should check if the hosting offer properly includes the
following elements:

.. i18n: * server hardware,
.. i18n: 
.. i18n: * hosting,
.. i18n: 
.. i18n: * maintenance,
.. i18n: 
.. i18n: * future migrations,
.. i18n: 
.. i18n: * backups,
.. i18n: 
.. i18n: * server redundancy,
.. i18n: 
.. i18n: * telephone and email support,
.. i18n: 
.. i18n: * frequent updates to the modules.
..

* server hardware,

* hosting,

* maintenance,

* future migrations,

* backups,

* server redundancy,

* telephone and email support,

* frequent updates to the modules.

.. i18n: Also get yourself up to speed on the following points:
..

Also get yourself up to speed on the following points:

.. i18n: * the version of OpenERP proposed,
.. i18n: 
.. i18n: * the costs of implementation (configuration, data loading, training),
.. i18n: 
.. i18n: * the cost of configuration (if it is proposed),
.. i18n: 
.. i18n: * the technology and the procedure used for securing your database,
.. i18n: 
.. i18n: * the technology and the procedure for preventing system faults,
.. i18n: 
.. i18n: * the technology and the procedure for restoring a faulty system,
.. i18n: 
.. i18n: * limitations on the number of users, the number of simultaneous users, and the size of the
.. i18n:   database,
.. i18n: 
.. i18n: * the level of support and its costs,
.. i18n: 
.. i18n: * the procedure used to update OpenERP (to fault-fixed versions)
.. i18n: 
.. i18n: * the procedure adopted for OpenERP upgrades (to versions that have both fault fixes and new
.. i18n:   functionality).
..

* the version of OpenERP proposed,

* the costs of implementation (configuration, data loading, training),

* the cost of configuration (if it is proposed),

* the technology and the procedure used for securing your database,

* the technology and the procedure for preventing system faults,

* the technology and the procedure for restoring a faulty system,

* limitations on the number of users, the number of simultaneous users, and the size of the
  database,

* the level of support and its costs,

* the procedure used to update OpenERP (to fault-fixed versions)

* the procedure adopted for OpenERP upgrades (to versions that have both fault fixes and new
  functionality).

.. i18n: Calling such suppliers can be a good solution if you are willing to entrust all the technical
.. i18n: specifications for the functioning of OpenERP to them, especially if you need to use customized or
.. i18n: extension modules that are not in the stable version released by Tiny.
..

Calling such suppliers can be a good solution if you are willing to entrust all the technical
specifications for the functioning of OpenERP to them, especially if you need to use customized or
extension modules that are not in the stable version released by Tiny.

.. i18n: .. index::
.. i18n:    single: internal installation
..

.. index::
   single: internal installation

.. i18n: Internal Installation
.. i18n: ^^^^^^^^^^^^^^^^^^^^^
..

内部安装
^^^^^^^^^^^^^^^^^^^^^

.. i18n: Large and medium-large companies typically install OpenERP using their own internal company
.. i18n: resources. They usually prefer to have their own IT service in charge of maintenance.
..

Large and medium-large companies typically install OpenERP using their own internal company
resources. They usually prefer to have their own IT service in charge of maintenance.

.. i18n: Such companies can do the implementation work themselves internally, or turn to an OpenERP partner
.. i18n: who will do the ERP implementation work or assist them with it. Generally, companies prefer to adopt
.. i18n: an intermediate solution which consists of:
..

Such companies can do the implementation work themselves internally, or turn to an OpenERP partner
who will do the ERP implementation work or assist them with it. Generally, companies prefer to adopt
an intermediate solution which consists of:

.. i18n:     #. Turning the initial implementation over to a partner to limit the risks and delays of integration.
.. i18n:        That enables them to be managed by experts and obtain a high quality configuration.
.. i18n: 
.. i18n:     #. Taking charge of the simple needs for themselves once the software has been implemented. It is
.. i18n:        quite a lot more convenient for them to be able to modify the database tables, forms, templates and
.. i18n:        workflows internally than routinely depend on a supplier.
..

    #. Turning the initial implementation over to a partner to limit the risks and delays of integration.
       That enables them to be managed by experts and obtain a high quality configuration.

    #. Taking charge of the simple needs for themselves once the software has been implemented. It is
       quite a lot more convenient for them to be able to modify the database tables, forms, templates and
       workflows internally than routinely depend on a supplier.

.. i18n: An internal installation will probably prove more costly than a SaaS package or hosted service.
.. i18n: Even if you put yourself in charge of it all, you will take quite a bit of time learning how to manage
.. i18n: the implementation unless the team already has an experience of OpenERP. This represents a
.. i18n: significant risk.
..

An internal installation will probably prove more costly than a SaaS package or hosted service.
Even if you put yourself in charge of it all, you will take quite a bit of time learning how to manage
the implementation unless the team already has an experience of OpenERP. This represents a
significant risk.

.. i18n: However, an internal implementation can be particularly interesting when:
..

However, an internal implementation can be particularly interesting when:

.. i18n: * you want to keep your data within your company,
.. i18n: 
.. i18n: * you think you want to modify your software,
.. i18n: 
.. i18n: * you want a specific package of modules,
.. i18n: 
.. i18n: * you would like a very fast response time,
.. i18n: 
.. i18n: * you want the software to be available even if your Internet connection goes down.
..

* you want to keep your data within your company,

* you think you want to modify your software,

* you want a specific package of modules,

* you would like a very fast response time,

* you want the software to be available even if your Internet connection goes down.

.. i18n: These factors, and access to the resources needed to handle an implementation and the subsequent
.. i18n: maintenance, are the reasons that large and medium-large companies usually do it for themselves, at
.. i18n: least partly.
..

These factors, and access to the resources needed to handle an implementation and the subsequent
maintenance, are the reasons that large and medium-large companies usually do it for themselves, at
least partly.

.. i18n: Deployment Procedure
.. i18n: --------------------
..

部署过程
--------------------

.. i18n: The deployment of a version of OpenERP is quite simple when your server has been configured in
.. i18n: your production environment. The security of data will then be a key element.
..

The deployment of a version of OpenERP is quite simple when your server has been configured in
your production environment. The security of data will then be a key element.

.. i18n: When you have installed the server, you should create at least two databases:
..

When you have installed the server, you should create at least two databases:

.. i18n: * a test or development database, in which the users can test the system and familiarize themselves
.. i18n:   with it,
.. i18n: 
.. i18n: * a production database, which will be the one used by the company in daily use.
..

* a test or development database, in which the users can test the system and familiarize themselves
  with it,

* a production database, which will be the one used by the company in daily use.

.. i18n: .. note::  Version Numbering
.. i18n: 
.. i18n: 	OpenERP uses a version numbering model that comprises 3 numbers A.B.C (for example 4.2.2 or
.. i18n: 	5.0.0) where changes in the number A signify a major functional change, changes to number B signify
.. i18n: 	an update that includes a batch of fault fixes and some new functionality, and the number C
.. i18n: 	generally refers to some limited updates or fixes to the existing functionality.
.. i18n: 
.. i18n: 	The number B is special: if it is an odd number, (for example 4.3.2 or 5.1.0) it is for a development
.. i18n: 	version which is not designed for a production environment. The even numbers are for stable
.. i18n: 	versions.
..

.. note::  Version Numbering

	OpenERP uses a version numbering model that comprises 3 numbers A.B.C (for example 4.2.2 or
	5.0.0) where changes in the number A signify a major functional change, changes to number B signify
	an update that includes a batch of fault fixes and some new functionality, and the number C
	generally refers to some limited updates or fixes to the existing functionality.

	The number B is special: if it is an odd number, (for example 4.3.2 or 5.1.0) it is for a development
	version which is not designed for a production environment. The even numbers are for stable
	versions.

.. i18n: If you have prepared a data module for OpenERP (that is a module that consists just of data, not
.. i18n: altered functionality), you should test it in your development version and check that it does not
.. i18n: require any more manual adjustments. If the import runs correctly, it shows that you are ready to
.. i18n: load your data in the production database.
..

If you have prepared a data module for OpenERP (that is a module that consists just of data, not
altered functionality), you should test it in your development version and check that it does not
require any more manual adjustments. If the import runs correctly, it shows that you are ready to
load your data in the production database.

.. i18n: You can use the OpenERP database backup procedure at different stages of configuration (see
.. i18n: :ref:`ch-inst`). Then, if you have made a false step that you cannot recover from, you can always return to a
.. i18n: prior state.
..

You can use the OpenERP database backup procedure at different stages of configuration (see
:ref:`ch-inst`). Then, if you have made a false step that you cannot recover from, you can always return to a
prior state.

.. i18n: Since your data describes much of your company's value, take particular care both when you need to
.. i18n: transfer it (in backups and across your network) and when you are managing the super-administrator
.. i18n: password. Make sure that the connection between a PC client and the two servers is correctly
.. i18n: secured. You can configure OpenERP to use the HTTPS protocol, which provides security for data
.. i18n: transfer
..

Since your data describes much of your company's value, take particular care both when you need to
transfer it (in backups and across your network) and when you are managing the super-administrator
password. Make sure that the connection between a PC client and the two servers is correctly
secured. You can configure OpenERP to use the HTTPS protocol, which provides security for data
transfer

.. i18n: .. index::
.. i18n:    single: HTTPS
..

.. index::
   single: HTTPS

.. i18n: .. note:: HTTPS
.. i18n: 
.. i18n: 	The HTTPS protocol (Secured Hyper Text Transfer Protocol) is the standard HTTP protocol secured by
.. i18n: 	using the SSL (Secure Socket Layer) or TLS (Transport Layer Security) security protocols.
.. i18n: 	It allows a user to verify her identify to the site to which she wants access, using a certificate
.. i18n: 	of authentication.
.. i18n: 	It also guarantees the integrity and confidentiality of the data sent between the user and the
.. i18n: 	server.
.. i18n: 	It can, optionally, provide highly secure client authentication by using a numbered certificate.
.. i18n: 
.. i18n: 	The default HTTPS port is 443.
..

.. note:: HTTPS

	The HTTPS protocol (Secured Hyper Text Transfer Protocol) is the standard HTTP protocol secured by
	using the SSL (Secure Socket Layer) or TLS (Transport Layer Security) security protocols.
	It allows a user to verify her identify to the site to which she wants access, using a certificate
	of authentication.
	It also guarantees the integrity and confidentiality of the data sent between the user and the
	server.
	It can, optionally, provide highly secure client authentication by using a numbered certificate.

	The default HTTPS port is 443.

.. i18n: You could also use the PostgreSQL database directly to backup and restore data on the server,
.. i18n: depending on access rights and the availability of passwords for the server.
..

You could also use the PostgreSQL database directly to backup and restore data on the server,
depending on access rights and the availability of passwords for the server.

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
