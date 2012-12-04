
.. i18n: .. index:: FTP
..

.. index:: FTP

.. i18n: Internal and External Access using FTP
.. i18n: ======================================
..

Internal and External Access using FTP
======================================

.. i18n: .. index::
.. i18n:    single: directory
.. i18n:    single: module; document
..

.. index::
   single: directory
   single: module; document

.. i18n: The first configuration step is to create a directory structure that will be used to classify your
.. i18n: document set. You can use the structure automatically proposed by OpenERP from the menu
.. i18n: :menuselection:`Knowledge --> Configuration --> Document Management --> Directories' Structure`.
..

The first configuration step is to create a directory structure that will be used to classify your
document set. You can use the structure automatically proposed by OpenERP from the menu
:menuselection:`Knowledge --> Configuration --> Document Management --> Directories' Structure`.

.. i18n: .. figure::  images/document_structure.png
.. i18n:    :scale: 75
.. i18n:    :align: center
.. i18n: 
.. i18n:    *Structure of directories when the document module has been installed*
..

.. figure::  images/document_structure.png
   :scale: 75
   :align: center

   *Structure of directories when the document module has been installed*

.. i18n: In addition to the usual access to documents through OpenERP, you will be able to connect to them
.. i18n: directly through the file system using the FTP protocol. To connect to the FTP server, use the
.. i18n: following address:
..

In addition to the usual access to documents through OpenERP, you will be able to connect to them
directly through the file system using the FTP protocol. To connect to the FTP server, use the
following address:

.. i18n: ========= ==========================================
.. i18n: Parameter Value
.. i18n: ========= ==========================================
.. i18n: Server    Your OpenERP server, for example 127.0.0.1
.. i18n: Port      8021
.. i18n: Path      The '/' character, for the root
.. i18n: User      Your user account in OpenERP
.. i18n: Password  Your OpenERP password
.. i18n: ========= ==========================================
..

========= ==========================================
Parameter Value
========= ==========================================
Server    Your OpenERP server, for example 127.0.0.1
Port      8021
Path      The '/' character, for the root
User      Your user account in OpenERP
Password  Your OpenERP password
========= ==========================================

.. i18n: .. note:: FTP Server
.. i18n: 
.. i18n:    These comments about an FTP server may appear a bit technical, but
.. i18n:    it is just a general standard for getting hold of files without worrying too much about the platform
.. i18n:    (Windows, Mac, Linux, or other Unix-like system).
.. i18n:    So FTP is just a way of getting access to files without needing to use an OpenERP client.
.. i18n:    There could have been other ways, but FTP proved itself to the developers to be the one that performed best
.. i18n:    at lowest cost.
..

.. note:: FTP Server

   These comments about an FTP server may appear a bit technical, but
   it is just a general standard for getting hold of files without worrying too much about the platform
   (Windows, Mac, Linux, or other Unix-like system).
   So FTP is just a way of getting access to files without needing to use an OpenERP client.
   There could have been other ways, but FTP proved itself to the developers to be the one that performed best
   at lowest cost.

.. i18n: Once you are connected using FTP, you get to the root of a directory for the document
.. i18n: management system. Once you enter that directory you find a structure that matches the structure
.. i18n: defined in OpenERP.
..

Once you are connected using FTP, you get to the root of a directory for the document
management system. Once you enter that directory you find a structure that matches the structure
defined in OpenERP.

.. i18n: .. figure::  images/document_ftp_structure_root.png
.. i18n:    :scale: 75
.. i18n:    :align: center
.. i18n: 
.. i18n:    *Root of the database directory seen through FTP*
..

.. figure::  images/document_ftp_structure_root.png
   :scale: 75
   :align: center

   *Root of the database directory seen through FTP*

.. i18n: .. figure::  images/document_ftp_structure_tree.png
.. i18n:    :scale: 75
.. i18n:    :align: center
.. i18n: 
.. i18n:    *Structure of the directories in the document management system*
..

.. figure::  images/document_ftp_structure_tree.png
   :scale: 75
   :align: center

   *Structure of the directories in the document management system*

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
