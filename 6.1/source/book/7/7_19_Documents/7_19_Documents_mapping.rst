
Mapping between OpenERP Resources and Directories
=================================================

Each directory can either have the type ``Static`` or ``Folders per resource``. A static directory, as
with operating systems, is the classic directory that can contain a set of files. On the other hand, the directories
linked to systems resources automatically possess sub-directories for each of the resource types defined in
the parent directory.

.. tip:: Directories in English

    To keep them synchronized to the working language, directory names are not translatable.
    But OpenERP's demonstration data automatically creates directories in English.
    You can rename them through the menu :menuselection:`Knowledge --> Configuration --> Document Management -->
    Directories`.

For example, you can look at the directory shown in :menuselection:`Documents --> Sales Order
--> All Sales Order`. You will see the directory for all the orders present in OpenERP that was
created automatically by the system.

.. figure::  images/document_sale.png
   :scale: 75
   :align: center

   *Orders in OpenERP*

.. figure::  images/document_ftp_sale.png
   :scale: 75
   :align: center

   *Directories representing all the orders in the document management system*

Directories can follow a tree structure, like the tree of resources in OpenERP. For example, if you go to the
directory :menuselection:`Documents --> Projects` you will see the structure of the analytic
accounts.

To define a directory containing a specific type of resource, you have to define parameters when you
define the directory itself:

* :guilabel:`Type` : Folders per resource

* :guilabel:`Resource model` : Choose one of the system objects

* :guilabel:`Domain` :  an event filtered so that it sees only a subset of the resources

* :guilabel:`Tree Structure` : to show the resources hierarchically

.. figure::  images/document_dir_form.png
   :scale: 75
   :align: center

   *Configuration of the directory containing All Sales Orders*

This is a very flexible approach because any modification of the resource in OpenERP is
automatically reflected in the document management system. So when the quotation gets confirmed in
OpenERP the directory no longer appears as a quotation through FTP access.

Here are some examples of directories linked to OpenERP resources that could be helpful when
configured in the document management system:

* Quotations and Order: storing documents that relate to orders,

* Products: for storing products' technical datasheets,

* Users: to automatically define a directory owned by each user of the system,

* Employees: to store documents about employees, such as their CVs, your interview notes, contract
  details, and their annual assessments,

* Support Requests: storing items about requests or about technical support responses,

* Analytic Accounts or Project: to store project management and tracking documents.


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
