from datetime import datetime, timedelta
from src.conversation import Information


speakers = {1: 'Ira', 2: 'Bob', 3: 'Ira', 4: 'Elizabeth', 5: 'Ira', 6: 'Bob', }
listeners = ['Ira', 'Bob', 'Elizabeth', ]
relationships = ['source', 'father', 'mother', ]
topics = []
sentiment_score = -0.5
sentiment_magnitude = 7.699999809265137
sentiment_value = 'negative'
location = 'dining room'
mean_label = 3.0
control_level = 'moderate'
realistic_label = 4.230769230769231

timestamps = {
    1: datetime.utcnow() + timedelta(seconds=0),
    2: datetime.utcnow() + timedelta(seconds=5),
    3: datetime.utcnow() + timedelta(seconds=10),
    4: datetime.utcnow() + timedelta(seconds=15),
    5: datetime.utcnow() + timedelta(seconds=20),
    6: datetime.utcnow() + timedelta(seconds=25),
}

INFO = Information(speakers=speakers, listeners=listeners, topics=topics, timestamps=timestamps, location=location)
