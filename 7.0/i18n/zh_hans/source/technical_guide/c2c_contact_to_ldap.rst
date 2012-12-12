
.. i18n: .. module:: c2c_contact_to_ldap
.. i18n:     :synopsis: Camptocamp Partner extension to synchronize OpenERP with LDAP 
.. i18n:     :noindex:
.. i18n: .. 
..

.. module:: c2c_contact_to_ldap
    :synopsis: Camptocamp Partner extension to synchronize OpenERP with LDAP 
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
.. i18n:     <div class="js-kit-rating" title="" permalink="" standalone="yes" path="/c2c_contact_to_ldap"></div>
.. i18n:     <script src="http://js-kit.com/ratings.js"></script>
..

.. raw:: html

    <div class="js-kit-rating" title="" permalink="" standalone="yes" path="/c2c_contact_to_ldap"></div>
    <script src="http://js-kit.com/ratings.js"></script>

.. i18n: Camptocamp Partner extension to synchronize OpenERP with LDAP (*c2c_contact_to_ldap*)
.. i18n: =====================================================================================
.. i18n: :Module: c2c_contact_to_ldap
.. i18n: :Name: Camptocamp Partner extension to synchronize OpenERP with LDAP
.. i18n: :Version: 5.0.1.2
.. i18n: :Author: Camptocamp
.. i18n: :Directory: c2c_contact_to_ldap
.. i18n: :Web: http://www.camptocamp.com
.. i18n: :Official module: no
.. i18n: :Quality certified: no
..

Camptocamp Partner extension to synchronize OpenERP with LDAP (*c2c_contact_to_ldap*)
=====================================================================================
:Module: c2c_contact_to_ldap
:Name: Camptocamp Partner extension to synchronize OpenERP with LDAP
:Version: 5.0.1.2
:Author: Camptocamp
:Directory: c2c_contact_to_ldap
:Web: http://www.camptocamp.com
:Official module: no
:Quality certified: no

.. i18n: Description
.. i18n: -----------
..

Description
-----------

.. i18n: ::
.. i18n: 
.. i18n:   Live partner address synchronization through a LDAP module (inetOrgPerson). 
.. i18n:   Tiny becomes the master of the LDAP. Each time an address is deleted, created or updated the same is done in the LDAP (a new record is pushed).
.. i18n:   The LDAP configuration is done in the company view. There can be one different LDAP per company! Do not forget to activate
.. i18n:   the LDAP link in the configuration. 
.. i18n:   The LDAP used depends on the current user company.
.. i18n:       
.. i18n:   This module does not allow bulk batching synchronisation into the LDAP and is thus not suitable for instant use with an existing LDAP.
.. i18n:   In order to use it with an existing LDAP you have to alter the uid of contact in your LDAP. The uid should be terp_ plus the OpenERP contact id (for example terp_10).  
.. i18n:       
.. i18n:   N.B: the module requires the python-ldap library
.. i18n:   
.. i18n:   ---------------------------------------------------------------------------------------------------------------------------------------
.. i18n:   Ce module interface les partenaires OpenERP avec un repository LDAP existant. Ainsi, OpenERP devient le master, l'interface unique
.. i18n:   de saisie des partenaires de l'entreprise. Tous ce qui est renseigné dans OpenERP est automatiquement reporté dans 
.. i18n:   LDAP (ajout, suppression, modification). 
.. i18n:   
.. i18n:   L'avantage d'utiliser un tel système est la constitution d'une base de données
.. i18n:   client unique , qui pourra s'interfacer avec un client mail (Outlook, Thunderbird, etc..) pour avoir la complétion des adresses dans la 
.. i18n:   rédaction des mails. De plus, de nombreux systèmes de téléphonie utilisent maintenant une telle base pour la gestion des appels 
.. i18n:   (click to dial ou remontée de fiche).
.. i18n:   
.. i18n:   
.. i18n:   --!!!!!!! V5 change log 
.. i18n:   added OU specification
.. i18n:   Unicode support --> As python LDAP does not support unicode we try to decode string - if it fails we transliterate values
.. i18n:   Active Directory Support
..

::

  Live partner address synchronization through a LDAP module (inetOrgPerson). 
  Tiny becomes the master of the LDAP. Each time an address is deleted, created or updated the same is done in the LDAP (a new record is pushed).
  The LDAP configuration is done in the company view. There can be one different LDAP per company! Do not forget to activate
  the LDAP link in the configuration. 
  The LDAP used depends on the current user company.
      
  This module does not allow bulk batching synchronisation into the LDAP and is thus not suitable for instant use with an existing LDAP.
  In order to use it with an existing LDAP you have to alter the uid of contact in your LDAP. The uid should be terp_ plus the OpenERP contact id (for example terp_10).  
      
  N.B: the module requires the python-ldap library
  
  ---------------------------------------------------------------------------------------------------------------------------------------
  Ce module interface les partenaires OpenERP avec un repository LDAP existant. Ainsi, OpenERP devient le master, l'interface unique
  de saisie des partenaires de l'entreprise. Tous ce qui est renseigné dans OpenERP est automatiquement reporté dans 
  LDAP (ajout, suppression, modification). 
  
  L'avantage d'utiliser un tel système est la constitution d'une base de données
  client unique , qui pourra s'interfacer avec un client mail (Outlook, Thunderbird, etc..) pour avoir la complétion des adresses dans la 
  rédaction des mails. De plus, de nombreux systèmes de téléphonie utilisent maintenant une telle base pour la gestion des appels 
  (click to dial ou remontée de fiche).
  
  
  --!!!!!!! V5 change log 
  added OU specification
  Unicode support --> As python LDAP does not support unicode we try to decode string - if it fails we transliterate values
  Active Directory Support

.. i18n: Download links
.. i18n: --------------
..

Download links
--------------

.. i18n: You can download this module as a zip file in the following version:
..

You can download this module as a zip file in the following version:

.. i18n:   * `4.2 <http://www.openerp.com/download/modules/4.2/c2c_contact_to_ldap.zip>`_
..

  * `4.2 <http://www.openerp.com/download/modules/4.2/c2c_contact_to_ldap.zip>`_

.. i18n: Dependencies
.. i18n: ------------
..

Dependencies
------------

.. i18n:  * :mod:`base`
.. i18n:  * :mod:`c2c_partner_address`
..

 * :mod:`base`
 * :mod:`c2c_partner_address`

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

.. i18n: None
..

None

.. i18n: Views
.. i18n: -----
..

Views
-----

.. i18n:  * \* INHERIT res.company.form (form)
..

 * \* INHERIT res.company.form (form)

.. i18n: Objects
.. i18n: -------
..

Objects
-------

.. i18n: None
..

None
