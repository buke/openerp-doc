
.. i18n: OpenERP Installation on Linux
.. i18n: =============================
..

OpenERP Installation on Linux
=============================

.. i18n: The installation procedure for OpenERP 6.1 under Linux is explained in this chapter. This procedure is well tested on Ubuntu
.. i18n: version 10.04 LTS. For those familiar with earlier OpenERP versions, the 6.1 series has a different architecture:
..

The installation procedure for OpenERP 6.1 under Linux is explained in this chapter. This procedure is well tested on Ubuntu
version 10.04 LTS. For those familiar with earlier OpenERP versions, the 6.1 series has a different architecture:

.. i18n: * The web client is now embedded in the main OpenERP Server, and does not require separate deployment
.. i18n: * The native GTK client is preserved as a legacy component, but the recommended way to use OpenERP is
.. i18n:   the web interface, as for all modern applications. There is usually no need to install the GTK client
.. i18n:   at all.
..

* The web client is now embedded in the main OpenERP Server, and does not require separate deployment
* The native GTK client is preserved as a legacy component, but the recommended way to use OpenERP is
  the web interface, as for all modern applications. There is usually no need to install the GTK client
  at all.

.. i18n: For **Debian-based distributions**, OpenERP is available as an All-In-One application package (``.deb``), that
.. i18n: can be installed with a simple click. The package is available on the `OpenERP website's download page <http://www.openerp.com/downloads>`_ 
..

For **Debian-based distributions**, OpenERP is available as an All-In-One application package (``.deb``), that
can be installed with a simple click. The package is available on the `OpenERP website's download page <http://www.openerp.com/downloads>`_ 

.. i18n: For **RedHat-based platforms**, an experimental RPM distribution is available in our nightly builds. See the `downloads page <http://www.openerp.com/downloads>`_ for more details. 
..

For **RedHat-based platforms**, an experimental RPM distribution is available in our nightly builds. See the `downloads page <http://www.openerp.com/downloads>`_ for more details. 

.. i18n: For **other Linux distributions** and for those who prefer a **manual installation**, there are only two steps
.. i18n: to deploy OpenERP under Linux: install PostgreSQL, the database engine used by OpenERP, then install OpenERP
.. i18n: itself. These steps are described in the following sections:
..

For **other Linux distributions** and for those who prefer a **manual installation**, there are only two steps
to deploy OpenERP under Linux: install PostgreSQL, the database engine used by OpenERP, then install OpenERP
itself. These steps are described in the following sections:

.. i18n: .. toctree::
.. i18n:     :glob:
.. i18n: 
.. i18n:     postgres/index
.. i18n:     server/index
.. i18n:     client/index
.. i18n:     web/index
.. i18n:     updating
..

.. toctree::
    :glob:

    postgres/index
    server/index
    client/index
    web/index
    updating
