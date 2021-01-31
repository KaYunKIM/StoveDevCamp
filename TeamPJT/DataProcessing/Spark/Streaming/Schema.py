from pyspark.sql.types import StringType, IntegerType, LongType, BooleanType, StructField, StructType, ArrayType


attachment = StructType(
    [
        StructField('media_keys', ArrayType(StringType(), True), True)
    ]
)

url = StructType(
    [
        StructField('start', IntegerType(), True),
        StructField('end', IntegerType(), True),
        StructField('url', StringType(), True),
        StructField('expanded_url', StringType(), True),
        StructField('display_url', StringType(), True),
        StructField('unwounded_url', StringType(), True),
        StructField('status', StringType(), True),
        StructField('title', StringType(), True),
        StructField('description', StringType(), True)
    ]
)

mention = StructType(
    [
        StructField('start', IntegerType(), True),
        StructField('end', IntegerType(), True),
        StructField('username', StringType(), True),
    ]
)

tag = StructType(
    [
        StructField('start', IntegerType(), True),
        StructField('end', IntegerType(), True),
        StructField('tag', StringType(), True)
    ]
)

entity = StructType(
    [
        StructField('urls', ArrayType(url, True), True),
        StructField('mentions', ArrayType(mention, True), True),
        StructField('hashtags', ArrayType(tag, True), True),
        StructField('cashtags', ArrayType(tag, True), True)
    ]
)

public_metric = StructType(
    [
        StructField('retweet_count', IntegerType(), True),
        StructField('reply_count', IntegerType(), True),
        StructField('like_count', IntegerType(), True),
        StructField('quote_count', IntegerType(), True)
    ]
)

media_public_metric = StructType(
    [
        StructField('view_count', IntegerType(), True)
    ]
)

referenced_tweet = StructType(
    [
        StructField('type', StringType(), True),
        StructField('id', StringType(), True)
    ]
)

tweet = StructType(
    [
        StructField('id', StringType(), True),
        StructField('author_id', StringType(), True),
        StructField('created_at', StringType(), True),
        StructField('public_metrics', public_metric, True),
        StructField('reply_settings', StringType(), True),
        StructField('text', StringType(), True),
        StructField('conversation_id', StringType(), True),
        StructField('in_reply_to_user_id', StringType(), True),
        StructField('possibly_sensitive', BooleanType(), True),
        StructField('attachments', attachment, True),
        StructField('lang', StringType(), True),
        StructField('source', StringType(), True),
        StructField('entities', entity, True),
        StructField('referenced_tweets', ArrayType(referenced_tweet, True), True)
    ]
)

user = StructType(
    [
        StructField('id', StringType(), True),
        StructField('name', StringType(), True),
        StructField('username', StringType(), True),
        StructField('profile_image_url', StringType(), True),
        StructField('verified', BooleanType(), True)
    ]
)

media = StructType(
    [
        StructField('type', StringType(), True),
        StructField('media_key', StringType(), True),
        StructField('url', StringType(), True),
        StructField('preview_image_url', StringType(), True),
        StructField('public_metrics', media_public_metric, True)
    ]
)

place = StructType(
    [
        StructField('full_name', StringType(), True),
        StructField('id', StringType(), True),
        StructField('country', StringType(), True),
        StructField('country_code', StringType(), True),
        StructField('name', StringType(), True),
        StructField('place_type', StringType(), True)
    ]
)

coordinate = StructType(
    [
        StructField('type', StringType(), True),
        StructField('coordinates', ArrayType(IntegerType(), True), True)
    ]
)

geo = StructType(
    [
        StructField('coordinates', coordinate, True),
        StructField('place_id', StringType(), True)
    ]
)

data = StructType(
    [
        StructField('id', StringType(), True),
        StructField('author_id', StringType(), True),
        StructField('created_at', StringType(), True),
        StructField('public_metrics', public_metric, True),
        StructField('reply_settings', StringType(), True),
        StructField('text', StringType(), True),
        StructField('conversation_id', StringType(), True),
        StructField('possibly_sensitive', BooleanType(), True),
        StructField('attachments', attachment, True),
        StructField('lang', StringType(), True),
        StructField('source', StringType(), True),
        StructField('entities', entity, True),
        StructField('referenced_tweets', ArrayType(referenced_tweet, True), True),
        StructField('geo', geo, True)
    ]
)

includes = StructType(
    [
        StructField('tweets', ArrayType(tweet, True), True),
        StructField('users', ArrayType(user, True), True),
        StructField('media', ArrayType(media, True), True),
        StructField('places', ArrayType(place, True), True)
    ]
)

matching_rules = StructType(
    [
        StructField('id', StringType(), True),
        StructField('tag', StringType(), True)
    ]
)

tweet_data = StructType(
    [
        StructField('data', data, True),
        StructField('includes', includes, True),
        StructField('matching_rules', ArrayType(matching_rules, True), True)

    ]
)
