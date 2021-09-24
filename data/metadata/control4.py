from datetime import datetime, timedelta
from src.conversation import Information


speakers = {1: 'Grace', 2: 'Vanderholt', 3: 'Grace', 4: 'Vanderholt', 5: 'Grace', 6: 'Vanderholt', }
listeners = ['Grace', 'Vanderholt', ]
relationships = ['source', 'coworker', ]
topics = []
sentiment_score = -0.20000000298023224
sentiment_magnitude = 2.799999952316284
sentiment_value = 'negative'
location = 'medical lab'
mean_label = 3.338235294117647
control_level = 'moderate'
realistic_label = 4.764705882352941

timestamps = {
    1: datetime.utcnow() + timedelta(seconds=0),
    2: datetime.utcnow() + timedelta(seconds=5),
    3: datetime.utcnow() + timedelta(seconds=10),
    4: datetime.utcnow() + timedelta(seconds=15),
    5: datetime.utcnow() + timedelta(seconds=20),
    6: datetime.utcnow() + timedelta(seconds=25),
}

INFO = Information(speakers=speakers, listeners=listeners, topics=topics, timestamps=timestamps, location=location)
