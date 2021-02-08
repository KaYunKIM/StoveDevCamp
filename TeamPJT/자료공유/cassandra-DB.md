# cassandra DB

address=10.250.93.207

port=9042

Cluster=Tweetrend Cluster

keyspace=tweettrend

## __Tables__

| Description | Type | Name |
| --- | --- | --- |
| [partition key], [primary key] | [text] | topic |
| [partition key], [primary key] | [int] | datehour |
| [clustering key], [primary key] | [timestamp] | created_at |
| [clustering key], [primary key] | [bigint] | id |
|     | [text] | message |
| [] | [attachment] | attachments |
|     | [text] | author_id |
|     | [text] | conversation_id |
|     | [entity] | entities |
|     | [text] | in_reply_to_user_id |
|     | [boolean] | possibly_sensitive |
|     | [public_metric] | public_metrics |
|     | [list(referenced_tweet)] | referenced_tweet |
|     | [text] | reply_settings |
|     | [text] | source |
|     | [text] | lang |
|     | [text] | place_id |
|     | [include] | includes |
|     | [timestamp] | stored_at |

## Types

| Description | Type | Name |
| --- | --- | --- |
| [] | [list(text)] | media_keys |

| Description | Type | Name |
| --- | --- | --- |
| [] | [int] | start |
|     | [int] | end |
|     | [text] | url |
|     | [text] | expanded_url |
|     | [text] | display_url |
|     | [text] | unwound_url |

| Description | Type | Name |
| --- | --- | --- |
| [] | [int] | start |
|     | [int] | end |
|     | [text] | username |

| Description | Type | Name |
| --- | --- | --- |
| [] | [int] | start |
|     | [int] | end |
|     | [text] | tag |

| Description | Type | Name |
| --- | --- | --- |
| [] | [list(url)] | urls |
|     | [list(mention)] | mentions |
|     | [list(tags)] | hashtags |
|     | [list(tags)] | cashtags |

| Description | Type | Name |
| --- | --- | --- |
| [] | [int] | retweet_count |
|     | [int] | reply_count |
|     | [int] | like_count |
|     | [int] | quote_count |

| Description | Type | Name |
| --- | --- | --- |
| [] | [text] | type |
|     | [text] | id |

| Description | Type | Name |
| --- | --- | --- |
| [] | [text] | id |
|     | [text] | author_id |
|     | [text] | message |
|     | [text] | conversation_id |
|     | [boolean] | possibly_sensitive |
|     | [attachment] | attachments |
|     | [text] | reply_settings |
|     | [text] | lang |
|     | [text] | source |
|     | [public_metric] | public_metrics |
|     | [entity] | entities |
|     | [list(referenced_tweet)] | referenced_tweets |
|     | [timestamp] | created_at |

| Description | Type | Name |
| --- | --- | --- |
| [] | [bigint] | id |
|     | [text] | name |
|     | [text] | username |
|     | [text] | profile_image_url |
|     | [boolean] | verified |

| Description | Type | Name |
| --- | --- | --- |
| [] | [text] | type |
|     | [text] | media_key |
|     | [text] | url |
|     | [text] | preview_image_url |
|     | [int] | view_count |

| Description | Type | Name |
| --- | --- | --- |
| [] | [text] | full_name |
|     | [text] | id |
|     | [text] | country |
|     | [text] | country_code |
|     | [text] | name |
|     | [text] | place_type |

| Description | Type | Name |
| --- | --- | --- |
| [] | [list(tweet)] | tweets |
|     | [list(user)] | users |
|     | [list(media)] | media |
|     | [list(place)] | places |

#### Query

```sql
CREATE keyspace IF NOT EXISTS tweettrend WITH REPLICATION={'class':'SimpleStrategy', 'replication_factor':3}; 

USE tweettrend; 

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
```

