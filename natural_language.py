from google.cloud import language_v1
import os


class Google_NLP:

    def __init__(self, text):
        self.client = language_v1.LanguageServiceClient()
        self.language = "en"

        print("Text: {}".format(text))
        self.document = language_v1.Document(content=text, type_=language_v1.Document.Type.PLAIN_TEXT, language=self.language)

    def get_entity_sentiment(self):
        """
        Analyzing Entity Sentiment in a String

        Args:
          text_content The text content to analyze
        """
        response = self.client.analyze_entity_sentiment(request={'document': self.document})
        entities = []
        for entity in response.entities:
            e_name = entity.name
            e_type = language_v1.Entity.Type(entity.type_).name
            e_salience = entity.salience
            e_sentiment_score = entity.sentiment.score
            e_sentiment_magnitude = entity.sentiment.magnitude

            print(u"Representative name for the entity: {}".format(e_name))
            print(u"Entity type: {}".format(e_type))
            print(u"Salience score: {}".format(e_salience))
            print(u"Entity sentiment score: {}".format(e_sentiment_score))
            print(u"Entity sentiment magnitude: {}".format(e_sentiment_magnitude))

            e_metadata = {}
            for metadata_name, metadata_value in entity.metadata.items():
                print(u"{} = {}".format(metadata_name, metadata_value))
                emetadata[metadata_name] = metadata_value

            e_mention = ''
            e_mentiontype = ''
            for mention in entity.mentions:
                print(u"Mention text: {}".format(mention.text.content))
                print(u"Mention type: {}".format(language_v1.EntityMention.Type(mention.type_).name))
                e_mention += mention.text.content
                e_mention_type += language_v1.EntityMention.Type(mention.type_).name


            e = {'representation': e_name,
                 'type': e_type,
                 'salience': e_salience,
                 'mention_text': e_mention,
                 'mention_type': e_mention_type,
                 'sentiment_score': e_sentiment_score,
                 'sentiment_magnitude': e_sentiment_magnitude}
            e.update(e_metadata)
            entities.append(e)
        return entities

    def get_sentiment(self):
        return self.client.analyze_sentiment(request={'document': self.document})

    def get_topic(self):
        return self.client.classify_text(request={'document': self.document}).split('/')[1]

    def update_document(self, text):
        print("Text: {}".format(text))
        self.document = language_v1.Document(content=text, type_=language_v1.Document.Type.PLAIN_TEXT, language=self.language)