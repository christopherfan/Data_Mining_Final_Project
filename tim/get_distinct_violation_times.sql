--Copy (
	select pv.violationtimes, count(pv.violationtimes) as vcount from
		(select
			CAST(
				CASE length(pv3.violation_time) 
					WHEN 5 THEN 
						CASE 
							WHEN RIGHT(pv3.violation_time,1) = 'A' THEN
								CASE 
									WHEN CAST(LEFT(pv3.violation_time,2) AS smallint) > 11 THEN
										CAST(CAST(LEFT(pv3.violation_time,2) AS smallint) - 12 AS VARCHAR(2)) || ':' || SUBSTRING(pv3.violation_time, 3,2) || ':00'
									ELSE
										LEFT(pv3.violation_time,2) || ':' || SUBSTRING(pv3.violation_time, 3,2) || ':00'
								END
							WHEN RIGHT(pv3.violation_time,1) = 'P' THEN
								CASE 
									WHEN CAST(LEFT(pv3.violation_time,2) AS smallint) < 12 THEN
										CAST(CAST(LEFT(pv3.violation_time,2) AS smallint) + 12 AS VARCHAR(2)) || ':' || SUBSTRING(pv3.violation_time, 3,2) || ':00'
									ELSE
										LEFT(pv3.violation_time,2) || ':' || SUBSTRING(pv3.violation_time, 3,2) || ':00'
								END
							ELSE
								'00:00:00'
						END
					ELSE
						'00:00:00'
				END
			AS TIME) as violationtimes 
		from parking_violations pv3) pv
	group by pv.violationtimes
--) To '/users/timothymeyers/projects/parkingviolations/violationtimes.csv' With CSV HEADER;