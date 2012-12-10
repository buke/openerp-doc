
.. i18n: .. index::
.. i18n:    single: Update; Upgrade; OpenERP (Windows)
..

.. index::
   single: Update; Upgrade; OpenERP (Windows)

.. i18n: .. _updating-windows-link:
.. i18n: 
.. i18n: ===============================================================================
.. i18n: Updating your OpenERP Installation
.. i18n: ===============================================================================
..

.. _updating-windows-link:

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
.. i18n: (copy of your production environment) before actually applying them on the real
.. i18n: production systems.
..

Of course you should always test these updates on a staging environment
(copy of your production environment) before actually applying them on the real
production systems.

.. i18n: For more details regarding the release cycle, have a look at the section
.. i18n: :ref:`release_cycle`.
..

For more details regarding the release cycle, have a look at the section
:ref:`release_cycle`.

.. i18n: Minor/patch releases of OpenERP are identified by an increasing 3rd release
.. i18n: number, for example, v6.0.15 would be the 15th patch release of OpenERP v6.0.
..

Minor/patch releases of OpenERP are identified by an increasing 3rd release
number, for example, v6.0.15 would be the 15th patch release of OpenERP v6.0.

.. i18n: .. note:: Minor Versions
.. i18n: 
.. i18n:         You can skip minor versions, for example, you do not need to install all the intermediary versions between 6.0.6 and 6.0.15 if you need to upgrade an outdated installation, as long as you stay in the same version line (6.0 in this example).
..

.. note:: Minor Versions

        You can skip minor versions, for example, you do not need to install all the intermediary versions between 6.0.6 and 6.0.15 if you need to upgrade an outdated installation, as long as you stay in the same version line (6.0 in this example).

.. i18n: Updating an existing OpenERP installation to a newer patch release boils down to 2 operations:
..

Updating an existing OpenERP installation to a newer patch release boils down to 2 operations:

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
.. i18n:     #. Stop the OpenERP server.
.. i18n:     #. Update the source files to the latest release, or simply install the new releases
.. i18n:        over the previous ones. If need be, you can uninstall the previous version, but
.. i18n:        be sure to avoid uninstalling PostgreSQL, as this could delete
.. i18n:        your current databases!
.. i18n:     #. Locate the separate server executable ``openerp-server.exe`` (this is not the
.. i18n:        executable used by the Windows Service!). It should be in the location where
.. i18n:        you installed OpenERP Server, for example in ``C:\Programs\OpenERP 6.0\Server``.
.. i18n:     #. From a Command-Line Prompt, start the server executable manually (directly call
.. i18n:        the executable you located above), with the following parameters, to trigger an
.. i18n:        update of all module data and views in the database, based on the new source files
.. i18n:        (include your usual startup parameters, if any, and replace ``DB_NAME`` with the name
.. i18n:        of the OpenERP database you wish to update)::
.. i18n: 
.. i18n:          openerp-server.exe -d DB_NAME -u all
.. i18n: 
.. i18n:     #. Let the server complete its startup (watch the log file for the final message that
.. i18n:        says ``OpenERP server is running, waiting for connections`` or wait until you can
.. i18n:        connect to that database with a GTK client), then stop the server using the :kbd:`Ctrl+C`
.. i18n:        key combination and repeat previous step for each database on this OpenERP installation
.. i18n:        (any database not updated will use the latest business logic but might have errors
.. i18n:        or missing improvements in the views until you update it using this procedure).
.. i18n:     #. Stop the server again with :kbd:`Ctrl+C` and restart it normally as a service.
.. i18n:     #. You can now proceed with the update of the GTK clients, which can be done
.. i18n:        separately by simply reinstalling the latest version over the previous one.
..

    #. Make a fresh backup of all existing databases, as well as a backup of the files
       of your OpenERP installation (server and addons), just in case.
    #. Stop the OpenERP server.
    #. Update the source files to the latest release, or simply install the new releases
       over the previous ones. If need be, you can uninstall the previous version, but
       be sure to avoid uninstalling PostgreSQL, as this could delete
       your current databases!
    #. Locate the separate server executable ``openerp-server.exe`` (this is not the
       executable used by the Windows Service!). It should be in the location where
       you installed OpenERP Server, for example in ``C:\Programs\OpenERP 6.0\Server``.
    #. From a Command-Line Prompt, start the server executable manually (directly call
       the executable you located above), with the following parameters, to trigger an
       update of all module data and views in the database, based on the new source files
       (include your usual startup parameters, if any, and replace ``DB_NAME`` with the name
       of the OpenERP database you wish to update)::

         openerp-server.exe -d DB_NAME -u all

    #. Let the server complete its startup (watch the log file for the final message that
       says ``OpenERP server is running, waiting for connections`` or wait until you can
       connect to that database with a GTK client), then stop the server using the :kbd:`Ctrl+C`
       key combination and repeat previous step for each database on this OpenERP installation
       (any database not updated will use the latest business logic but might have errors
       or missing improvements in the views until you update it using this procedure).
    #. Stop the server again with :kbd:`Ctrl+C` and restart it normally as a service.
    #. You can now proceed with the update of the GTK clients, which can be done
       separately by simply reinstalling the latest version over the previous one.

.. i18n: .. note:: Server 
.. i18n: 
.. i18n:         As an alternative to restarting the server in update mode for each database, as described above, you may try to start the server normally after installing the new version, and then connect to each database as the *Administrator* user, open the list of modules and manually trigger an update of the *base* module.
.. i18n:         
.. i18n:         Because all modules depend on *base* they will be updated too. However this requires the *Administrator* password of each database and may not work for some updates, specifically when the update prevents you from logging into the system.
..

.. note:: Server 

        As an alternative to restarting the server in update mode for each database, as described above, you may try to start the server normally after installing the new version, and then connect to each database as the *Administrator* user, open the list of modules and manually trigger an update of the *base* module.
        
        Because all modules depend on *base* they will be updated too. However this requires the *Administrator* password of each database and may not work for some updates, specifically when the update prevents you from logging into the system.

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

.. i18n: OpenERP's release policy states that one or two major releases are published from the
.. i18n: development version every year. Transitioning to the next major release implies a lot
.. i18n: more changes than jumping to another minor release.
.. i18n: As the underlying OpenERP data structures usually evolve quite a bit from one major release
.. i18n: to the next, a full migration of the existing data is needed.
.. i18n: Each major release will be published with specific recommendations and procedures for
.. i18n: upgrading an existing OpenERP system to the next major version.
..

OpenERP's release policy states that one or two major releases are published from the
development version every year. Transitioning to the next major release implies a lot
more changes than jumping to another minor release.
As the underlying OpenERP data structures usually evolve quite a bit from one major release
to the next, a full migration of the existing data is needed.
Each major release will be published with specific recommendations and procedures for
upgrading an existing OpenERP system to the next major version.

.. i18n: .. note:: Major Release
.. i18n: 
.. i18n:         For major releases, it is usually not possible to skip one release, for example upgrading directly from OpenERP 4.2 to OpenERP 6.0. If you need to do such an upgrade, you will simply have to do each intermediary upgrade one after the other.
..

.. note:: Major Release

        For major releases, it is usually not possible to skip one release, for example upgrading directly from OpenERP 4.2 to OpenERP 6.0. If you need to do such an upgrade, you will simply have to do each intermediary upgrade one after the other.
