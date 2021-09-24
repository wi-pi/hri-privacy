from datetime import datetime, timedelta
from src.conversation import Information


speakers = {1: 'Andrew', 2: 'Clarence', 3: 'Andrew', 4: 'Clarence', }
listeners = ['Andrew', 'Clarence', ]
relationships = ['source', 'father', ]
topics = []
sentiment_score = -0.4000000059604645
sentiment_magnitude = 3.5
sentiment_value = 'negative'
location = 'kitchen'
mean_label = 3.578125
control_level = 'high'
realistic_label = 4.9375

timestamps = {
    1: datetime.utcnow() + timedelta(seconds=0),
    2: datetime.utcnow() + timedelta(seconds=5),
    3: datetime.utcnow() + timedelta(seconds=10),
    4: datetime.utcnow() + timedelta(seconds=15),
}

INFO = Information(speakers=speakers, listeners=listeners, topics=topics, timestamps=timestamps, location=location)
