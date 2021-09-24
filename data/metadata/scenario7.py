from datetime import datetime, timedelta
from src.conversation import Information


speakers = {1: 'Autumn', 2: 'Moe', 3: 'Terry', 4: 'Autumn', 5: 'Terry', 6: 'Autumn', 7: 'Rudy', 8: 'Terry', 9: 'Rudy', 10: 'Terry', }
listeners = ['Terry', 'Autumn', 'Moe', ]
relationships = ['source', 'mother', 'father', ]
topics = ['Finance', 'Business & Industrial', ]
sentiment_score = 0.0
sentiment_magnitude = 7.400000095367432
sentiment_value = 'neutral'
location = 'living room'
mean_label = 3.3214285714285716
control_level = 'moderate'
realistic_label = 4.857142857142857

timestamps = {
    1: datetime.utcnow() + timedelta(seconds=0),
    2: datetime.utcnow() + timedelta(seconds=5),
    3: datetime.utcnow() + timedelta(seconds=10),
    4: datetime.utcnow() + timedelta(seconds=15),
    5: datetime.utcnow() + timedelta(seconds=20),
    6: datetime.utcnow() + timedelta(seconds=25),
    7: datetime.utcnow() + timedelta(seconds=30),
    8: datetime.utcnow() + timedelta(seconds=35),
    9: datetime.utcnow() + timedelta(seconds=40),
    10: datetime.utcnow() + timedelta(seconds=45),
}

INFO = Information(speakers=speakers, listeners=listeners, topics=topics, timestamps=timestamps, location=location)
