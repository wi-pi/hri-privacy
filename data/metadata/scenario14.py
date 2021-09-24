from datetime import datetime, timedelta
from src.conversation import Information


speakers = {1: 'Ross', 2: 'Ike', 3: 'Ross', 4: 'Ike', 5: 'Ross', 6: 'Ike', 7: 'Ross', 8: 'Janey', 9: 'Ross', }
listeners = ['Ross', 'Ike', ]
relationships = ['source', 'neighbor', ]
topics = ['Arts & Entertainment', ]
sentiment_score = -0.30000001192092896
sentiment_magnitude = 5.300000190734863
sentiment_value = 'negative'
location = 'front yard'
mean_label = 4.044117647058823
control_level = 'high'
realistic_label = 5.235294117647059

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
