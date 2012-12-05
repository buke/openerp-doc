
.. i18n: .. index::
.. i18n:    single: Configuration
.. i18n:    single: Administration
..

.. index::
   single: Configuration
   single: Administration

.. i18n: .. _ch-config:
.. i18n: 
.. i18n: ******************************
.. i18n: Configuration & Administration
.. i18n: ******************************
..

.. _ch-config:

******************************
Configuration & Administration
******************************

.. i18n:  *This chapter is for the administrators of an OpenERP system.
.. i18n:  You will learn to configure OpenERP to match it to your company's needs and
.. i18n:  those of each individual user of the system.*
..

 *This chapter is for the administrators of an OpenERP system.
 You will learn to configure OpenERP to match it to your company's needs and
 those of each individual user of the system.*

.. i18n: OpenERP gives you great flexibility in configuring and using it, letting you modify
.. i18n: its appearance, the general way it functions and the different analysis tools chosen to match your
.. i18n: company's needs most closely. These configuration changes are carried out through the user
.. i18n: interface.
..

OpenERP gives you great flexibility in configuring and using it, letting you modify
its appearance, the general way it functions and the different analysis tools chosen to match your
company's needs most closely. These configuration changes are carried out through the user
interface.

.. i18n: Users can each arrange their own welcome page and their own menu, and you can also personalize
.. i18n: OpenERP by assigning each user their own dashboard on their welcome page to provide them with the
.. i18n: most up to date information. Then, they can immediately see the information most relevant to them
.. i18n: each time they sign in.
..

Users can each arrange their own welcome page and their own menu, and you can also personalize
OpenERP by assigning each user their own dashboard on their welcome page to provide them with the
most up to date information. Then, they can immediately see the information most relevant to them
each time they sign in.

.. i18n: And OpenERP's main menu can be entirely reorganized. The management of access rights lets you
.. i18n: assign certain functions to specific system users. You can also assign groups to the user,
.. i18n: which lets him move system documents from state to state (such as
.. i18n: the ability to approve employee expense requests).
..

And OpenERP's main menu can be entirely reorganized. The management of access rights lets you
assign certain functions to specific system users. You can also assign groups to the user,
which lets him move system documents from state to state (such as
the ability to approve employee expense requests).

.. i18n: .. index::
.. i18n:    single: configuration
.. i18n:    single: configuration; parametrization
.. i18n:    single: configuration; personalization
.. i18n:    single: configuration; customization
.. i18n:    single: configuration; setup
.. i18n: ..
..

.. index::
   single: configuration
   single: configuration; parametrization
   single: configuration; personalization
   single: configuration; customization
   single: configuration; setup
..

.. i18n: .. note:: Configuration, Parametrization, Personalization, Customization
.. i18n: 
.. i18n: 	The word *personalization* is sometimes used in this book where you might expect to find
.. i18n: 	*configuration* or *customization*.
.. i18n: 
.. i18n: 	*Customization* generally refers to something that requires a bit of technical effort
.. i18n: 	(such as creating specialized code modules) and creates a non-standard system.
.. i18n: 
.. i18n: 	*Configuration* is less radical – it is the general process of setting all
.. i18n: 	the parameters of the software to fit the needs of your system (often called *parametrization* or *setup*).
.. i18n: 	Configuration is also, by convention, the name of the sub-menu below each of OpenERP's top-level menus that
.. i18n: 	is accessible only to the administrative user for that section.
.. i18n: 
.. i18n: 	*Personalization* is just that subset of configuration options that shapes the system to the
.. i18n: 	particular operational and/or stylistic wishes of a person or company.
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

.. i18n: Using the *OpenOffice Report Designer* module (:mod:`base_report_designer`), you can change any part of any of the reports
.. i18n: produced by the system. The system administrator can configure each report to modify its layout and
.. i18n: style, or even the data that is provided there.
..

Using the *OpenOffice Report Designer* module (:mod:`base_report_designer`), you can change any part of any of the reports
produced by the system. The system administrator can configure each report to modify its layout and
style, or even the data that is provided there.

.. i18n: .. note::  The OpenOffice Report Designer
.. i18n: 
.. i18n: 	The OpenOffice Report Designer plug-in enables you not only to configure the reports of the basic products in
.. i18n: 	OpenERP, but also to create entirely new report templates.
.. i18n: 	When the user uses OpenERP's client interface, OpenOffice can create a report template 
.. i18n: 	that has access to all the data available to any OpenERP document type.
.. i18n: 
.. i18n: 	You can easily create fax documents, quotations, or any other commercial document.
.. i18n: 	This functionality enables you to considerably extend the productivity of your salespeople who have
.. i18n: 	to send many proposals to customers.
..

.. note::  The OpenOffice Report Designer

	The OpenOffice Report Designer plug-in enables you not only to configure the reports of the basic products in
	OpenERP, but also to create entirely new report templates.
	When the user uses OpenERP's client interface, OpenOffice can create a report template 
	that has access to all the data available to any OpenERP document type.

	You can easily create fax documents, quotations, or any other commercial document.
	This functionality enables you to considerably extend the productivity of your salespeople who have
	to send many proposals to customers.

.. i18n: Finally, you will see how to import your data into OpenERP automatically, to migrate all of your
.. i18n: data in one single go.
..

Finally, you will see how to import your data into OpenERP automatically, to migrate all of your
data in one single go.

.. i18n: For this chapter, you should start with a fresh database that includes demo data,
.. i18n: with :mod:`sale` and its dependencies installed and no particular chart of accounts configured. 
..

For this chapter, you should start with a fresh database that includes demo data,
with :mod:`sale` and its dependencies installed and no particular chart of accounts configured. 

.. i18n: .. raw:: html
.. i18n: 
.. i18n:     <div class="all-toctree">
..

.. raw:: html

    <div class="all-toctree">

.. i18n: .. toctree::
.. i18n: 
.. i18n:     8_20_Config_module
.. i18n:     8_20_Config_menu
.. i18n:     8_20_Config_accessRights
.. i18n:     8_20_Config_workflow
.. i18n:     8_20_Config_reports
.. i18n:     8_20_Config_import_export
..

.. toctree::

    8_20_Config_module
    8_20_Config_menu
    8_20_Config_accessRights
    8_20_Config_workflow
    8_20_Config_reports
    8_20_Config_import_export

.. i18n: .. raw:: html
.. i18n: 
.. i18n:     </div>
.. i18n:     
.. i18n: .. Copyright © Open Object Press. All rights reserved.
..

.. raw:: html

    </div>
    
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
