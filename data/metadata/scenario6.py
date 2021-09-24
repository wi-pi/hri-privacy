from datetime import datetime, timedelta
from src.conversation import Information


speakers = {1: 'Helen', 2: 'Kate', 3: 'Helen', 4: 'Kate', 5: 'Helen', }
listeners = ['Kate', 'Helen', 'Joe', ]
relationships = ['source', 'supervisor', 'coworker', ]
topics = []
sentiment_score = -0.5
sentiment_magnitude = 5.800000190734863
sentiment_value = 'negative'
location = 'office'
mean_label = 3.3181818181818183
control_level = 'moderate'
realistic_label = 4.545454545454546

timestamps = {
    1: datetime.utcnow() + timedelta(seconds=0),
    2: datetime.utcnow() + timedelta(seconds=5),
    3: datetime.utcnow() + timedelta(seconds=10),
    4: datetime.utcnow() + timedelta(seconds=15),
    5: datetime.utcnow() + timedelta(seconds=20),
}

INFO = Information(speakers=speakers, listeners=listeners, topics=topics, timestamps=timestamps, location=location)
