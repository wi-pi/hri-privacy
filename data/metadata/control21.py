from datetime import datetime, timedelta
from src.conversation import Information


speakers = {1: 'Parrish', 2: 'Joe', 3: 'Joe', 4: 'Parrish', 5: 'Joe', 6: 'Parrish', }
listeners = ['Joe', 'Parrish', ]
relationships = ['source', 'grandson', ]
topics = ['Food & Drink', ]
sentiment_score = 0.10000000149011612
sentiment_magnitude = 3.299999952316284
sentiment_value = 'slightly_positive'
location = 'dining room'
mean_label = 2.041666666666667
control_level = 'low'
realistic_label = 5.0

timestamps = {
    1: datetime.utcnow() + timedelta(seconds=0),
    2: datetime.utcnow() + timedelta(seconds=5),
    3: datetime.utcnow() + timedelta(seconds=10),
    4: datetime.utcnow() + timedelta(seconds=15),
    5: datetime.utcnow() + timedelta(seconds=20),
    6: datetime.utcnow() + timedelta(seconds=25),
}

INFO = Information(speakers=speakers, listeners=listeners, topics=topics, timestamps=timestamps, location=location)
