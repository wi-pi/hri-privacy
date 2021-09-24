from datetime import datetime, timedelta
from src.conversation import Information


speakers = {1: 'Letty', 2: 'Paul', 3: 'Letty', 4: 'Paul', 5: 'Letty', 6: 'Paul', 7: 'Letty', 8: 'Paul', }
listeners = ['Letty', 'Paul', ]
relationships = ['source', 'boyfriend', ]
topics = []
sentiment_score = -0.30000001192092896
sentiment_magnitude = 8.300000190734863
sentiment_value = 'negative'
location = 'apartment'
mean_label = 3.0166666666666666
control_level = 'moderate'
realistic_label = 4.866666666666666

timestamps = {
    1: datetime.utcnow() + timedelta(seconds=0),
    2: datetime.utcnow() + timedelta(seconds=5),
    3: datetime.utcnow() + timedelta(seconds=10),
    4: datetime.utcnow() + timedelta(seconds=15),
    5: datetime.utcnow() + timedelta(seconds=20),
    6: datetime.utcnow() + timedelta(seconds=25),
    7: datetime.utcnow() + timedelta(seconds=30),
    8: datetime.utcnow() + timedelta(seconds=35),
}

INFO = Information(speakers=speakers, listeners=listeners, topics=topics, timestamps=timestamps, location=location)
