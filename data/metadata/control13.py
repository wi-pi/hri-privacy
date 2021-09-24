from datetime import datetime, timedelta
from src.conversation import Information


speakers = {1: 'Terry', 2: 'Dante', 3: 'Terry', 4: 'Dante', 5: 'Terry', }
listeners = ['Dante', 'Terry', ]
relationships = ['source', 'trainer', ]
topics = ['Beauty & Fitness', ]
sentiment_score = -0.20000000298023224
sentiment_magnitude = 4.199999809265137
sentiment_value = 'negative'
location = 'gym'
mean_label = 3.109375
control_level = 'moderate'
realistic_label = 4.625

timestamps = {
    1: datetime.utcnow() + timedelta(seconds=0),
    2: datetime.utcnow() + timedelta(seconds=5),
    3: datetime.utcnow() + timedelta(seconds=10),
    4: datetime.utcnow() + timedelta(seconds=15),
    5: datetime.utcnow() + timedelta(seconds=20),
}

INFO = Information(speakers=speakers, listeners=listeners, topics=topics, timestamps=timestamps, location=location)
