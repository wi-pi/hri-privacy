from datetime import datetime, timedelta
from src.conversation import Information


speakers = {1: 'Ramon', 2: 'Kate', 3: 'Hillary', 4: 'Kate', 5: 'Ramon', 6: 'Kate', 7: 'Angela', }
listeners = ['Kate', 'Ramon', 'Hillary', 'Angela', ]
relationships = ['source', 'friend', 'friend', 'friend', ]
topics = ['Arts & Entertainment', ]
sentiment_score = -0.10000000149011612
sentiment_magnitude = 1.399999976158142
sentiment_value = 'neutral'
location = 'living room'
mean_label = 2.703125
control_level = 'low'
realistic_label = 4.6875

timestamps = {
    1: datetime.utcnow() + timedelta(seconds=0),
    2: datetime.utcnow() + timedelta(seconds=5),
    3: datetime.utcnow() + timedelta(seconds=10),
    4: datetime.utcnow() + timedelta(seconds=15),
    5: datetime.utcnow() + timedelta(seconds=20),
    6: datetime.utcnow() + timedelta(seconds=25),
    7: datetime.utcnow() + timedelta(seconds=30),
}

INFO = Information(speakers=speakers, listeners=listeners, topics=topics, timestamps=timestamps, location=location)
