-- {'model': 'product.category', 'db_conf': 'SNJB', 'xmlid_prefix': 'cat-'}
SELECT CONCAT('cat', '-', cl_no) AS id, 
cl_intitule AS name
, IIF (cl_noparent > 0, CONCAT('cat', '-', CAST(cl_noparent AS varchar)), '') AS 'parent_id'
, cbmodification AS write_date
FROM F_CATALOGUE
ORDER BY cl_no ASC;
