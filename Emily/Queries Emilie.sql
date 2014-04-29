# In POSTGRESQL

# create database and import data
CREATE DATABASE parkingviolations;

CREATE TABLE parking_violations 
(summons_number bigint,
 plate_id varchar,
 registration_state varchar,
 plate_type varchar,
 issue_date date, 
 violation_code integer,
 vehicle_body_type varchar,
 vehicle_make varchar,
 issuing_agency varchar,
 street_code_1 integer,
 street_code_2 integer,
 street_code_3 integer,
 vehicle_expiration_date varchar,
 violation_location varchar,
 violation_precinct smallint,
 issuer_precinct smallint,
 issuer_code integer,
 issuer_command varchar,
 issuer_squad varchar,
 violation_time varchar,
 time_first_observed varchar,
 violation_county varchar,
 violation_in_front_of_or_opposite varchar,
 house_number varchar,
 street_name varchar,
 intersecting_street varchar,
 date_first_observed varchar,
 law_section smallint,
 sub_division varchar,
 violation_legal_code varchar,
 days_parking_in_effect varchar,
 from_hours_in_effect varchar,
 to_hours_in_effect varchar,
 vehicle_color varchar,
 unregistered_vehicle boolean,
 vehicle_year smallint,
 meter_number varchar,
 feet_from_curb smallint,
 violation_post_code varchar,
 violation_description text,
 no_standing_or_stopping_violation text,
 hydrant_violation text,
 double_parking_violation text);

COPY parking_violations FROM '/Users/Emilie/_Github/Data_Mining_Final_Project/Myfiles/Parking_Violations_Issued.csv' DELIMITER ',' CSV HEADER;


#remove errors and select issuers only in NY
delete from parking_violations where issuer_code = 0;
delete from parking_violations where violation_time like '%:%' or violation_time like'%*%' or violation_time like'%/%';
delete from parking_violations where violation_county !='NY';

# import in table list of issuers_id who worked more than 50 days (tim's file)
create table issuers(
issuer_code bigint,
vcount int,
dcount int,
avgcount real);
COPY issuers FROM '/Users/Emilie/_Github/Data_Mining_Final_Project/tim/issuers.csv' DELIMITER ',' CSV HEADER;

# keep only issuers who worked more than 50 days
 delete from parking_violations where issuer_code not in (select issuer_code from issuers);





# Create new tables with selected features: 
#summons_number, issue_date, violation_code,vehicle_body_type, violation_location, issuer_code, violation_time, street_name, vehicle_color, vehicle_year

create table selected_data 
AS select summons_number, 
issue_date, 
extract(isodow from issue_date) as day_week,
(CASE extract(isodow from issue_date) 
WHEN 1 then 'Week'
WHEN 2 then 'Week'
WHEN 3 then 'Week'
WHEN 4 then 'Week'
WHEN 5 then 'Week'
ELSE 'Weekend'
END) as type_day,
violation_code, 
vehicle_body_type, 
violation_location, 
issuer_code, 
violation_time,
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
as new_violation_time, # need to be converted to time after out-of-range values deleted
street_name, 
vehicle_color
from parking_violations;


# Delete raws with time in wrong format
delete from selected_data where new_violation_time similar to '[2-9][4-9]:_____';
delete from selected_data where new_violation_time similar to '[3-9][0-9]:_____';




# New data with time formatted, time bucket, time restriction to 6am/6pm, violation_category, and day_period (AM/PM)
create table new_data 
AS select summons_number, 
issue_date, 
day_week,
type_day,
violation_code,
case violation_code
	when 1 then 5
	when 2 then 5
	when 3 then 6
	when 4 then 2
	when 5 then 6
	when 6 then 2
	when 7 then 6
	when 8 then 2
	when 9 then 3
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
	when 52 then 3
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
end as violation_category, 
vehicle_body_type, 
violation_location, 
issuer_code, 
cast(new_violation_time as time) as violation_time_formatted,
extract(hour from cast(new_violation_time as time)) - 5 as violation_time_bucket,
case (extract(hour from cast(new_violation_time as time)) - 5)
	when 1 then 'AM'
	when 2 then 'AM'
	when 3 then 'AM'
	when 4 then 'AM'
	when 5 then 'AM'
	when 6 then 'AM'
	when 7 then 'PM'
	when 8 then 'PM'
	when 9 then 'PM'
	when 10 then 'PM'
	when 11 then 'PM'
	when 12 then 'PM'
	else Null
	END as day_period,
street_name, 
vehicle_color
from selected_data
where (extract(hour from cast(new_violation_time as time)) - 5) >= 1 and (extract(hour from cast(new_violation_time as time)) - 5) <=12;





'''FILES CREATION from Table new_data'''


# Extraction of selected data for top performers: to use for both analysis and clusterings (try with different features and combinations)
Copy(
select issuer_code, 
issue_date, 
day_week, 
type_day, 
violation_time_bucket, 
day_period, 
violation_code, 
violation_category, 
vehicle_body_type, 
vehicle_color, 
violation_location
from new_data
where issuer_code in (349570,351274,353486,346105,356304,347489,347687,358194,355134,357792,358623,349481,357783,357360,354098,355538,346346,353070,346330,340051,356225,358128,354084,350433,352079,358117,351929,342966,352950,357735,345221,353194,355567,357724,356484,352946,345238,351280,355220,358119,351997,358600,355224,356964,331510,358948,357073,357338,355156,330692,358204,357736,355710,353424,354125,349850,357088,341298,356512,358617,355497,346381,357771,355283,355691,352070,345275,356261,344778,337778,350423,353408,358570,357721,353508,353069,330001,358214,330198,353164,357086,345560,356314,350425,352036,355144,354043,347593,358936,355588,356181,341980,355453,355532,356262,356259,355438,352992,358857,355417,356308,355428,355451,355073,355446,358594,333386,357751,347674,355218,331220,349538,346409,355675,350401,355546,355619,358944,358607,355205,355113,351919,355639,357700,356518,358579,356352,349576,333163,355117,343918,358228,351995,357113,354205,357689,358863,345536,350407,356356,355642,345131,359336,350439,355212,346109,358187,355677,353176,358892,358603,355050,357701,356959,355080,356214,357802,355492,345331,330291,351239,355145,358608,358847,333733,350424,341943,355530,358126,357068,348520,357078,356522,356565,348566,358873)
order by issuer_code
)
To '/Users/Emilie/_Github/Data_Mining_Final_Project/Myfiles/new_data_top_perfomers' With CSV HEADER;


# Selected data that could be interested to analyze: INFO_TOP_PERFOMERS --> to make pivot tables
Copy(
select issuer_code, 
day_week, 
type_day,  
day_period, 
violation_code, 
violation_category,
count(issuer_code)
from new_data
where issuer_code in (349570,351274,353486,346105,356304,347489,347687,358194,355134,357792,358623,349481,357783,357360,354098,355538,346346,353070,346330,340051,356225,358128,354084,350433,352079,358117,351929,342966,352950,357735,345221,353194,355567,357724,356484,352946,345238,351280,355220,358119,351997,358600,355224,356964,331510,358948,357073,357338,355156,330692,358204,357736,355710,353424,354125,349850,357088,341298,356512,358617,355497,346381,357771,355283,355691,352070,345275,356261,344778,337778,350423,353408,358570,357721,353508,353069,330001,358214,330198,353164,357086,345560,356314,350425,352036,355144,354043,347593,358936,355588,356181,341980,355453,355532,356262,356259,355438,352992,358857,355417,356308,355428,355451,355073,355446,358594,333386,357751,347674,355218,331220,349538,346409,355675,350401,355546,355619,358944,358607,355205,355113,351919,355639,357700,356518,358579,356352,349576,333163,355117,343918,358228,351995,357113,354205,357689,358863,345536,350407,356356,355642,345131,359336,350439,355212,346109,358187,355677,353176,358892,358603,355050,357701,356959,355080,356214,357802,355492,345331,330291,351239,355145,358608,358847,333733,350424,341943,355530,358126,357068,348520,357078,356522,356565,348566,358873)
group by issuer_code, day_week, type_day, day_period, violation_code, violation_category
order by issuer_code
)
To '/Users/Emilie/_Github/Data_Mining_Final_Project/Emily/inf_top_performers.csv' With CSV HEADER;


# Create the features for custering (for best issuers): FEATURES_TOP_PERFOMERS
Copy(
select issuer_code, 
sum(case when day_week = 1 then 1 else 0 end) as tickets_monday,
sum(case when day_week = 2 then 1 else 0 end) as tickets_tuesday,
sum(case when day_week = 3 then 1 else 0 end) as tickets_wednesdays,
sum(case when day_week = 4 then 1 else 0 end) as tickets_thursday,
sum(case when day_week = 5 then 1 else 0 end) as tickets_friday,
sum(case when day_week = 6 then 1 else 0 end) as tickets_saturday,
sum(case when day_week = 7 then 1 else 0 end) as tickets_sunday,
sum(case when violation_category = 1 then 1 else 0 end) as tickets_cat_1,
sum(case when violation_category = 2 then 1 else 0 end) as tickets_cat_2,
sum(case when violation_category = 3 then 1 else 0 end) as tickets_cat_3,
sum(case when violation_category = 4 then 1 else 0 end) as tickets_cat_4,
sum(case when violation_category = 5 then 1 else 0 end) as tickets_cat_5,
sum(case when violation_category = 6 then 1 else 0 end) as tickets_cat_6,
sum(case when type_day = 'Week' then 1 else 0 end) as tickets_week,
sum(case when type_day = 'Weekend' then 1 else 0 end) as tickets_weekend,
sum(case when day_period = 'AM' then 1 else 0 end) as tickets_AM,
sum(case when day_period = 'PM' then 1 else 0 end) as tickets_PM
from new_data
where issuer_code in (349570,351274,353486,346105,356304,347489,347687,358194,355134,357792,358623,349481,357783,357360,354098,355538,346346,353070,346330,340051,356225,358128,354084,350433,352079,358117,351929,342966,352950,357735,345221,353194,355567,357724,356484,352946,345238,351280,355220,358119,351997,358600,355224,356964,331510,358948,357073,357338,355156,330692,358204,357736,355710,353424,354125,349850,357088,341298,356512,358617,355497,346381,357771,355283,355691,352070,345275,356261,344778,337778,350423,353408,358570,357721,353508,353069,330001,358214,330198,353164,357086,345560,356314,350425,352036,355144,354043,347593,358936,355588,356181,341980,355453,355532,356262,356259,355438,352992,358857,355417,356308,355428,355451,355073,355446,358594,333386,357751,347674,355218,331220,349538,346409,355675,350401,355546,355619,358944,358607,355205,355113,351919,355639,357700,356518,358579,356352,349576,333163,355117,343918,358228,351995,357113,354205,357689,358863,345536,350407,356356,355642,345131,359336,350439,355212,346109,358187,355677,353176,358892,358603,355050,357701,356959,355080,356214,357802,355492,345331,330291,351239,355145,358608,358847,333733,350424,341943,355530,358126,357068,348520,357078,356522,356565,348566,358873)
group by issuer_code
order by issuer_code
)
To '/Users/Emilie/_Github/Data_Mining_Final_Project/Myfiles/features_top_performers.csv' With CSV HEADER;



# Create the features for custering (for other issuers): FEATURES_OTHER_PERFOMERS
Copy(
select issuer_code, 
sum(case when day_week = 1 then 1 else 0 end) as tickets_monday,
sum(case when day_week = 2 then 1 else 0 end) as tickets_tuesday,
sum(case when day_week = 3 then 1 else 0 end) as tickets_wednesdays,
sum(case when day_week = 4 then 1 else 0 end) as tickets_thursday,
sum(case when day_week = 5 then 1 else 0 end) as tickets_friday,
sum(case when day_week = 6 then 1 else 0 end) as tickets_saturday,
sum(case when day_week = 7 then 1 else 0 end) as tickets_sunday,
sum(case when violation_category = 1 then 1 else 0 end) as tickets_cat_1,
sum(case when violation_category = 2 then 1 else 0 end) as tickets_cat_2,
sum(case when violation_category = 3 then 1 else 0 end) as tickets_cat_3,
sum(case when violation_category = 4 then 1 else 0 end) as tickets_cat_4,
sum(case when violation_category = 5 then 1 else 0 end) as tickets_cat_5,
sum(case when violation_category = 6 then 1 else 0 end) as tickets_cat_6,
sum(case when type_day = 'Week' then 1 else 0 end) as tickets_week,
sum(case when type_day = 'Weekend' then 1 else 0 end) as tickets_weekend,
sum(case when day_period = 'AM' then 1 else 0 end) as tickets_AM,
sum(case when day_period = 'PM' then 1 else 0 end) as tickets_PM
from new_data
where issuer_code not in (349570,351274,353486,346105,356304,347489,347687,358194,355134,357792,358623,349481,357783,357360,354098,355538,346346,353070,346330,340051,356225,358128,354084,350433,352079,358117,351929,342966,352950,357735,345221,353194,355567,357724,356484,352946,345238,351280,355220,358119,351997,358600,355224,356964,331510,358948,357073,357338,355156,330692,358204,357736,355710,353424,354125,349850,357088,341298,356512,358617,355497,346381,357771,355283,355691,352070,345275,356261,344778,337778,350423,353408,358570,357721,353508,353069,330001,358214,330198,353164,357086,345560,356314,350425,352036,355144,354043,347593,358936,355588,356181,341980,355453,355532,356262,356259,355438,352992,358857,355417,356308,355428,355451,355073,355446,358594,333386,357751,347674,355218,331220,349538,346409,355675,350401,355546,355619,358944,358607,355205,355113,351919,355639,357700,356518,358579,356352,349576,333163,355117,343918,358228,351995,357113,354205,357689,358863,345536,350407,356356,355642,345131,359336,350439,355212,346109,358187,355677,353176,358892,358603,355050,357701,356959,355080,356214,357802,355492,345331,330291,351239,355145,358608,358847,333733,350424,341943,355530,358126,357068,348520,357078,356522,356565,348566,358873)
group by issuer_code
order by issuer_code
)
To '/Users/Emilie/_Github/Data_Mining_Final_Project/Myfiles/features_other_performers.csv' With CSV HEADER;





'''MIDDLE ISSUERS: 1/2 std below and above the average: 150 issuers '''
# import in table list of middle_issuers_id (between 1/2 std below and above the mean)

create table middle_issuers(
issuer_code bigint);
COPY middle_issuers FROM '/Users/Emilie/_Github/Data_Mining_Final_Project/Myfiles/middle_issuers_id.csv' DELIMITER ',' CSV HEADER;


Copy(
select issuer_code, 
day_week, 
type_day,  
day_period, 
violation_code, 
violation_category,
count(issuer_code)
from new_data
where issuer_code in (select issuer_code from middle_issuers)
group by issuer_code, day_week, type_day, day_period, violation_code, violation_category
order by issuer_code
)
To '/Users/Emilie/_Github/Data_Mining_Final_Project/Emily/inf_middle_performers.csv' With CSV HEADER;



Copy(
select issuer_code, 
sum(case when day_week = 1 then 1 else 0 end) as tickets_monday,
sum(case when day_week = 2 then 1 else 0 end) as tickets_tuesday,
sum(case when day_week = 3 then 1 else 0 end) as tickets_wednesdays,
sum(case when day_week = 4 then 1 else 0 end) as tickets_thursday,
sum(case when day_week = 5 then 1 else 0 end) as tickets_friday,
sum(case when day_week = 6 then 1 else 0 end) as tickets_saturday,
sum(case when day_week = 7 then 1 else 0 end) as tickets_sunday,
sum(case when violation_category = 1 then 1 else 0 end) as tickets_cat_1,
sum(case when violation_category = 2 then 1 else 0 end) as tickets_cat_2,
sum(case when violation_category = 3 then 1 else 0 end) as tickets_cat_3,
sum(case when violation_category = 4 then 1 else 0 end) as tickets_cat_4,
sum(case when violation_category = 5 then 1 else 0 end) as tickets_cat_5,
sum(case when violation_category = 6 then 1 else 0 end) as tickets_cat_6,
sum(case when type_day = 'Week' then 1 else 0 end) as tickets_week,
sum(case when type_day = 'Weekend' then 1 else 0 end) as tickets_weekend,
sum(case when day_period = 'AM' then 1 else 0 end) as tickets_AM,
sum(case when day_period = 'PM' then 1 else 0 end) as tickets_PM
from new_data
where issuer_code in (select issuer_code from middle_issuers)
group by issuer_code
order by issuer_code
)
To '/Users/Emilie/_Github/Data_Mining_Final_Project/Myfiles/features_middle_performers.csv' With CSV HEADER;







