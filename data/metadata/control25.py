from datetime import datetime, timedelta
from src.conversation import Information


speakers = {1: 'Henry', 2: 'Benjamin', 3: 'Henry', 4: 'Benjamin', 5: 'Henry', }
listeners = ['Henry', 'Benjamin', ]
relationships = ['source', 'brother', ]
topics = ['Food & Drink', ]
sentiment_score = -0.20000000298023224
sentiment_magnitude = 2.299999952316284
sentiment_value = 'slightly_negative'
location = 'coffee shop'
mean_label = 3.057692307692308
control_level = 'moderate'
realistic_label = 4.923076923076923

timestamps = {
    1: datetime.utcnow() + timedelta(seconds=0),
    2: datetime.utcnow() + timedelta(seconds=5),
    3: datetime.utcnow() + timedelta(seconds=10),
    4: datetime.utcnow() + timedelta(seconds=15),
    5: datetime.utcnow() + timedelta(seconds=20),
}

INFO = Information(speakers=speakers, listeners=listeners, topics=topics, timestamps=timestamps, location=location)
