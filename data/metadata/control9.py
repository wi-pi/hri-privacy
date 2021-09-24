from datetime import datetime, timedelta
from src.conversation import Information


speakers = {1: 'Paul', 2: 'Donna', 3: 'Paul', 4: 'Donna', 5: 'Paul', 6: 'Donna', }
listeners = ['Paul', 'Donna', ]
relationships = ['source', 'friend', ]
topics = []
sentiment_score = -0.20000000298023224
sentiment_magnitude = 3.0
sentiment_value = 'negative'
location = 'house'
mean_label = 2.9791666666666665
control_level = 'low'
realistic_label = 4.583333333333333

timestamps = {
    1: datetime.utcnow() + timedelta(seconds=0),
    2: datetime.utcnow() + timedelta(seconds=5),
    3: datetime.utcnow() + timedelta(seconds=10),
    4: datetime.utcnow() + timedelta(seconds=15),
    5: datetime.utcnow() + timedelta(seconds=20),
    6: datetime.utcnow() + timedelta(seconds=25),
}

INFO = Information(speakers=speakers, listeners=listeners, topics=topics, timestamps=timestamps, location=location)
