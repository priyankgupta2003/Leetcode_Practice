# Write your MySQL query statement below
select machine_id,
    round(sum(case when activity_type='start' then timestamp*-1 else timestamp end)/count(Distinct process_id),3) as processing_time 
from activity
group by machine_id

