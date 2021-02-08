from konlpy.tag import Okt, Kkma

okt = Okt()   ##  단어 개별 분석
kkma = Kkma()   ## 단어 중복 분석

tweet_message = '[속보] 정은경 코로나 전담병원 의료진부터 2월 중 접종 시작 https://twitter.com/JTBC_news/status/1354659426787987463/photo/1'
tweet_okt = okt.nouns(tweet_message)
tweet_kkma = kkma.nouns(tweet_message)
print(tweet_okt)
print(tweet_kkma)