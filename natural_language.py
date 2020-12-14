from google.cloud import language_v1


def iterate_entities(response):
	for entity in response.entities:
	    print(u"Representative name for the entity: {}".format(entity.name))

	    # Get entity type, e.g. PERSON, LOCATION, ADDRESS, NUMBER, et al
	    print(u"Entity type: {}".format(language_v1.Entity.Type(entity.type_).name))

	    # Get the salience score associated with the entity in the [0, 1.0] range
	    print(u"Salience score: {}".format(entity.salience))

	    # Loop over the metadata associated with entity. For many known entities,
	    # the metadata is a Wikipedia URL (wikipedia_url) and Knowledge Graph MID (mid).
	    # Some entity types may have additional metadata, e.g. ADDRESS entities
	    # may have metadata for the address street_name, postal_code, et al.
	    for metadata_name, metadata_value in entity.metadata.items():
	        print(u"{}: {}".format(metadata_name, metadata_value))

	    # Loop over the mentions of this entity in the input document.
	    # The API currently supports proper noun mentions.
	    for mention in entity.mentions:
	        print(u"Mention text: {}".format(mention.text.content))

	        # Get the mention type, e.g. PROPER for proper noun
	        print(
	            u"Mention type: {}".format(language_v1.EntityMention.Type(mention.type_).name)
	        )

	# Get the language of the text, which will be the same as
	# the language specified in the request or, if not specified,
	# the automatically-detected language.
	print(u"Language of the text: {}".format(response.language))


def iterate_entity_sentiment(response):
    """
    Analyzing Entity Sentiment in a String

    Args:
      text_content The text content to analyze
    """

    for entity in response.entities:
        print(u"Representative name for the entity: {}".format(entity.name))
        # Get entity type, e.g. PERSON, LOCATION, ADDRESS, NUMBER, et al
        print(u"Entity type: {}".format(language_v1.Entity.Type(entity.type_).name))
        # Get the salience score associated with the entity in the [0, 1.0] range
        print(u"Salience score: {}".format(entity.salience))
        # Get the aggregate sentiment expressed for this entity in the provided document.
        sentiment = entity.sentiment
        print(u"Entity sentiment score: {}".format(sentiment.score))
        print(u"Entity sentiment magnitude: {}".format(sentiment.magnitude))
        # Loop over the metadata associated with entity. For many known entities,
        # the metadata is a Wikipedia URL (wikipedia_url) and Knowledge Graph MID (mid).
        # Some entity types may have additional metadata, e.g. ADDRESS entities
        # may have metadata for the address street_name, postal_code, et al.
        for metadata_name, metadata_value in entity.metadata.items():
            print(u"{} = {}".format(metadata_name, metadata_value))

        # Loop over the mentions of this entity in the input document.
        # The API currently supports proper noun mentions.
        for mention in entity.mentions:
            print(u"Mention text: {}".format(mention.text.content))
            # Get the mention type, e.g. PROPER for proper noun
            print(
                u"Mention type: {}".format(language_v1.EntityMention.Type(mention.type_).name)
            )

    # Get the language of the text, which will be the same as
    # the language specified in the request or, if not specified,
    # the automatically-detected language.
    print(u"Language of the text: {}".format(response.language))


client = language_v1.LanguageServiceClient()
with open('sample2.txt', 'r') as infile:
	text = infile.read()
language = "en"
document = language_v1.Document(content=text, type_=language_v1.Document.Type.PLAIN_TEXT, language=language)
# sentiment = client.analyze_sentiment(request={'document': document})
# topic = client.classify_text(request={'document': document})
# response = client.analyze_entities(request={'document': document})
# response = client.analyze_entity_sentiment(request={'document': document})


print("Text: {}".format(text))
# Score < 0 is negative, > 0 is positive, around 0 is neutral
# Magnitude around 0 is neutral, the higher is more emotion expression
# print(sentiment)
# print(topic)
# iterate_entities(response)
# iterate_entity_sentiment(response)