from datetime import datetime, timedelta
from src.conversation import Information


speakers = {1: 'Hazel', 2: 'Caden', 3: 'Hazel', 4: 'Holly', }
listeners = ['Hazel', 'Caden', 'Holly', ]
relationships = ['source', 'friend', 'friend', ]
topics = []
sentiment_score = 0.10000000149011612
sentiment_magnitude = 4.099999904632568
sentiment_value = 'slightly_positive'
location = 'living room'
mean_label = 2.1176470588235294
control_level = 'low'
realistic_label = 4.294117647058823

timestamps = {
    1: datetime.utcnow() + timedelta(seconds=0),
    2: datetime.utcnow() + timedelta(seconds=5),
    3: datetime.utcnow() + timedelta(seconds=10),
    4: datetime.utcnow() + timedelta(seconds=15),
}

INFO = Information(speakers=speakers, listeners=listeners, topics=topics, timestamps=timestamps, location=location)
