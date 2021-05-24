from datetime import datetime, timedelta
from src.conversation import Information


speakers = {
    1: 'alice',
    2: 'bob',
    3: 'alice',
    4: 'bob',
}

listeners = ['alice', 'bob', 'misty']

topics = ['Health', 'Beauty & Fitness']

timestamps = {
    1: datetime.utcnow(),
    2: datetime.utcnow() + timedelta(seconds=5),
    3: datetime.utcnow() + timedelta(seconds=10),
    4: datetime.utcnow() + timedelta(seconds=15),
}


INFO2 = Information(speakers=speakers,
                   listeners=listeners,
                   topics=topics,
                   timestamps=timestamps)
