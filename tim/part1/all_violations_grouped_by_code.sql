Copy (
	select 
		pv.violation_code,
		--violations_top_performers.violation_time_bucket, 
		count(pv.issuer_code)
	from
		(
			select 
				issuer_code, 
				violation_time,
				CAST(
					CASE length(violation_time)
						WHEN 5 THEN 
							CASE 
								WHEN RIGHT(violation_time,1) = 'A' THEN
									CASE 
										WHEN CAST(LEFT(violation_time,2) AS smallint) > 11 THEN
											CAST(CAST(LEFT(violation_time,2) AS smallint) - 12 AS VARCHAR(2)) || ':' || SUBSTRING(violation_time, 3,2) || ':00'
										ELSE
											LEFT(violation_time,2) || ':' || SUBSTRING(violation_time, 3,2) || ':00'
									END
								WHEN RIGHT(violation_time,1) = 'P' THEN
									CASE 
										WHEN CAST(LEFT(violation_time,2) AS smallint) < 12 THEN
											CAST(CAST(LEFT(violation_time,2) AS smallint) + 12 AS VARCHAR(2)) || ':' || SUBSTRING(violation_time, 3,2) || ':00'
										ELSE
											LEFT(violation_time,2) || ':' || SUBSTRING(violation_time, 3,2) || ':00'
									END
								ELSE
									'00:00:00'
							END
						ELSE
							'00:00:00'
					END
				AS TIME) as violation_time_formatted,
				extract(hour from 
					CAST(
						CASE length(violation_time)
							WHEN 5 THEN 
								CASE 
									WHEN RIGHT(violation_time,1) = 'A' THEN
										CASE 
											WHEN CAST(LEFT(violation_time,2) AS smallint) > 11 THEN
												CAST(CAST(LEFT(violation_time,2) AS smallint) - 12 AS VARCHAR(2)) || ':' || SUBSTRING(violation_time, 3,2) || ':00'
											ELSE
												LEFT(violation_time,2) || ':' || SUBSTRING(violation_time, 3,2) || ':00'
										END
									WHEN RIGHT(violation_time,1) = 'P' THEN
										CASE 
											WHEN CAST(LEFT(violation_time,2) AS smallint) < 12 THEN
												CAST(CAST(LEFT(violation_time,2) AS smallint) + 12 AS VARCHAR(2)) || ':' || SUBSTRING(violation_time, 3,2) || ':00'
											ELSE
												LEFT(violation_time,2) || ':' || SUBSTRING(violation_time, 3,2) || ':00'
										END
									ELSE
										'00:00:00'
								END
							ELSE
								'00:00:00'
						END
					AS TIME)
				) - 5 as violation_time_bucket,
				violation_code
			from parking_violations 
			where issuer_code in (
				select 
					distinct pv1.issuer_code
				from parking_violations pv1
				where pv1.violation_county = 'NY' 
				group by pv1.issuer_code
				having count(distinct pv1.issue_date) > 50
			)
		) as pv
	where pv.violation_time_bucket >= 1 and pv.violation_time_bucket <= 12
	group by pv.violation_code
	order by pv.violation_code
) To '/users/timothymeyers/projects/parkingviolations/tim/part1/all_violations_grouped_by_code.csv' With CSV HEADER;