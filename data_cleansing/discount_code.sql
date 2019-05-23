SELECT 
 [id] --as '優惠券ID'
,[campaign_id] --as '優惠活動ID'
      --,[code]
      --,[amount]
      --,[use_time]
,isnull([use_amount],0) as [use_amount] --as '使用金額'
,[order_guid] --as '訂單編號'
,isnull([order_amount],0) as [order_amount] --as '訂單金額'
,[cancel_time] --as '取消時間'
,isnull([order_cost],0) as [order_cost] --as '訂單扣除優惠金額'
      --,[order_classification]
      --,[receivable_id]
      --,[sender]
,[send_date] --as '發放日期'
,isnull([use_id],0) as [use_id] --as '使用者ID'
,[owner] --as '擁有者ID'
	  --,[nick_name]
	  --,[referrer_id]
  FROM [lunchking].[dbo].[discount_code] with(nolock)
  where send_date<'20190501' and owner is not null
