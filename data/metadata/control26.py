from datetime import datetime, timedelta
from src.conversation import Information


speakers = {1: 'Brian', 2: 'Roger', 3: 'Brian', 4: 'Roger', 5: 'Brian', 6: 'Roger', 7: 'Kathy', 8: 'Roger', }
listeners = ['Roger', 'Brian', 'Kathy', ]
relationships = ['source', 'friend', 'sister', ]
topics = ['Arts & Entertainment', ]
sentiment_score = 0.0
sentiment_magnitude = 3.0
sentiment_value = 'neutral'
location = 'living room'
mean_label = 2.75
control_level = 'low'
realistic_label = 4.764705882352941

timestamps = {
    1: datetime.utcnow() + timedelta(seconds=0),
    2: datetime.utcnow() + timedelta(seconds=5),
    3: datetime.utcnow() + timedelta(seconds=10),
    4: datetime.utcnow() + timedelta(seconds=15),
    5: datetime.utcnow() + timedelta(seconds=20),
    6: datetime.utcnow() + timedelta(seconds=25),
    7: datetime.utcnow() + timedelta(seconds=30),
    8: datetime.utcnow() + timedelta(seconds=35),
}

INFO = Information(speakers=speakers, listeners=listeners, topics=topics, timestamps=timestamps, location=location)
