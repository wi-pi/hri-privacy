from datetime import datetime, timedelta
from data.metadata.conversation import Information


speakers = {
    1: 'alice',
    2: 'bob',
    3: 'alice',
    4: 'bob',
    5: 'eve',
    6: 'charlie',
    7: 'alice',
}

listeners = ['alice', 'bob', 'charlie', 'eve', 'misty']

topics = ['Beauty & Fitness']

timestamps = {
    1: datetime.utcnow(),
    2: datetime.utcnow() + timedelta(seconds=5),
    3: datetime.utcnow() + timedelta(seconds=10),
    4: datetime.utcnow() + timedelta(seconds=15),
    5: datetime.utcnow() + timedelta(seconds=20),
    6: datetime.utcnow() + timedelta(seconds=25),
    7: datetime.utcnow() + timedelta(seconds=30),
}

INFO1 = Information(speakers=speakers,
                   listeners=listeners,
                   topics=topics,
                   timestamps=timestamps)
