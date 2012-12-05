
.. i18n: .. module:: network_extension
.. i18n:     :synopsis: Network Management Extension 
.. i18n:     :noindex:
.. i18n: .. 
..

.. module:: network_extension
    :synopsis: Network Management Extension 
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
.. i18n:     <div class="js-kit-rating" title="" permalink="" standalone="yes" path="/network_extension"></div>
.. i18n:     <script src="http://js-kit.com/ratings.js"></script>
..

.. raw:: html

    <div class="js-kit-rating" title="" permalink="" standalone="yes" path="/network_extension"></div>
    <script src="http://js-kit.com/ratings.js"></script>

.. i18n: Network Management Extension (*network_extension*)
.. i18n: ==================================================
.. i18n: :Module: network_extension
.. i18n: :Name: Network Management Extension
.. i18n: :Version: 5.0.1.0.1
.. i18n: :Author: Zikzakmedia SL
.. i18n: :Directory: network_extension
.. i18n: :Web: www.zikzakmedia.com
.. i18n: :Official module: no
.. i18n: :Quality certified: no
..

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

.. i18n: Description
.. i18n: -----------
..

Description
-----------

.. i18n: ::
.. i18n: 
.. i18n:   Organize your software and configurations.
.. i18n:       - Additional network information: IP, domain, DNS, gateway
.. i18n:       - Protocols
.. i18n:       - Services
.. i18n:       - Ports
.. i18n:       - Public and private URLs
.. i18n:       - Password encryption
.. i18n:   
.. i18n:   System dependency: package python-crypto required.
..

::

  Organize your software and configurations.
      - Additional network information: IP, domain, DNS, gateway
      - Protocols
      - Services
      - Ports
      - Public and private URLs
      - Password encryption
  
  System dependency: package python-crypto required.

.. i18n: Download links
.. i18n: --------------
..

Download links
--------------

.. i18n: You can download this module as a zip file in the following version:
..

You can download this module as a zip file in the following version:

.. i18n:   * `5.0 <http://www.openerp.com/download/modules/5.0/network_extension.zip>`_
.. i18n:   * `trunk <http://www.openerp.com/download/modules/trunk/network_extension.zip>`_
..

  * `5.0 <http://www.openerp.com/download/modules/5.0/network_extension.zip>`_
  * `trunk <http://www.openerp.com/download/modules/trunk/network_extension.zip>`_

.. i18n: Dependencies
.. i18n: ------------
..

Dependencies
------------

.. i18n:  * :mod:`network`
..

 * :mod:`network`

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

.. i18n:  * Tools/Network/Software
.. i18n:  * Tools/Network/Logins/Passwords
.. i18n:  * Tools/Network/Services
.. i18n:  * Tools/Network/Configuration/Protocol
.. i18n:  * Tools/Network/Configuration/Encrypt/Decrypt password
..

 * Tools/Network/Software
 * Tools/Network/Logins/Passwords
 * Tools/Network/Services
 * Tools/Network/Configuration/Protocol
 * Tools/Network/Configuration/Encrypt/Decrypt password

.. i18n: Views
.. i18n: -----
..

Views
-----

.. i18n:  * \* INHERIT network.network.tree.ext1 (form)
.. i18n:  * \* INHERIT network.network.form.ext1 (form)
.. i18n:  * \* INHERIT network.network.form.ext2 (form)
.. i18n:  * \* INHERIT network.network.form.ext3 (form)
.. i18n:  * \* INHERIT network.network.form.ext4 (form)
.. i18n:  * \* INHERIT network.network.form.ext5 (form)
.. i18n:  * \* INHERIT network.material.tree.ext1 (form)
.. i18n:  * \* INHERIT network.material.form.ext1 (form)
.. i18n:  * \* INHERIT network.material.form.ext2 (form)
.. i18n:  * \* INHERIT network.view.software.tree.ext1 (form)
.. i18n:  * \* INHERIT network.software.form.ext1 (form)
.. i18n:  * \* INHERIT network.software.form.ext2 (form)
.. i18n:  * \* INHERIT network.password.tree.ext1 (form)
.. i18n:  * \* INHERIT network.password.tree.ext2 (form)
.. i18n:  * \* INHERIT network.password.form.ext1 (form)
.. i18n:  * \* INHERIT network.password.form.ext2 (form)
.. i18n:  * network.service.tree (tree)
.. i18n:  * network.service.form (form)
.. i18n:  * network.protocol.tree (tree)
.. i18n:  * network.protocol.form (form)
.. i18n:  * network.encrypt.password.tree (tree)
.. i18n:  * network.encrypt.password.form (form)
..

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

.. i18n: Objects
.. i18n: -------
..

Objects
-------

.. i18n: Object: Protocol (network.protocol)
.. i18n: ###################################
..

Object: Protocol (network.protocol)
###################################

.. i18n: :protocol: Protocol, selection, required
..

:protocol: Protocol, selection, required

.. i18n: :description: Description, char
..

:description: Description, char

.. i18n: :name: Name, char, required
..

:name: Name, char, required

.. i18n: :port: Port, integer, required
..

:port: Port, integer, required

.. i18n:     *Default port defined see(http://www.iana.org/assignments/port-numbers)*
..

    *Default port defined see(http://www.iana.org/assignments/port-numbers)*

.. i18n: Object: Service Network (network.service)
.. i18n: #########################################
..

Object: Service Network (network.service)
#########################################

.. i18n: :material: Material, many2one, readonly
..

:material: Material, many2one, readonly

.. i18n: :name: Name, char
..

:name: Name, char

.. i18n: :protocol_id: Protocol, many2one
..

:protocol_id: Protocol, many2one

.. i18n: :public_port: Public port, integer
..

:public_port: Public port, integer

.. i18n:     *Sometimes public and private ports are different.*
..

    *Sometimes public and private ports are different.*

.. i18n: :public_url: Public URL, char
..

:public_url: Public URL, char

.. i18n: :private_url: Private URL, char
..

:private_url: Private URL, char

.. i18n: :path: Path, char
..

:path: Path, char

.. i18n: :software_id: Software, many2one, required
..

:software_id: Software, many2one, required

.. i18n: :port: Port, integer, required
..

:port: Port, integer, required

.. i18n: Object: Password encryption (network.encrypt.password)
.. i18n: ######################################################
..

Object: Password encryption (network.encrypt.password)
######################################################

.. i18n: :name: Encrypt/Decrypt password, char
..

:name: Encrypt/Decrypt password, char
