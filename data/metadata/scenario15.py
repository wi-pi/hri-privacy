from datetime import datetime, timedelta
from src.conversation import Information


speakers = {1: 'Jay', 2: 'Dr. Virgil', 3: 'Jay', 4: 'Dr. Virgil', 5: 'Jay', }
listeners = ['Jay', 'Dr. Virgil', 'Dana', 'Desiree', ]
relationships = ['source', 'doctor', 'spouse', 'daughter', ]
topics = []
sentiment_score = -0.20000000298023224
sentiment_magnitude = 1.600000023841858
sentiment_value = 'slightly_negative'
location = 'dining room'
mean_label = 4.052631578947369
control_level = 'high'
realistic_label = 4.315789473684211

timestamps = {
    1: datetime.utcnow() + timedelta(seconds=0),
    2: datetime.utcnow() + timedelta(seconds=5),
    3: datetime.utcnow() + timedelta(seconds=10),
    4: datetime.utcnow() + timedelta(seconds=15),
    5: datetime.utcnow() + timedelta(seconds=20),
}

INFO = Information(speakers=speakers, listeners=listeners, topics=topics, timestamps=timestamps, location=location)
