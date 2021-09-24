from datetime import datetime, timedelta
from src.conversation import Information


speakers = {1: 'Roy', 2: 'Peter', 3: 'Roy', 4: 'Peter', 5: 'Roy', 6: 'Peter', 7: 'Roy', 8: 'Peter', }
listeners = ['Roy', 'Peter', ]
relationships = ['source', 'manager', ]
topics = ['Home & Garden', ]
sentiment_score = 0.0
sentiment_magnitude = 3.299999952316284
sentiment_value = 'neutral'
location = 'office'
mean_label = 2.359375
control_level = 'low'
realistic_label = 4.9375

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
