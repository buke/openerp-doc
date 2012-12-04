
.. index:: 
   pair: document; optimize

Optimizing Document Management
==============================

All documents produced by OpenERP are automatically indexed and classified for
maximum efficiency. There is an ultra-rapid access to documents, which are
directly available from your email client or the company management software.
The user access rights are managed just the same way as those that are available
in the company management system. All these features help you to get the best
out of OpenERP's document management system.

Searching for Documents
-----------------------

You have seen several methods of accessing documents quickly:

* From attachments to an OpenERP resource,

* Through FTP access to OpenERP,

* Using the menu :menuselection:`Knowledge --> Document Management --> Directories' Structure`.

But if you do not know where a specific document can be found, OpenERP also has a search tool
integrated into its document management to simplify your search. To search for a file, use the menu :menuselection:`Knowledge
--> Documents --> Documents`. You get to a document search view that lets you search amongst
all the attachments and all the documents in the FTP server.

You can search for a file using various different criteria:

* The attachment name,

* The attachment type,

* The filename,

* The owner of a file,

* The directory that it is found in,

* The indexed content.

Notice here an important advantage for an integrated document management system. Information such as
which partner is associated with a document is automatically detected by OpenERP when the document
has been stored in a directory. This information is never input by the user – it is detected
automatically using the information about the resource when it is being saved as a file.

But your search is not limited to these few fields. You can also search on the content in the files.
Each file is automatically indexed by the system to give you a search engine rather like Google's on
the whole set of company documents.

.. note:: Supported File Formats

    The OpenERP document management system can index the following file formats:

    * **TXT** : text files,

    * **PDF** : PDF files,

    * **SXW** : OpenOffice V1 files,

    * **ODT** : OpenOffice V2 files,

    * **DOC** : Microsoft Word files.

    The other file formats are properly handled in the document management system, but their content
    is not indexed automatically.

This functionality is very significant. All you need to do is search for a partner name or an order
number to automatically get all the documents that are referenced there. And you can use a fragment
of text to find the document you need from within that subset.

Integration with Emails
-----------------------

Using Outlook and Thunderbird
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

OpenERP's document management system is well-integrated with popular email clients like Microsoft Outlook and Mozilla Thunderbird. For this, you can install the required plugins available in OpenERP, usually made available when you install and configure :mod:`crm`. Or you may install :mod:`outlook` or :mod:`thunderbird` module according to your requirement, and take advantage of its compatibility with OpenERP's documents. For more on this, refer :ref:`ch-commtools`.

.. figure::  images/create_contact_outlook.png
   :scale: 65
   :align: center

   *Creating a new contact through the Document Management System from Outlook*

.. figure::  images/document_attachment_thunderbird.png
   :scale: 65
   :align: center

   *Pushing an attachment in the Document Management System from Thunderbird*

Working with Users' Changes
---------------------------

To make the document management system's use as unobtrusive as possible, the system's users should
easily be able to store all the documents that they produce or receive from their customers and
suppliers. So OpenERP supplies dashboards to help system users approve their acceptance of such
documents.

So you will find two dashboards in the menu :menuselection:`Knowledge --> Reporting --> Dashboard`. One
dashboard is for the document management system manager and one dashboard is for tracking use by different
users.

The first lets you track the changes to documents by month, by customer and by type of resource. You
could also quickly assess the use that is made of the system by the various users.

.. figure::  images/document_board1.png
   :scale: 75
   :align: center

   *Dashboard for the document management system manager*

The second dashboard shows you how different employees use the system.
You can see the number of files sent by each user and who uses the document
management system the least. That tells you something about your user training
and whether you need to do something about changing work methods.

.. figure::  images/document_board2.png
   :scale: 75
   :align: center

   *Dashboard for the document management system analyzed by user*

Version Management
------------------

There is usually a need to keep track of all the important documents that you have printed. For
example, when you send an invoice to a customer it is a good idea to store a copy of that invoice
internally in paper or electronic form. Then you can reprint it exactly in the same format as when
you sent it, even if the company's details have changed in the meantime.

To do this, OpenERP can automatically store as attachments the different reports printed by users.
By default, only invoices are saved as attachments, and they are saved when they are printed.
That is because they are commonly legally required.

But you can configure the system so that it does not matter which type of report is printed - 
they can all be stored automatically. To
activate that functionality on another type of report, modify this in the menu
:menuselection:`Administration --> Low Level Objects --> Actions --> Reports`.
To be able to access this menu, the user should be added to the group :guilabel:`Useability / No One`.

.. figure::  images/document_report_modif.png
   :scale: 75
   :align: center

   *Modifying the definition of a report*

Select the report that you want to change and complete the field :guilabel:`Save As Attachment Prefix`.
Once you have done that, each document print action will automatically be saved as an
attachment to the document.

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
