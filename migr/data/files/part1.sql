-- {'code': 'partner', 'db_conf_id': 'SNJB'}
SELECT CT_Num AS id, CT_Intitule AS name
 , CT_Adresse AS street, CT_Complement AS street2, CT_CodePostal AS zip, CT_Ville AS city
 --, CT_Pays AS country_id
 , CT_Identifiant AS vat
 , CT_Commentaire AS comment
 , CT_Sommeil AS active, CT_Telephone AS phone, 1 AS is_company
 , CT_EMail AS email, CT_Site AS website, cbModification AS write_date, CT_Siret AS siret
 , CONCAT('N_CatTarif=',N_CatTarif ,'|CT_Type=', CT_Type ,'|CT_Ape=',CT_Ape ,'|CT_Contact=', CT_Contact, '|CG_NumPrinc=', CG_NumPrinc,'|CT_Qualite=',CT_Qualite) AS extra_data
FROM F_COMPTET ;
