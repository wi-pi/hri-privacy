from datetime import datetime, timedelta
from src.conversation import Information


speakers = {1: 'Jake', 2: 'Kathy', 3: 'Tony', 4: 'Jake', 5: 'Kathy', 6: 'Jake', 7: 'Kathy', 8: 'Jake', 9: 'Tony', }
listeners = ['Jake', 'Kathy', 'Tony', ]
relationships = ['source', 'mother', 'friend', ]
topics = []
sentiment_score = 0.30000001192092896
sentiment_magnitude = 5.699999809265137
sentiment_value = 'slightly_positive'
location = 'home'
mean_label = 2.216666666666667
control_level = 'low'
realistic_label = 5.133333333333334

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
}

INFO = Information(speakers=speakers, listeners=listeners, topics=topics, timestamps=timestamps, location=location)
