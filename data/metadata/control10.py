from datetime import datetime, timedelta
from src.conversation import Information


speakers = {1: 'Samantha', 2: 'Theodore', 3: 'Samantha', 4: 'Theodore', }
listeners = ['Theodore', 'Samantha', ]
relationships = ['source', 'assistant', ]
topics = []
sentiment_score = 0.10000000149011612
sentiment_magnitude = 1.100000023841858
sentiment_value = 'neutral'
location = 'office'
mean_label = 2.6730769230769234
control_level = 'low'
realistic_label = 4.923076923076923

timestamps = {
    1: datetime.utcnow() + timedelta(seconds=0),
    2: datetime.utcnow() + timedelta(seconds=5),
    3: datetime.utcnow() + timedelta(seconds=10),
    4: datetime.utcnow() + timedelta(seconds=15),
}

INFO = Information(speakers=speakers, listeners=listeners, topics=topics, timestamps=timestamps, location=location)
