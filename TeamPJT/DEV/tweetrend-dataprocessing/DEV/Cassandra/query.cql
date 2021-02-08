-- create keyspace
CREATE keyspace IF NOT EXISTS tweettrend WITH REPLICATION={'class':'SimpleStrategy', 'replication_factor':3}; 

-- alter keyspace
USE tweettrend; 

-- create types
CREATE TYPE attachment 
( 
media_keys LIST<TEXT> 
); 

CREATE TYPE url 
( 
start INT, 
end INT, 
url TEXT, 
expanded_url TEXT, 
display_url TEXT, 
unwound_url TEXT 
); 

CREATE TYPE mention 
( 
start INT, 
end INT, 
username TEXT 
); 

CREATE TYPE tag 
( 
start INT, 
end INT, 
tag TEXT 
); 

CREATE TYPE entity 
( 
urls LIST<frozen<url>>, 
mentions LIST<frozen<mention>>, 
hashtags LIST<frozen<tag>>, 
cashtags LIST<frozen<tag>> 
); 

CREATE TYPE public_metric 
( 
retweet_count INT, 
reply_count INT, 
like_count INT, 
quote_count INT 
); 

CREATE TYPE referenced_tweet 
( 
type TEXT, 
id TEXT 
); 

CREATE TYPE tweet 
( 
id TEXT, 
author_id TEXT,
message TEXT, 
conversation_id TEXT,
possibly_sensitive BOOLEAN,
attachments frozen<attachment>,
reply_settings TEXT,
source TEXT,
place_id TEXT,
lang TEXT,
in_reply_to_user_id TEXT,
public_metrics frozen<public_metric>, 
entities frozen<entity>,
referenced_tweets LIST<frozen<referenced_tweet>>, 
created_at TIMESTAMP
); 

CREATE TYPE user
(
id BIGINT,
name TEXT,
username TEXT,
profile_image_url TEXT,
verified BOOLEAN
);

CREATE TYPE media 
( 
type TEXT, 
media_key TEXT, 
url TEXT, 
preview_image_url TEXT, 
view_count INT
);  

CREATE TYPE place
(
full_name TEXT,
id TEXT,
country TEXT,
country_code TEXT,
name TEXT,
place_type TEXT
);

CREATE TYPE include 
( 
tweets LIST<frozen<tweet>>, 
users LIST<frozen<user>>, 
media LIST<frozen<media>>,
places LIST<frozen<place>>
);

-- create tables
CREATE TABLE tweettrend.tweets 
( 
topic TEXT, 
datehour INT, 
id BIGINT, 
message TEXT, 
attachments frozen<attachment>, 
author_id BIGINT,
conversation_id BIGINT,
created_at TIMESTAMP, 
entities frozen<entity>, 
in_reply_to_user_id BIGINT,
possibly_sensitive BOOLEAN, 
public_metrics frozen<public_metric>, 
referenced_tweets LIST<frozen<referenced_tweet>>, 
reply_settings TEXT, 
source TEXT, 
lang TEXT, 
place_id TEXT,
includes frozen<include>, 
stored_at TIMESTAMP, 
PRIMARY KEY((topic, datehour), created_at, id) 
) 
WITH clustering ORDER BY (created_at desc, id desc) ;

-- view all tables in keyspace
select * from system_schema.tables where keyspace_name='tweettrend';

-- view all columns in table
select * from system_schema.columns where keyspace_name='tweettrend' and table_name='tweets';

-- view all types in keyspace
select * from system_schema.types where keyspace_name='tweettrend';

-- select data with datehour range without ALLOW FILTERING
select * from tweettrend.tweets where topic='temp' and datehour in (2021011302, 2021011402); 

-- query for feed
select * from tweets where topic='covid-19' and datehour in (2040455, 2040456, 2040457) and created_at>='2021-02-04T04:55:55.000Z' and created_at<='2021-02-04T04:56:55.000Z';

-- query for trend
select message, author_id, place_id, source, referenced_tweets, includes from tweets where topic='covid-19' and datehour=2040456;

-- set table compacted everyday
ALTER TABLE tweets
WITH compaction={
    'class': 'TimeWindowCompactionStrategy',
    'compaction_window_size': '1',
    'compaction_window_unit': 'DAYS',
    'tombstone_threshold': '0.5',
    'unchecked_tombstone_compaction': true};