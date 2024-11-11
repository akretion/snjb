--{'model_code': 'Catégorie', 'db_conf': 'snjb', 'name': 'Categories', 'sequence': 10, 'uidstring': 'cat-'}
SELECT CONCAT('cat', '-', cl_no) AS id
, IIF (cl_noparent > 0, CONCAT('cat-', CAST(cl_noparent AS varchar)), '') AS 'parent_id'
, cl_intitule AS name
, cbmodification AS write_date
FROM F_CATALOGUE
WHERE 1=1
ORDER BY cl_no ASC;
