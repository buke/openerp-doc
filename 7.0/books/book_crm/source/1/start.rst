OpenERP is an impressive software system, being easy to use and yet providing great benefits
in helping you manage your company.
It is easy to install under both Windows and Linux compared with other enterprise-scale systems,
and offers unmatched functionality.

.. index::
   single: Installation
   single: Initial Setup
   pair: configuration; setup

.. _ch-inst:

Installation and Initial Setup
==============================

Whether you want to test OpenERP or put it into full production, you have at least two possible starting
points:

* you can use OpenERP Online by subscribing to http://www.openerp.com/online/;

* you can install the solution on your own computers to test it in your company's system environment.

In this chapter, the easy-to-use *OpenERP Online* solution will be briefly explained. For more information about installing OpenERP on your computer, please refer to the chapter :ref:`part5-crm-install`.

.. note:: Some Interesting Websites from OpenERP

   * Main Site: http://www.openerp.com,

   * OpenERP Online Site: http://www.openerp.com/online,
   
   * Online demo at http://demo.openerp.com,

   * Documentation site: http://doc.openerp.com/,

   * Community discussion forum where you can often receive assistance: http://www.openerp.com/forum/.

.. tip:: Current documentation

   The procedure for installing OpenERP and its web server are likely to change and improve with
   each new version, so you should always check each release's documentation on the website for the latest installation procedures.

Use OpenERP Online
------------------

.. index::
   single: OpenERP Online

Nothing is easier for you to discover OpenERP than subscribing to the OpenERP Online offer. You just need a web browser to get started.

The Online service can be particularly useful to small companies, that just want to get going quickly at low cost.
You have immediate access to OpenERP's Integrated Management System built on the type of enterprise architecture used in many organizations.

OpenERP's Online offer includes several services: hosting at high bandwidth, database management, stable security update, backups, maintenance (24/7 server monitoring), bug fixing and migrations.

OpenERP guarantees that the software running on OpenERP Online is exactly the same as the Open Source official
version of OpenERP. Any improvement made on OpenERP will be available online. This allows you to easily switch from the online version to the local version anytime.

So even if the OpenERP Online solution might be the best solution to suit your needs today, you can easily switch to an installation on your own servers according to your company's changing requirements or growth. You are also able to change your service provider
anytime, while continuing to use the exact same system. Hence, you do not depend on your host. In addition, OpenERP works with standard and open formats and programming languages which allow
you to export your data and use them in any other software.

These advantages give you total control over your data, your software, your platform.

.. figure:: images/start_saas.jpeg
   :align: center
   :scale: 90

   *Subscribe and Start with OpenERP Online*

If you want to start working with the online platform, you can navigate to http://www.openerp.com/online. After successful registration, you will be able to configure and use OpenERP online. To log in to your OpenERP Online account, you will receive a username and password. You can build the software to fit your needs, at your own pace! 

OpenERP Online - Software as a Service - is hosted by OpenERP and paid in the form of a monthly subscription. The pricing model is extremely simple. OpenERP charges a fixed fee per month per user. You will get an invoice each month according to the number of users registered in the system at that time. If you add new users during the next 30 days, they will only be charged with the next invoice.
You can find the details of current pricing and payment options at http://www.openerp.com/online.

.. tip:: Free Trial

       For a month's free trial, check out OpenERP's http://www.openerp.com/online, which enables you to get started quickly without incurring costs for integration or for buying computer systems. After the free trial expires, you can easily continue using OpenERP Online.

.. _ch-start:

Getting Started with OpenERP Online
-----------------------------------

.. todo:: to be reviewed according to specs for connecting to Online

If you want to focus on your customers, you need tools: to capture all the knowledge you have available; to help you analyze what you know; to make it easy to use all of that knowledge and analysis. OpenERP invites you to discover the CRM & Sales Management Business Application!

In this chapter, you can start exploring OpenERP!

Use a web browser of your choice to connect to OpenERP Web.

.. figure:: images/web_startup_new.png
   :scale: 80
   :align: center

   *Web Client at Startup*

OpenERP suggests that you configure your database using a series of questions. In the software, these series of questions are managed through so-called ``Configuration Wizards``.

Click the ``Start Configuration`` button to continue.

The next configuration wizard will help you to decide what your user interface will look like, whether the screens will only show the most important fields - ``Simplified`` - or whether you also want to see the fields for the more advanced users, the ``Extended`` view. Select ``Extended`` and click :guilabel:`Next` to continue.

.. tip:: User Preferences

       You can easily switch from Simplified to Extended view by changing your `User Preferences`.

In the next wizard, you can fill your company data, select your company's base currency and add your company logo which can be printed on reports. Click :guilabel:`Next` to continue.

Select the ``Customer Relationship Management`` and ``Sales Management`` business applications for installation and click :guilabel:`Install`. Now OpenERP will start to install CRM & Sales, allowing you to do a complete sales cycle, from lead / opportunity to quotation and sales order. You will have to wait for the next configuration wizard to be displayed (*Loading* will appear).

.. figure:: images/install_ba.jpeg
   :scale: 80
   :align: center

   *Selecting the CRM & Sales Functionality*

OpenERP's modularity enables you to install a single Business Application (such as CRM) if that is all you need.
Of course, you can choose to also install Sales Management, to handle quotations, sales orders and sales invoices as well.
For now, please install ``Customer Relationship Management`` and ``Sales Management``, as these two Business Applications will be discussed in this book.

.. tip:: Reconfigure

      Keep in mind that you can change or reconfigure the system any time, for instance through the `Reconfigure` option in the main bar.

When you choose a business application for installation, OpenERP will automatically propose to add or configure related (smaller) applications to enrich your system. When you install CRM, OpenERP will also ask you whether you want to install Fetchmail, or Sales FAQ, for instance.

The figure :ref:`fig-accconwiz` shows the Accounting Application Configuration screen that appears when you select ``Sales Management`` to be installed.

.. _fig-accconwiz:

.. figure:: images/crm_account.jpeg
   :scale: 80
   :align: center

   *Selecting Accounting Configuration*

Indeed, accounting is required to create sales invoices. Select the `Generic Chart of Account` and fill in the Sale Tax (%) applicable in your country. Click `Configure` to continue the configuration. 

.. note:: Accounting

       Please note that you can perfectly well use OpenERP's CRM without doing your accounting in OpenERP. When you only install CRM, there is no need to configure accounting.


OpenERP CRM offers lots of features. You can easily manage your address book (prospects, customers, ...), keep track of leads and/or opportunities, manage meetings & phone calls, share (sales) knowledge and much more.

The figure :ref:`fig-crmconwiz` shows the CRM Application Configuration screen that appears when you select ``Customer Relationship Management`` to be installed.

.. _fig-crmconwiz:

.. figure:: images/crm_configuration_wizard.jpeg
   :scale: 80
   :align: center

   *Selecting CRM Configuration*

To stay in line with what will be described later in this book, please install the following options:

* ``Opportunity to Quotation`` will be checked by default, allowing you to create quotations from an opportunity,

* ``Sale FAQ`` to install a company wiki to share your sales knowledge,

* ``Calendar Synchronizing`` to link your OpenERP calendar to your mobile device, for instance,

* ``Fetch Emails`` to manage incoming and outgoing emails in OpenERP directly,

* ``Thunderbird`` or ``Outlook`` according to the email client you are using, to link your current mailbox to OpenERP and to create new leads or partners in OpenERP, directly from your mailbox.

If you have selected all of the above options, the following Configuration Wizards will appear:

* Configure your *Sales* application: click ``Configure`` to accept the default settings (no options checked).

* Configure your *Knowledge* application: click ``Configure`` to accept the default settings.

* *Thunderbird / Outlook* Plug-in Configuration: for now, you only have to click the ``Save as`` button to save the plug-in to your disk (or desktop). Then you can click ``Configure`` to continue the installation. 

* Configure your *Accounting* application: click ``Configure`` to accept the default settings.

* Configure your *Sales* application: click ``Configure`` to accept the default settings.

* *Knowledge* application configuration: click ``Next`` to accept the default settings for the server address.

.. note:: Plug-ins 

        For the configuration of the plug-in, please refer to the settings in chapter :ref:`thunder` or :ref:`outl`.

OpenERP's menu will be displayed, because your system is now ready for actual configuration. To get started, you click the Sales button in OpenERP's main screen. In the next chapter :ref:`ch-team` you will start working in the CRM application by telling OpenERP how your company's sales teams are organized.

As your business is growing and evolving all the time, your requirements as to the use of OpenERP are likely to change. To sustain your growth, you can easily extend your CRM with other OpenERP business applications, such as logistics or HR, to name some. OpenERP offers this flexibility; you can start with one business application, such as Customer Relationship Management, and gradually complete OpenERP to suit your ever changing needs! 

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


