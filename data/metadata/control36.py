from datetime import datetime, timedelta
from src.conversation import Information


speakers = {1: 'Kathy', 2: 'Jake', 3: 'Kathy', 4: 'Leonor', 5: 'Kathy', 6: 'Jake', 7: 'Kathy', }
listeners = ['Kathy', 'Jake', 'Leonor', ]
relationships = ['source', 'son', 'daughter', ]
topics = ['Arts & Entertainment', ]
sentiment_score = 0.0
sentiment_magnitude = 3.0
sentiment_value = 'neutral'
location = 'living room'
mean_label = 2.2083333333333335
control_level = 'low'
realistic_label = 5.083333333333333

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
