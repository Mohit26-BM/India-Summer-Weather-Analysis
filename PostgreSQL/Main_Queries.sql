                                                                 /* Total Days Observed */

Select count(*) as total_days from indian_summers -- The number of days observed for all cities (13,514)
Select count(*) as total_days from indian_summers where city = 'Ahmedabad'; -- The number of days observed for Ahmedabad city (819)

                                                                 /* Average Temperature */
																 
Select round(avg(temp)::numeric,1) as avg_temperature from indian_summers; -- The Average Temperature across all cities: 31.1 C
Select round(avg(temp)::numeric,1) as avg_temperature from indian_summers where city = 'Ahmedabad'; -- The Average Temperature in Ahmedabad: 33.8 C

                                                                 /* Average Feels Like Temperature */
																 
Select round(avg(feelslike)::numeric,1) as avg_feels_like from indian_summers;  -- Average Feels Like Temperature is 33.7 C
Select round(avg(feelslike)::numeric,1) as avg_feels_like from indian_summers where city = 'Ahmedabad'; -- Average Feels Like Temperature is 36.6 C

                                                                /* Average Humidity */

Select round(avg(humidity)::numeric,1) as avg_humidity from indian_summers; -- The Average humidity across all the cities is 54.7%
Select round(avg(humidity)::numeric,1) as avg_humidity from indian_summers where city = 'Ahmedabad'; -- The Average Humidity in Ahmedabad is 46.2%.

                                                                 /* Average Windspeed */
																 
Select round(avg(windspeed)::numeric,1) as avg_wind_speed from indian_summers; -- The average windspeed is 20.1 kmph
Select round(avg(windspeed)::numeric,1) as avg_wind_speed from indian_summers where city = 'Ahmedabad'; -- The average windspeed is 18.8 kmph

                                                                /* Average Temperature Trend (Line Chart) */
																
Select extract(year from recorded_at) as year, round(avg(temp)::numeric,3) as avg_temperature from indian_summers where city = 'Ahmedabad' group by year order by year;


                                                                /*Days by Conditions (Pie Chart)*/
																
Select conditions, count(*) as days from indian_summers group by conditions order by days desc;															
Select conditions, count(*) as days from indian_summers where city = 'Ahmedabad' group by conditions order by days desc;

                                                                /*Humidity Trends (Bar Chart)*/
																
Select city, round(avg(humidity)::numeric) AS avg_humidity from indian_summers where city = 'Ahmedabad' group by city; 


                                                               /*Temperature Distribution by City (Box Plot)*/
															   
Select city, percentile_cont(0.25) within group (order by temp) as q1, percentile_cont(0.5) within group (order by temp) as median,
percentile_cont(0.75) within group (order by temp) as q3, min(temp) as min_temp, max(temp) as max_temp from indian_summers where city = 'Ahmedabad' group by city;



