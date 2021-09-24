from datetime import datetime, timedelta
from src.conversation import Information


speakers = {1: 'Paul', 2: 'Jacob', 3: 'Paul', 4: 'Jacob', 5: 'Paul', 6: 'Jacob', 7: 'Paul', }
listeners = ['Paul', 'Jacob', ]
relationships = ['source', 'brother', ]
topics = ['Autos & Vehicles', ]
sentiment_score = -0.20000000298023224
sentiment_magnitude = 6.800000190734863
sentiment_value = 'negative'
location = 'car shop'
mean_label = 3.083333333333334
control_level = 'moderate'
realistic_label = 4.666666666666667

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
