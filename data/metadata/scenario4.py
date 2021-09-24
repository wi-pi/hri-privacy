from datetime import datetime, timedelta
from src.conversation import Information


speakers = {1: 'Brett', 2: 'Kirsten', 3: 'Sharyl', 4: 'Kirsten', 5: 'Sharyl', 6: 'Kirsten', }
listeners = ['Brett', 'Sharyl', 'Kirsten', ]
relationships = ['source', 'coworker', 'manager', ]
topics = []
sentiment_score = -0.10000000149011612
sentiment_magnitude = 3.9000000953674316
sentiment_value = 'slightly_negative'
location = 'office'
mean_label = 3.6764705882352944
control_level = 'high'
realistic_label = 5.0588235294117645

timestamps = {
    1: datetime.utcnow() + timedelta(seconds=0),
    2: datetime.utcnow() + timedelta(seconds=5),
    3: datetime.utcnow() + timedelta(seconds=10),
    4: datetime.utcnow() + timedelta(seconds=15),
    5: datetime.utcnow() + timedelta(seconds=20),
    6: datetime.utcnow() + timedelta(seconds=25),
}

INFO = Information(speakers=speakers, listeners=listeners, topics=topics, timestamps=timestamps, location=location)
