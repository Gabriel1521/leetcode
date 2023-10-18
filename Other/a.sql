# SQL

#Last enrolled employee

select * from employees
where hire_date =
(select max(hire_date) from employees)；

# Last third enrolled
select * from employees
where hire_date =
  (select distinct hire_date
  from employees order by hire_date desc limit 1 offset 2);

# Dept Manager salaries and dept no
select s.*, d.dept_no
from salaries as s
join dept_manager as d
on s.emp_no = d.emp_no
where s.to_date = '9999-01-01'
and d.to_date = '9999-01-01';

# 查找所有已经分配部门的员工的last_name和first_name
select e.last_name, e.first_name,d.dept_no
from dept_emp as d
inner join employees as e
on e.emp_no = d.emp_no;

# 查找所有员工的last_name和first_name以及对应部门编号dept_no，也包括展示没有分配具体部门的员工
select e.last_name, e.first_name, d.dept_no
from employees as e
left join dept_emp as d
on e.emp_no = d.emp_no;

# 查找所有员工入职时候的薪水情况，给出emp_no以及salary， 并按照emp_no进行逆序
select e.emp_no, s.salary
from employees as e join salaries as s
on e.emp_no = s.emp_no
where s.from_date = e.hire_date
order by e.emp_no desc;

# 查找薪水涨幅超过15次的员工号emp_no以及其对应的涨幅次数t
select emp_no, count(*) as c
from salaries
group by emp_no having c > 15;

# 找出所有员工当前(to_date='9999-01-01')具体的薪水salary情况，对于相同的薪水只显示一次,并按照逆序显示

select distinct salary
from salaries
where to_date = '9999-01-01'
order by salary desc;

# 获取所有部门当前manager的当前薪水情况，给出dept_no, emp_no以及salary，当前表示to_date='9999-01-01'

SELECT d.dept_no,d.emp_no,s.salary
from dept_manager as d
join salaries as s on d.emp_no = s.emp_no
where d.to_date = '9999-01-01'
and s.to_date = '9999-01-01';

# 获取所有非manager的员工emp_no

select emp_no from employees
where emp_no not in
(select emp_no from dept_manager);

# 获取所有员工当前的manager，如果当前的manager是自己的话结果不显示，当前表示

select e.emp_no,m.emp_no as manager_no
from dept_emp as e,dept_manager as m
where e.dept_no=m.dept_no
and m.to_date='9999-01-01'
and e.emp_no<>m.emp_no
