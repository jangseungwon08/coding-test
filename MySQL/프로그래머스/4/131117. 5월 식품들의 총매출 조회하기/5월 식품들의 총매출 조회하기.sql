-- 코드를 입력하세요
SELECT prod.product_id, prod.product_name, sum(prod.price * ord.amount) as total_sales
FROM food_product as prod
inner join food_order as ord
on prod.product_id = ord.product_id
where ord.produce_date >= '2022-05-01' AND ord.produce_date < '2022-06-01'
group by prod.product_name
order by total_sales desc, prod.product_id asc