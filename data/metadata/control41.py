from datetime import datetime, timedelta
from src.conversation import Information


speakers = {1: 'Laura', 2: 'Sebastian', 3: 'Laura', 4: 'Sebastian', 5: 'Laura', 6: 'Sebastian', 7: 'Laura', 8: 'Sebastian', }
listeners = ['Laura', 'Sebastian', ]
relationships = ['source', 'friend', ]
topics = []
sentiment_score = 0.10000000149011612
sentiment_magnitude = 4.900000095367432
sentiment_value = 'slightly_positive'
location = 'apartment'
mean_label = 2.375
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
    8: datetime.utcnow() + timedelta(seconds=35),
}

INFO = Information(speakers=speakers, listeners=listeners, topics=topics, timestamps=timestamps, location=location)
