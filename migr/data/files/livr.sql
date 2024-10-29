-- {'code': 'partner', 'db_conf_id': 'SNJB'}
-- {'model': 'res.partner', 'db_conf_id': 'SNJB'}
SELECT CONCAT('liv', l.CBMARQ, p.ct_num) as id, p.ct_num as 'parent_id/id', 'delivery' AS type, l.CBMARQ
, CONCAT(l.li_intitule, '  ', l.li_contact) AS name, l.li_adresse AS street, l.li_complement AS street2, l.LI_CodePostal as zip
, l.li_ville AS city, l.LI_Telephone AS phone, l.li_telecopie AS fax, l.li_email AS email, l.cbModification as write_date
, l.N_Expedition, l.N_Condition, l.cbCreateur
--, l.*
FROM F_LIVRAISON l LEFT OUTER JOIN F_COMPTET p ON p.ct_num = l.ct_num
WHERE p.ct_num like 'A%'
order by l.cbmarq, l.LI_Principal DESC;
