-- {'model': 'product.category', 'db_conf_id': 'SNJB'}
SELECT CONCAT('cat', '-', cl_no) AS id, 
cl_intitule AS name
, iif (cl_noparent > 0, CONCAT('cat', '-', CAST(cl_noparent AS varchar)), '') AS 'parent_id_'
, cbmodification AS write_date
FROM F_CATALOGUE
ORDER BY cl_no ASC;
