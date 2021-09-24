from datetime import datetime, timedelta
from src.conversation import Information


speakers = {1: 'Lavern', 2: 'Misty', 3: 'Lavern', 4: 'Misty', 5: 'Lavern', 6: 'Josh', 7: 'Ericka', }
listeners = ['Lavern', 'Dennis', 'Misty', 'Ericka', ]
relationships = ['source', 'spouse', 'daughter', 'family friend', ]
topics = []
sentiment_score = -0.20000000298023224
sentiment_magnitude = 4.900000095367432
sentiment_value = 'negative'
location = 'dining room'
mean_label = 3.9642857142857144
control_level = 'high'
realistic_label = 5.214285714285714

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
