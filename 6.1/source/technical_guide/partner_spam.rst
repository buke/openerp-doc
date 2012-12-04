
.. module:: partner_spam
    :synopsis: SMS and Email spam to partner 
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

    <div class="js-kit-rating" title="" permalink="" standalone="yes" path="/partner_spam"></div>
    <script src="http://js-kit.com/ratings.js"></script>

SMS and Email spam to partner (*partner_spam*)
==============================================
:Module: partner_spam
:Name: SMS and Email spam to partner
:Version: 5.0.1.0
:Author: Zikzakmedia SL
:Directory: partner_spam
:Web: www.zikzakmedia.com
:Official module: no
:Quality certified: no

Description
-----------

::

  Improved SMS and Email spam to partner:
    * Spam to partners and to partner.address (contacts)
    * Choice to spam all partner addresses or partner default addresses
    * The email field can contain several email addresses separated by ,
    * A maximum of 3 files can be attached to emails
    * Clickatell gateway to send SMS can be configured by http or by email
    * The spam text can include special [[field]] tags to create personalized messages (they will be replaced by the corresponding values of each partner contact):
        [[partner_id]] -> Partner name
        [[name]] -> Contact name
        [[function]] -> Function
        [[title]] -> Title
        [[street]] -> Street
        [[street2]] -> Street 2
        [[zip]] -> Zip code
        [[city]] -> City
        [[state_id]] -> State
        [[country_id]] -> Country
        [[email]] -> Email
        [[phone]] -> Phone
        [[fax]] -> Fax
        [[mobile]] -> Mobile
        [[birthdate]] -> Birthday

Download links
--------------

You can download this module as a zip file in the following version:

  * `4.2 <http://www.openerp.com/download/modules/4.2/partner_spam.zip>`_
  * `5.0 <http://www.openerp.com/download/modules/5.0/partner_spam.zip>`_
  * `trunk <http://www.openerp.com/download/modules/trunk/partner_spam.zip>`_


Dependencies
------------

 * :mod:`base`
 * :mod:`smtpclient`

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
