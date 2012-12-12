=========
Appendice
=========

Conventions
===========

Guidelines
----------
For guidelines and general recommendations with regard to the development of OpenERP modules,
please refer to the :ref:`Guidelines <contribution_guidelines-link>` of the
:doc:`Contribution section </contribute/index>`.


Module structure and file names
-------------------------------

The structure of a module should be::

    /module/

        /__init__.py
        /__openerp__.py
        /module.py
        /module_other.py
        /module_view.xml
        /module_data.xml
        /module_demo.xml

        /wizard/
        /wizard/__init__.py
        /wizard/wizard_name.py

        /report/
        /report/
        /report/__init__.py
        /report/report_name.sxw
        /report/report_name.rml
        /report/report_name.py


Naming conventions
------------------

    * modules: modules must be written in lower case, with underscores. The name of the module is the name of the directory in the addons path of the server. If the module depends on other modules, you can write several module names separated by underscores, starting by the most important name. Example:
          + sale
          + sale_commission 

    * objects: the name of an object must be of the form name_of_module.name1.name2.name3.... The namei part of the object must go from the most important name to the least important one, from left to right, in lower case. Try not to use plurals in object names and to avoid shortcuts in the names. Example:
          + sale.order
          + sale.order.line
          + sale.shop
          + sale_commission.commission.rate 

    * fields: field must be in lowercase, separated by underscores. Try to use commonly used names for fields: name, state, active, partner_id, eso. Conventions for the field name depends on the field type:
          + many2one: must end by '_id' (eg: partner_id, order_line_id)
          + many2many: must end by '_ids' (eg: category_ids)
          + one2many: must end by '_ids' (eg: line_ids


Translations
============

OpenERP is multilingual. You can add as many languages as you wish. Each user may work with the interface in his own language. Moreover, some resources (the text of reports, product names, etc.) may also be translated.

This section explains how to change the language of the program shown to individual users, and how to add new languages to OpenERP.

Nearly all the labels used in the interface are stored on the server. In the same way, the translations are also stored on the server. By default the English dictionary is stored on the server, so if the users want to try OpenERP in a language other than English you must store these languages definitions on the server.

However, it is not possible to store "everything" on the server. Indeed, the user gets some menus, buttons, etc... that must contain some text *even before* being connected to the server. These few words and sentences are translated using GETTEXT. The chosen language by default for these is the language of the computer from which the user connects.

The translation system of OpenERP is not limited to interface texts; it also works with reports and the "content" of some database fields. Obviously, not all the database fields need to be translated. The fields where the content is multilingual are marked thus by a flag icon.


.. TODO: add image
.. .. figure:: images/field_flag.png
..    :scale: 120
..    :align: left

	
How to change the language of the user interface ?
--------------------------------------------------

The language is a user preference. To change the language of the current user, click on the menu: User > Preferences.

.. TODO: add image
.. .. figure:: images/trans_user_pref.png
..    :scale: 120
..    :align: left


An administrator may also modify the preferences of a user (including the language of the interface) in the menu: Administration > Users > Users. He merely has to choose a user and toggle on "preferences".

.. TODO: add image
.. .. figure:: images/menu_bar_pref.png
..    :scale: 120
..    :align: left


Store a translation file on the server
--------------------------------------

To import a file having translations, use this command:

    ./openerp_server.py --i18n-import=file.csv -l **LANG** 

where **LANG** is the language of the translation data in the CSV file.

Note that the translation file must be encoded in **UTF8!**

Translate to a new language
---------------------------

**Please keep in mind to use the same translation string for identical sources**	. Launchpad Online Translation may give helpful hints.

More information on accelerators on this website: http://translate.sourceforge.net/wiki/guide/translation/accelerators

To translate or modify the translation of a language already translated, you have to:

1. Export all the sentences to translate in a CSV file
+++++++++++++++++++++++++++++++++++++++++++++++++++++++

To export this file, use this command:

        ./openerp_server.py --i18n-export=file.csv -l**LANG** 

where **LANG** is the language to which you want to translate the program.

2. Translate the last column of the file
++++++++++++++++++++++++++++++++++++++++

You can make a translation for a language, which has already been translated or for a new one. If you ask for a language already translated, the sentences already translated will be written in the last column.

For example, here are the first lines of a translation file (Dutch):
 
+--------+------------------------+---------+----------------+--------------------+
| type   | name                   | res_id  |      src       |   value            |
+--------+------------------------+---------+----------------+--------------------+
| field  | "account.account,code" |  0      |    Code        |    Code            |
+--------+------------------------+---------+----------------+--------------------+
|  field | "account.account,name" |  0      |    Name        |   Name             |
+--------+------------------------+---------+----------------+--------------------+
|  model | "account.account,name" |  2      |    Assets      |   Aktiva           |
+--------+------------------------+---------+----------------+--------------------+
|  model | "account.account,name" |  25     |    Results     |   Salden           |
+--------+------------------------+---------+----------------+--------------------+
|  model | "account.account,name" |   61    |    Liabilities |  Verbindlichkeiten |
+--------+------------------------+---------+----------------+--------------------+

3. Import this file into OpenERP (as explained in the preceding section)
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

**Notes**

    * You should perform all these tasks on an empty database, so as to avoid over-writing data. 

To create a new database (named 'terp_test'), use these commands:

    createdb terp_test --encoding=unicode 
    terp_server.py --database=terp_test --init=all 

Alternatively, you could also delete your current database with these:

    dropdb terp 
    createdb terp --encoding=unicode 
    terp_server.py --init=all 

4. Using Launchpad / Rosetta to translate modules and applications
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

A good starting point is here https://launchpad.net/openobject

**Online**

Select the module translation section and enter your translation.

**Offline**

Use this, if you want to translate some 100 terms.

It seems mandatory to follow theses steps to successfully complete a translation cycle. (tested on Linux)

   1. Download the <po file> from Launchpad
   2. Get the message template file <pot file> from bzr branches
         1. keep in mind that the <pot file> might not always contain all strings, the <pot files> are updated irregularly.
         2. msgmerge <pot file> <po file> -o <new po file> 
   3. translate <new po file> using poedit, kbabel (KDE)
         1. some programs (like kbabel) allow using dictionaries to create rough translations.
         2. It is especially useful to create a complete dictionary from existing translations to reuse existing terms related to the application.
               1. In OpenERP load most/all of the modules
               2. Load your language
               3. export all modules of your language as po file and use this one as dictionary. Depending on context of the module this creates 30-80% exact translations. 
   4. the <new po file> must not contain <fuzzy> comments inserted by kbabel for rough translation
         1. grep -v fuzzy <new po file> > <po file> 
   5. check for correct spelling
         1. msgfmt <po file> -o <mo file> 
   6. check your translation for correct context
         1. import the <po file> (for modules)
         2. install the <mo file> and restart the application (for applications) 
   7. adjust the translation Online in OpenERP
         1. check context
         2. check length of strings
         3. export <po file> 
   8. upload <po file> to Launchpad
         1. keep in mind that Launchpad / Rosetta uses some tags (not sure which) in the header section of the exported <po file> to recognize the imported <po file> as valid.
         2. after some time (hours) you will receive a confirmation E-Mail (success / error) 

Using context Dictionary for Translations
-----------------------------------------

The context dictionary is explained in details in section "The Objects - Methods - The context Dictionary". If an additional language is installed using the Administration menu, the context dictionary will contain an additional key : lang. For example, if you install the French language then select it for the current user, his or her context dictionary will contain the key lang to which will be associated the value *fr_FR*. 


.. _tech_memento_link:

.. index::
    pair: cheat; sheet
    single: cheatsheet
    single: memento
    single: reference

Technical Memento
=================

A technical reference memento is available, to be used as a quick reference guide for
OpenERP developers, often nicknamed a "cheat sheet".

.. |t| image:: ../images/pdf.png
    :target: http://doc.openerp.com/memento
    :align: bottom

* |t| `Technical Memento <http://doc.openerp.com/memento>`_ 

The memento is usually updated for each `major version <release_cycle>`_ of OpenERP,
and contains a global overview of OpenERP's Application Programming Interface,
including the declaration of modules, the ORM, the XML syntax, Dynamic views and Workflows.
The memento is not an extensive reference, but a way to quickly find out how
a certain OpenERP feature is accessed or used. Therefore each topic is only described
in a few words, usually with a small example.

The examples in the technical memento all come from the example module ``idea``, which
allows an organisation to manage the generic *ideas* submitted by its members.

There are 2 versions of the memento. One is suited for printing in A4 landscape mode,
with 3 columns of text per page, so that the whole memento is contained in less than 20
mini-pages (columns). The idea is to print and bind these pages as a reference booklet.
The second version contains some more details and is formatted in A4 portrait
mode, making it easier to read, but larger.

All versions of the technical memento (including previous ones) can be found at this
location: |t| `Technical Memento <http://doc.openerp.com/memento>`_


Information Repository
======================

The information repository is a semantics tree in which the data that are not the resources are stored. We find in this structure:

   1. the values by default
   2. the conditional values;
          * the state depends on the zip code,
          * the payment method depends of the partner, ...
   3. the reactions to the events client;
          * click on the invoice menu,
          * print an invoice,
          * action on a partner, ...

The IR has 3 methods;

    * add a value in the tree
    * delete a value in the tree
    * obtain all the values of a selected sheet


Setting Value
-------------

The ir_set tag allows you to insert new values in the  "Information
Repository". This tag must contain several *field* tags with *name* and *eval*
attributes.

The attributes are those defined by the access methods to the information
repository. We must provide it with several attributes: *keys*, *args*, *name*,
*value*, *isobject*, *replace*, *meta* and some optional fields.

Example:

.. code-block:: xml

    <ir_set>
        <field name="keys" eval="[('action','client_print_multi'),('res_model','account.invoice')]"/>
        <field name="args" eval="[]"/>
        <field name="name">Print Invoices</field>
        <field name="value" eval="'ir.actions.report.xml,'+str(l0)"/>
        <field name="isobject" eval="True"/>
        <field name="replace" eval="False"/>
    </ir_set>


IR Methods
-----------

.. code-block:: python

    def ir_set(cr, uid, key, key2, name, models, value, replace=True, isobject=False, meta=None)

.. code-block:: python

    def ir_get(cr, uid, key, key2, models, meta=False, context={}, res_id_req=False)

.. code-block:: python

    def ir_del(cr, uid, id):


:Description of the fields:

   1. key:
   2. key2:
   3. name:
   4. models:
   5. value:
   6. isobject:
   7. replace: whether or not the action described should override an existing action or be appended to the list of actions.
   8. meta:

:Using ir_set and ir_get:

.. code-block:: python

    ...

        res = ir.ir_set(cr, uid, key, key2, name, models, value, replace, isobject, meta)

    ...


    ...

        if not report.menu_id:

            ir.ir_set(cr, uid, 'action', 'client_print_multi', name, [(model, False)], action, False, True)

        else:

            ir.ir_set(cr, uid, 'action', 'tree_but_open', 'Menuitem', [('ir.ui.menu', int(m_id))], action, False, True)

    ...


    ...

        res = ir.ir_get(cr, uid, [('default', self._name), ('field', False)], [('user_id',str(uid))])

    ...

        account_payable = ir.ir_get(cr, uid, [('meta','res.partner'), ('name','account.payable')], opt)[0][2]

    ...

