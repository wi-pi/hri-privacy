from datetime import datetime, timedelta
from src.conversation import Information


speakers = {1: 'Larry', 2: 'Paul', 3: 'Larry', 4: 'Paul', 5: 'Joni', }
listeners = ['Larry', 'Paul', 'Joni', ]
relationships = ['source', 'friend', 'sister', ]
topics = []
sentiment_score = 0.10000000149011612
sentiment_magnitude = 4.800000190734863
sentiment_value = 'slightly_positive'
location = 'garage'
mean_label = 2.4411764705882355
control_level = 'low'
realistic_label = 4.764705882352941

timestamps = {
    1: datetime.utcnow() + timedelta(seconds=0),
    2: datetime.utcnow() + timedelta(seconds=5),
    3: datetime.utcnow() + timedelta(seconds=10),
    4: datetime.utcnow() + timedelta(seconds=15),
    5: datetime.utcnow() + timedelta(seconds=20),
}

INFO = Information(speakers=speakers, listeners=listeners, topics=topics, timestamps=timestamps, location=location)
