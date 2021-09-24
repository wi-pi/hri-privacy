from datetime import datetime, timedelta
from src.conversation import Information


speakers = {1: 'Kirbo', 2: 'Dale', 3: 'Kirbo', }
listeners = ['Kirbo', 'Dale', ]
relationships = ['source', 'acquaintance', ]
topics = []
sentiment_score = -0.10000000149011612
sentiment_magnitude = 2.0
sentiment_value = 'slightly_negative'
location = 'courthouse'
mean_label = 2.916666666666667
control_level = 'low'
realistic_label = 4.266666666666667

timestamps = {
    1: datetime.utcnow() + timedelta(seconds=0),
    2: datetime.utcnow() + timedelta(seconds=5),
    3: datetime.utcnow() + timedelta(seconds=10),
}

INFO = Information(speakers=speakers, listeners=listeners, topics=topics, timestamps=timestamps, location=location)
