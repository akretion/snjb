-- {'code': 'partner', 'db_conf': 'SNJB'}
--{'model_code': 'Categories', 'db_conf': 'SNJB', 'name': 'Categories', 'xmlid_prefix': 'cat-'}

SELECT CONCAT('delivery', l.CBMARQ, p.ct_num) as id, CONCAT('societe', p.ct_num) as 'parent_id', 'delivery' AS type, l.CBMARQ
, CONCAT(l.li_intitule, '  ', l.li_contact) AS name, l.li_adresse AS street, l.li_complement AS street2, l.LI_CodePostal as zip
, l.li_ville AS city, l.LI_Telephone AS phone, l.li_telecopie AS fax, l.li_email AS email, l.cbModification as write_date
, l.N_Expedition, l.N_Condition, l.cbCreateur
FROM F_LIVRAISON l LEFT OUTER JOIN F_COMPTET p ON p.ct_num = l.ct_num
WHERE p.ct_num like 'A%'
order by l.cbmarq, l.LI_Principal DESC;
