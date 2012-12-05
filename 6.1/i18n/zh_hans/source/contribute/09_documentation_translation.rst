.. i18n: .. _documentation_translation:
.. i18n: 
.. i18n: OpenERP Documentation Translation
.. i18n: =================================
..

.. _documentation_translation:

OpenERP 文档翻译
=================================

.. i18n: Prerequisite
.. i18n: ------------
..

先决条件
------------

.. i18n: You should be able to build the untranslated documentation. So `Sphinx
.. i18n: <http://sphinx.pocoo.org>`_ should be installed on your system and you should
.. i18n: know how to use it.
..

You should be able to build the untranslated documentation. So `Sphinx
<http://sphinx.pocoo.org>`_ should be installed on your system and you should
know how to use it.

.. i18n: If this is not the case, please read about :ref:`building_documentation` in the
.. i18n: Community Guide.
..

If this is not the case, please read about :ref:`building_documentation` in the
Community Guide.

.. i18n: You can download the sources of the documentation from launchpad:
..

You can download the sources of the documentation from launchpad:

.. i18n:   bzr branch lp:openobject-doc
..

  bzr branch lp:openobject-doc

.. i18n: Understanding the directory structure
.. i18n: -------------------------------------
..

理解目录结构
-------------------------------------

.. i18n: We are supposing that **<openobject-doc>** is the root of the Open Object
.. i18n: documentation bazaar branch.
..

We are supposing that **<openobject-doc>** is the root of the Open Object
documentation bazaar branch.

.. i18n: The *untranslated sources* are located in **<openobject-doc>/source**.
..

The *untranslated sources* are located in **<openobject-doc>/source**.

.. i18n: The translated documentation will be located in **<openobject-doc>>/i18n/<lang>/source**.
..

The translated documentation will be located in **<openobject-doc>>/i18n/<lang>/source**.

.. i18n: For example, the documentation in French will be
.. i18n: located in **<openobject-doc>/i18n/fr/source** and it will be built
.. i18n: in **<openobject-doc>/i18n/fr/build/html** for example.
..

For example, the documentation in French will be
located in **<openobject-doc>/i18n/fr/source** and it will be built
in **<openobject-doc>/i18n/fr/build/html** for example.

.. i18n: Summary
.. i18n: +++++++
..

总览
+++++++

.. i18n: .. csv-table::
.. i18n:     :header: "Directory", "Description"
.. i18n:     :widths: 5,5
.. i18n: 
.. i18n:     <openobject-doc>/source,untranslated sources
.. i18n:     <openobject-doc>/i18n/<lang>/source,translated sources
.. i18n:     <openobject-doc>/i18n/<lang>/build/html,translated documentation in html
..

.. csv-table::
    :header: "Directory", "Description"
    :widths: 5,5

    <openobject-doc>/source,untranslated sources
    <openobject-doc>/i18n/<lang>/source,translated sources
    <openobject-doc>/i18n/<lang>/build/html,translated documentation in html

.. i18n: Creating the translation directory structure
.. i18n: --------------------------------------------
..

创建翻译目录结构
--------------------------------------------

.. i18n: Use the **make** command (with target **i18n**) to create the translation
.. i18n: templates. You'll need to pass the language as an additional parameter to the *make* command.
..

Use the **make** command (with target **i18n**) to create the translation
templates. You'll need to pass the language as an additional parameter to the *make* command.

.. i18n: For example, supposing you want to translate the documentation in French: ::
.. i18n: 
.. i18n:   make i18n LANG=fr
..

For example, supposing you want to translate the documentation in French: ::

  make i18n LANG=fr

.. i18n: This command will do several things:
..

This command will do several things:

.. i18n: * create these directories, if they does not exist yet:
.. i18n: 
.. i18n:   * i18n
.. i18n:   * i18n/fr
.. i18n:   * i18n/fr/source
.. i18n:   * i18n/fr/build
.. i18n: 
.. i18n: * copy files in *i18n/fr/* required for the html build:
.. i18n: 
.. i18n:   * MakeFile
.. i18n:   * conf.py
.. i18n: 
.. i18n: * create the *translation templates* based on the untranslated restructured text files. They will be created in *i18n/fr/source*
.. i18n: 
.. i18n: * copy all the other necessary files (images for example)
..

* create these directories, if they does not exist yet:

  * i18n
  * i18n/fr
  * i18n/fr/source
  * i18n/fr/build

* copy files in *i18n/fr/* required for the html build:

  * MakeFile
  * conf.py

* create the *translation templates* based on the untranslated restructured text files. They will be created in *i18n/fr/source*

* copy all the other necessary files (images for example)

.. i18n: Translation templates
.. i18n: ---------------------
..

翻译模版
---------------------

.. i18n: The template structure for a given file is very simple. Each text section is
.. i18n: prepended by the original context. Here is a title, for example: ::
.. i18n: 
.. i18n:   .. i18n: %%%%%%%%%%%%%%%%%%%%%%%%%
.. i18n:   .. i18n: Open Object Documentation
.. i18n:   .. i18n: %%%%%%%%%%%%%%%%%%%%%%%%%
.. i18n: 
.. i18n:   %%%%%%%%%%%%%%%%%%%%%%%%%
.. i18n:   Open Object Documentation
.. i18n:   %%%%%%%%%%%%%%%%%%%%%%%%%
..

The template structure for a given file is very simple. Each text section is
prepended by the original context. Here is a title, for example: ::

  .. i18n: %%%%%%%%%%%%%%%%%%%%%%%%%
  .. i18n: Open Object Documentation
  .. i18n: %%%%%%%%%%%%%%%%%%%%%%%%%

  %%%%%%%%%%%%%%%%%%%%%%%%%
  Open Object Documentation
  %%%%%%%%%%%%%%%%%%%%%%%%%

.. i18n: The context is a commented section starting with **.. i18n:**. It helps you
.. i18n: understand the section in context. It also helps you remember the original
.. i18n: section.
..

The context is a commented section starting with **.. i18n:**. It helps you
understand the section in context. It also helps you remember the original
section.

.. i18n: And here is the translated section: ::
.. i18n: 
.. i18n:   .. i18n: %%%%%%%%%%%%%%%%%%%%%%%%%
.. i18n:   .. i18n: Open Object Documentation
.. i18n:   .. i18n: %%%%%%%%%%%%%%%%%%%%%%%%%
.. i18n: 
.. i18n:   %%%%%%%%%%%%%%%%%%%%%%%%%%%%%
.. i18n:   Documentation sur Open Object
.. i18n:   %%%%%%%%%%%%%%%%%%%%%%%%%%%%%
..

And here is the translated section: ::

  .. i18n: %%%%%%%%%%%%%%%%%%%%%%%%%
  .. i18n: Open Object Documentation
  .. i18n: %%%%%%%%%%%%%%%%%%%%%%%%%

  %%%%%%%%%%%%%%%%%%%%%%%%%%%%%
  Documentation sur Open Object
  %%%%%%%%%%%%%%%%%%%%%%%%%%%%%

.. i18n: Managing source changes
.. i18n: -----------------------
..

源文件更改管理
-----------------------

.. i18n: If someone adds or changes something in the documentation, that section will
.. i18n: have to be retranslated but all the other sections should keep their
.. i18n: translation.
..

If someone adds or changes something in the documentation, that section will
have to be retranslated but all the other sections should keep their
translation.

.. i18n: When you get the documentation changes with bzr pull (for example), the
.. i18n: new sections and some changed sections will be reset to the untranslated text
.. i18n: when you will rebuild the translation with *make i18n LANG=fr*.
..

When you get the documentation changes with bzr pull (for example), the
new sections and some changed sections will be reset to the untranslated text
when you will rebuild the translation with *make i18n LANG=fr*.

.. i18n: Building the documentation in your language
.. i18n: -------------------------------------------
..

以您的语言生成文档
-------------------------------------------

.. i18n: That is very simple because the directory and file structure is exactly the
.. i18n: same as the original structure: ::
.. i18n: 
.. i18n:   i18n
.. i18n:   `-- fr
.. i18n:       |-- build
.. i18n:       `-- source
..

That is very simple because the directory and file structure is exactly the
same as the original structure: ::

  i18n
  `-- fr
      |-- build
      `-- source

.. i18n: For example, in *i18n/fr*, you just have to do a simple *make*::
.. i18n: 
.. i18n:   make html
..

For example, in *i18n/fr*, you just have to do a simple *make*::

  make html

.. i18n: And the html documentation will be built in *i18n/fr/build/html*.
..

And the html documentation will be built in *i18n/fr/build/html*.

.. i18n: Uploading to Launchpad
.. i18n: ----------------------
..

上传到Launchpad
----------------------

.. i18n: Once you have translated a few pages, you should commit back to launchpad.
.. i18n: To do this, your launchpad account must be subscribed in the 
.. i18n: `openobject-community group <http://https://launchpad.net/~openerp-community>`_.
..

Once you have translated a few pages, you should commit back to launchpad.
To do this, your launchpad account must be subscribed in the 
`openobject-community group <http://https://launchpad.net/~openerp-community>`_.

.. i18n: To upload your modifications, you should commit on launchpad:
..

To upload your modifications, you should commit on launchpad:

.. i18n:   bzr add YOUR_NEW_FILES_OR_DIR
.. i18n:   bzr ci
.. i18n:   bzr push
..

  bzr add YOUR_NEW_FILES_OR_DIR
  bzr ci
  bzr push

.. i18n: Status
.. i18n: ------
..

状态
------

.. i18n: At the moment, this script is in alpha status and has not been thoroughly
.. i18n: tested. It should work but expect some bugs to pop up at unexpected times.
.. i18n: Contact olt AT openerp.com if you notice some troubles.
..

At the moment, this script is in alpha status and has not been thoroughly
tested. It should work but expect some bugs to pop up at unexpected times.
Contact olt AT openerp.com if you notice some troubles.
