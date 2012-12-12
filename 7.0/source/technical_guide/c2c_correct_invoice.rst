
.. module:: c2c_correct_invoice
    :synopsis: Invoice Correcting 
    :noindex:
.. 

.. raw:: html

    <link rel="stylesheet" href="../_static/hide_objects_in_sidebar.css" type="text/css" />

Invoice Correcting (*c2c_correct_invoice*)
==========================================
:Module: c2c_correct_invoice
:Name: Invoice Correcting
:Version: 1.1
:Author: Camptocamp
:Directory: c2c_correct_invoice
:Web: http://www.camptocamp.com
:Official module: no
:Quality certified: no

Description
-----------

::

  
  	This module allows correction of a paid invoice in one action. 
  	-This will create a refund, 
  	-Unreconcile the invoice and reconcile it with the refund 
  	-If needed recreate an invoice
  	This wizard overrides the invoice Refund wizard
  	It adds two actions:
  	-The cancel invoice that will create a refund and unreconcile/reconcile it.
  	-The modify invoice that does the same as before but also creates a new invoice
  	which is a copy of the original.
  	 
  
Download links
--------------

You can download this module as a zip file in the following version:

  * `4.2 <http://www.openerp.com/download/modules/4.2/c2c_correct_invoice.zip>`_

Dependencies
------------

 * :mod:`base`
 * :mod:`c2c_partner_address`
 * :mod:`account`

Reports
-------

None


Menus
-------


None


Views
-----


None



Objects
-------

None
