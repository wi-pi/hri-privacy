from datetime import datetime, timedelta
from src.conversation import Information


speakers = {1: 'Kenwright', 2: 'Divya', 3: 'Kenwright', }
listeners = ['Kenwright', 'Divya', ]
relationships = ['source', 'friend', ]
topics = ['Online Communities', ]
sentiment_score = 0.0
sentiment_magnitude = 2.200000047683716
sentiment_value = 'neutral'
location = 'park'
mean_label = 2.7272727272727275
control_level = 'low'
realistic_label = 4.818181818181818

timestamps = {
    1: datetime.utcnow() + timedelta(seconds=0),
    2: datetime.utcnow() + timedelta(seconds=5),
    3: datetime.utcnow() + timedelta(seconds=10),
}

INFO = Information(speakers=speakers, listeners=listeners, topics=topics, timestamps=timestamps, location=location)
