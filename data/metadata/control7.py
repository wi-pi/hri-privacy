from datetime import datetime, timedelta
from src.conversation import Information


speakers = {1: 'Bud', 2: 'Panos', 3: 'Bud', 4: 'Panos', }
listeners = ['Bud', 'Panos', ]
relationships = ['source', 'acquaintance', ]
topics = ['Arts & Entertainment', ]
sentiment_score = 0.4000000059604645
sentiment_magnitude = 3.0
sentiment_value = 'slightly_positive'
location = 'coffee shop'
mean_label = 2.875
control_level = 'low'
realistic_label = 4.125

timestamps = {
    1: datetime.utcnow() + timedelta(seconds=0),
    2: datetime.utcnow() + timedelta(seconds=5),
    3: datetime.utcnow() + timedelta(seconds=10),
    4: datetime.utcnow() + timedelta(seconds=15),
}

INFO = Information(speakers=speakers, listeners=listeners, topics=topics, timestamps=timestamps, location=location)
