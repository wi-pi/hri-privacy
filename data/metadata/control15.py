from datetime import datetime, timedelta
from src.conversation import Information


speakers = {1: 'Anna', 2: 'Eliot', 3: 'Anna', 4: 'Eliot', 5: 'Anna', 6: 'Eliot', }
listeners = ['Anna', 'Eliot', ]
relationships = ['source', 'friend', ]
topics = []
sentiment_score = 0.10000000149011612
sentiment_magnitude = 3.200000047683716
sentiment_value = 'slightly_positive'
location = 'kitchen'
mean_label = 2.0657894736842106
control_level = 'low'
realistic_label = 4.947368421052632

timestamps = {
    1: datetime.utcnow() + timedelta(seconds=0),
    2: datetime.utcnow() + timedelta(seconds=5),
    3: datetime.utcnow() + timedelta(seconds=10),
    4: datetime.utcnow() + timedelta(seconds=15),
    5: datetime.utcnow() + timedelta(seconds=20),
    6: datetime.utcnow() + timedelta(seconds=25),
}

INFO = Information(speakers=speakers, listeners=listeners, topics=topics, timestamps=timestamps, location=location)
