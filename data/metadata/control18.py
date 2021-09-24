from datetime import datetime, timedelta
from src.conversation import Information


speakers = {1: 'Pamela', 2: 'Doug', 3: 'Pamela', 4: 'Doug', 5: 'Pamela', 6: 'Doug', 7: 'Pamela', }
listeners = ['Pamela', 'Doug', ]
relationships = ['source', 'friend', ]
topics = []
sentiment_score = -0.10000000149011612
sentiment_magnitude = 3.299999952316284
sentiment_value = 'slightly_negative'
location = 'apartment lobby'
mean_label = 2.892857142857143
control_level = 'low'
realistic_label = 4.5

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
