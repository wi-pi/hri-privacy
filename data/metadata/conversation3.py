from datetime import datetime, timedelta
from src.conversation import Information


speakers = {
    1: 'alice',
    2: 'misty',
    3: 'alice',
}

listeners = ['alice', 'misty']

topics = ['Sensitive Subjects', 'Finance']

timestamps = {
    1: datetime.utcnow(),
    2: datetime.utcnow() + timedelta(seconds=5),
    3: datetime.utcnow() + timedelta(seconds=10),
}

INFO3 = Information(speakers=speakers,
                   listeners=listeners,
                   topics=topics,
                   timestamps=timestamps)