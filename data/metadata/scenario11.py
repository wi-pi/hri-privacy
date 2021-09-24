from datetime import datetime, timedelta
from src.conversation import Information


speakers = {1: 'Tess', 2: 'Brendan', 3: 'Tess', 4: 'Brendan', 5: 'Tess', 6: 'Brendan', }
listeners = ['Brendan', 'Tess', ]
relationships = ['source', 'spouse', ]
topics = []
sentiment_score = -0.20000000298023224
sentiment_magnitude = 4.599999904632568
sentiment_value = 'negative'
location = 'living room'
mean_label = 2.5999999999999996
control_level = 'low'
realistic_label = 5.133333333333334

timestamps = {
    1: datetime.utcnow() + timedelta(seconds=0),
    2: datetime.utcnow() + timedelta(seconds=5),
    3: datetime.utcnow() + timedelta(seconds=10),
    4: datetime.utcnow() + timedelta(seconds=15),
    5: datetime.utcnow() + timedelta(seconds=20),
    6: datetime.utcnow() + timedelta(seconds=25),
}

INFO = Information(speakers=speakers, listeners=listeners, topics=topics, timestamps=timestamps, location=location)
