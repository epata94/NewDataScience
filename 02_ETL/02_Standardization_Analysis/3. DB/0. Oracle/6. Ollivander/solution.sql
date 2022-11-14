-- Harry Potter and his friends are at Ollivander's with Ron, finally replacing Charlie's old broken wand.
-- Hermione decides the best way to choose is by determining the minimum number of gold galleons needed to buy 
-- each "non-evil"
-- wand of high power and age.

-- Write a query to print the id, age, coins_needed, and power of the wands that Ron's interested in,
-- sorted in order of descending power. 
-- If more than one wand has same power, sort the result in order of descending age.

-- Best Answer
select id,age,coins_needed,power   
	from (select id,age,coins_needed,power, min(coins_needed) 
		over (partition by w.code,age,power) as min_coins from wands w 
		inner join wands_property wp on w.code = wp.code
			where wp.is_evil =0
	) where coins_needed = min_coins 
order by power desc,age desc;

-- q]
select id,age,coins_needed,power   
	from (select id,age,coins_needed, power,  min(coins_needed) as min_coins from wands w 
		inner join wands_property wp on w.code = wp.code
			where wp.is_evil =0
            group by id, wp.age, coins_needed, power;
	) where coins_needed = min_coins 
order by power desc,age desc;


select w.id, p.age, w.coins_needed,w.power
    from wands w
    join wands_property p
      on p.code = w.code
    where (p.age,w.power,w.coins_needed) in (
            select p1.age,w1.power,min(w1.coins_needed)
                from wands_property p1
                join wands w1
                  on w1.code = p1.code
                where p1.is_evil = 0
                group by p1.age, w1.power)
    order by w.power desc, p.age desc












