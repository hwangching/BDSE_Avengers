SELECT 
      --[user_name]
      --,[last_name]
      --,[first_name]
      --,[building_GUID],
	  --,[birthday]
FLOOR(DATEDIFF(DY,[birthday],GETDATE())/365.25) as age --年齡
,[gender] --性別
      --,[mobile]
      --,[company_name]
      --,[company_department]
      --,[company_tel]
      --,[company_tel_ext]
      --,[company_address]
      --,[delivery_method]
      --,[primary_contact_method]
      --,m.[status]
,[create_time] --建立帳號時間
      --,[modify_time]
      --,[modify_id]
      --,[comment]
      --,[pic]
,[unique_id] --使用者代號
      --,[order_count]
      --,[order_total]
      --,[city_id]
,c.city_name --居住區域
      --,[edm_type]
      --,[version]
      --,[is_locked_out]
      --,[password]
      --,[password_format]
      --,[password_salt]
      --,[failed_password_attempt_count]
      --,[failed_password_attempt_window_start]
 ,[last_login_date] --最近登入時間
      --,[is_approved]
      --,[carrier_type]
      --,[carrier_id]
      --,[collect_deal_expire_message]
      --,[true_email]
      --,[user_email]
      --,[is_guest]
     --,[upgraded_time]
      --,[invoice_buyer_name]
      --,[invoice_buyer_address]
  FROM [lunchking].[dbo].[member] m with(nolock) 
  join city c on c.id=m.city_id
  where create_time<'20190501'
order by unique_id desc
