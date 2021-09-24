from datetime import datetime, timedelta
from src.conversation import Information


speakers = {1: 'Oscar', 2: 'Wanda', 3: 'Oscar', 4: 'Wanda', 5: 'Oscar', }
listeners = ['Oscar', 'Wanda', ]
relationships = ['source', 'nanny', ]
topics = ['Games', 'Arts & Entertainment', ]
sentiment_score = 0.4000000059604645
sentiment_magnitude = 3.700000047683716
sentiment_value = 'slightly_positive'
location = 'house'
mean_label = 1.9423076923076925
control_level = 'low'
realistic_label = 4.538461538461538

timestamps = {
    1: datetime.utcnow() + timedelta(seconds=0),
    2: datetime.utcnow() + timedelta(seconds=5),
    3: datetime.utcnow() + timedelta(seconds=10),
    4: datetime.utcnow() + timedelta(seconds=15),
    5: datetime.utcnow() + timedelta(seconds=20),
}

INFO = Information(speakers=speakers, listeners=listeners, topics=topics, timestamps=timestamps, location=location)
