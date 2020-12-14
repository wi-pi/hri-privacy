from src.natural_language import Google_NLP
from src.database import Database
from data.metadata.conversation1 import INFO1
from data.metadata.conversation2 import INFO2
from data.metadata.conversation3 import INFO3
from data.metadata.people import PEOPLE

path = os.path.join('data', 'conversation{}'.format(conversation))
text = ''
texts = []
for num, file in enumerate(os.listdir(path)):
    with open(os.path.join(path, '{}.txt'.format(num)), 'r') as infile:
        text += infile.read()
        self.texts.append(infile.read())
information = {}
contents = []

nlp = Google_NLP(text)
sentiment = nlp.get_sentiment()
information[''] = 
information[''] = 

for t in texts:
	content = {}
	nlp.update_document(t)
	 = nlp.get_entity_sentiment()
	 = nlp.get_sentiment()

INFO1.speakers
INFO1.listeners
INFO1.topics
INFO1.timestamps

db = Database()
db.add_people()
db.add_information()
db.add_person_information()
db.add_person_content()
db.add_content()
db.add_entity()
