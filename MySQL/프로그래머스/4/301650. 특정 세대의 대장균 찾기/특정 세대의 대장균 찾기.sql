-- 코드를 작성해주세요
select e1.id
from ecoli_data as e1
inner join ecoli_data as e2
on e1.parent_id = e2.id
inner join ecoli_data as e3
on e2.parent_id = e3.id
where e3.parent_id is null
order by e1.id asc