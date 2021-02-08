class attachment(object):
    def __init__(self, media_keys=None):
        self.media_keys = media_keys

    def __init__(self, new_attachment):
        self.media_keys = new_attachment.media_keys if new_attachment.media_keys else None


class url(object):
    def __init__(self, start, end, url, expanded_url, display_url, unwounded_url=None):
        self.start = start
        self.end = end
        self.url = url
        self.expanded_url = expanded_url
        self.display_url = display_url
        self.unwounded_url = unwounded_url

    def __init__(self, new_url):
        self.start = new_url.start
        self.end = new_url.end
        self.url = new_url.url
        self.expanded_url = new_url.expanded_url
        self.display_url = new_url.display_url
        self.unwounded_url = new_url.unwounded_url if new_url.unwounded_url else None


class mention(object):
    def __init__(self, start, end, username):
        self.start = start
        self.end = end
        self.username = username

    def __init__(self, new_mention):
        self.start = new_mention.start
        self.end = new_mention.end
        self.username = new_mention.username


class tag(object):
    def __init__(self, start, end, tag):
        self.start = start
        self.end = end
        self.tag = tag

    def __init__(self, new_tag):
        self.start = new_tag.start
        self.end = new_tag.end
        self.tag = new_tag.tag


class entity(object):
    def __init__(self, urls=None, mentions=None, hashtags=None, cashtags=None):
        self.urls = urls
        self.mentions = mentions
        self.hashtags = hashtags
        self.cashtags = cashtags

    def __init__(self, new_entity):
        self.urls = new_entity.urls if new_entity.urls else None
        self.mentions = new_entity.mentions if new_entity.mentions else None
        self.hashtags = new_entity.hashtags if new_entity.hashtags else None
        self.cashtags = new_entity.cashtags if new_entity.cashtags else None


class public_metric(object):
    def __init__(self, retweet_count=0, reply_count=0, like_count=0, quote_count=0):
        self.retweet_count = retweet_count
        self.reply_count = reply_count
        self.like_count = like_count
        self.quote_count = quote_count

    def __init__(self, new_tuple):
        self.retweet_count = new_tuple.retweet_count
        self.reply_count = new_tuple.reply_count
        self.like_count = new_tuple.like_count
        self.quote_count = new_tuple.quote_count

    def sum(self):
        return self.retweet_count+self.reply_count+self.like_count+self.quote_count


class referenced_tweet(object):
    def __init__(self, type, id):
        self.type = type
        self.id = id

    def __init__(self, new_referenced_tweet):
        self.type = new_referenced_tweet.type
        self.id = new_referenced_tweet.id


class tweet(object):
    def __init__(self, id, author_id, public_metrics, created_at, reply_settings=None, message=None, conversation_id=0, possibily_sensitive=False, attachments=None, source=None, lang=None, in_reply_to_user_id=None, place_id=None, entities=None, referenced_tweets=None):
        self.id = id
        self.author_id = author_id
        self.public_metrics = public_metrics
        self.created_at = created_at
        self.reply_settings = reply_settings
        self.message = message
        self.conversation_id = conversation_id
        self.possibly_sensitive = possibily_sensitive
        self.attachments = attachments
        self.source = source
        self.lang = lang
        self.in_reply_to_user_id = in_reply_to_user_id
        self.place_id = place_id
        self.entities = entities
        self.referenced_tweets = referenced_tweets

    def __int__(self, new_tweet):
        self.id = new_tweet.id
        self.author_id = new_tweet.author_id
        self.public_metrics = new_tweet.public_metrics
        self.created_at = new_tweet.created_at
        self.reply_settings = new_tweet.reply_settings if new_tweet.reply_settings else None
        self.message = new_tweet.message if new_tweet.message else None
        self.conversation_id = new_tweet.conversation_id if new_tweet.conversation_id else 0
        self.possibly_sensitive = new_tweet.possibily_sensitive if new_tweet.possibily_sensitive else False
        self.attachments = new_tweet.attachments if new_tweet.attachments else None
        self.source = new_tweet.source if new_tweet.source else None
        self.lang = new_tweet.lang if new_tweet.lang else None
        self.in_reply_to_user_id = new_tweet.in_reply_to_user_id if new_tweet.in_reply_to_user_id else None
        self.place_id = new_tweet.place_id if new_tweet.place_id else None
        self.entities = new_tweet.entities if new_tweet.entities else None
        self.referenced_tweets = new_tweet.referenced_tweets if new_tweet.referenced_tweets else None


class user(object):
    def __init__(self, id, name, username, profile_image_url=None, verified=False):
        self.id = id
        self.name = name
        self.username = username
        self.profile_image_url = profile_image_url
        self.verified = verified

    def __init__(self, new_user):
        self.id = new_user.id
        self.name = new_user.name
        self.username = new_user.username
        self.profile_image_url = new_user.profile_image_url if new_user.profile_image_url else None
        self.verified = new_user.verified if new_user.verified else False


class media(object):
    def __init__(self, type, media_key, url, preview_image_url=None, view_count=0):
        self.type = type
        self.media_key = media_key
        self.url = url
        self.preview_image_url = preview_image_url
        self.view_count = view_count

    def __init__(self, new_media):
        self.type = new_media.type
        self.media_key = new_media.media_key
        self.url = new_media.url
        self.preview_image_url = new_media.preview_image_url if new_media.preview_image_url else None
        self.view_count = new_media.view_count if new_media.view_count else 0


class place(object):
    def __init__(self, full_name, id, country=None, country_code=None, name=None, place_type=None):
        self.full_name = full_name
        self.id = id
        self.country = country
        self.country_code = country_code
        self.name = name
        self.place_type = place_type

    def __init__(self, new_place):
        self.full_name = new_place.full_name
        self.id = new_place.id
        self.country = new_place.country if new_place.country else None
        self.country_code = new_place.country_code if new_place.country_code else None
        self.name = new_place.name if new_place.name else None
        self.place_type = new_place.place_type if new_place.place_type else None


class include(object):
    def __init__(self, tweets=None, users=None, media=None, places=None):
        self.tweets = tweets
        self.users = users
        self.media = media
        self.places = places

    def __init__(self, new_includes):
        self.tweets = new_includes.tweets if new_includes.tweets else None
        self.users = new_includes.users if new_includes.users else None
        self.media = new_includes.media if new_includes.media else None
        self.places = new_includes.places if new_includes.places else None