SELECT l.firstname as firstname,
l.lastname as lastname,
r.city as city,
r.state as state
from person as l
left join address as r
on l.personid = r.personid;