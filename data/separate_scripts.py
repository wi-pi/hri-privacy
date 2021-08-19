import json
from random import shuffle


SEARCH = 'ex-husband'


data = json.load(open('scripts.json'))
shuffle(data)
for i in data:
	if 'Drama' in i['genre']:
		split = i['script_text'][0].split('<b>')
		for j, line in enumerate(split):
			if SEARCH in line.lower():
				print(split[max(j-2, 0)])
				print(split[max(j-1, 0)])
				print(split[j])
				print(split[min(j+1, len(split)-1)])
				print(split[min(j+2, len(split)-1)])
				print(i['title'])
				print(i['genre'])
