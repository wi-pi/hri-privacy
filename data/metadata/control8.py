from datetime import datetime, timedelta
from src.conversation import Information


speakers = {1: 'Mary', 2: 'Nicole', 3: 'Mary', 4: 'Nicole', }
listeners = ['Mary', 'Nicole', ]
relationships = ['source', 'daughter', ]
topics = []
sentiment_score = 0.30000001192092896
sentiment_magnitude = 2.700000047683716
sentiment_value = 'slightly_positive'
location = 'bedroom'
mean_label = 1.7708333333333333
control_level = 'low'
realistic_label = 4.666666666666667

timestamps = {
    1: datetime.utcnow() + timedelta(seconds=0),
    2: datetime.utcnow() + timedelta(seconds=5),
    3: datetime.utcnow() + timedelta(seconds=10),
    4: datetime.utcnow() + timedelta(seconds=15),
}

INFO = Information(speakers=speakers, listeners=listeners, topics=topics, timestamps=timestamps, location=location)
