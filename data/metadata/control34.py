from datetime import datetime, timedelta
from src.conversation import Information


speakers = {1: 'Rebecca', 2: 'Marc', 3: 'Rebecca', 4: 'Marc', 5: 'Rebecca', }
listeners = ['Rebecca', 'Marc', ]
relationships = ['source', 'friend', ]
topics = []
sentiment_score = 0.20000000298023224
sentiment_magnitude = 1.5
sentiment_value = 'slightly_positive'
location = 'apartment'
mean_label = 2.514705882352941
control_level = 'low'
realistic_label = 4.705882352941177

timestamps = {
    1: datetime.utcnow() + timedelta(seconds=0),
    2: datetime.utcnow() + timedelta(seconds=5),
    3: datetime.utcnow() + timedelta(seconds=10),
    4: datetime.utcnow() + timedelta(seconds=15),
    5: datetime.utcnow() + timedelta(seconds=20),
}

INFO = Information(speakers=speakers, listeners=listeners, topics=topics, timestamps=timestamps, location=location)
