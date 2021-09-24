from datetime import datetime, timedelta
from src.conversation import Information


speakers = {1: 'Dr. Holt', 2: 'Dr. Calla', 3: 'Dr. Holt', 4: 'Dr. Calla', 5: 'Dr. Holt', 6: 'Dr. Calla', }
listeners = ['Dr. Holt', 'Dr. Calla', 'Andy', ]
relationships = ['source', 'coworker', 'son', ]
topics = ['Shopping', 'Hobbies & Leisure', ]
sentiment_score = 0.10000000149011612
sentiment_magnitude = 2.700000047683716
sentiment_value = 'slightly_positive'
location = 'hospital elevator'
mean_label = 3.4558823529411766
control_level = 'moderate'
realistic_label = 4.588235294117647

timestamps = {
    1: datetime.utcnow() + timedelta(seconds=0),
    2: datetime.utcnow() + timedelta(seconds=5),
    3: datetime.utcnow() + timedelta(seconds=10),
    4: datetime.utcnow() + timedelta(seconds=15),
    5: datetime.utcnow() + timedelta(seconds=20),
    6: datetime.utcnow() + timedelta(seconds=25),
}

INFO = Information(speakers=speakers, listeners=listeners, topics=topics, timestamps=timestamps, location=location)
