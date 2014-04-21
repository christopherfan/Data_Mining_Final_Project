-- CREATE FUNCTION convertTimeString(@time_in varchar) RETURNS time
-- 	BEGIN 
-- 		DECLARE @time_out time;
-- 		SET @time_out = 
-- 			CASE LEN(@time_in) 
-- 				WHEN 5 THEN 
-- 					CASE 
-- 						WHEN RIGHT(CAST(@time_in AS VARCHAR(5)),1) == 'A' THEN
-- 							CASE 
-- 								WHEN LEFT(CAST(@time_in AS smallint),2) > 11 THEN
-- 									CAST(LEFT(CAST(@time_in AS smallint),2) - 12,VARCHAR(2)) + SUBSTRING(CAST(@time_in AS VARCHAR(6)), 3,2) + ':00'
-- 								ELSE
-- 									LEFT(CAST(@time_in AS VARCHAR(6)),2) + SUBSTRING(CAST(@time_in AS VARCHAR(6)), 3,2) + ':00'
-- 							END;
-- 						WHEN RIGHT(CAST(@time_in AS VARCHAR(5)),1) == 'P' THEN
-- 							CASE 
-- 								WHEN LEFT(CAST(@time_in AS smallint),2) < 12 THEN
-- 									CAST(LEFT(CAST(@time_in AS smallint),2) + 12,VARCHAR(2)) + SUBSTRING(CAST(@time_in AS VARCHAR(6)), 3,2) + ':00'
-- 								ELSE
-- 									LEFT(CAST(@time_in AS VARCHAR(6)),2) + SUBSTRING(CAST(@time_in AS VARCHAR(6)), 3,2) + ':00'
-- 							END;
-- 						ELSE
-- 							'00:00:00'
-- 					END;
-- 				ELSE
-- 					'00:00:00'
-- 			END;
-- 		RETURN CAST(@time_out, TIME);
-- 	END;

-- select pv1.issuer_code, count(pv1.issuer_code) as vcount, count(distinct pv1.issue_date) as dcount
-- 	from parking_violations pv1
-- 	where pv1.violation_county = 'NY' 
-- 	group by pv1.issuer_code;

-- Copy (
	-- select pvq1.issuer_code, pvq1.vcount, pvq1.dcount, pvq2.hcount from 
	-- 	(select pv1.issuer_code, count(pv1.issuer_code) as vcount, count(distinct pv1.issue_date) as dcount
	-- 		from parking_violations pv1
	-- 		where pv1.violation_county = 'NY' 
	-- 		group by pv1.issuer_code) pvq1 
	-- 	join 
	-- 	(select pv2.issuer_code, sum(pv3.hours) as hcount
	-- 		from (
	 			select 
	 				pv3.issuer_code, 
	 				EXTRACT(EPOCH FROM 
	 					(
	 						MAX(
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
								AS TIME)
							) - MIN(
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
												WHEN RIGHT(CAST(pv3.violation_time AS VARCHAR(5)),1) = 'P' THEN
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
								AS TIME)
							)
						)
					)/3600.0 as hours
	 			from parking_violations pv3
	 			where pv3.violation_county = 'NY'
	 			group by pv3.issuer_code,pv3.issue_date
	-- 		)
	-- 		where pv2.violation_county = 'NY' 
	-- 		group by pv2.issuer_code) pvq2 
	-- 	on pvq1.issuer_code = pvq2.issuer_code)
-- To '/users/timothymeyers/projects/parkingviolations/violationscount.csv' With CSV HEADER;