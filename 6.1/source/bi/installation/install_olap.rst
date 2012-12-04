.. _install-olap:

Installation of Open Object
===========================

To install BI we need to have :

#. Getting and running `OpenERP Server`_

#. Getting `SQLAlchemy-0.3.11`_

Once everything is working i.e. OpenERP Server and OpenERP Client we need to add OLAP module in Server.

Steps to install OLAP modules.

	For server module:

	* First install the Bazaar on your Linux box (apt-get install bzr) then “cd” to /usr/ 
	  local/src folder or other, as you work usually.  
	* Get the Launchpad’s BI branch with the command: 
	  From : https://code.launchpad.net/~openerp/openobject-addons/trunk bzr branch lp:openobject-addons This openobject-addons
	  contain the bi in Olap modules

	For client-web-bi:
	
	* https://code.launchpad.net/~openerp-dev/openobject-client-web/trunk-dev-web-bi
	* bzr branch for client-web-bi lp:~openerp-dev/openobject-client-web/trunk-dev-web-bi
	
	* Get SQLAlchemy-x.x.x.tar.gz from sourceforge.net and untar (tar –xzvf file_name) it to
	  the /usr/local/src folder then cd to /usr/local/src/ SQLAlchemy-x.x.x and run ‘’python
	  setup.py install’’
	
	* The SQLAlchemy install will push all that we need to the /usr/lib/python2.5/site-
	  packages/SQLAlchemy-0.5.2-py2.5.egg, ‘’cd’’ to this folder and do the “zip” like this:
	
	* zip /somewhere/sqlalchemy.zip -r sqlalchemy
	
	* Move or copy (mv or cp) the sqlachemy.zip to the openerp-server addons folder (/usr/lib
	  /python2.5/site-packages/openerp -server/addons) and unzip the file within.
	
	* Check also the owner and the rights of ~/addons folder, as I run the openerp-server
	  with postgres user I switched the ~/addons owner to ‘’chown -R postgres addons’’
	
	* Retrieve all the olap’s ‘’zip’’ files and import/install them to OpenERP v5.

	Setup install packages for Windows:
	
	* http://bazaar.launchpad.net/~openerp/openerp/win-installer-trunk/files/head%3A/dependencies/

=======


.. _OpenERP Server: http://openerp.com/wiki/index.php/InstallationManual/HomePage
.. _SQLAlchemy-0.3.11: http://sourceforge.net/projects/sqlalchemy/ SQLAlchemy-0.3.11


