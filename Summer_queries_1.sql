Create Table indian_summers ( id SERIAL Primary Key,city VARCHAR(100) Not Null, recorded_at TIMESTAMP WITHOUT TIME ZONE NOT NULL, tempmax FLOAT, tempmin FLOAT,
temp FLOAT, feelslikemax FLOAT, feelslikemin FLOAT, feelslike FLOAT, dew FLOAT, humidity FLOAT, windspeed FLOAT, winddir FLOAT, sealevelpressure FLOAT, cloudcover FLOAT,
visibility FLOAT, sunrise TIMESTAMP WITHOUT TIME ZONE, sunset TIMESTAMP WITHOUT TIME ZONE, moonphase FLOAT,conditions VARCHAR(255), description TEXT);

Copy indian_summers(city, recorded_at, tempmax, tempmin, temp, feelslikemax, feelslikemin,feelslike, dew, humidity, windspeed, winddir, sealevelpressure, cloudcover, 
visibility, sunrise, sunset, moonphase, conditions, description) 

From 'C:\Program Files\PostgreSQL\17\data\Indian Summers - Over the years.csv' 
Delimiter ',' 
csv header;

Alter Table indian_summers Alter Column recorded_at Type DATE Using recorded_at::DATE;

Select count(*) as Row_Count from Indian_Summers;

Select distinct(City) from Indian_Summers;

Select * from indian_summers limit 5;

Select  city, Min(recorded_at) As min_date, Max(recorded_at) As max_date, Count(*) As total_days From indian_summers Group By city Order By city;

Select city, Count(Distinct recorded_at) as total_days from indian_summers group by city order by total_days desc;

SELECT COUNT(DISTINCT recorded_at) AS unique_days, COUNT(DISTINCT city) AS total_cities
FROM indian_summers;


















