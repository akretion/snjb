-- {'model_code': 'partner_import', 'db_conf': 'snjb', 'name': 'addr-livr', 'sequence': 2}
SELECT CONCAT('delivery', CAST(l.cbmarq AS varchar)) AS id
, l.li_Pays AS country
, CONCAT('societe', CAST(p.cbmarq AS varchar), LOWER(p.ct_num)) AS 'parent_id'
, 'delivery' AS type, l.CBMARQ, IIF(p.ct_sommeil=0,1,0) AS active
, CONCAT(l.li_intitule, '  ', l.li_contact) AS name, l.li_adresse AS street, l.li_complement AS street2, l.LI_CodePostal AS zip
, l.li_ville AS city, l.LI_Telephone AS phone, l.li_telecopie AS fax, l.li_email AS email, l.cbModification AS write_date
, l.N_Expedition, l.N_Condition, l.cbCreateur
FROM F_LIVRAISON l LEFT OUTER JOIN F_COMPTET p ON p.ct_num = l.ct_num
WHERE 1=1 --p.ct_num like 'A%'
order by l.cbmarq, l.LI_Principal DESC
