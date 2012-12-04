
.. module:: network_extension
    :synopsis: Network Management Extension 
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

    <div class="js-kit-rating" title="" permalink="" standalone="yes" path="/network_extension"></div>
    <script src="http://js-kit.com/ratings.js"></script>

Network Management Extension (*network_extension*)
==================================================
:Module: network_extension
:Name: Network Management Extension
:Version: 5.0.1.0.1
:Author: Zikzakmedia SL
:Directory: network_extension
:Web: www.zikzakmedia.com
:Official module: no
:Quality certified: no

Description
-----------

::

  Organize your software and configurations.
      - Additional network information: IP, domain, DNS, gateway
      - Protocols
      - Services
      - Ports
      - Public and private URLs
      - Password encryption
  
  System dependency: package python-crypto required.

Download links
--------------

You can download this module as a zip file in the following version:

  * `5.0 <http://www.openerp.com/download/modules/5.0/network_extension.zip>`_
  * `trunk <http://www.openerp.com/download/modules/trunk/network_extension.zip>`_


Dependencies
------------

 * :mod:`network`

Reports
-------

None


Menus
-------

 * Tools/Network/Software
 * Tools/Network/Logins/Passwords
 * Tools/Network/Services
 * Tools/Network/Configuration/Protocol
 * Tools/Network/Configuration/Encrypt/Decrypt password

Views
-----

 * \* INHERIT network.network.tree.ext1 (form)
 * \* INHERIT network.network.form.ext1 (form)
 * \* INHERIT network.network.form.ext2 (form)
 * \* INHERIT network.network.form.ext3 (form)
 * \* INHERIT network.network.form.ext4 (form)
 * \* INHERIT network.network.form.ext5 (form)
 * \* INHERIT network.material.tree.ext1 (form)
 * \* INHERIT network.material.form.ext1 (form)
 * \* INHERIT network.material.form.ext2 (form)
 * \* INHERIT network.view.software.tree.ext1 (form)
 * \* INHERIT network.software.form.ext1 (form)
 * \* INHERIT network.software.form.ext2 (form)
 * \* INHERIT network.password.tree.ext1 (form)
 * \* INHERIT network.password.tree.ext2 (form)
 * \* INHERIT network.password.form.ext1 (form)
 * \* INHERIT network.password.form.ext2 (form)
 * network.service.tree (tree)
 * network.service.form (form)
 * network.protocol.tree (tree)
 * network.protocol.form (form)
 * network.encrypt.password.tree (tree)
 * network.encrypt.password.form (form)


Objects
-------

Object: Protocol (network.protocol)
###################################



:protocol: Protocol, selection, required





:description: Description, char





:name: Name, char, required





:port: Port, integer, required

    *Default port defined see(http://www.iana.org/assignments/port-numbers)*


Object: Service Network (network.service)
#########################################



:material: Material, many2one, readonly





:name: Name, char





:protocol_id: Protocol, many2one





:public_port: Public port, integer

    *Sometimes public and private ports are different.*



:public_url: Public URL, char





:private_url: Private URL, char





:path: Path, char





:software_id: Software, many2one, required





:port: Port, integer, required




Object: Password encryption (network.encrypt.password)
######################################################



:name: Encrypt/Decrypt password, char


