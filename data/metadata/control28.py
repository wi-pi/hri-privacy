from datetime import datetime, timedelta
from src.conversation import Information


speakers = {1: 'Marjorie', 2: 'David', 3: 'Marjorie', 4: 'David', 5: 'Marjorie', 6: 'David', }
listeners = ['David', 'Marjorie', ]
relationships = ['source', 'librarian', ]
topics = ['Books & Literature', ]
sentiment_score = 0.0
sentiment_magnitude = 1.600000023841858
sentiment_value = 'neutral'
location = 'public library'
mean_label = 2.296875
control_level = 'low'
realistic_label = 5.0

timestamps = {
    1: datetime.utcnow() + timedelta(seconds=0),
    2: datetime.utcnow() + timedelta(seconds=5),
    3: datetime.utcnow() + timedelta(seconds=10),
    4: datetime.utcnow() + timedelta(seconds=15),
    5: datetime.utcnow() + timedelta(seconds=20),
    6: datetime.utcnow() + timedelta(seconds=25),
}

INFO = Information(speakers=speakers, listeners=listeners, topics=topics, timestamps=timestamps, location=location)
