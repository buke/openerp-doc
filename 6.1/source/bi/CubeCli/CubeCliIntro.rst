
.. i18n: .. _CLI-link:
.. i18n: 
.. i18n: Command Line Interface
.. i18n: ======================
..

.. _CLI-link:

Command Line Interface
======================

.. i18n: Introduction to the cli
.. i18n: -----------------------
..

Introduction to the cli
-----------------------

.. i18n: *The CLI - Command Line Interface*
..

*The CLI - Command Line Interface*

.. i18n: Command Line Interface is similar to that of psql, but used for MDX queries on the cube.
.. i18n: As
..

Command Line Interface is similar to that of psql, but used for MDX queries on the cube.
As

.. i18n: ::
.. i18n: 
.. i18n:  Welcome to OpenObject BI , the interactive terminal. 
.. i18n:  Communication: XML-RPC.
.. i18n:  Type: \? for help with MDX commands
.. i18n:       \e for execute the MDX query
.. i18n:       \d for quit
.. i18n:  BI-terp=#
..

::

 Welcome to OpenObject BI , the interactive terminal. 
 Communication: XML-RPC.
 Type: \? for help with MDX commands
      \e for execute the MDX query
      \d for quit
 BI-terp=#

.. i18n: Currently we can use CLI to test different queries, it can also be used for running automated tests.
..

Currently we can use CLI to test different queries, it can also be used for running automated tests.

.. i18n: The basic syntax for testing query is:
..

The basic syntax for testing query is:

.. i18n: **./tinybi.py -d <<Database Name>> -H localhost -U <<User Name> -W <<Password>> -p <<Port Number>> -s <<Schema Name>> -c <<MDX Query>>**
..

**./tinybi.py -d <<Database Name>> -H localhost -U <<User Name> -W <<Password>> -p <<Port Number>> -s <<Schema Name>> -c <<MDX Query>>**

.. i18n: One can check all these options by typing
..

One can check all these options by typing

.. i18n: *$python tinybi.py --help*
..

*$python tinybi.py --help*

.. i18n: Usage: tinybi.py [options]
..

Usage: tinybi.py [options]

.. i18n: Options:
..

Options:

.. i18n: ::
.. i18n: 
.. i18n:  --version             show program's version number and exit
.. i18n:  -h, --help            show this help message and exit
..

::

 --version             show program's version number and exit
 -h, --help            show this help message and exit

.. i18n: .. 
..

.. 

.. i18n: ::
.. i18n: 
.. i18n:  General options:
.. i18n:    -c COMMAND, --command=COMMAND
.. i18n:                        The query to execute
.. i18n:    -s SCHEMA, --schema=SCHEMA
.. i18n:                        The schema to use for the query
..

::

 General options:
   -c COMMAND, --command=COMMAND
                       The query to execute
   -s SCHEMA, --schema=SCHEMA
                       The schema to use for the query

.. i18n: .. 
..

.. 

.. i18n: ::
.. i18n: 
.. i18n:  Connection options:
.. i18n:    -d DATABASE, --database=DATABASE
.. i18n:                        Database name
.. i18n:    -H HOSTNAME, --hostname=HOSTNAME
.. i18n:                        Server hostname
.. i18n:    -U USERNAME, --username=USERNAME
.. i18n:                        Username
.. i18n:    -W PASSWORD, --password=PASSWORD
.. i18n:                        Password
.. i18n:    -p PORT, --port=PORT
.. i18n:                        Server port
..

::

 Connection options:
   -d DATABASE, --database=DATABASE
                       Database name
   -H HOSTNAME, --hostname=HOSTNAME
                       Server hostname
   -U USERNAME, --username=USERNAME
                       Username
   -W PASSWORD, --password=PASSWORD
                       Password
   -p PORT, --port=PORT
                       Server port

.. i18n: .. 
..

.. 

.. i18n: :Example:
..

:Example:

.. i18n: ./tinybi.py -d "terp" -H localhost -U admin -W admin -p 8069 -s "tinyerp" -c "select {[user].[all]} on rows, {[measures].[credit_limit],[measures].[count]} on columns from res_partner"
..

./tinybi.py -d "terp" -H localhost -U admin -W admin -p 8069 -s "tinyerp" -c "select {[user].[all]} on rows, {[measures].[credit_limit],[measures].[count]} on columns from res_partner"

.. i18n: This will give output on CLI as:
..

This will give output on CLI as:

.. i18n: .. csv-table:: 
.. i18n:    :header: "\ ","credit_limit","count"
.. i18n: 
.. i18n:    "All user","[66700.0]","[21.0]"
..

.. csv-table:: 
   :header: "\ ","credit_limit","count"

   "All user","[66700.0]","[21.0]"
