select 
	  --[code_group]
	  --,[code_group_name]
 [code_id] --as '商品類別ID'
,[code_name] --as '商品類別名稱'
	  --,[enabled]
      --,[is_default]
      --,[create_id]
      --,[create_time]
      --,[modify_id]
      --,[modify_time]
      --,[seq]
      --,[short_name]
,[parent_code_id] --as '父類別ID'
,[code] --as 'google分類ID'
	  --,[expired_time]
from system_code where code_group='DealType'
