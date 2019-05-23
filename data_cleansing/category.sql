/****** Script for SelectTopNRows command from SSMS  ******/
SELECT 
 [id] --as '前台目錄ID'
,[name] --as '目錄名稱'
      --,[rank]
      --,[code]
      --,[create_id]
      --,[create_time]
      --,[modify_id]
      --,[modify_time]
      --,[type] 
      --,[status] 
      --,[parent_code]
      --,[is_final]
      --,[name_in_console]
      --,[is_show_front_end]
      --,[icon_type]
      --,[is_show_back_end]
,cd.parent_id --as '父目錄名稱'
  FROM [lunchking].[dbo].[category] c
  left join category_dependency cd on cd.category_id=c.id
