from datetime import datetime, timedelta
from src.conversation import Information


speakers = {1: 'Frank', 2: 'Maureen', 3: 'Frank', 4: 'Maureen', 5: 'Frank', }
listeners = ['Frank', 'Maureen', ]
relationships = ['source', 'employee', ]
topics = []
sentiment_score = -0.10000000149011612
sentiment_magnitude = 3.5
sentiment_value = 'slightly_negative'
location = 'office'
mean_label = 1.9
control_level = 'low'
realistic_label = 4.666666666666667

timestamps = {
    1: datetime.utcnow() + timedelta(seconds=0),
    2: datetime.utcnow() + timedelta(seconds=5),
    3: datetime.utcnow() + timedelta(seconds=10),
    4: datetime.utcnow() + timedelta(seconds=15),
    5: datetime.utcnow() + timedelta(seconds=20),
}

INFO = Information(speakers=speakers, listeners=listeners, topics=topics, timestamps=timestamps, location=location)
