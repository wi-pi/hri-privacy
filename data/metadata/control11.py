from datetime import datetime, timedelta
from src.conversation import Information


speakers = {1: 'Ted', 2: 'Sally', 3: 'Ted', 4: 'Sally', 5: 'Ted', 6: 'Sally', 7: 'Ted', }
listeners = ['Ted', 'Sally', ]
relationships = ['source', 'girlfriend', ]
topics = ['Arts & Entertainment', ]
sentiment_score = 0.10000000149011612
sentiment_magnitude = 3.200000047683716
sentiment_value = 'slightly_positive'
location = 'living room'
mean_label = 1.6666666666666667
control_level = 'low'
realistic_label = 5.266666666666667

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
