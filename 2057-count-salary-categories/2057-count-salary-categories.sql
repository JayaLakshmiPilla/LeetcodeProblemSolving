# Write your MySQL query statement below
select "Low Salary" As category ,
sum(income < 20000) as accounts_count 
from Accounts 
union 
select "Average Salary" As category ,
sum(income between 20000 and 50000) as accounts_count 
from Accounts 
union   
select "High Salary" As category ,
sum(income > 50000) as accounts_count 
from Accounts ;
