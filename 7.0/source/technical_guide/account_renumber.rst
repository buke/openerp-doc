
.. module:: account_renumber
    :synopsis: Account renumber wizard 
    :noindex:
.. 

.. raw:: html

      <br />
    <link rel="stylesheet" href="../_static/hide_objects_in_sidebar.css" type="text/css" />

.. tip:: This module is part of the OpenERP software, the leading Open Source 
  enterprise management system. If you want to discover OpenERP, check our 
  `screencasts <http://openerp.tv>`_ or download 
  `OpenERP <http://openerp.com>`_ directly.

.. raw:: html

    <div class="js-kit-rating" title="" permalink="" standalone="yes" path="/account_renumber"></div>
    <script src="http://js-kit.com/ratings.js"></script>

Account renumber wizard (*account_renumber*)
============================================
:Module: account_renumber
:Name: Account renumber wizard
:Version: 5.0.0.1
:Author: Pexego
:Directory: account_renumber
:Web: http://www.pexego.es
:Official module: no
:Quality certified: no

Description
-----------

::

  This module adds a wizard to renumber account moves by date.
  
  The wizard, that will be added to the "End of Year Treatments",
  let's you select one or more journals and fiscal periods,
  set a starting number; and then renumber all the posted moves
  from those journals and periods sorted by date.
  
  It will recreate the sequence number of each account move using their journal sequence so:
      - Sequences per journal are supported.
      - Sequences with prefixes and suffixes based on the move date are also supported.

Download links
--------------

You can download this module as a zip file in the following version:

(No download links available)


Dependencies
------------

 * :mod:`base`
 * :mod:`account`

Reports
-------

None


Menus
-------

 * Financial Management/Periodical Processing/End of Year Treatments/Renumber Account Moves

Views
-----


None



Objects
-------

None
