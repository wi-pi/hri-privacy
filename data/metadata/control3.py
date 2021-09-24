from datetime import datetime, timedelta
from src.conversation import Information


speakers = {1: 'Morino', 2: 'Gillis', 3: 'Morino', 4: 'Gillis', 5: 'Morino', }
listeners = ['Morino', 'Gillis', ]
relationships = ['source', 'friend', ]
topics = []
sentiment_score = -0.20000000298023224
sentiment_magnitude = 3.9000000953674316
sentiment_value = 'negative'
location = 'production studio'
mean_label = 4.05
control_level = 'high'
realistic_label = 4.133333333333334

timestamps = {
    1: datetime.utcnow() + timedelta(seconds=0),
    2: datetime.utcnow() + timedelta(seconds=5),
    3: datetime.utcnow() + timedelta(seconds=10),
    4: datetime.utcnow() + timedelta(seconds=15),
    5: datetime.utcnow() + timedelta(seconds=20),
}

INFO = Information(speakers=speakers, listeners=listeners, topics=topics, timestamps=timestamps, location=location)
