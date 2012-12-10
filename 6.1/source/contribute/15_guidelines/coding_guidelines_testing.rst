
.. i18n: .. sectnum::
.. i18n:     :start: 3
..

.. sectnum::
    :start: 3

.. i18n: .. _yaml-testing-guidelines:
.. i18n: 
.. i18n: ==============================
.. i18n: Automated YAML Tests Guideline
.. i18n: ==============================
..

.. _yaml-testing-guidelines:

==============================
Automated YAML Tests Guideline
==============================

.. i18n: .. note::
.. i18n: 
.. i18n:     Please see also section :ref:`yaml-serialization`
..

.. note::

    Please see also section :ref:`yaml-serialization`

.. i18n: This is a guideline for project managers and developers on automated tests. 
..

This is a guideline for project managers and developers on automated tests. 

.. i18n: Syntax
.. i18n: ------
..

Syntax
------

.. i18n:     Write scenarios using the YAML syntax, not the "cucumber" syntax,  so
.. i18n:     that we can directly integrate these tests in OpenERP modules (and implement
.. i18n:     them later).
..

    Write scenarios using the YAML syntax, not the "cucumber" syntax,  so
    that we can directly integrate these tests in OpenERP modules (and implement
    them later).

.. i18n: Tests are run on the server side
.. i18n: --------------------------------
..

Tests are run on the server side
--------------------------------

.. i18n: As tests are performed server side, you don't need to write things like
..

As tests are performed server side, you don't need to write things like

.. i18n:     ::
.. i18n: 
.. i18n:         # wrong
.. i18n:         * Given I am logged in as admin user with proper password
.. i18n:         * module pos is installed
.. i18n: 
.. i18n:     The user is admin by default, so no need to write this in each test
.. i18n:     file. Instead of saying 'I check that the module pos is installed',
.. i18n:     just write the name of the module where you will put this test. The first
.. i18n:     line would then be **"module: pos"**.
..

    ::

        # wrong
        * Given I am logged in as admin user with proper password
        * module pos is installed

    The user is admin by default, so no need to write this in each test
    file. Instead of saying 'I check that the module pos is installed',
    just write the name of the module where you will put this test. The first
    line would then be **"module: pos"**.

.. i18n: Be precise about the goal of the test
.. i18n: ------------------------------------------
.. i18n: Try to use functional terms instead of object
..

Be precise about the goal of the test
------------------------------------------
Try to use functional terms instead of object

.. i18n:     * This is not good enough::
.. i18n: 
.. i18n:         I will test the manufacturing order
.. i18n: 
.. i18n:     * An example of a good introduction::
.. i18n: 
.. i18n:          In order to test the CRM in OpenERP, I will do a customer qualification 
.. i18n:          process that begins with the first customer contact (a lead), 
.. i18n:          which will be converted to a business opportunity and a partner.
.. i18n: 
.. i18n:     ::
.. i18n: 
.. i18n:         # wrong
.. i18n:         *In caldav testing of creation of calendar as Admin
.. i18n: 
.. i18n:         # better
.. i18n:         *In order to test the calendar synchronisation with mobile phones and
.. i18n:         outlook, I will test the caldav interface for meetings.
.. i18n: 
.. i18n:         # wrong:
.. i18n:         In order to test the manufacturing order process and modules as an       
.. i18n:         administrator I want to see if the features work correctly.
.. i18n: 
.. i18n:         # better:
.. i18n:           In order to test the manufacturing of products, I will test the
.. i18n:           features of the manufacturing order document: consume raw materials,
.. i18n:           produce finished goods, scrap some products and split in production
.. i18n:           lots.
.. i18n: 
.. i18n:         # wrong:
.. i18n:         Testing of Document for ftp server is running and being connected or
.. i18n:         not
.. i18n:         # better:
.. i18n:           In order to test the document management system, I will try different
.. i18n:           operations on the FTP interface, and check their impacts on OpenERP's
.. i18n:           documents.
..

    * This is not good enough::

        I will test the manufacturing order

    * An example of a good introduction::

         In order to test the CRM in OpenERP, I will do a customer qualification 
         process that begins with the first customer contact (a lead), 
         which will be converted to a business opportunity and a partner.

    ::

        # wrong
        *In caldav testing of creation of calendar as Admin

        # better
        *In order to test the calendar synchronisation with mobile phones and
        outlook, I will test the caldav interface for meetings.

        # wrong:
        In order to test the manufacturing order process and modules as an       
        administrator I want to see if the features work correctly.

        # better:
          In order to test the manufacturing of products, I will test the
          features of the manufacturing order document: consume raw materials,
          produce finished goods, scrap some products and split in production
          lots.

        # wrong:
        Testing of Document for ftp server is running and being connected or
        not
        # better:
          In order to test the document management system, I will try different
          operations on the FTP interface, and check their impacts on OpenERP's
          documents.

.. i18n: Avoid relying on data that can be changed by the user before launching the test
.. i18n: -------------------------------------------------------------------------------
.. i18n:     ::
.. i18n: 
.. i18n:         # wrong (mrp):
.. i18n:         Then my manufacturing order turned into 'Waiting for goods' state.
.. i18n:         And one picking was also generated for my manufacturing order:
.. i18n:         'INT/00001'.
.. i18n: 
.. i18n:     This is not a good test, who knows if it will be 'INT/0001' or another
.. i18n:     sequence 'INT/0002' ? Because the user may have created internal
.. i18n:     pickings before they installed the mrp module.
.. i18n: 
.. i18n:     ::
.. i18n: 
.. i18n:         # wrong (pos):
.. i18n:         I press new record from toolbar.
.. i18n:         Some default values are filled automatically like:
.. i18n:         Company>Tinysprl,Journal>x Sales Journal
.. i18n: 
.. i18n:     You can not test if the company is 'Tiny SPRL'. The user may have
.. i18n:     configured it to his own company name. It's better to test:
.. i18n:     "The company is set by default to the company of the admin user."
.. i18n: 
.. i18n:     Take care of these data dependencies, because it may crash the tests
.. i18n:     simply because the user changed some demo data before launching the tests.
.. i18n: 
.. i18n:     You can rely on demo data defined by the module where you put your test
.. i18n:     file, but if the demo data are defined by another module, try to either
.. i18n:     create your own data or find a way to work with ids instead of names.
..

Avoid relying on data that can be changed by the user before launching the test
-------------------------------------------------------------------------------
    ::

        # wrong (mrp):
        Then my manufacturing order turned into 'Waiting for goods' state.
        And one picking was also generated for my manufacturing order:
        'INT/00001'.

    This is not a good test, who knows if it will be 'INT/0001' or another
    sequence 'INT/0002' ? Because the user may have created internal
    pickings before they installed the mrp module.

    ::

        # wrong (pos):
        I press new record from toolbar.
        Some default values are filled automatically like:
        Company>Tinysprl,Journal>x Sales Journal

    You can not test if the company is 'Tiny SPRL'. The user may have
    configured it to his own company name. It's better to test:
    "The company is set by default to the company of the admin user."

    Take care of these data dependencies, because it may crash the tests
    simply because the user changed some demo data before launching the tests.

    You can rely on demo data defined by the module where you put your test
    file, but if the demo data are defined by another module, try to either
    create your own data or find a way to work with ids instead of names.

.. i18n: Write things in test that can be easily tested by the YAML system
.. i18n: -----------------------------------------------------------------
..

Write things in test that can be easily tested by the YAML system
-----------------------------------------------------------------

.. i18n: **For** **example,**
.. i18n: the mail gateway. You can not write this::
.. i18n: 
.. i18n:        First I have made one fetchmail rc script using the proper syntax
.. i18n:        with specific email server and address information and used crm.lead
.. i18n:        as model Then I run the fetchmail command like: fetchmail -f <created
.. i18n:        rc file name> The script should exit successfully
..

**For** **example,**
the mail gateway. You can not write this::

       First I have made one fetchmail rc script using the proper syntax
       with specific email server and address information and used crm.lead
       as model Then I run the fetchmail command like: fetchmail -f <created
       rc file name> The script should exit successfully

.. i18n: Because you can not set-up an email pop account to test this.
..

Because you can not set-up an email pop account to test this.

.. i18n: I would rather do::
.. i18n: 
.. i18n:        I have a list of different emails with different encoding and
.. i18n:        different kind of attachments stored in the directory test/emails.
.. i18n:        I test to pass all these documents through the mailgateway script:
.. i18n:          something like:
.. i18n:            for each email file:
.. i18n:              call the script with stdin<this email file
..

I would rather do::

       I have a list of different emails with different encoding and
       different kind of attachments stored in the directory test/emails.
       I test to pass all these documents through the mailgateway script:
         something like:
           for each email file:
             call the script with stdin<this email file

.. i18n: If possible call in python directly, not using os.system.
..

If possible call in python directly, not using os.system.

.. i18n: For the FTP, it can be tested by the YAML as you simply have to use the Python
.. i18n: FTP client in your yaml code::
.. i18n: 
.. i18n:         import ftplib
..

For the FTP, it can be tested by the YAML as you simply have to use the Python
FTP client in your yaml code::

        import ftplib

.. i18n: Avoid relying on existing demo data if the user can change it.
.. i18n: --------------------------------------------------------------
..

Avoid relying on existing demo data if the user can change it.
--------------------------------------------------------------

.. i18n:    **Bad** **example**:
..

   **Bad** **example**:

.. i18n:    When I pressed *'Confirm Production'* button.
.. i18n:    Then I could see the Finished Products into Products to Consume with
.. i18n:    quantity 10.00.
..

   When I pressed *'Confirm Production'* button.
   Then I could see the Finished Products into Products to Consume with
   quantity 10.00.

.. i18n:    Then my manufacturing order turned into 'Waiting for goods' state.
.. i18n:    And one picking was also generated for my manufacturing order:
.. i18n:    'INT/00001'.
..

   Then my manufacturing order turned into 'Waiting for goods' state.
   And one picking was also generated for my manufacturing order:
   'INT/00001'.

.. i18n:    .. csv-table::  And the following values appeared in the Products to Consume
.. i18n:       :header: "product_id","product_qty","product_uom","location_id","||","||"
.. i18n:       :widths: 30,6,6,15,2,2
.. i18n: 
.. i18n:       "[CPU_GEN] Regular processor config","10.00","PCE","Stock","||","||"
.. i18n:       "[HDD1] HDD Seagate 7200.8 80GB","10.00","PCE","Stock","||","||"
.. i18n:       "[TOW1] ATX Mid-size Tower","10.00","PCE","Stock","||","||"
.. i18n:       "[MOU] Mouse","10.00","PCE","Stock","||","||"
.. i18n:       "[KEYA] Keyboard -AZERTY","10.00","PCE","Stock","||","||"
.. i18n: 
.. i18n:    For such an example, I would have created a few products and a bom in the test scenario. And test the manufacturing order on these test data.
..

   .. csv-table::  And the following values appeared in the Products to Consume
      :header: "product_id","product_qty","product_uom","location_id","||","||"
      :widths: 30,6,6,15,2,2

      "[CPU_GEN] Regular processor config","10.00","PCE","Stock","||","||"
      "[HDD1] HDD Seagate 7200.8 80GB","10.00","PCE","Stock","||","||"
      "[TOW1] ATX Mid-size Tower","10.00","PCE","Stock","||","||"
      "[MOU] Mouse","10.00","PCE","Stock","||","||"
      "[KEYA] Keyboard -AZERTY","10.00","PCE","Stock","||","||"

   For such an example, I would have created a few products and a bom in the test scenario. And test the manufacturing order on these test data.

.. i18n: Don't check the full text of an exception
.. i18n: -----------------------------------------
.. i18n:    Then I got the following error message:
..

Don't check the full text of an exception
-----------------------------------------
   Then I got the following error message:

.. i18n:    xmlrpclib.Fault: <Fault warning -- Error::
.. i18n: 
.. i18n:         Couldn't find bill of material for product: 'Traceback (most recent call last):
.. i18n:         File in dispatch
.. i18n:         result = ExportService.getService(service_name).dispatch(method, auth, params)
.. i18n:          File "/home/uco/workspace/Trunk/openobject-server/bin/service/web_services.py", line 587, in dispatch
.. i18n:          res = fn(db, uid, *params)
.. i18n:          File "/home/uco/workspace/Trunk/openobject-server/bin/osv/osv.py", line 64, in wrapper
.. i18n:          self.abortResponse(1, inst.name, inst.exc_type, inst.value)
.. i18n:          File "/home/uco/workspace/Trunk/openobject-server/bin/netsvc.py", line 66, in abortResponse
.. i18n:          raise Exception("%s -- %s\\n\\n%s"%(origin, description, details))
.. i18n:         Exception: warning -- Error
.. i18n:         
.. i18n:         Couldn\'t find bill of material for product\n'>
.. i18n: 
.. i18n:     Simply do::
.. i18n: 
.. i18n:       And it should generate an exception to say that it cannot find a BoM
.. i18n:       defined for this product.
..

   xmlrpclib.Fault: <Fault warning -- Error::

        Couldn't find bill of material for product: 'Traceback (most recent call last):
        File in dispatch
        result = ExportService.getService(service_name).dispatch(method, auth, params)
         File "/home/uco/workspace/Trunk/openobject-server/bin/service/web_services.py", line 587, in dispatch
         res = fn(db, uid, *params)
         File "/home/uco/workspace/Trunk/openobject-server/bin/osv/osv.py", line 64, in wrapper
         self.abortResponse(1, inst.name, inst.exc_type, inst.value)
         File "/home/uco/workspace/Trunk/openobject-server/bin/netsvc.py", line 66, in abortResponse
         raise Exception("%s -- %s\\n\\n%s"%(origin, description, details))
        Exception: warning -- Error
        
        Couldn\'t find bill of material for product\n'>

    Simply do::

      And it should generate an exception to say that it cannot find a BoM
      defined for this product.

.. i18n: Be more functional, explain what the user means to do, not where she clicks
.. i18n: ---------------------------------------------------------------------------
..

Be more functional, explain what the user means to do, not where she clicks
---------------------------------------------------------------------------

.. i18n: ::
.. i18n: 
.. i18n:         # wrong:
.. i18n:         I press new record from toolbar of lead's view
.. i18n:         Some default values are filled automatically like: priority>Normal,user_id>Administrator, state>Draft
.. i18n:         Then I give some values for lead:
.. i18n:         |name|section_id|partner_name|phone|mobile|
.. i18n:         |Carrie Helle|Sales Department|Stonage IT|(855) 924-4364|(333) 715-1450|
.. i18n:         Then I press the save button from toolbar
.. i18n:         The lead is created successfully
..

::

        # wrong:
        I press new record from toolbar of lead's view
        Some default values are filled automatically like: priority>Normal,user_id>Administrator, state>Draft
        Then I give some values for lead:
        |name|section_id|partner_name|phone|mobile|
        |Carrie Helle|Sales Department|Stonage IT|(855) 924-4364|(333) 715-1450|
        Then I press the save button from toolbar
        The lead is created successfully

.. i18n: No need to write the all the data of the form in the English text
.. i18n: (phone, mobile, ...). These data will be written in the final YAML, when
.. i18n: you implement the test. A better final YAML for the above example should
.. i18n: look like this::
.. i18n: 
.. i18n:     -
.. i18n:      As I met a new customer in a fair, I create a new lead "Stonage IT"
.. i18n:      to record his data.
.. i18n:     -
.. i18n:      !record {model:rcrm.lead, id:partner_carrie}
.. i18n:        name: Stonage IT
.. i18n:        contact_name: Carrie Helle
.. i18n:        phone: (855) 924-4364
.. i18n:        mobile: (333) 715-1450
.. i18n:     -
.. i18n:       I check that the state field is set automatically by default.
.. i18n:     -
.. i18n:       !assert {model:crm.lead, id:partner_carrie} state
..

No need to write the all the data of the form in the English text
(phone, mobile, ...). These data will be written in the final YAML, when
you implement the test. A better final YAML for the above example should
look like this::

    -
     As I met a new customer in a fair, I create a new lead "Stonage IT"
     to record his data.
    -
     !record {model:rcrm.lead, id:partner_carrie}
       name: Stonage IT
       contact_name: Carrie Helle
       phone: (855) 924-4364
       mobile: (333) 715-1450
    -
      I check that the state field is set automatically by default.
    -
      !assert {model:crm.lead, id:partner_carrie} state

.. i18n: You can use "onchange" calls in your tests, to simulate the client interface
.. i18n: ----------------------------------------------------------------------------
..

You can use "onchange" calls in your tests, to simulate the client interface
----------------------------------------------------------------------------

.. i18n:     -
.. i18n:       I create a new sale order by filling the partner.
.. i18n:       I want addresses to be filled up by the onchange call but I still need to
.. i18n:       provide dummy addresses (required fields) to allow the record to be created.
.. i18n:     -
.. i18n:       !record {model: sale.order, id: my_order}:
.. i18n:         partner_id: base.res_partner_asus
.. i18n:         pricelist_id: product.list0
.. i18n:         partner_order_id: base.main_address
.. i18n:         partner_invoice_id: base.main_address
.. i18n:         partner_shipping_id: base.main_address
.. i18n:     -
.. i18n:       I then call the onchange method and update the record with the returned value.
.. i18n:     -
.. i18n:       !python {model: sale.order}: |
.. i18n:         my_order = self.browse(cr, uid, ref('my_order'))
.. i18n:         value = my_order.onchange_partner_id(my_order['partner_id']).get('value', {})
.. i18n:         my_order.write(value)
..

    -
      I create a new sale order by filling the partner.
      I want addresses to be filled up by the onchange call but I still need to
      provide dummy addresses (required fields) to allow the record to be created.
    -
      !record {model: sale.order, id: my_order}:
        partner_id: base.res_partner_asus
        pricelist_id: product.list0
        partner_order_id: base.main_address
        partner_invoice_id: base.main_address
        partner_shipping_id: base.main_address
    -
      I then call the onchange method and update the record with the returned value.
    -
      !python {model: sale.order}: |
        my_order = self.browse(cr, uid, ref('my_order'))
        value = my_order.onchange_partner_id(my_order['partner_id']).get('value', {})
        my_order.write(value)
