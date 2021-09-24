from datetime import datetime, timedelta
from src.conversation import Information


speakers = {1: 'Sara', 2: 'Holly', 3: 'Norton', 4: 'Mickey', }
listeners = ['Holly', 'Mickey', 'Sara', ]
relationships = ['source', 'manager', 'friend/coworker', ]
topics = []
sentiment_score = -0.6000000238418579
sentiment_magnitude = 5.699999809265137
sentiment_value = 'negative'
location = 'office'
mean_label = 4.25
control_level = 'high'
realistic_label = 4.75

timestamps = {
    1: datetime.utcnow() + timedelta(seconds=0),
    2: datetime.utcnow() + timedelta(seconds=5),
    3: datetime.utcnow() + timedelta(seconds=10),
    4: datetime.utcnow() + timedelta(seconds=15),
}

INFO = Information(speakers=speakers, listeners=listeners, topics=topics, timestamps=timestamps, location=location)
