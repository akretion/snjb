-- {'model_code': 'partner_import', 'db_conf': 'SNJB', 'name': 'partner1', 'sequence': 1}
SELECT CONCAT('societe', CT_Num) AS id, CT_Intitule AS name
-- {'model_code': 'partner_import', 'db_conf': 'SNJB', 'name': 'Main partners', xmlid_prefix': 'societe'}
 , CT_Adresse AS street, CT_Complement AS street2, CT_CodePostal AS zip, CT_Ville AS city
 , CT_Pays AS country
 --, CT_Identifiant AS vat
 , CT_Commentaire AS comment, IIF (CT_Sommeil=0, 1, 0) AS active
 , CT_Telephone AS phone, 1 AS is_company
 , CT_EMail AS email, CT_Site AS website, cbModification AS write_date, CT_Siret AS siret
 , CONCAT('VAT=',CT_Identifiant, 'N_CatTarif=',N_CatTarif ,'|CT_Type=', CT_Type ,'|CT_Ape=',CT_Ape ,'|CT_Contact=', CT_Contact, '|CG_NumPrinc=', CG_NumPrinc,'|CT_Qualite=',CT_Qualite) AS extra_data
FROM F_COMPTET ;
