Copy (
	select 
		pv1.issuer_code, 
		count(pv1.issuer_code) as vcount, 
		count(distinct pv1.issue_date) as dcount,
		count(pv1.issuer_code)*1.0 / count(distinct pv1.issue_date) as avgcount
	from parking_violations pv1
	where pv1.violation_county = 'NY' 
	group by pv1.issuer_code
	having count(distinct pv1.issue_date) > 50
	order by avgcount desc
) To '/users/timothymeyers/projects/parkingviolations/issuers.csv' With CSV HEADER;