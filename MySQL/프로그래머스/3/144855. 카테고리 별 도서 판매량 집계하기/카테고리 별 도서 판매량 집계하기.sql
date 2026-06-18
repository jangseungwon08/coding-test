-- 코드를 입력하세요
SELECT b.category, sum(bs.sales) as total_sales
FROM BOOK as b
JOIN BOOK_SALES as bs
ON b.book_id = bs.book_id
WHERE bs.sales_date >= '2022-01-01' AND bs.sales_date < '2022-02-01'
GROUP BY b.category
ORDER BY b.category asc