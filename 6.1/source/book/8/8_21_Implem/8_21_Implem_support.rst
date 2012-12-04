
.. index::
   single: maintenance
   single: support

Support and Maintenance
=======================

It is when you actually use your ERP that you will obtain value from your investment. For that reason,
maintenance and support are critical for your long term success.

* Support aims to ensure that end users get the maximum productivity from their use of OpenERP, by
  responding to their questions on the use of the system. Support can be technical or functional.

* Maintenance aims to ensure that the system itself continues to function as required. It includes
  system upgrades, which give you access to the latest functionality available.

Some partners offer preventative maintenance. This makes sure that all the specific developments for
your system are revised and tested for each new version so that they remain compatible with the base
OpenERP.

Tiny themselves have changed their support strategy from time to time. At the time of writing,
they propose a maintenance contract supplied either direct to the end user or through partners
that guarantees a quick fix to any faults discovered in the covered code. Although you can 
expect these fixes to become available to all users of the code in time, maintenance
guarantees quick attention. And you are likely to get quicker migration support to new upgrades.

If you have not anticipated your needs with a preventive maintenance contract, the costs of migration
after a few years can become significant. If special modules that you developed have been allowed to
become too old, you may eventually need a new development according to your specifications.

.. index:: 
   single: update
   single: upgrade
   
Updates and Upgrades
--------------------

There are four sources of code change for OpenERP:

* patches supplied by Tiny to correct faults: after validation these patches should not cause any
  secondary effects,

* minor updates, which gather the fault corrections together in one package, and are generally
  announced with a modification of the version number, such as from 6.0.0 to 6.0.1,

* upgrades, which bundle both the fault corrections and the improvements to the functionality in a
  major release, such as from 6.0.3 to 6.2.0,

* new functions, generally released in the form of new modules.

You should establish a procedure with your supplier to define how to respond to changes in the
OpenERP code.

For simple updates, your maintenance team will evaluate the patches to determine if they are
beneficial to the use of your OpenERP. These patches should be tested on an offline instance of
OpenERP before being installed in your live production version.

The maintenance team would also take charge of regular updates to the software.

Patches and updates can only be installed if you have the necessary access to the OpenERP server.
You must first install the patch or update and then restart the server using the command line: \
``--update=all``\  .

Once Tiny has released a new upgraded version, your response should be a cautious one. If you are
perfectly satisfied with the existing system, it would be best to not touch the new version. If you
want to have access to the new functionality supplied by an upgraded version, you have a delicate
operation to carry out. Most upgrades require your data to be migrated, because the databases before
and after the upgrade can be a little different.

.. index:: 
   single: migration

Version Migration
-----------------

OpenERP has a system to manage migrations semi-automatically. To update specific modules, or the whole
database, you only need to start the server with the argument: \ ``--update=NAME_OF_MODULE`` \ or
\ ``--update=all`` \ (that is minor module changes).

New stable versions of OpenERP sometimes require operations that are not provided in the automated
migration. Tiny, the creator and maintainer of OpenERP, has a policy of supporting migration from
all official stable releases to the latest. Scripts are provided for each new release of a stable
version. These carry out the upgrade from the previous major version to the new major version.

Managers responsible for the migration between two versions of OpenERP will find the
documentation and the necessary scripts in the directory \ ``doc/migrate`` \ of the OpenERP
server.

The changes between version 4 and 5 made the migration process more difficult than in the past,
so there was a greater delay in the provision of migration assistance and more manual work
than usual.

The procedure for migrating runs like this:

	#. Make a backup of the database from the old version of OpenERP.

	#. Stop the server running the old version.

	#. Start the script called \ ``pre.py``\  for the versions you are moving between.

	#. Start the new version of the server using the option \ ``--update=all`` \.

	#. Stop the server running the new version.

	#. Start the script called \ ``post.py`` \ for the versions you are moving between.

	#. Start the new version of the server and test it.

A migration is never an easy process. It may be possible that your system does not function as it did before,
or that something requires new developments in the functionality of the modules that have already
been installed. So you should only move to a new version if you have a real need, and should engage a
competent partner to help if the version that you use differs greatly from the basic version of
OpenERP.

Similarly, you should take care that this migration does not incorrectly change any setting
that has already been made. The main menu structure might have been modified in place
without proper recording of the changes. 
So you could find that you are making the wrong assumptions about that structure
when later loading data that was recorded with the :guilabel:`Module Recorder`.

.. Copyright © Open Object Press. All rights reserved.

.. You may take electronic copy of this publication and distribute it if you don't
.. change the content. You can also print a copy to be read by yourself only.

.. We have contracts with different publishers in different countries to sell and
.. distribute paper or electronic based versions of this book (translated or not)
.. in bookstores. This helps to distribute and promote the OpenERP product. It
.. also helps us to create incentives to pay contributors and authors using author
.. rights of these sales.

.. Due to this, grants to translate, modify or sell this book are strictly
.. forbidden, unless Tiny SPRL (representing Open Object Press) gives you a
.. written authorisation for this.

.. Many of the designations used by manufacturers and suppliers to distinguish their
.. products are claimed as trademarks. Where those designations appear in this book,
.. and Open Object Press was aware of a trademark claim, the designations have been
.. printed in initial capitals.

.. While every precaution has been taken in the preparation of this book, the publisher
.. and the authors assume no responsibility for errors or omissions, or for damages
.. resulting from the use of the information contained herein.

.. Published by Open Object Press, Grand Rosière, Belgium

