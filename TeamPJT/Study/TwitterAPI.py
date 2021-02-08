twitter_consumer_key = "MDChL61g110GGIbAqyjNit1mo"
    # "n5pDd7b90YFdi7ROEabtVZxA8"  # API key

twitter_consumer_secret = (
    # "uTBQRPTsKC7Dcio7cLKsSkFQZsviWqPXlDS4FjsDegXRA0P5qQ"  # API key secret
    "lXAcHECKZY0iwPtcccZN8NqIYuWNZMRThlngRL3gQgzCRSLN1d"
)
twitter_access_token = (
    # "1339093534704472066-HMxOxLviot8hdQblaw3RkKWAAeQhwZ"  # Access token
    "1341561265701810176-bG0DR18Nir0c9ly4iRAu5ekQ5Gz6us"
)
twitter_access_secret = (
    # "WvePkPNaipoTHcXF6mg0e9h1qyQfKtrryQKe8Nx7edeVH"  # Access token secret
    "LwayE0sdz1EpaKEw1feBIIqJ1udBMdp2PkG6aLOrQLbOy"
)

import twitter
import json
from kafka import KafkaProducer
import time

twitter_api = twitter.Api(
    consumer_key=twitter_consumer_key,
    consumer_secret=twitter_consumer_secret,
    access_token_key=twitter_access_token,
    access_token_secret=twitter_access_secret,
)

# 키워드랑 트윗 작성한 유저아이디, 트윗메세지, 작성시간, 리트윗수, 좋아요수, 인용트윗수, 위치(가능하면)


"""
Kafka Producer Option
 - bootstrap_servers(default=9092): 브로커(host:port)를 리스트로 나열, 노드 전부를 쓸 필요는 없음
 - acks(default=1): 0, 서버로부터 어떠한 ack도 기다리지 않음. 처리량 증가하지만 유실율도 증가
                    1, 리더의 기록을 확인 후 ack 받음. 모든 팔로워에 대해서 확인하지는 않음
                    'all', 모든 ISR(리더의 모든 팔로워)의 기록을 확인 후 ack 받음. 무손실 보장
 - compression_type(default=None): 데이터를 압축하여 보낼 포멧 (‘gzip’, ‘snappy’, ‘lz4’, or None)
 - value_serializer(default=None): 유저가 보내려는 msg를 byte의 형태로 변환할 함수(callable). 여기서는 변환 후 인코딩
"""
producer = KafkaProducer(
    bootstrap_servers=["localhost:9092"],
    acks=0,
    compression_type="gzip",
    value_serializer=lambda x: json.dumps(x).encode("utf-8"),
    # value_serializer=lambda x: json.dumps(x),
    batch_size=10000,
)
topicName = "test"

query = ["마스크"]
output_file_name = "stream_result.txt"
# with open(output_file_name, "w", encoding="utf-8") as output_file:
stream = twitter_api.GetStreamFilter(track=query)
while True:
    for tweets in stream:
        # print(tweets)
        tweet = json.dumps(tweets, ensure_ascii=False)
        # print(tweet)
        text = tweets["text"]
        date = tweets["created_at"]
        data = "\n[" + date + "]\n" + text
        data = tweet
        # print(data, file=output_file, flush=True)
        producer.send(topicName, value=tweet)
        producer.flush()
        print(tweet)