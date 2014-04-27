Copy (
	select count(pv.issuer_code) from parking_violations pv where pv.issuer_code in
	(
		select 
			distinct pv1.issuer_code
		from parking_violations pv1
		where pv1.violation_county = 'NY' 
		group by pv1.issuer_code
		having count(distinct pv1.issue_date) > 50
	)
) To '/users/timothymeyers/projects/parkingviolations/tim/issuers_count.csv' With CSV HEADER;