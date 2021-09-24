from datetime import datetime, timedelta
from src.conversation import Information


speakers = {1: 'Barbara', 2: 'Bill', 3: 'Jason', 4: 'Bill', 5: 'Jason', }
listeners = ['Barbara', 'Jason', ]
relationships = ['source', 'brother', ]
topics = []
sentiment_score = -0.20000000298023224
sentiment_magnitude = 3.200000047683716
sentiment_value = 'negative'
location = 'home'
mean_label = 3.75
control_level = 'high'
realistic_label = 4.8125

timestamps = {
    1: datetime.utcnow() + timedelta(seconds=0),
    2: datetime.utcnow() + timedelta(seconds=5),
    3: datetime.utcnow() + timedelta(seconds=10),
    4: datetime.utcnow() + timedelta(seconds=15),
    5: datetime.utcnow() + timedelta(seconds=20),
}

INFO = Information(speakers=speakers, listeners=listeners, topics=topics, timestamps=timestamps, location=location)
