from datetime import datetime, timedelta
from src.conversation import Information


speakers = {1: 'Ella', 2: 'Ben', 3: 'Ella', 4: 'Ben', 5: 'Ella', }
listeners = ['Ella', 'Ben', ]
relationships = ['source', 'friend', ]
topics = ['Books & Literature', ]
sentiment_score = 0.0
sentiment_magnitude = 0.699999988079071
sentiment_value = 'neutral'
location = 'living room'
mean_label = 2.05
control_level = 'low'
realistic_label = 4.133333333333334

timestamps = {
    1: datetime.utcnow() + timedelta(seconds=0),
    2: datetime.utcnow() + timedelta(seconds=5),
    3: datetime.utcnow() + timedelta(seconds=10),
    4: datetime.utcnow() + timedelta(seconds=15),
    5: datetime.utcnow() + timedelta(seconds=20),
}

INFO = Information(speakers=speakers, listeners=listeners, topics=topics, timestamps=timestamps, location=location)
