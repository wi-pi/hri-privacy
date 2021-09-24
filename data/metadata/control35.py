from datetime import datetime, timedelta
from src.conversation import Information


speakers = {1: 'Timmy', 2: 'Lambeau', 3: 'Sean', 4: 'Sean', 5: 'Timmy', 6: 'Sean', 7: 'Lambeau', 8: 'Sean', 9: 'Timmy', }
listeners = ['Sean', 'Timmy', 'Lambeau', ]
relationships = ['source', 'friend', 'friend', ]
topics = ['Online Communities', ]
sentiment_score = 0.10000000149011612
sentiment_magnitude = 4.199999809265137
sentiment_value = 'slightly_positive'
location = 'restaurant'
mean_label = 2.8166666666666664
control_level = 'low'
realistic_label = 4.666666666666667

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
