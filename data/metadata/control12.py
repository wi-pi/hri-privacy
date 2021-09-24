from datetime import datetime, timedelta
from src.conversation import Information


speakers = {1: 'Wade', 2: 'Sueleen', 3: 'Wade', 4: 'Sueleen', 5: 'Wade', 6: 'Sueleen', }
listeners = ['Wade', 'Sueleen', ]
relationships = ['source', 'friend', ]
topics = ['Arts & Entertainment', ]
sentiment_score = 0.0
sentiment_magnitude = 3.700000047683716
sentiment_value = 'neutral'
location = 'school choir room'
mean_label = 2.0625
control_level = 'low'
realistic_label = 4.875

timestamps = {
    1: datetime.utcnow() + timedelta(seconds=0),
    2: datetime.utcnow() + timedelta(seconds=5),
    3: datetime.utcnow() + timedelta(seconds=10),
    4: datetime.utcnow() + timedelta(seconds=15),
    5: datetime.utcnow() + timedelta(seconds=20),
    6: datetime.utcnow() + timedelta(seconds=25),
}

INFO = Information(speakers=speakers, listeners=listeners, topics=topics, timestamps=timestamps, location=location)
