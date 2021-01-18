from datetime import datetime, timedelta
from src.conversation import Information


speakers = {
    1: 'bob',
    2: 'misty',
    3: 'bob',
}

listeners = ['bob', 'misty']

topics = ['Sensitive Subjects', 'Finance']

timestamps = {
    1: datetime.utcnow(),
    2: datetime.utcnow() + timedelta(seconds=5),
    3: datetime.utcnow() + timedelta(seconds=10),
    4: datetime.utcnow() + timedelta(seconds=15),
    5: datetime.utcnow() + timedelta(seconds=20),
}

INFO3 = Information(speakers=speakers,
                   listeners=listeners,
                   topics=topics,
                   timestamps=timestamps)