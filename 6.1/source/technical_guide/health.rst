
.. module:: health
    :synopsis: Tiny TERP Health Management (Official, Quality Certified)
    :noindex:
.. 

.. raw:: html

      <br />
    <link rel="stylesheet" href="../_static/hide_objects_in_sidebar.css" type="text/css" />

.. tip:: This module is part of the OpenERP software, the leading Open Source 
  enterprise management system. If you want to discover OpenERP, check our 
  `screencasts <http://openerp.tv>`_ or download 
  `OpenERP <http://openerp.com>`_ directly.

.. raw:: html

    <div class="js-kit-rating" title="" permalink="" standalone="yes" path="/health"></div>
    <script src="http://js-kit.com/ratings.js"></script>

Tiny TERP Health Management (*health*)
======================================
:Module: health
:Name: Tiny TERP Health Management
:Version: 5.0.0.9.3
:Author: EVI
:Directory: health
:Web: 
:Official module: yes
:Quality certified: yes

Description
-----------

::

  Health Management System

Download links
--------------

You can download this module as a zip file in the following version:

  * `5.0 <http://www.openerp.com/download/modules/5.0/health.zip>`_
  * `trunk <http://www.openerp.com/download/modules/trunk/health.zip>`_


Dependencies
------------

 * :mod:`base`
 * :mod:`product`
 * :mod:`account`

Reports
-------

 * Present

 * Entry Exit

 * Semester Movement

 * Birthday

 * Fund Regime

Menus
-------

 * EHPAD
 * EHPAD/Configuration
 * EHPAD/Fund Regime
 * EHPAD/Residents
 * EHPAD/Applicants
 * EHPAD/Medicaments
 * EHPAD/Events
 * EHPAD/AGGIR
 * EHPAD/Prescriptions
 * EHPAD/Billing 
 * EHPAD/Absences
 * EHPAD/Rooms
 * EHPAD/Configuration/Rooms Rate
 * EHPAD/Configuration/Fund Regime
 * EHPAD/Configuration/Localisation
 * EHPAD/Care
 * EHPAD/Configuration/Medicament form
 * EHPAD/Configuration/Care 
 * EHPAD/Configuration/Rate Dependance
 * EHPAD/Configuration/Situations
 * EHPAD/Configuration/Religions
 * EHPAD/Configuration/Events type
 * EHPAD/Configuration/Pathos
 * EHPAD/Configuration/Pathos/States Pathologique
 * EHPAD/Configuration/Pathos/Profiles
 * EHPAD/Configuration/Pathos/Category States 
 * EHPAD/Configuration/Absences
 * EHPAD/Configuration/Semesters

Views
-----

 * health.semestre.form (form)
 * health.semestre.tree (tree)
 * health.absences.fiche-simple (form)
 * health.absences.arbre-simple (tree)
 * health.tarif.absences.tree (tree)
 * health.tarif.absences.form (form)
 * health.absences.tree (tree)
 * health.absences.form (form)
 * health.prescription.fiche-simple (form)
 * health.prescription.arbre-simple (tree)
 * health.facturation.tree (tree)
 * health.facturation.form (form)
 * health.prescription.tree (tree)
 * health.prescription.form (form)
 * health.aggir.tree (tree)
 * health.aggir.form (form)
 * health.evenement.type.tree (tree)
 * health.evenement.type.form (form)
 * health.patient.evenement.tree (tree)
 * health.patient.evenement.tree-simple (tree)
 * health.patient.evenement.form (form)
 * health.patient.evenement.form-simple (form)
 * health.droits.tree (tree)
 * health.droits.form (form)
 * health.religion.tree (tree)
 * health.religion.form (form)
 * health.situation.tree (tree)
 * health.situation.form (form)
 * health.care.tree (tree)
 * health.care.form (form)
 * health.drug.form (form)
 * health.drug.tree (tree)
 * health.drugform.tree (tree)
 * health.drugform.form (form)
 * health.tarif.dependance.tree (tree)
 * health.tarif.apa.form (form)
 * health.patient.tree (tree)
 * health.patient.form (form)
 * health.room.tarif.tree (tree)
 * health.room.tarif.form (form)
 * health.room.localisation.tree (tree)
 * health.room.localisation.form (form)
 * health.room.tree (tree)
 * health.room.form (form)
 * health.pathosprofils.tree (tree)
 * health.pathosprofils.form (form)
 * health.pathosetatspatho.tree (tree)
 * health.pathosetatspatho.form (form)
 * health.pathoscategetats.tree (tree)
 * health.pathoscategetats.form (form)
 * health.regime.tree (tree)
 * health.regime.tree (tree)
 * health.regime.form (form)


Objects
-------

Object: Semestre (health.semestre)
##################################



:fiscalyear_id: Fiscal Year, many2one, required





:code: Code, char





:date_stop: End of period, date, required





:date_start: Start of period, date, required





:name: Semester, char, required




Object: religion (health.religion)
##################################



:name: name, char




Object: situation (health.situation)
####################################



:name: name, char




Object: Room Rate (health.room.tarif)
#####################################



:type: Room type, selection





:age: Age Limit, selection





:ref: reference, char





:name: Fare type, char





:prix: Prix, float




Object: Localisation (health.room.localisation)
###############################################



:nbrchambre: Number of room, integer





:name: Code, char





:designation: Designation, char




Object: Chambres (health.room)
##############################



:localisation: Localisation, many2one





:type: Room type, selection





:name: Name of Room, char





:bed: Number of bed, integer




Object: Rate Dependence (health.tarif.dependance)
#################################################



:name: GIR, char





:montant: Rate Dependence, float




Object: Drug Form (health.drugform)
###################################



:name: name, char




Object: Drug Family (health.drugfamilly)
#########################################



:name: name, char




Object: Profils Pathos (health.pathosprofils)
#############################################



:definition: Definition, text





:name: Profile, char





:description: Description, char




Object: Category States Pathologique Pathos (health.pathoscategetats)
#####################################################################



:name: Category States Pathologique, char




Object: States Patholohgique Pathos (health.pathosetatspatho)
#############################################################



:definition: Definition, text





:categorie: Category, many2one





:name: Etats Pathologique, char





:profils: Profils, many2many





:description: Description, char




Object: Facturation (health.facturation)
########################################



:aidesociale: Social Assistance, char





:absences: Personal absences, char





:name: Resident, many2one, required





:decomptes: No. of days for the period, char





:allocation: Allocation Logement, char





:hebergement: Accommodation Rates, float





:period_id: Billing period, many2one, required





:datefacturation: Invoice Date, date





:hospitalisation: Absences Hospitalization, char





:commentaire: Comment, text





:dependance: Tarida Dependence, float





:ticketmoderateur: Moderator Ticket, float





:apa: A.P.A., char





:chambre: Rooms, many2one





:absautres: Other absences, char




Object: Aggir (health.aggir)
############################



:cuisine: Kitchen, selection





:alimentation: Food, selection





:orientation: Orientation, selection





:menage: Menage, selection





:achats: Procurement, selection





:communication: Communication to alert, selection





:coherence: Coherence, selection





:transports: Transport, selection





:toilette: Toilet, selection





:name: Resident, many2one





:activite: Free time, selection





:resultat: AG-GIR, char





:moveint: Internal displacement, selection





:gestion: Management, selection





:traitement: monitoring treatment, selection





:elimination: Elimination, selection





:habillage: Dressing, selection





:transferts: Transfers, selection





:deplacementexterieur: Deplacement External, selection





:gir: GIR, char




Object: Drugs (health.drug)
###########################



:vidal: vidal, boolean





:atc: ATC, char





:forme: Shape, many2one





:commentaire: Comments, text





:description: Description, text





:volume: Volume, float





:uom_id: Unit, many2one, required





:ucd: UCD, char





:cip: CIP, char





:categ_id: Category, many2one, required





:famille: family, many2one





:name: name, char, required




Object: category (health.category)
##################################



:name: name, char, required




Object: soins (health.care)
###########################



:name: Care, char




Object: Type Evenement (health.evenement.type)
##############################################



:name: Event Type, char, required





:creator: Users, many2one




Object: evenement (health.patient.evenement)
############################################



:date: Date, datetime





:user_id: User, many2one





:partner_id: Patient, many2one





:description: Description, text, required





:type_evenements: Event Type, many2one




Object: prescription (health.prescription)
##########################################



:partner_id: Patient, many2one





:user_id: For seizure, many2one





:commentaire: Comments, text





:prescripteur: Doctor, many2one





:au: to, date





:medicament: Medicaments, many2one





:du: from, date





:heure: Time, char





:nbrprise: Number per dose, char




Object: Tarif Absences (health.tarif.absences)
##############################################



:name: Reason of Absence, selection





:montant: Absences Rate, float




Object: Regime (health.regime)
##############################



:parent_id: parent, many2one





:code: Regime Code, char





:child_ids: Childs Category, one2many





:name: Social security, char




Object: Output Type (health.exit)
#################################



:name: reason, char




Object: absences (health.absences)
##################################



:user_id: For seizure, many2one





:commentaire: Comments, text





:facture: Billed, boolean





:nbrjour: Number of days, float, readonly





:au: to, date





:categorie: Category, selection





:du: from, date





:partner_id: Resident, many2one




Object: Resident (health.patient)
#################################



:ean13: EAN, char

    *Barcode number for EAN8 EAN13 UPC JPC GTIN*



:property_account_position: Fiscal Position, many2one

    *The fiscal position will determine taxes and the accounts used for the partner.*



:nomusage: Name use, char





:excise: Exices Number, char





:ref_companies: Companies that refers to partner, one2many





:pharmacie: Pharmacy, many2one





:alddu: from, date





:aidelogementndossier: File No., char





:property_product_pricelist: Sale Pricelist, many2one

    *This pricelist will be used, instead of the default one,                     for sales to the current partner*



:property_account_payable: Account Payable, many2one, required

    *This account will be used instead of the default one as the payable account for the current partner*



:title: Title, selection





:vat_no: VAT Number, char





:caissedu: from, date





:participation_ids: Participations, one2many





:parent_id: Main Company, many2one





:photo: Resident Photo, binary





:ergo: Ergonomist, many2one





:respcivil: Civil Liability, char





:nom: Name, char





:child_ids: Partner Ref., one2many





:congregation: Congregation, boolean





:date_liberation: Release date of the Board, date





:aidelogementdestinataire: Addressee, selection





:invaau: to, date





:name: Name, char, required





:debit_limit: Payable Limit, float





:incineration: Incineration, boolean





:aldtaux: RATE A.L.D, float





:property_account_receivable: Account Receivable, many2one, required

    *This account will be used instead of the default one as the receivable account for the current partner*



:date_sortie: Date Release, date





:evenements: events, one2many





:div: Division, char





:ncpaiement: Number Payment Center, char





:numerosecu: Social Security Number, char





:aidesocialendossier: No Dossier, char





:logo: Logo, binary





:invadu: from, date





:religion: Religion, many2one





:room_id: Rooms, many2one





:aidesocialemontant: amount, float





:debit: Total Payable, float, readonly

    *Total amount you have to pay to this supplier.*



:supplier: Supplier, boolean

    *Check this box if the partner is a supplier. If unchecked, purchasing staff will not see it when encoding a purchase order.*



:ref: Code, char, readonly





:obseque: Obseques, char





:apamontant: amount, float





:prescriptions: prescriptions, one2many





:respau: to, date





:address: Contacts, one2many





:aidesocialeau: to, date





:cmu: C.M.U, many2one





:cst_no: CST Number, char





:care: Care, many2many





:aidelogementdu: from, date





:prenom: First Name, char





:country: Country, many2one





:admission_date: Date of admission, date





:credit: Total Receivable, float, readonly

    *Total amount this customer owes you.*



:range: Range, char





:apadu: from, date





:mutdu: from, date





:signature: Signature, binary





:comment: Notes, text





:hopital: Hopital, many2one





:aidesocialedestinataire: Addressee, selection





:header: Header (.odt), binary





:motif_sortie: Reason for Release, many2one





:apa: APA, many2one





:aidelogementmontant: amount, float





:city: City, char





:user_id: Dedicated Salesman, many2one

    *The internal user that is in charge of communicating with this partner if any.*



:nomreligieux: Religious Name, char





:provenance: Provenance, char





:cmundossier: Nr File, char





:partner_ids: Parent Companies, one2many





:vat: VAT, char

    *Value Added Tax number. Check the box if the partner is subjected to the VAT. Used by the VAT legal statement.*



:website: Website, char





:aidesociale: Social Assistance, many2one





:apadestinataire: Addressee, selection





:mutndossier: Nr File, char





:pacemaker: Pace Maker / C.I., boolean





:respdu: from, date





:answers_ids: Answers, many2many





:caisse: Fund, many2one





:active: Active, boolean





:cmudu: from, date





:aldau: to, date





:customer: Customer, boolean

    *Check this box if the partner is a customer.*



:apandossier: Nr File, char





:kine: Kine, many2one





:invalidite: Disability, char





:situation: Family situation, many2one





:birthdaydate: Date of Birth, date





:relation_ids: Relations, one2many





:medecin: Doctor, many2one





:aidesocialedu: from, date





:aidelogementau: to, date





:regime: Regime, many2one





:mutuelle: Mutual, many2one





:absences: Absences, one2many





:mutau: to, date





:assure: Assuree, many2one





:aidelogement: Housing assistance, many2one





:pan_no: PAN Number, char





:cmuau: to, date





:note: notes, text





:doncorps: Body donation, boolean





:lieunaissance: Place of birth, char





:girage: GIR Billing, selection





:turnover_id: Turnover, one2many





:donorganes: Organ Donation, boolean





:events: Events, one2many





:obsinformations: Informations, char





:bank_ids: Banks, one2many





:laboratoire: Laboratory, many2one





:ser_tax: Service Tax Number, char





:apaau: to, date





:date: Date, date





:lang: Language, selection

    *If the selected language is loaded in the system, all documents related to this partner will be printed in that language. If not, it will be English.*



:caisseau: to, date





:credit_limit: Credit Limit, float





:hopitalant: Hopital Ant., many2one





:psy: psy, many2one





:livretremis: Booklet Remis, boolean





:hospitalisation: In Hospitalization, boolean





:ambulance: Ambulance, many2one





:property_payment_term: Payment Term, many2one

    *This payment term will be used instead of the default one for the current partner*



:category_id: Categories, many2many


