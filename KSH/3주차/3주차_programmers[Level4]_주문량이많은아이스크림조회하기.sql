'''
배운점
- union, join, 서브쿼리의 사용
- 문제 해석이 중요하다.
    왜냐면, first_half는 공장과 맛이 고정인데,
    july는 다른 공장에서도 특정 맛을 생산하기 때문.
    
    그래서 first_half에 있는 맛들만 존재하는 거기 때문에
    left join, join을 쓸 수 있는 것임.
'''


# 풀이 1 - union all+서브쿼리
select a.flavor
    from
        (select * from first_half
        union all
        select * from july) as a
group by a.flavor
order by sum(a.total_order) desc
limit 3

# 풀이 2 - left join+서브쿼리
select f.flavor
    from first_half f
    left join
    (select july.flavor, sum(july.total_order) as t from july
    group by july.flavor) as j on f.flavor = j.flavor
order by f.total_order+j.t desc
limit 3

# 풀이 3 - join
select f.flavor from first_half as f
join july as j
on f.flavor = j.flavor
group by f.flavor
order by f.total_order+sum(j.total_order) desc
limit 3