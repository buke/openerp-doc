
.. i18n: .. module:: network
.. i18n:     :synopsis: Network Management 
.. i18n:     :noindex:
.. i18n: .. 
..

.. module:: network
    :synopsis: Network Management 
    :noindex:
.. 

.. i18n: .. raw:: html
.. i18n: 
.. i18n:       <br />
.. i18n:     <link rel="stylesheet" href="../_static/hide_objects_in_sidebar.css" type="text/css" />
..

.. raw:: html

      <br />
    <link rel="stylesheet" href="../_static/hide_objects_in_sidebar.css" type="text/css" />

.. i18n: .. tip:: This module is part of the OpenERP software, the leading Open Source 
.. i18n:   enterprise management system. If you want to discover OpenERP, check our 
.. i18n:   `screencasts <http://openerp.tv>`_ or download 
.. i18n:   `OpenERP <http://openerp.com>`_ directly.
..

.. tip:: This module is part of the OpenERP software, the leading Open Source 
  enterprise management system. If you want to discover OpenERP, check our 
  `screencasts <http://openerp.tv>`_ or download 
  `OpenERP <http://openerp.com>`_ directly.

.. i18n: .. raw:: html
.. i18n: 
.. i18n:     <div class="js-kit-rating" title="" permalink="" standalone="yes" path="/network"></div>
.. i18n:     <script src="http://js-kit.com/ratings.js"></script>
..

.. raw:: html

    <div class="js-kit-rating" title="" permalink="" standalone="yes" path="/network"></div>
    <script src="http://js-kit.com/ratings.js"></script>

.. i18n: Network Management (*network*)
.. i18n: ==============================
.. i18n: :Module: network
.. i18n: :Name: Network Management
.. i18n: :Version: 5.0.1.0.1
.. i18n: :Author: Tiny
.. i18n: :Directory: network
.. i18n: :Web: 
.. i18n: :Official module: no
.. i18n: :Quality certified: no
..

Network Management (*network*)
==============================
:Module: network
:Name: Network Management
:Version: 5.0.1.0.1
:Author: Tiny
:Directory: network
:Web: 
:Official module: no
:Quality certified: no

.. i18n: Description
.. i18n: -----------
..

Description
-----------

.. i18n: ::
.. i18n: 
.. i18n:   A simple module to encode your networks and materials:
.. i18n:       - networks and connections between networks
.. i18n:       - hardware and software with:
.. i18n:           - versions, access rights, warranties
.. i18n:   
.. i18n:       You can print interventions form for technical people.
..

::

  A simple module to encode your networks and materials:
      - networks and connections between networks
      - hardware and software with:
          - versions, access rights, warranties
  
      You can print interventions form for technical people.

.. i18n: Download links
.. i18n: --------------
..

Download links
--------------

.. i18n: You can download this module as a zip file in the following version:
..

You can download this module as a zip file in the following version:

.. i18n:   * `4.2 <http://www.openerp.com/download/modules/4.2/network.zip>`_
.. i18n:   * `5.0 <http://www.openerp.com/download/modules/5.0/network.zip>`_
.. i18n:   * `trunk <http://www.openerp.com/download/modules/trunk/network.zip>`_
..

  * `4.2 <http://www.openerp.com/download/modules/4.2/network.zip>`_
  * `5.0 <http://www.openerp.com/download/modules/5.0/network.zip>`_
  * `trunk <http://www.openerp.com/download/modules/trunk/network.zip>`_

.. i18n: Dependencies
.. i18n: ------------
..

Dependencies
------------

.. i18n:  * :mod:`base`
..

 * :mod:`base`

.. i18n: Reports
.. i18n: -------
..

Reports
-------

.. i18n: None
..

None

.. i18n: Menus
.. i18n: -------
..

Menus
-------

.. i18n:  * Tools
.. i18n:  * Tools/Network
.. i18n:  * Tools/Network/Configuration
.. i18n:  * Tools/Network/Configuration/Software
.. i18n:  * Tools/Network/Configuration/Software/Types
.. i18n:  * Tools/Network/Configuration/Hardware
.. i18n:  * Tools/Network/Configuration/Hardware/Types
.. i18n:  * Tools/Network/Network List
.. i18n:  * Tools/Network/Networks
.. i18n:  * Tools/Network/All Materials
.. i18n:  * Tools/Network/Top Materials
.. i18n:  * Tools/Network/Material List
..

 * Tools
 * Tools/Network
 * Tools/Network/Configuration
 * Tools/Network/Configuration/Software
 * Tools/Network/Configuration/Software/Types
 * Tools/Network/Configuration/Hardware
 * Tools/Network/Configuration/Hardware/Types
 * Tools/Network/Network List
 * Tools/Network/Networks
 * Tools/Network/All Materials
 * Tools/Network/Top Materials
 * Tools/Network/Material List

.. i18n: Views
.. i18n: -----
..

Views
-----

.. i18n:  * network.material.form (form)
.. i18n:  * network.material.tree (tree)
.. i18n:  * network.material.tree (tree)
.. i18n:  * network.software.type.form (form)
.. i18n:  * network.hardware.type.form (form)
.. i18n:  * network.software.logpass.form (form)
.. i18n:  * network.software.logpass.tree (tree)
.. i18n:  * network.software.form (form)
.. i18n:  * network.software.tree (tree)
.. i18n:  * network.network.tree (tree)
.. i18n:  * network.network.form (form)
.. i18n:  * network.changes.form (form)
.. i18n:  * network.changes.tree (tree)
..

 * network.material.form (form)
 * network.material.tree (tree)
 * network.material.tree (tree)
 * network.software.type.form (form)
 * network.hardware.type.form (form)
 * network.software.logpass.form (form)
 * network.software.logpass.tree (tree)
 * network.software.form (form)
 * network.software.tree (tree)
 * network.network.tree (tree)
 * network.network.form (form)
 * network.changes.form (form)
 * network.changes.tree (tree)

.. i18n: Objects
.. i18n: -------
..

Objects
-------

.. i18n: Object: Hardware type (network.hardware.type)
.. i18n: #############################################
..

Object: Hardware type (network.hardware.type)
#############################################

.. i18n: :name: Type of material, char, required
..

:name: Type of material, char, required

.. i18n: :networkable: Networkable hardware, boolean
..

:networkable: Networkable hardware, boolean

.. i18n: Object: Network (network.network)
.. i18n: #################################
..

Object: Network (network.network)
#################################

.. i18n: :material_ids: Members, one2many
..

:material_ids: Members, one2many

.. i18n: :range: Address range, char
..

:range: Address range, char

.. i18n: :user_id: Onsite Contact person, many2one
..

:user_id: Onsite Contact person, many2one

.. i18n: :name: Network name, char, required
..

:name: Network name, char, required

.. i18n: :contact_id: Partner, many2one, required
..

:contact_id: Partner, many2one, required

.. i18n: Object: Material (network.material)
.. i18n: ###################################
..

Object: Material (network.material)
###################################

.. i18n: :warranty: Warranty deadline, date
..

:warranty: Warranty deadline, date

.. i18n: :ip_addr: IP Address, char
..

:ip_addr: IP Address, char

.. i18n: :name: Device Name, char, required
..

:name: Device Name, char, required

.. i18n: :network_id: Network, many2one
..

:network_id: Network, many2one

.. i18n: :change_id: Changes on this machine, one2many
..

:change_id: Changes on this machine, one2many

.. i18n: :note: Notes, text
..

:note: Notes, text

.. i18n: :parent_id: Parent Material, many2one
..

:parent_id: Parent Material, many2one

.. i18n: :date: Installation Date, date
..

:date: Installation Date, date

.. i18n: :child_id: Childs Materials, one2many
..

:child_id: Childs Materials, one2many

.. i18n: :supplier: Supplier, many2one
..

:supplier: Supplier, many2one

.. i18n: :type: Hardware type, many2one, required
..

:type: Hardware type, many2one, required

.. i18n: :software_id: Installed Software, one2many
..

:software_id: Installed Software, one2many

.. i18n: Object: Network changes (network.changes)
.. i18n: #########################################
..

Object: Network changes (network.changes)
#########################################

.. i18n: :date: Change date, datetime
..

:date: Change date, datetime

.. i18n: :machine_id: Machine, many2one
..

:machine_id: Machine, many2one

.. i18n: :user_id: User, many2one, required
..

:user_id: User, many2one, required

.. i18n: :name: Short Description, char, required
..

:name: Short Description, char, required

.. i18n: :description: Long Description, text
..

:description: Long Description, text

.. i18n: Object: Software type (network.software.type)
.. i18n: #############################################
..

Object: Software type (network.software.type)
#############################################

.. i18n: :note: Notes, text
..

:note: Notes, text

.. i18n: :name: Composant Name, char, required
..

:name: Composant Name, char, required

.. i18n: Object: Software (network.software)
.. i18n: ###################################
..

Object: Software (network.software)
###################################

.. i18n: :name: Composant Name, char, required
..

:name: Composant Name, char, required

.. i18n: :logpass: Login / Password, one2many
..

:logpass: Login / Password, one2many

.. i18n: :material_id: Material, many2one
..

:material_id: Material, many2one

.. i18n: :note: Notes, text
..

:note: Notes, text

.. i18n: :version: Software version, char
..

:version: Software version, char

.. i18n: :date: Installation Date, date
..

:date: Installation Date, date

.. i18n: :type: Software Type, many2one, required
..

:type: Software Type, many2one, required

.. i18n: :email: Contact Email, char
..

:email: Contact Email, char

.. i18n: Object: Software login (network.software.logpass)
.. i18n: #################################################
..

Object: Software login (network.software.logpass)
#################################################

.. i18n: :login: Login, char, required
..

:login: Login, char, required

.. i18n: :password: Password, char, required
..

:password: Password, char, required

.. i18n: :software_id: Software, many2one, required
..

:software_id: Software, many2one, required
