from datetime import datetime, timedelta
from src.conversation import Information


speakers = {1: 'Amy', 2: 'Sean', 3: 'Amy', 4: 'Sean', 5: 'Amy', 6: 'Sean', 7: 'Amy', 8: 'Sean', 9: 'Amy', 10: 'Sean', 11: 'Amy', 12: 'Sean', }
listeners = ['Sean', 'Amy', ]
relationships = ['source', 'acquaintance', ]
topics = ['Arts & Entertainment', ]
sentiment_score = -0.10000000149011612
sentiment_magnitude = 2.5999999046325684
sentiment_value = 'slightly_negative'
location = 'restaurant'
mean_label = 3.21875
control_level = 'moderate'
realistic_label = 4.25

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
    11: datetime.utcnow() + timedelta(seconds=50),
    12: datetime.utcnow() + timedelta(seconds=55),
}

INFO = Information(speakers=speakers, listeners=listeners, topics=topics, timestamps=timestamps, location=location)
