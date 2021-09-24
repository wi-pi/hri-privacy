from datetime import datetime, timedelta
from src.conversation import Information


speakers = {1: 'George', 2: 'Mary', 3: 'George', 4: 'Mary', 5: 'George', 6: 'Mary', }
listeners = ['George', 'Mary', ]
relationships = ['source', 'friend', ]
topics = ['Arts & Entertainment', ]
sentiment_score = -0.10000000149011612
sentiment_magnitude = 1.7999999523162842
sentiment_value = 'neutral'
location = 'bar'
mean_label = 3.0277777777777777
control_level = 'moderate'
realistic_label = 4.888888888888889

timestamps = {
    1: datetime.utcnow() + timedelta(seconds=0),
    2: datetime.utcnow() + timedelta(seconds=5),
    3: datetime.utcnow() + timedelta(seconds=10),
    4: datetime.utcnow() + timedelta(seconds=15),
    5: datetime.utcnow() + timedelta(seconds=20),
    6: datetime.utcnow() + timedelta(seconds=25),
}

INFO = Information(speakers=speakers, listeners=listeners, topics=topics, timestamps=timestamps, location=location)
