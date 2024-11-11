-- {'code': 'Product', 'db_conf': 'SNJB', 'xmlid_prefix': 'art'}
SELECT CONCAT('art', AR_Ref) AS id, AR_Ref AS default_code, IIF(AR_Sommeil=0,1,0) AS active
--, CONCAT('AR_Coef=',AR_Coef, '|AR_Condition=',AR_Condition, '|AR_Contremarque=',AR_Contremarque, '|AR_Escompte=',AR_Escompte, '|AR_Garantie=',AR_Garantie, '|AR_Nomencl=',AR_Nomencl, '|AR_NotImp=',AR_NotImp, '|AR_PUNet=',AR_PUNet, '|AR_Stat01=',AR_Stat01, '|AR_Substitut=',AR_Substitut, '|AR_SuiviStock=',AR_SuiviStock), 
, AR_CodeBarre AS barcode, CONCAT('cat-', CL_No2) AS categ_id, AR_DateCreation AS create_date, FA_CodeFamille AS FA_CodeFamille, cbMarq AS id, AR_PrixVen AS list_price, AR_Design AS name, AR_PrixAch AS standard_price, AR_DateModif AS write_date
FROM F_ARTICLE
WHERE AR_Sommeil = 0
 and cbMarq > 7000
;
