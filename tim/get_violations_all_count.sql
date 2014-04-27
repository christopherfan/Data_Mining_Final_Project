Copy (
	select 
		count(*)
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
				violation_code,
				case violation_code
					when 1 then 5
					when 2 then	5
					when 3 then	6
					when 4 then	2
					when 5 then	6
					when 6 then	2
					when 7 then	6
					when 8 then	2
					when 9 then	3
					when 10 then 2
					when 11 then 2
					when 12 then 2
					when 13 then 2
					when 14 then 2
					when 16 then 2
					when 17 then 2
					when 18 then 2
					when 19 then 2
					when 20 then 2
					when 21 then 1
					when 22 then 2
					when 23 then 2
					when 24 then 2
					when 25 then 2
					when 26 then 2
					when 27 then 2
					when 28 then 2
					when 29 then 6
					when 30 then 6
					when 31 then 2
					when 32 then 4
					when 33 then 4
					when 34 then 4
					when 35 then 6
					when 36 then 6
					when 37 then 4
					when 38 then 5
					when 39 then 4
					when 40 then 2
					when 42 then 4
					when 43 then 4
					when 44 then 4
					when 45 then 3
					when 46 then 3
					when 47 then 3
					when 48 then 3
					when 49 then 3
					when 50 then 3
					when 51 then 3
					when 52	then 3
					when 53 then 3
					when 55 then 3
					when 56 then 3
					when 57 then 2
					when 58 then 2
					when 59 then 3
					when 60 then 3
					when 61 then 3
					when 62 then 3
					when 63 then 2
					when 64 then 2
					when 65 then 4
					when 66 then 6
					when 67 then 3
					when 68 then 2
					when 69 then 5
					when 70 then 5
					when 71 then 5
					when 72 then 5
					when 73 then 5
					when 74 then 5
					when 75 then 5
					when 77 then 6
					when 78 then 2
					when 79 then 3
					when 80 then 6
					when 81 then 2
					when 82 then 5
					when 83 then 5
					when 84 then 5
					when 85 then 4
					when 86 then 2
					when 89 then 2
					when 91 then 6
					when 92 then 6
					when 93 then 6
					when 94 then 6
					when 96 then 2
					when 97 then 2
					when 98 then 2
					when 99 then 6
				end as violation_category
			from parking_violations
		) as violations_top_performers
	where violations_top_performers.violation_time_bucket >= 1 and violations_top_performers.violation_time_bucket <= 12
) To '/users/timothymeyers/projects/parkingviolations/violations_all_count.csv' With CSV HEADER;