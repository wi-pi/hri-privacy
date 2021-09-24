from datetime import datetime, timedelta
from src.conversation import Information


speakers = {1: 'Paul', 2: 'Jules', 3: 'Paul', 4: 'Jules', 5: 'Jules', 6: 'Paul', }
listeners = ['Jules', 'Paul', ]
relationships = ['source', 'roommate', ]
topics = ['Business & Industrial', ]
sentiment_score = 0.0
sentiment_magnitude = 2.799999952316284
sentiment_value = 'neutral'
location = 'apartment'
mean_label = 2.75
control_level = 'low'
realistic_label = 4.9375

timestamps = {
    1: datetime.utcnow() + timedelta(seconds=0),
    2: datetime.utcnow() + timedelta(seconds=5),
    3: datetime.utcnow() + timedelta(seconds=10),
    4: datetime.utcnow() + timedelta(seconds=15),
    5: datetime.utcnow() + timedelta(seconds=20),
    6: datetime.utcnow() + timedelta(seconds=25),
}

INFO = Information(speakers=speakers, listeners=listeners, topics=topics, timestamps=timestamps, location=location)
