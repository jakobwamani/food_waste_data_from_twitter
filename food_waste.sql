-- Create Database
create database food;

--  select database;
use food;

-- create table inside the food database
create table device_action(
date varchar(50),
source varchar(50)
);

-- Look inside the table
select * from device_action;

-- How many tweets in totals
select count(source) from device_action;

-- How many sources of Tweets are available
select  count(distinct source) as number_of_tweets from device_action; 

-- How many tweets were made from each of the different sources;
select source ,count(source) from device_action group by source order by 2 desc;

