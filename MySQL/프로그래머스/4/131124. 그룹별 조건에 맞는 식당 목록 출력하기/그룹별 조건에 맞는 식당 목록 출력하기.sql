SELECT mp.member_name,
       rr.review_text,
       DATE_FORMAT(rr.review_date,'%Y-%m-%d') AS review_date
FROM MEMBER_PROFILE mp
JOIN REST_REVIEW rr
ON mp.member_id = rr.member_id
WHERE mp.member_id = (
    SELECT member_id
    FROM REST_REVIEW
    GROUP BY member_id
    ORDER BY COUNT(*) DESC
    LIMIT 1
)
ORDER BY rr.review_date, rr.review_text;