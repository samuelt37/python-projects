#assignment 3
#Samuel Tse 20893002

import os
import sys
import re
import mysql.connector

#loop though WEBPAGES_CLEAN
for directory in os.listdir("WEBPAGES_CLEAN")[:-2]:
	if not directory.startswith('.'):
		query = "INSERT INTO termindex VALUES "
		print("dir:" + directory)
		for filename in os.listdir("WEBPAGES_CLEAN/"+directory):

			try:
				word_dict = {}
				#filter out some pages
				if directory+"/"+filename not in ["39/373", "74/49", "73/404", "71/451", "70/55", "74/78"]:
					file = open("WEBPAGES_CLEAN/"+directory+"/"+filename,'r')
					word_number = 1
					for line in file.readlines():
						weight = 1
						if("</strong>" in line):
							weight = 2

						#split the line by its tokens
						for word in re.split('<.*>|&gt;|&amp;|[^a-zA-Z]|\n',line):
							if word != "" and word[-1] in ".@-":
								word = word[:-1]
							if word != "" and word[0] in ".":
								word = word[1:]

							if len(word) < 4:
								word_number -= 1
							elif word.lower() in ["your", "from", "their", "they", "them"]:
								word_number -= 1
							elif word.lower() not in word_dict:
								l = [directory+"/"+filename, 1, weight, str(word_number)]
								word_dict[word.lower()] = l
							else:
								word_dict[word.lower()][1] += 1
								word_dict[word.lower()][2] += weight
								word_dict[word.lower()][3] = word_dict[word.lower()][3] + "/" + str(word_number)
							

							word_number += 1
			except:
				print('Not a file');

			for key, value in word_dict.items():
			    query +="('" + str(key) + "', '" + str(value[0]) + "', " + str(value[1]) + ", " + str(value[2]) + ", '" + str(value[3]) + "'), "




		#insert into database, needs:
		#term, docid, termfrequency, weight(bold or reg?), termlocation
		#													(this will be a string like "1,5,10", 1=1st word in file)
		conn = mysql.connector.connect(user='root', password='',
		                              host='127.0.0.1',
		                              database='termindex')


		x = conn.cursor()

		try:
		   	x.execute(query[:-2]+";")
		   	conn.commit()
		except:
			print("error")
		   	conn.rollback()

		conn.close()
