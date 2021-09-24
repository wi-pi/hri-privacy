from datetime import datetime, timedelta
from src.conversation import Information


speakers = {1: 'Dr. Murphy', 2: 'Andy', 3: 'Dr. Murphy', 4: 'Andy', 5: 'Dr. Murphy', 6: 'Dr. Murphy', 7: 'Evan', }
listeners = ['Andy', 'Dr. Murphy', ]
relationships = ['source', 'doctor', ]
topics = ['Health', ]
sentiment_score = 0.10000000149011612
sentiment_magnitude = 5.199999809265137
sentiment_value = 'slightly_positive'
location = 'office'
mean_label = 4.233333333333333
control_level = 'high'
realistic_label = 5.0

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
