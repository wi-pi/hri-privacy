from datetime import datetime, timedelta
from src.conversation import Information


speakers = {1: 'Henry', 2: 'Henry', 3: 'Cynthia', 4: 'Henry', 5: 'William', 6: 'Elliot', 7: 'William', 8: 'Helen', 9: 'Cynthia', 10: 'Helen', 11: 'Cynthia', 12: 'Helen', 13: 'Cynthia', }
listeners = ['William', 'Cynthia', 'Elliot', 'Henry', ]
relationships = ['source', 'acquaintance', 'lawyer', 'bailiff', ]
topics = []
sentiment_score = -0.10000000149011612
sentiment_magnitude = 4.599999904632568
sentiment_value = 'slightly_negative'
location = 'courthouse'
mean_label = 3.958333333333333
control_level = 'high'
realistic_label = 4.666666666666667

timestamps = {
    1: datetime.utcnow() + timedelta(seconds=0),
    2: datetime.utcnow() + timedelta(seconds=5),
    3: datetime.utcnow() + timedelta(seconds=10),
    4: datetime.utcnow() + timedelta(seconds=15),
    5: datetime.utcnow() + timedelta(seconds=20),
    6: datetime.utcnow() + timedelta(seconds=25),
    7: datetime.utcnow() + timedelta(seconds=30),
    8: datetime.utcnow() + timedelta(seconds=35),
    9: datetime.utcnow() + timedelta(seconds=40),
    10: datetime.utcnow() + timedelta(seconds=45),
    11: datetime.utcnow() + timedelta(seconds=50),
    12: datetime.utcnow() + timedelta(seconds=55),
    13: datetime.utcnow() + timedelta(seconds=60),
}

INFO = Information(speakers=speakers, listeners=listeners, topics=topics, timestamps=timestamps, location=location)
