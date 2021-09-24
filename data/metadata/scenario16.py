from datetime import datetime, timedelta
from src.conversation import Information


speakers = {1: 'Kimmie', 2: 'Audrey', 3: 'Shaun', 4: 'Kimmie', 5: 'Shaun', 6: 'Kimmie', 7: 'Audrey', }
listeners = ['Audrey', 'Shaun', 'Kimmie', ]
relationships = ['source', 'brother', 'mother', ]
topics = []
sentiment_score = 0.0
sentiment_magnitude = 3.200000047683716
sentiment_value = 'neutral'
location = 'home'
mean_label = 3.833333333333333
control_level = 'high'
realistic_label = 4.111111111111111

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
