from datetime import datetime, timedelta
from src.conversation import Information


speakers = {1: 'Dana', 2: 'Walter', 3: 'Jill', 4: 'Walter', 5: 'Dana', 6: 'Walter', 7: 'Jill', 8: 'Walter', }
listeners = ['Dana', 'Walter', 'Jill', ]
relationships = ['source', 'coworker', 'coworker', ]
topics = ['Arts & Entertainment', ]
sentiment_score = 0.0
sentiment_magnitude = 4.099999904632568
sentiment_value = 'neutral'
location = 'office'
mean_label = 2.765625
control_level = 'low'
realistic_label = 4.875

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
