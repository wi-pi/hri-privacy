from datetime import datetime, timedelta
from src.conversation import Information


speakers = {1: 'Hellen', 2: 'David', 3: 'Hellen', 4: 'Hellen', 5: 'Alex', 6: 'Hellen', 7: 'Alex', 8: 'Hellen', 9: 'Alex', 10: 'David', }
listeners = ['Hellen', 'David', ]
relationships = ['grandmother', 'father', ]
topics = []
sentiment_score = 0.30000001192092896
sentiment_magnitude = 9.0
sentiment_value = 'slightly_positive'
location = 'school graduation event'
mean_label = 4.232142857142857
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
    8: datetime.utcnow() + timedelta(seconds=35),
    9: datetime.utcnow() + timedelta(seconds=40),
    10: datetime.utcnow() + timedelta(seconds=45),
}

INFO = Information(speakers=speakers, listeners=listeners, topics=topics, timestamps=timestamps, location=location)
