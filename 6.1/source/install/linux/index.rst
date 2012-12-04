
OpenERP Installation on Linux
=============================

The installation procedure for OpenERP 6.1 under Linux is explained in this chapter. This procedure is well tested on Ubuntu
version 10.04 LTS. For those familiar with earlier OpenERP versions, the 6.1 series has a different architecture:

* The web client is now embedded in the main OpenERP Server, and does not require separate deployment
* The native GTK client is preserved as a legacy component, but the recommended way to use OpenERP is
  the web interface, as for all modern applications. There is usually no need to install the GTK client
  at all.

For **Debian-based distributions**, OpenERP is available as an All-In-One application package (``.deb``), that
can be installed with a simple click. The package is available on the `OpenERP website's download page <http://www.openerp.com/downloads>`_ 

For **RedHat-based platforms**, an experimental RPM distribution is available in our nightly builds. See the `downloads page <http://www.openerp.com/downloads>`_ for more details. 

For **other Linux distributions** and for those who prefer a **manual installation**, there are only two steps
to deploy OpenERP under Linux: install PostgreSQL, the database engine used by OpenERP, then install OpenERP
itself. These steps are described in the following sections:


.. toctree::
    :glob:

    postgres/index
    server/index
    client/index
    web/index
    updating
