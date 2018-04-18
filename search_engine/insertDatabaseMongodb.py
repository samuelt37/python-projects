#assignment 3
#Samuel Tse 20893002

import os
import sys
import re
import json
import math
from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.termindex
terms = db.termindex

#loop though WEBPAGES_CLEAN
termindex = {}
filecount = 0;


with open('WEBPAGES_CLEAN/bookkeeping.json') as json_data:
    jobj = json.load(json_data)

progress = 0
for i in jobj:
	progress += 1
	if progress%500 == 0:
		print("~" + str(progress/500) + " out of 74")


	#filter out unwanted links
	if jobj[i][jobj[i].rfind('.'):] != ".txt" and len(jobj[i].split("/"))<20:
		filecount += 1
		docindex = {}
		word_number = 1

		file = open("WEBPAGES_CLEAN/"+i,'r')
		for line in file.readlines():
			weight = 1
			if("</strong>" in line):
				weight = 2

			#split the line by its tokens
			for word in re.split('<.*>|&gt;|&amp;|[^a-zA-Z]|\n',line):
				if word != "" and word[-1] in ".@-":
					word = word[:-1]

				if len(word) < 3:
					word_number -= 1
				elif word.lower() in ["your", "from", "their", "they", "them"]:
					word_number -= 1
				elif word.lower() not in termindex:
					doc = {i:{"tf_idf":1, "weight":weight, "location":str(word_number)}}
					termindex[word.lower()] = doc
				elif i not in termindex[word.lower()]:
					data = {"tf_idf":1, "weight":weight, "location":str(word_number)}
					termindex[word.lower()][i] = data
				else:
					termindex[word.lower()][i]["tf_idf"] += 1
					termindex[word.lower()][i]["weight"] += weight
					termindex[word.lower()][i]["location"] = termindex[word.lower()][i]["location"] + "/" + str(word_number)
				

				word_number += 1

# with open('data.txt', 'w') as outfile:
#     json.dump(termindex, outfile)

print(filecount)

for term in termindex:
	for doc in termindex[term]:
		termindex[term][doc]["tf_idf"] = (1+math.log(termindex[term][doc]["tf_idf"])) * math.log(filecount/len(termindex[term]))



for i in termindex:
	terms.insert_one({i:termindex[i]})

		#how the index will look
		# [{
		# 	term:[
		# 		docid:{
		# 			tf:1
		# 			weight:1
		# 			location:1
		# 		}
		# 		docid...
		# 	]
		
		#  }
		#  {
		#  	term2: ...

		#  }
		# ]
