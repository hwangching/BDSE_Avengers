SELECT 
 dcp.[id] --as '優惠活動ID'
,REPLACE ([name], ',', '，') as [name] --as '優惠活動名稱'
,[amount] --as '優惠面額'
,[qty] --as '發放總量'
,[total] --as '優惠總額'
      --,[apply_time]
,[start_time] --as '活動開始時間'
,[end_time] --as '活動結束時間'
,[cancel_time] --as '活動取消時間'
      --,[create_time] 
      --,[create_id]
      --,[apply_id]
      --,[cancel_id]
      --,[flag] 
,[minimum_amount] --as '訂單金額下限'
      --,[card_group_id] 
      --,[type] 
      --,[modify_id]
      --,[modify_time]
      --,[event_date_s] 
      --,[event_date_e]
      --,[free_gift_discount as 
      --,[template_id] as 
      --,[available_date_type] 
      --,[card_combine_use] 
      --,[seller_user_id] 
      --,[campaign_no] as 
,[min_gross_margin] --as '最小毛利率'
,[is_discount_price_for_deal] --as '是否在前台顯示優惠後價格'
,dct.category_id --as '分類編號'
  FROM [lunchking].[dbo].[discount_campaign] dcp left join discount_category dct on dcp.id=dct.campaign_id
  where dcp.id in(
  select campaign_id from [discount_code] with(nolock)  where send_date<'20190501'
  )
