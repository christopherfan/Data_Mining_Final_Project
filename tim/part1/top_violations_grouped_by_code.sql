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
			where issuer_code in (349570,351274,353486,346105,356304,347489,347687,358194,355134,357792,358623,349481,357783,357360,354098,355538,346346,353070,346330,340051,356225,358128,354084,350433,352079,358117,351929,342966,352950,357735,345221,353194,355567,357724,356484,352946,345238,351280,355220,358119,351997,358600,355224,356964,331510,358948,357073,357338,355156,330692,358204,357736,355710,353424,354125,349850,357088,341298,356512,358617,355497,346381,357771,355283,355691,352070,345275,356261,344778,337778,350423,353408,358570,357721,353508,353069,330001,358214,330198,353164,357086,345560,356314,350425,352036,355144,354043,347593,358936,355588,356181,341980,355453,355532,356262,356259,355438,352992,358857,355417,356308,355428,355451,355073,355446,358594,333386,357751,347674,355218,331220,349538,346409,355675,350401,355546,355619,358944,358607,355205,355113,351919,355639,357700,356518,358579,356352,349576,333163,355117,343918,358228,351995,357113,354205,357689,358863,345536,350407,356356,355642,345131,359336,350439,355212,346109,358187,355677,353176,358892,358603,355050,357701,356959,355080,356214,357802,355492,345331,330291,351239,355145,358608,358847,333733,350424,341943,355530,358126,357068,348520,357078,356522,356565,348566,358873)
		) as pv
	where pv.violation_time_bucket >= 1 and pv.violation_time_bucket <= 12
	group by pv.violation_code
	order by pv.violation_code
) To '/users/timothymeyers/projects/parkingviolations/tim/part1/top_violations_grouped_by_code.csv' With CSV HEADER;