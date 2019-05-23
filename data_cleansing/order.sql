SELECT 
 [GUID] --as '訂單編號'
      --,[order_id]
,o.[seller_GUID] --as '廠商ID'
,o.[seller_name] --as '廠商名稱'
      --,[member_name]
      --,[phone_number]
      --,[mobile_number]
      --,[delivery_address]
      --,case when (isnumeric(substring([delivery_address],0,4))=1) then convert(int,substring([delivery_address],0,4)) else '' end --as '收件郵遞區號'
,[subtotal] --as '訂單金額'
      --,[total]
      --,[user_memo]
      --,[order_memo]
,case when [order_status]&512>0 then 1 else 0 end --as '是否退貨'
      --,[order_stage]
      --,[bonus_point]
      --,[create_id]
,o.[create_time] --as '訂購日期'
      --,[modify_id]
      --,[modify_time]
      --,[access_lock]
      --,[city_id]
      --,[parent_order_id]
,d.business_hour_guid --as '商品檔次ID'
      --,[invoice_no]
      --,[return_paper]
      --,[export_log]
      --,[paid_by_travelcard]
,[order_from_type] --as '來源裝置'
,[user_id] --as '訂購人ID'
      --,[is_partial_cancel]
      --,[is_canceling]
      --,[serial_no]
      --,[guest_buy]
,[installment] --as '刷卡分期'
      --,[order_settlement_time]
      --,[cart_d_guid]
      --,[cart_guid]
      --,[is_freights_order]
,[mobile_pay_type] --as '行動支付類別'
      --,[turnover] 
  FROM [lunchking].[dbo].[order] o with(nolock) 
  join view_ppon_deal d with(nolock) on d.order_guid=o.parent_order_id
where order_status&8>0 and subtotal>0 and d.delivery_type=2
and o.create_time<'20190501'
order by o.create_time
