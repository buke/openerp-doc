
.. module:: account_bob_import
    :synopsis: Import accounting entries from Bob 
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

    <div class="js-kit-rating" title="" permalink="" standalone="yes" path="/account_bob_import"></div>
    <script src="http://js-kit.com/ratings.js"></script>

Import accounting entries from Bob (*account_bob_import*)
=========================================================
:Module: account_bob_import
:Name: Import accounting entries from Bob
:Version: 5.0.1.0
:Author: Tiny
:Directory: account_bob_import
:Web: 
:Official module: no
:Quality certified: no

Description
-----------

::

  This module provide an easy way to migrate your financial data from Bob software to OpenERP. It includes the import of
              * chart of accounts,
              * financial journals,
              * customers, suppliers and prospects,
              * contacts,
              * accounting entries
  
          Once the module is installed, all you have to do is run the configuration wizard and provide OpenERP the location of the Bob directory where is your data.

Download links
--------------

You can download this module as a zip file in the following version:

  * `5.0 <http://www.openerp.com/download/modules/5.0/account_bob_import.zip>`_
  * `trunk <http://www.openerp.com/download/modules/trunk/account_bob_import.zip>`_


Dependencies
------------

 * :mod:`base_contact`
 * :mod:`account_l10nbe_domiciliation`
 * :mod:`l10n_be`

Reports
-------

None


Menus
-------


None


Views
-----

 * Configure BOB Import (form)
 * Select Folder for BOB Import (form)


Objects
-------

Object: config.bob.import (config.bob.import)
#############################################



:path: Path for BOB Folder, char

    *Supply a path that is a Bob Installation Folder.*



:company_id: Company, many2one, required





:zipped_file: Upload a Zip File, binary

    *Upload a .zip file containing information of BOB Installation'*



:location: Location, selection, required

    *If this machine is the server, select 'locally' as the location. If this is the client machine, create a zip of the 'Bob' folder placed in Root(Drive Letter)://Program Files/Bob. Upload it and follow the further instructions.*


Object: config.path.folder (config.path.folder)
###############################################



:folder: Folder, selection, required


