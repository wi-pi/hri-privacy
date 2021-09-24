from datetime import datetime, timedelta
from src.conversation import Information


speakers = {1: 'Theodore', 2: 'Amy', 3: 'Theodore', 4: 'Charles', 5: 'Theodore', 6: 'Amy', }
listeners = ['Amy', 'Theodore', 'Charles', ]
relationships = ['source', 'friend', 'friend', ]
topics = ['Arts & Entertainment', ]
sentiment_score = 0.0
sentiment_magnitude = 2.9000000953674316
sentiment_value = 'neutral'
location = 'university dorm'
mean_label = 2.3653846153846154
control_level = 'low'
realistic_label = 4.923076923076923

timestamps = {
    1: datetime.utcnow() + timedelta(seconds=0),
    2: datetime.utcnow() + timedelta(seconds=5),
    3: datetime.utcnow() + timedelta(seconds=10),
    4: datetime.utcnow() + timedelta(seconds=15),
    5: datetime.utcnow() + timedelta(seconds=20),
    6: datetime.utcnow() + timedelta(seconds=25),
}

INFO = Information(speakers=speakers, listeners=listeners, topics=topics, timestamps=timestamps, location=location)
