from datetime import datetime, timedelta
from src.conversation import Information


speakers = {
    1: 'Dolly',
    2: 'Dolly',
    3: 'Dolly',
    1: 'Dolly',
    2: 'Dolly',
    3: 'Dolly',
}

listeners = ['Dolly', 'misty']

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