from datetime import datetime, timedelta
from src.conversation import Information


speakers = {1: 'Jefferson', 2: 'Damone', 3: 'Jefferson', 4: 'Damone', 5: 'Jefferson', 6: 'Damone', }
listeners = ['Jefferson', 'Damone', ]
relationships = ['source', 'cashier', ]
topics = ['Arts & Entertainment', ]
sentiment_score = 0.30000001192092896
sentiment_magnitude = 4.099999904632568
sentiment_value = 'slightly_positive'
location = 'ticket booth'
mean_label = 2.1333333333333333
control_level = 'low'
realistic_label = 4.666666666666667

timestamps = {
    1: datetime.utcnow() + timedelta(seconds=0),
    2: datetime.utcnow() + timedelta(seconds=5),
    3: datetime.utcnow() + timedelta(seconds=10),
    4: datetime.utcnow() + timedelta(seconds=15),
    5: datetime.utcnow() + timedelta(seconds=20),
    6: datetime.utcnow() + timedelta(seconds=25),
}

INFO = Information(speakers=speakers, listeners=listeners, topics=topics, timestamps=timestamps, location=location)
