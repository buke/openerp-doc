
.. index::
   single: Installation; OpenERP Web (Windows)
   single: OpenERP Web; Installation (Windows)
.. 

.. windows-web-link:

OpenERP Web Installation
========================

You have to install, configure and run the OpenERP Server before using the
OpenERP Web. The web client needs the server to run. You can install the server
application on your computer, or on an independent server accessible by
network.

*Downloading the OpenERP Web*

The OpenERP Web can be downloaded from
`OpenERP website's download page <http://www.openerp.com/downloads>`_.

Under `Windows Auto-Installer`, choose **Web** to download the OpenERP Web standalone.

*Installing the OpenERP Web*

Click the executable installation file you have just downloaded, and proceed with the following steps:

* 1. Select installation language
	The default is ``English``. The other option is ``French``.

* 2. Welcome message
	Carefully follow the recommendations given in this step.

* 3. Licence Agreement
	It is important that you accept the OpenERP Public License (OEPL) Version 1.1 to proceed with installation. This licence is based on the Mozilla Public Licence (MPL) Version 1.1.

  .. image:: ../../img/w3_licence.png

  *OpenERP Public Licence*

* 4. Select folder for installation
	By default, OpenERP Web is installed in ``C:\Program Files\OpenERP 6.0\Web``. To install in a different folder, browse for a different location(folder) in this step.

* 5. Create shortcuts
	Select a folder in the `Start` menu where you would like to create the program's shortcuts.

  .. image:: ../../img/w5_shortcuts.png

  *Create Start menu shortcuts*

* 6. Install
	The automatic installation of OpenERP Web begins and you can view its progress simultaneously.

* 7. Finish
	On successful installation of OpenERP Web, you will get an appropriate confirmation. You can click `Finish` to close the setup wizard.

The Windows service for OpenERP Web Server is also installed and is set up
to start the server automatically on system boot.

*Starting the Web Client*

Now as the web server is initialized and the settings are saved, you can finally start 
the OpenERP Web.

Use a web browser of your choice to connect to OpenERP Web. If your web client is installed on the same computer as the server, you can navigate to http://localhost:8080 to connect to the OpenERP web version. If the server is installed on a separate computer, you must know the name or IP address of the server over the network and navigate to http://<server_address>:8080 to connect to OpenERP.

.. figure:: ../../img/web_startup.png
   :scale: 70
   :align: center

   *Web Client at startup*

