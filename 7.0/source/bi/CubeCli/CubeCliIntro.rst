.. _CLI-link:

Command Line Interface
======================

Introduction to the cli
-----------------------

*The CLI - Command Line Interface*

Command Line Interface is similar to that of psql, but used for MDX queries on the cube.
As

::

 Welcome to OpenObject BI , the interactive terminal. 
 Communication: XML-RPC.
 Type: \? for help with MDX commands
      \e for execute the MDX query
      \d for quit
 BI-terp=#

Currently we can use CLI to test different queries, it can also be used for running automated tests.

The basic syntax for testing query is:

**./tinybi.py -d <<Database Name>> -H localhost -U <<User Name> -W <<Password>> -p <<Port Number>> -s <<Schema Name>> -c <<MDX Query>>**

One can check all these options by typing

*$python tinybi.py --help*

Usage: tinybi.py [options]

Options:

::

 --version             show program's version number and exit
 -h, --help            show this help message and exit

.. 

::

 General options:
   -c COMMAND, --command=COMMAND
                       The query to execute
   -s SCHEMA, --schema=SCHEMA
                       The schema to use for the query

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

.. 

:Example:

./tinybi.py -d "terp" -H localhost -U admin -W admin -p 8069 -s "tinyerp" -c "select {[user].[all]} on rows, {[measures].[credit_limit],[measures].[count]} on columns from res_partner"

This will give output on CLI as:

.. csv-table:: 
   :header: "\ ","credit_limit","count"

   "All user","[66700.0]","[21.0]"


