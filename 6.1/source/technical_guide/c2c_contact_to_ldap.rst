
.. module:: c2c_contact_to_ldap
    :synopsis: Camptocamp Partner extension to synchronize OpenERP with LDAP 
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

    <div class="js-kit-rating" title="" permalink="" standalone="yes" path="/c2c_contact_to_ldap"></div>
    <script src="http://js-kit.com/ratings.js"></script>

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

Description
-----------

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

Download links
--------------

You can download this module as a zip file in the following version:

  * `4.2 <http://www.openerp.com/download/modules/4.2/c2c_contact_to_ldap.zip>`_


Dependencies
------------

 * :mod:`base`
 * :mod:`c2c_partner_address`

Reports
-------

None


Menus
-------


None


Views
-----

 * \* INHERIT res.company.form (form)


Objects
-------

None
