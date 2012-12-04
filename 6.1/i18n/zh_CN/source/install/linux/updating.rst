
.. i18n: .. index::
.. i18n:    single: Update; Upgrade; OpenERP (Linux)
..

.. index::
   single: Update; Upgrade; OpenERP (Linux)

.. i18n: .. _updating-linux-link:
.. i18n: 
.. i18n: ===============================================================================
.. i18n: Updating your OpenERP Installation
.. i18n: ===============================================================================
..

.. _updating-linux-link:

===============================================================================
Updating your OpenERP Installation
===============================================================================

.. i18n: Going to a Newer Minor/Patch Release
.. i18n: ++++++++++++++++++++++++++++++++++++
..

Going to a Newer Minor/Patch Release
++++++++++++++++++++++++++++++++++++

.. i18n: OpenERP's release policy states that minor/patch releases of the stable
.. i18n: versions are usually published every month. These are recommended for
.. i18n: production deployment, as they include the latest security updates and bugfixes,
.. i18n: and do not require any migration process.
..

OpenERP's release policy states that minor/patch releases of the stable
versions are usually published every month. These are recommended for
production deployment, as they include the latest security updates and bugfixes,
and do not require any migration process.

.. i18n: Of course you should always test these updates on a staging environment
.. i18n: (copy of your production environment) before applying them on the real
.. i18n: production systems.
..

Of course you should always test these updates on a staging environment
(copy of your production environment) before applying them on the real
production systems.

.. i18n: Minor/patch releases of OpenERP are identified by an increasing 3rd release
.. i18n: number, for example, v6.0.15 would be the 15th patch release of OpenERP v6.0.
..

Minor/patch releases of OpenERP are identified by an increasing 3rd release
number, for example, v6.0.15 would be the 15th patch release of OpenERP v6.0.

.. i18n: For more details regarding the release cycle, have a look at the section
.. i18n: :ref:`release_cycle`.
..

For more details regarding the release cycle, have a look at the section
:ref:`release_cycle`.

.. i18n: .. note:: Minor Versions
.. i18n: 
.. i18n:         You can skip minor versions, for example, you do not need to install all the intermediary versions between 6.0.6 and 6.0.15 if you need to upgrade an outdated installation, as long as you stay in the same version line (6.0 in this example).
..

.. note:: Minor Versions

        You can skip minor versions, for example, you do not need to install all the intermediary versions between 6.0.6 and 6.0.15 if you need to upgrade an outdated installation, as long as you stay in the same version line (6.0 in this example).

.. i18n: Updating an existing OpenERP installation to a newer patch release boils down
.. i18n: to 2 operations:
..

Updating an existing OpenERP installation to a newer patch release boils down
to 2 operations:

.. i18n:     * Install the new code over the existing one
.. i18n:     * Synchronize each existing database with the new code
..

    * Install the new code over the existing one
    * Synchronize each existing database with the new code

.. i18n: In order to accomplish this, the following step-by-step procedure should give you
.. i18n: the best results:
..

In order to accomplish this, the following step-by-step procedure should give you
the best results:

.. i18n:     #. Make a fresh backup of all existing databases, as well as a backup of the files 
.. i18n:        of your OpenERP installation (server and addons), just in case.
.. i18n:     #. Locate the executable file to start the Server, it should be named
.. i18n:        ``openerp-server.py``. You may want to have a look at the running processes
.. i18n:        to find out the command-line parameters that are passed to the server (needed below).
.. i18n:     #. Stop the OpenERP server.
.. i18n:     #. Update the source files to the latest release, or simply install the new releases
.. i18n:        over the previous ones.
.. i18n:     #. Start the server manually (directly call the executable you located above), with
.. i18n:        the following additional parameters, to trigger an update of all module data and
.. i18n:        views in the database, based on the new source files (include your usual startup
.. i18n:        parameters, if any, and replace ``DB_NAME`` with the name of the OpenERP database you wish
.. i18n:        to update)::
.. i18n: 
.. i18n:          openerp-server.py -d DB_NAME -u all
.. i18n: 
.. i18n:     #. Let the server complete its startup (watch the log for the final message that says
.. i18n:        ``OpenERP server is running, waiting for connections`` or wait until you can connect
.. i18n:        to that database with a GTK client), then stop the server with :kbd:`Ctrl+C` and repeat the
.. i18n:        previous step for each database on this OpenERP installation (any database not updated
.. i18n:        will use the latest business logic but might have errors or missing improvements in
.. i18n:        the views until you update it using this procedure).
.. i18n:     #. Stop the server again with :kbd:`Ctrl+C` and restart it normally (no extra parameters anymore).
.. i18n:     #. You can now proceed with the update of the GTK clients,
.. i18n:        by simply reinstalling the latest version over the previous one.
..

    #. Make a fresh backup of all existing databases, as well as a backup of the files 
       of your OpenERP installation (server and addons), just in case.
    #. Locate the executable file to start the Server, it should be named
       ``openerp-server.py``. You may want to have a look at the running processes
       to find out the command-line parameters that are passed to the server (needed below).
    #. Stop the OpenERP server.
    #. Update the source files to the latest release, or simply install the new releases
       over the previous ones.
    #. Start the server manually (directly call the executable you located above), with
       the following additional parameters, to trigger an update of all module data and
       views in the database, based on the new source files (include your usual startup
       parameters, if any, and replace ``DB_NAME`` with the name of the OpenERP database you wish
       to update)::

         openerp-server.py -d DB_NAME -u all

    #. Let the server complete its startup (watch the log for the final message that says
       ``OpenERP server is running, waiting for connections`` or wait until you can connect
       to that database with a GTK client), then stop the server with :kbd:`Ctrl+C` and repeat the
       previous step for each database on this OpenERP installation (any database not updated
       will use the latest business logic but might have errors or missing improvements in
       the views until you update it using this procedure).
    #. Stop the server again with :kbd:`Ctrl+C` and restart it normally (no extra parameters anymore).
    #. You can now proceed with the update of the GTK clients,
       by simply reinstalling the latest version over the previous one.

.. i18n: .. note:: Server
.. i18n: 
.. i18n:         As an alternative to restarting the server in update mode for each database, as described above, you may try to start the server normally, and then connect to each database as the *Administrator* user, open the list of modules and manually trigger an update of the *base* module. Because all modules depend on *base* they will be updated too. However this requires the *Administrator* password of each database and may not work for some updates, specifically when the update prevents you from logging into the system.
..

.. note:: Server

        As an alternative to restarting the server in update mode for each database, as described above, you may try to start the server normally, and then connect to each database as the *Administrator* user, open the list of modules and manually trigger an update of the *base* module. Because all modules depend on *base* they will be updated too. However this requires the *Administrator* password of each database and may not work for some updates, specifically when the update prevents you from logging into the system.

.. i18n: .. tip:: Developer Book
.. i18n: 
.. i18n:         For more technical details on the actual operations accomplished by the server during such an update, you may refer to the corresponding section in the Developer Book: :ref:`technical_update_procedure`.
..

.. tip:: Developer Book

        For more technical details on the actual operations accomplished by the server during such an update, you may refer to the corresponding section in the Developer Book: :ref:`technical_update_procedure`.

.. i18n: Going to a Newer Major Release
.. i18n: ++++++++++++++++++++++++++++++
..

Going to a Newer Major Release
++++++++++++++++++++++++++++++

.. i18n: The frequency of major stable releases has fluctuated in the past, but the current policy is to release a new stable version every 6 months on average, with one out of three stable versions being a Long Term Support (LTS) version. An LTS version is a normal stable version, but one that is supported for an extended time under the OpenERP Publisher’s Warranty (OPW). Stable versions are labelled as a decimal number with 2 components (e.g. 6.1), where the leftmost part indicates the corresponding Long Term Support (LTS) version, and the second digit indicates successive stable releases between two LTS versions.
..

The frequency of major stable releases has fluctuated in the past, but the current policy is to release a new stable version every 6 months on average, with one out of three stable versions being a Long Term Support (LTS) version. An LTS version is a normal stable version, but one that is supported for an extended time under the OpenERP Publisher’s Warranty (OPW). Stable versions are labelled as a decimal number with 2 components (e.g. 6.1), where the leftmost part indicates the corresponding Long Term Support (LTS) version, and the second digit indicates successive stable releases between two LTS versions.

.. i18n: Transitioning to the next major release implies a lot more changes than jumping to another minor release.
.. i18n: As the underlying OpenERP data structures usually evolve quite a bit from one major release to the next, a full migration of the existing data is needed.
.. i18n: Each major release will be published with specific recommendations and procedures for upgrading an existing OpenERP system to the next major version.
..

Transitioning to the next major release implies a lot more changes than jumping to another minor release.
As the underlying OpenERP data structures usually evolve quite a bit from one major release to the next, a full migration of the existing data is needed.
Each major release will be published with specific recommendations and procedures for upgrading an existing OpenERP system to the next major version.
