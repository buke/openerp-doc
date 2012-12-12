
.. index::
   single: Configuration
   single: Administration

.. _ch-config:

******************************
Configuration & Administration
******************************

 *This chapter is for the administrators of an OpenERP system.
 You will learn to configure OpenERP to match it to your company's needs and
 those of each individual user of the system.*

OpenERP gives you great flexibility in configuring and using it, letting you modify
its appearance, the general way it functions and the different analysis tools chosen to match your
company's needs most closely. These configuration changes are carried out through the user
interface.

Users can each arrange their own welcome page and their own menu, and you can also personalize
OpenERP by assigning each user their own dashboard on their welcome page to provide them with the
most up to date information. Then, they can immediately see the information most relevant to them
each time they sign in.

And OpenERP's main menu can be entirely reorganized. The management of access rights lets you
assign certain functions to specific system users. You can also assign groups to the user,
which lets him move system documents from state to state (such as
the ability to approve employee expense requests).

.. index::
   single: configuration
   single: configuration; parametrization
   single: configuration; personalization
   single: configuration; customization
   single: configuration; setup
..

.. note:: Configuration, Parametrization, Personalization, Customization

	The word *personalization* is sometimes used in this book where you might expect to find
	*configuration* or *customization*.

	*Customization* generally refers to something that requires a bit of technical effort
	(such as creating specialized code modules) and creates a non-standard system.

	*Configuration* is less radical – it is the general process of setting all
	the parameters of the software to fit the needs of your system (often called *parametrization* or *setup*).
	Configuration is also, by convention, the name of the sub-menu below each of OpenERP's top-level menus that
	is accessible only to the administrative user for that section.

	*Personalization* is just that subset of configuration options that shapes the system to the
	particular operational and/or stylistic wishes of a person or company.

Using the *OpenOffice Report Designer* module (:mod:`base_report_designer`), you can change any part of any of the reports
produced by the system. The system administrator can configure each report to modify its layout and
style, or even the data that is provided there.

.. note::  The OpenOffice Report Designer

	The OpenOffice Report Designer plug-in enables you not only to configure the reports of the basic products in
	OpenERP, but also to create entirely new report templates.
	When the user uses OpenERP's client interface, OpenOffice can create a report template 
	that has access to all the data available to any OpenERP document type.

	You can easily create fax documents, quotations, or any other commercial document.
	This functionality enables you to considerably extend the productivity of your salespeople who have
	to send many proposals to customers.

Finally, you will see how to import your data into OpenERP automatically, to migrate all of your
data in one single go.

For this chapter, you should start with a fresh database that includes demo data,
with :mod:`sale` and its dependencies installed and no particular chart of accounts configured. 

.. raw:: html

    <div class="all-toctree">

.. toctree::

    8_20_Config_module
    8_20_Config_menu
    8_20_Config_accessRights
    8_20_Config_workflow
    8_20_Config_reports
    8_20_Config_import_export

.. raw:: html

    </div>
    
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

