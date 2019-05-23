SELECT
d.[business_hour_guid] --as '商品檔次代號'
,[seller_GUID] --as '廠商代號'
,[business_hour_order_time_s] --as '銷售開始時間'
,[business_hour_order_time_e] --as '銷售結束時間'
,[business_hour_deliver_time_s] --as '配送開始時間'
,[business_hour_deliver_time_e] --as '配送結束時間'
	  --,[business_hour_status] 
      --,[business_hour_delivery_charge]
	  --,[order_total_limit]
	  --,[business_hour_delivery_charge]
	  --,[business_hour_atm_maximum]
	  --,[page_title]
	  --,[page_desc]
,REPLACE (REPLACE ([pic_alt], ',', '|'), '"', '|') as [pic_alt] --as '標籤'
      --,[settlement_time]
      --,[changed_expire_date]
      --,[seller_id]
      --,[seller_name]
      --,[seller_tel]
      --,[seller_email]
      --,[seller_address]
      --,[department]
      --,[seller_city_id]
      --,[is_close_down]
      --,[close_down_date]
      --,[company_id]
      --,[company_name]
,cc.zip_code --as '供貨商郵遞區號'
,cp.city_name --as '供貨商城市'
,cc.city_name as district_name --as '供貨商鄉鎮'
	  --,[item_guid]
      --,[max_item_count]
,REPLACE (REPLACE ([item_name], ',', '|'), '"', '|') as [item_name] --as '商品名稱'
,[item_orig_price] --as '原價'
,[item_price]	--as '售價'
,[item_default_daily_amount] --as '訂單數量上限'
,REPLACE(REPLACE(REPLACE(REPLACE(REPLACE([event_name],CHAR(13),''), CHAR(10), ''),'	',''),',','|'),'"','|') as [event_name] --as '檔次名稱'
,REPLACE (REPLACE ([event_title], ',', '|'), '"', '|') as [event_title] --as '檔次標題'
	  --,[event_image_path]
	  --,[description]
      --,[app_description]
      --,[introduction]
      --,[restrictions]
      --,[reference_text]
      --,[availability]
      --,[remark]
      --,[reasons]
      --,[subject_name]
      --,[event_special_image_path]
      --,[app_deal_pic]
      --,[app_title]
      --,[coupon_usage]
      --,[event_modify_time]
,REPLACE(REPLACE(REPLACE(REPLACE(REPLACE(product_spec,CHAR(13),''), CHAR(10), ''),'	',''),',','|'),'"','|') as product_spec--as '商品規格'
	  --,REPLACE(REPLACE([product_spec],CHAR(13),''), CHAR(10), '') as product_spec--as '商品規格'
	  --,[product_spec]
	  --,[intro]
      --,[price_desc]
      --,[is_hide_content]
      --,[content_name]
      --,[remove_bg_pic]
      --,[is_close_menu]
      --,[delivery_type]
,[shopping_cart] --as '商品檔次是否為組合銷售'
,[combo_pack_count] --as '商品檔次組合數(幾入一組)'
	  --,[is_travelcard]
	  --,[quantity_multiplier] 
	  --,[unique_id]
	  --,[is_daily_restriction]
      --,[is_continued_quantity]
      --,[continued_quantity]
,REPLACE (REPLACE ([city_list], ',', '|'), '"', '|') as [city_list] --as '銷售頻道'
	  --,[activity_url]
	  --,[label_icon_list]
	  --,[label_tag_list]
	  --,[coupon_code_type]
      --,[pin_type]
      --,[custom_tag]
      --,[exchange_price]
	  --,[is_quantity_multiplier] 
	  --,[is_average_price]
      --,[is_zero_activity_show_coupon]
,isnull([deal_acc_business_group_id],0) as [deal_acc_business_group_id] --as '產品線事業群代號'
,bg.acc_business_group_name --as '產品線事業群名稱'
	  --,[deal_type]
,[deal_type_detail] --as '商品子分類代號'
,sc.code_name --as '商品子分類名稱'
,sc.code --as 'Google子分類代號'
,[is_travel_deal] --as '是否為旅遊票券'
      --,[deal_emp_name]
,[installment_3months] --as '信用卡交易可分3期'
,[installment_6months] --as '信用卡交易可分6期'
,[installment_12months] --as '信用卡交易可分12期'
,[deny_installment] --as '信用卡交易不可分期'
	  --,[sale_multiple_base]
	  --,[ship_type] as --'配送方式'
	  --,[shippingdate_type]
,[shippingdate] --as '配送天數'
	  --,[product_use_date_end_set]
	  --,[present_quantity]
	  --,[group_coupon_app_style]
	  --,[new_deal_type]
	  --,[is_experience]
	  --,[discount_type]
	  --,[discount_value]
      --,[travel_place]
      --,[entrust_sell]
      --,[multiple_branch]
,[is_long_contract] --as '是否為長約'
	  --,[complete_copy]
,[develope_sales_id] --as '開發業務'
,[operation_sales_id] --as '維護業務'
	  --,[is_freights_deal]
	  --,[cchannel]
	  --,[cchannel_link]
	  --,[is_expired_deal]
	  --,[booking_system_type]
      --,[coupon_separate_digits]
      --,[group_order_guid]
      --,[order_guid]
      --,[create_time]
      --,[close_time]
	  --,[group_order_status] 
,[slug] --as '最終售出商品數'
,[ordered_quantity] --as '已訂購商品數'
,[ordered_total] --as '已訂購商品營業額'
	  --,[ordered_include_refund_quantity]
	  --,[ordered_include_refund_total]
      --,[deal_promo_title]
      --,[deal_promo_description]
      --,[deal_promo_image]
      --,[pdf_item_name]
	  --,[main_bid]
	  --,[combo_deal_seq]
	  --,[group_coupon_deal_type]
,REPLACE (REPLACE (category_list, ',', '|'), '"', '|') as category_list-- as '前台分類'
	  --,[consignment]
	  --,[freights_id]
	  --,[bank_id]
	  --,[is_bank_deal]
	  --,[allow_guest_buy]
      --,[discount_use_type] 
      --,[verify_action_type] 
      --,[is_house_new_ver] 
,[freight_amount] --as '運費'
	  --,[enable_delivery]
      --,[isp_quantity_limit] 
	  --,[enable_isp]
,[discount_price] --as '折扣後金額'
	  --,[is_game]
	  --,[expire_redirect_display]
	  --,[expire_redirect_url]
	  --,[use_expire_redirect_url_as_canonical]
,[is_wms] --as '是否入倉',
,ancestor_business_hour_guid --as '上一檔'
from view_ppon_deal d with(nolock)
left join city cc with(nolock) on d.seller_city_id=cc.id
left join city cp with(nolock) on cc.parent_id=cp.id 
left join acc_business_group bg with(nolock) on d.deal_acc_business_group_id=bg.acc_business_group_id
left join system_code sc with(nolock) on (d.deal_type_detail=sc.code_id and sc.code_group='DealType')
left join (select business_hour_guid,ancestor_business_hour_guid from deal_property with(nolock))as dp on dp.business_hour_guid=d.business_hour_guid
where d.create_time<'20190501' and delivery_type=2
order by business_hour_order_time_s,d.business_hour_guid
