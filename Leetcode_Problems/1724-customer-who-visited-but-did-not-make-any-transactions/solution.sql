# Write your MySQL query statement below
select v.customer_id, 
count(*) as count_no_trans 
from Visits v 
where 
    visit_id not in 
        (select visit_id from transactions) 
group by v.customer_id
