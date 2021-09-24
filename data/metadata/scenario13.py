from datetime import datetime, timedelta
from src.conversation import Information


speakers = {1: 'Welles', 2: 'Amy', 3: 'Amy', 4: 'Welles', 5: 'Amy', 6: 'John', 7: 'Welles', }
listeners = ['Welles', 'Amy', 'John', ]
relationships = ['source', 'mother', 'friend', ]
topics = ['Hobbies & Leisure', 'Shopping', 'Arts & Entertainment', ]
sentiment_score = 0.4000000059604645
sentiment_magnitude = 7.599999904632568
sentiment_value = 'slightly_positive'
location = 'home birthday party'
mean_label = 3.71875
control_level = 'high'
realistic_label = 4.8125

timestamps = {
    1: datetime.utcnow() + timedelta(seconds=0),
    2: datetime.utcnow() + timedelta(seconds=5),
    3: datetime.utcnow() + timedelta(seconds=10),
    4: datetime.utcnow() + timedelta(seconds=15),
    5: datetime.utcnow() + timedelta(seconds=20),
    6: datetime.utcnow() + timedelta(seconds=25),
    7: datetime.utcnow() + timedelta(seconds=30),
}

INFO = Information(speakers=speakers, listeners=listeners, topics=topics, timestamps=timestamps, location=location)
