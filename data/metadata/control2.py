from datetime import datetime, timedelta
from src.conversation import Information


speakers = {1: 'Louise', 2: 'Carrie', 3: 'Louise', 4: 'Carrie', 5: 'Louise', 6: 'Carrie', }
listeners = ['Louise', 'Carrie', ]
relationships = ['source', 'friend', ]
topics = ['Shopping', ]
sentiment_score = 0.0
sentiment_magnitude = 3.0999999046325684
sentiment_value = 'neutral'
location = 'house'
mean_label = 2.357142857142857
control_level = 'low'
realistic_label = 3.7857142857142856

timestamps = {
    1: datetime.utcnow() + timedelta(seconds=0),
    2: datetime.utcnow() + timedelta(seconds=5),
    3: datetime.utcnow() + timedelta(seconds=10),
    4: datetime.utcnow() + timedelta(seconds=15),
    5: datetime.utcnow() + timedelta(seconds=20),
    6: datetime.utcnow() + timedelta(seconds=25),
}

INFO = Information(speakers=speakers, listeners=listeners, topics=topics, timestamps=timestamps, location=location)
