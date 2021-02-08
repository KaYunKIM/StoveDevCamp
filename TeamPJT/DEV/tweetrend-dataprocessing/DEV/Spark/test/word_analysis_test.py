import senti_word

from collections import Counter
from konlpy.tag import Okt

## count related words
okt = Okt()

tweet_message = '[속보] 정은경 코로나 전담병원 정은경 의료진부터 2월 중 접종 시작 https://twitter.com/JTBC_news/status/1354659426787987463/photo/1'
tweet_word = okt.nouns(tweet_message)
result = dict(Counter(list(tweet_word)))
print(type(result), result)
new_result = sorted(result.items(), key=lambda x: x[1], reverse=True)
print(new_result)

# for j in tweet_word:
#     senti_word.text_analysis(j)