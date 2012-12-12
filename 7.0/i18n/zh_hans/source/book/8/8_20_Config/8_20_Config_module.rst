
.. i18n: .. index::
.. i18n:    pair: configuring; module
..

.. index::
   pair: configuring; module

.. i18n: Creating a Configuration Module
.. i18n: ===============================
..

Creating a Configuration Module
===============================

.. i18n: It is very helpful to be able to backup your specific configuration settings in an OpenERP module
.. i18n: dedicated just to that. This enables you to:
..

It is very helpful to be able to backup your specific configuration settings in an OpenERP module
dedicated just to that. This enables you to:

.. i18n: * automatically duplicate the configuration settings by installing the module in another database,
.. i18n: 
.. i18n: * reinstall a clean database with your own configuration, in case you have problems with the initial
.. i18n:   configuration,
.. i18n: 
.. i18n: * simplify migrations. If you have modified some elements of the basic configuration, there is a risk
.. i18n:   in returning them to their original state after the migration, unless you have saved the modifications
.. i18n:   in a module.
..

* automatically duplicate the configuration settings by installing the module in another database,

* reinstall a clean database with your own configuration, in case you have problems with the initial
  configuration,

* simplify migrations. If you have modified some elements of the basic configuration, there is a risk
  in returning them to their original state after the migration, unless you have saved the modifications
  in a module.

.. i18n: .. index::
.. i18n:    single: module; base_module_record
..

.. index::
   single: module; base_module_record

.. i18n: Start by installing the module :mod:`base_module_record` in the usual way from
.. i18n: :menuselection:`Administration --> Modules --> Modules`. Manually make all your
.. i18n: configuration changes through the user
.. i18n: interface as you would normally do (such as menu management, dashboard assignments, screen
.. i18n: configuration, new reports, and access rights management – details of some of these possibilities
.. i18n: are described later in this chapter).
..

Start by installing the module :mod:`base_module_record` in the usual way from
:menuselection:`Administration --> Modules --> Modules`. Manually make all your
configuration changes through the user
interface as you would normally do (such as menu management, dashboard assignments, screen
configuration, new reports, and access rights management – details of some of these possibilities
are described later in this chapter).

.. i18n: Then start recording
.. i18n: your data using the menu :menuselection:`Administration --> Customization --> Module Creation -->
.. i18n: Export Customizations As a Module`. This opens a wizard through which you may select the date to record
.. i18n: from, choose records that have been \ ``Created`` \, \ ``Modified`` \ or both \ ``Created & Modified`` \.
.. i18n: You have to select the objects for recording and then start recording by clicking :guilabel:`Record`.
.. i18n: After the recording operation is complete, a dialog box appears giving you the opportunity to save
.. i18n: the recorded module at a desired location.
..

Then start recording
your data using the menu :menuselection:`Administration --> Customization --> Module Creation -->
Export Customizations As a Module`. This opens a wizard through which you may select the date to record
from, choose records that have been \ ``Created`` \, \ ``Modified`` \ or both \ ``Created & Modified`` \.
You have to select the objects for recording and then start recording by clicking :guilabel:`Record`.
After the recording operation is complete, a dialog box appears giving you the opportunity to save
the recorded module at a desired location.

.. i18n: OpenERP then creates a ZIP file for you containing all of the modifications you made while you
.. i18n: were carrying out your configuration work. You could reinstall this module on other databases.
.. i18n: This could turn out to be useful if you want to install a
.. i18n: test server for your company's users and give them the same configuration as the production server.
..

OpenERP then creates a ZIP file for you containing all of the modifications you made while you
were carrying out your configuration work. You could reinstall this module on other databases.
This could turn out to be useful if you want to install a
test server for your company's users and give them the same configuration as the production server.

.. i18n: To install a new module saved in ZIP file form, use the menu :menuselection:`Administration -->
.. i18n: Modules --> Import Module`.
..

To install a new module saved in ZIP file form, use the menu :menuselection:`Administration -->
Modules --> Import Module`.

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
