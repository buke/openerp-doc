
.. i18n: .. index:: 
.. i18n:    pair: document; optimize
..

.. index:: 
   pair: document; optimize

.. i18n: Optimizing Document Management
.. i18n: ==============================
..

Optimizing Document Management
==============================

.. i18n: All documents produced by OpenERP are automatically indexed and classified for
.. i18n: maximum efficiency. There is an ultra-rapid access to documents, which are
.. i18n: directly available from your email client or the company management software.
.. i18n: The user access rights are managed just the same way as those that are available
.. i18n: in the company management system. All these features help you to get the best
.. i18n: out of OpenERP's document management system.
..

All documents produced by OpenERP are automatically indexed and classified for
maximum efficiency. There is an ultra-rapid access to documents, which are
directly available from your email client or the company management software.
The user access rights are managed just the same way as those that are available
in the company management system. All these features help you to get the best
out of OpenERP's document management system.

.. i18n: Searching for Documents
.. i18n: -----------------------
..

Searching for Documents
-----------------------

.. i18n: You have seen several methods of accessing documents quickly:
..

You have seen several methods of accessing documents quickly:

.. i18n: * From attachments to an OpenERP resource,
.. i18n: 
.. i18n: * Through FTP access to OpenERP,
.. i18n: 
.. i18n: * Using the menu :menuselection:`Knowledge --> Document Management --> Directories' Structure`.
..

* From attachments to an OpenERP resource,

* Through FTP access to OpenERP,

* Using the menu :menuselection:`Knowledge --> Document Management --> Directories' Structure`.

.. i18n: But if you do not know where a specific document can be found, OpenERP also has a search tool
.. i18n: integrated into its document management to simplify your search. To search for a file, use the menu :menuselection:`Knowledge
.. i18n: --> Documents --> Documents`. You get to a document search view that lets you search amongst
.. i18n: all the attachments and all the documents in the FTP server.
..

But if you do not know where a specific document can be found, OpenERP also has a search tool
integrated into its document management to simplify your search. To search for a file, use the menu :menuselection:`Knowledge
--> Documents --> Documents`. You get to a document search view that lets you search amongst
all the attachments and all the documents in the FTP server.

.. i18n: You can search for a file using various different criteria:
..

You can search for a file using various different criteria:

.. i18n: * The attachment name,
.. i18n: 
.. i18n: * The attachment type,
.. i18n: 
.. i18n: * The filename,
.. i18n: 
.. i18n: * The owner of a file,
.. i18n: 
.. i18n: * The directory that it is found in,
.. i18n: 
.. i18n: * The indexed content.
..

* The attachment name,

* The attachment type,

* The filename,

* The owner of a file,

* The directory that it is found in,

* The indexed content.

.. i18n: Notice here an important advantage for an integrated document management system. Information such as
.. i18n: which partner is associated with a document is automatically detected by OpenERP when the document
.. i18n: has been stored in a directory. This information is never input by the user – it is detected
.. i18n: automatically using the information about the resource when it is being saved as a file.
..

Notice here an important advantage for an integrated document management system. Information such as
which partner is associated with a document is automatically detected by OpenERP when the document
has been stored in a directory. This information is never input by the user – it is detected
automatically using the information about the resource when it is being saved as a file.

.. i18n: But your search is not limited to these few fields. You can also search on the content in the files.
.. i18n: Each file is automatically indexed by the system to give you a search engine rather like Google's on
.. i18n: the whole set of company documents.
..

But your search is not limited to these few fields. You can also search on the content in the files.
Each file is automatically indexed by the system to give you a search engine rather like Google's on
the whole set of company documents.

.. i18n: .. note:: Supported File Formats
.. i18n: 
.. i18n:     The OpenERP document management system can index the following file formats:
.. i18n: 
.. i18n:     * **TXT** : text files,
.. i18n: 
.. i18n:     * **PDF** : PDF files,
.. i18n: 
.. i18n:     * **SXW** : OpenOffice V1 files,
.. i18n: 
.. i18n:     * **ODT** : OpenOffice V2 files,
.. i18n: 
.. i18n:     * **DOC** : Microsoft Word files.
.. i18n: 
.. i18n:     The other file formats are properly handled in the document management system, but their content
.. i18n:     is not indexed automatically.
..

.. note:: Supported File Formats

    The OpenERP document management system can index the following file formats:

    * **TXT** : text files,

    * **PDF** : PDF files,

    * **SXW** : OpenOffice V1 files,

    * **ODT** : OpenOffice V2 files,

    * **DOC** : Microsoft Word files.

    The other file formats are properly handled in the document management system, but their content
    is not indexed automatically.

.. i18n: This functionality is very significant. All you need to do is search for a partner name or an order
.. i18n: number to automatically get all the documents that are referenced there. And you can use a fragment
.. i18n: of text to find the document you need from within that subset.
..

This functionality is very significant. All you need to do is search for a partner name or an order
number to automatically get all the documents that are referenced there. And you can use a fragment
of text to find the document you need from within that subset.

.. i18n: Integration with Emails
.. i18n: -----------------------
..

Integration with Emails
-----------------------

.. i18n: Using Outlook and Thunderbird
.. i18n: ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
..

Using Outlook and Thunderbird
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. i18n: OpenERP's document management system is well-integrated with popular email clients like Microsoft Outlook and Mozilla Thunderbird. For this, you can install the required plugins available in OpenERP, usually made available when you install and configure :mod:`crm`. Or you may install :mod:`outlook` or :mod:`thunderbird` module according to your requirement, and take advantage of its compatibility with OpenERP's documents. For more on this, refer :ref:`ch-commtools`.
..

OpenERP's document management system is well-integrated with popular email clients like Microsoft Outlook and Mozilla Thunderbird. For this, you can install the required plugins available in OpenERP, usually made available when you install and configure :mod:`crm`. Or you may install :mod:`outlook` or :mod:`thunderbird` module according to your requirement, and take advantage of its compatibility with OpenERP's documents. For more on this, refer :ref:`ch-commtools`.

.. i18n: .. figure::  images/create_contact_outlook.png
.. i18n:    :scale: 65
.. i18n:    :align: center
.. i18n: 
.. i18n:    *Creating a new contact through the Document Management System from Outlook*
..

.. figure::  images/create_contact_outlook.png
   :scale: 65
   :align: center

   *Creating a new contact through the Document Management System from Outlook*

.. i18n: .. figure::  images/document_attachment_thunderbird.png
.. i18n:    :scale: 65
.. i18n:    :align: center
.. i18n: 
.. i18n:    *Pushing an attachment in the Document Management System from Thunderbird*
..

.. figure::  images/document_attachment_thunderbird.png
   :scale: 65
   :align: center

   *Pushing an attachment in the Document Management System from Thunderbird*

.. i18n: Working with Users' Changes
.. i18n: ---------------------------
..

Working with Users' Changes
---------------------------

.. i18n: To make the document management system's use as unobtrusive as possible, the system's users should
.. i18n: easily be able to store all the documents that they produce or receive from their customers and
.. i18n: suppliers. So OpenERP supplies dashboards to help system users approve their acceptance of such
.. i18n: documents.
..

To make the document management system's use as unobtrusive as possible, the system's users should
easily be able to store all the documents that they produce or receive from their customers and
suppliers. So OpenERP supplies dashboards to help system users approve their acceptance of such
documents.

.. i18n: So you will find two dashboards in the menu :menuselection:`Knowledge --> Reporting --> Dashboard`. One
.. i18n: dashboard is for the document management system manager and one dashboard is for tracking use by different
.. i18n: users.
..

So you will find two dashboards in the menu :menuselection:`Knowledge --> Reporting --> Dashboard`. One
dashboard is for the document management system manager and one dashboard is for tracking use by different
users.

.. i18n: The first lets you track the changes to documents by month, by customer and by type of resource. You
.. i18n: could also quickly assess the use that is made of the system by the various users.
..

The first lets you track the changes to documents by month, by customer and by type of resource. You
could also quickly assess the use that is made of the system by the various users.

.. i18n: .. figure::  images/document_board1.png
.. i18n:    :scale: 75
.. i18n:    :align: center
.. i18n: 
.. i18n:    *Dashboard for the document management system manager*
..

.. figure::  images/document_board1.png
   :scale: 75
   :align: center

   *Dashboard for the document management system manager*

.. i18n: The second dashboard shows you how different employees use the system.
.. i18n: You can see the number of files sent by each user and who uses the document
.. i18n: management system the least. That tells you something about your user training
.. i18n: and whether you need to do something about changing work methods.
..

The second dashboard shows you how different employees use the system.
You can see the number of files sent by each user and who uses the document
management system the least. That tells you something about your user training
and whether you need to do something about changing work methods.

.. i18n: .. figure::  images/document_board2.png
.. i18n:    :scale: 75
.. i18n:    :align: center
.. i18n: 
.. i18n:    *Dashboard for the document management system analyzed by user*
..

.. figure::  images/document_board2.png
   :scale: 75
   :align: center

   *Dashboard for the document management system analyzed by user*

.. i18n: Version Management
.. i18n: ------------------
..

Version Management
------------------

.. i18n: There is usually a need to keep track of all the important documents that you have printed. For
.. i18n: example, when you send an invoice to a customer it is a good idea to store a copy of that invoice
.. i18n: internally in paper or electronic form. Then you can reprint it exactly in the same format as when
.. i18n: you sent it, even if the company's details have changed in the meantime.
..

There is usually a need to keep track of all the important documents that you have printed. For
example, when you send an invoice to a customer it is a good idea to store a copy of that invoice
internally in paper or electronic form. Then you can reprint it exactly in the same format as when
you sent it, even if the company's details have changed in the meantime.

.. i18n: To do this, OpenERP can automatically store as attachments the different reports printed by users.
.. i18n: By default, only invoices are saved as attachments, and they are saved when they are printed.
.. i18n: That is because they are commonly legally required.
..

To do this, OpenERP can automatically store as attachments the different reports printed by users.
By default, only invoices are saved as attachments, and they are saved when they are printed.
That is because they are commonly legally required.

.. i18n: But you can configure the system so that it does not matter which type of report is printed - 
.. i18n: they can all be stored automatically. To
.. i18n: activate that functionality on another type of report, modify this in the menu
.. i18n: :menuselection:`Administration --> Low Level Objects --> Actions --> Reports`.
.. i18n: To be able to access this menu, the user should be added to the group :guilabel:`Useability / No One`.
..

But you can configure the system so that it does not matter which type of report is printed - 
they can all be stored automatically. To
activate that functionality on another type of report, modify this in the menu
:menuselection:`Administration --> Low Level Objects --> Actions --> Reports`.
To be able to access this menu, the user should be added to the group :guilabel:`Useability / No One`.

.. i18n: .. figure::  images/document_report_modif.png
.. i18n:    :scale: 75
.. i18n:    :align: center
.. i18n: 
.. i18n:    *Modifying the definition of a report*
..

.. figure::  images/document_report_modif.png
   :scale: 75
   :align: center

   *Modifying the definition of a report*

.. i18n: Select the report that you want to change and complete the field :guilabel:`Save As Attachment Prefix`.
.. i18n: Once you have done that, each document print action will automatically be saved as an
.. i18n: attachment to the document.
..

Select the report that you want to change and complete the field :guilabel:`Save As Attachment Prefix`.
Once you have done that, each document print action will automatically be saved as an
attachment to the document.

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
