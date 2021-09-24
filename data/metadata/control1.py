from datetime import datetime, timedelta
from src.conversation import Information


speakers = {1: 'Kathryn', 2: 'Cecile', 3: 'Kathryn', 4: 'Cecile', 5: 'Kathryn', 6: 'Cecile', 7: 'Kathryn', 8: 'Cecile', }
listeners = ['Cecile', 'Kathryn', ]
relationships = ['source', 'friend', ]
topics = ['People & Society', ]
sentiment_score = 0.0
sentiment_magnitude = 4.599999904632568
sentiment_value = 'neutral'
location = 'apartment'
mean_label = 3.8000000000000003
control_level = 'high'
realistic_label = 4.4

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
