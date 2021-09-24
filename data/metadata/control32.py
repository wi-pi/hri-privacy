from datetime import datetime, timedelta
from src.conversation import Information


speakers = {1: 'Mike', 2: 'Laura', 3: 'Mike', 4: 'Laura', }
listeners = ['Mike', 'Laura', ]
relationships = ['source', 'date', ]
topics = []
sentiment_score = 0.30000001192092896
sentiment_magnitude = 2.299999952316284
sentiment_value = 'slightly_positive'
location = 'restaurant'
mean_label = 2.884615384615384
control_level = 'low'
realistic_label = 5.076923076923077

timestamps = {
    1: datetime.utcnow() + timedelta(seconds=0),
    2: datetime.utcnow() + timedelta(seconds=5),
    3: datetime.utcnow() + timedelta(seconds=10),
    4: datetime.utcnow() + timedelta(seconds=15),
}

INFO = Information(speakers=speakers, listeners=listeners, topics=topics, timestamps=timestamps, location=location)
