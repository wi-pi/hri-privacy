import json
from random import shuffle


SEARCH_TERMS = ['i hope you weren']
# SEARCH_TERMS = ['gardening', 'literature', 'exercise', 'finances', 'online', 'real estate', 'shopping', 'lunch', 'internet', 'computer', 'games', 'employment', 'news', 'science', 'travel', 'hobby', 'business', 'artist', 'music']
# SEARCH_TERMS = ['cartoon', 'festival', 'jazz', 'painting', 'motorcycle', 'fragrance', 'technology', 'commerce', 'financial aid', 'seafood', 'arcade', 'respiratory', 'lottery', 'nursing', 'furniture', 'immigrated', 'environmental', 'vacation', 'toys', 'cycling', 'olympics', 'resort']

for SEARCH in SEARCH_TERMS:
    data = json.load(open('scripts.json'))
    shuffle(data)
    # output = open('conversation_dump/conversation_dump_{}.txt'.format(SEARCH), 'w')
    for i in data:
        if 'Drama' in i['genre']:
            split = i['script_text'][0].split('<b>')
            for j, val in enumerate(split):
                split[j] = split[j].replace('</b>', '')
            for j, line in enumerate(split):
                if SEARCH in line.lower():

                    # count = 0
                    # outstring = ''
                    # for k in range(-4, 5):
                    #     cur_line = split[min(max(j+k, 0), len(split)-1)].replace('</b>', '')
                    #     count += len(cur_line)
                    #     outstring += cur_line
                    # if count < 2000 and count > 300:
                    #     output.write('Title: {}\n'.format(i['title']))
                    #     output.write('Genres:\n')
                    #     for genre in i['genre']:
                    #         output.write(genre + ', ')
                    #     output.write('\n')
                    #     output.write(outstring)
                    #     # print(outstring)
                    print(split[max(j-8, 0)])
                    print(split[max(j-7, 0)])                    
                    print(split[max(j-6, 0)])
                    print(split[max(j-5, 0)])
                    print(split[max(j-4, 0)])
                    print(split[max(j-3, 0)])                    
                    print(split[max(j-2, 0)])
                    print(split[max(j-1, 0)])
                    print(split[j])
                    print(split[min(j+1, len(split)-1)])
                    print(split[min(j+2, len(split)-1)])
                    print(split[min(j+3, len(split)-1)])
                    print(split[min(j+4, len(split)-1)])
                    print(split[min(j+5, len(split)-1)])
                    print(split[min(j+6, len(split)-1)])
                    print(split[min(j+7, len(split)-1)])
                    print(split[min(j+8, len(split)-1)])
                    print(i['title'])
                    print(i['genre'])
