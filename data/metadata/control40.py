from datetime import datetime, timedelta
from src.conversation import Information


speakers = {1: 'Roy', 2: 'Sara', 3: 'Roy', 4: 'Sara', 5: 'Roy', 6: 'Sara', }
listeners = ['Roy', 'Sara', ]
relationships = ['source', 'student', ]
topics = ['Arts & Entertainment', ]
sentiment_score = 0.20000000298023224
sentiment_magnitude = 5.099999904632568
sentiment_value = 'slightly_positive'
location = 'office'
mean_label = 2.966666666666667
control_level = 'low'
realistic_label = 3.6666666666666665

timestamps = {
    1: datetime.utcnow() + timedelta(seconds=0),
    2: datetime.utcnow() + timedelta(seconds=5),
    3: datetime.utcnow() + timedelta(seconds=10),
    4: datetime.utcnow() + timedelta(seconds=15),
    5: datetime.utcnow() + timedelta(seconds=20),
    6: datetime.utcnow() + timedelta(seconds=25),
}

INFO = Information(speakers=speakers, listeners=listeners, topics=topics, timestamps=timestamps, location=location)
