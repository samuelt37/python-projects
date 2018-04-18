import json
from pymongo import MongoClient

def main():
	with open('WEBPAGES_CLEAN/bookkeeping.json') as json_data:
	    jobj = json.load(json_data)

	client = MongoClient('localhost', 27017)
	db = client.termindex
	terms = db.termindex
	link = []


	docs = {}
	term = list(terms.find({ "informatics": { '$exists': 'true', '$not': {'$size': 0} } }))

	count = 0;
	for doc in sorted(term[0]["informatics"], key=lambda x: (term[0]["informatics"][x]["tf_idf"]), reverse=True):
		if(count > 4):
			break
		count += 1
		links.append(jobj[doc])
		print(term[0]["informatics"][doc]["tf_idf"])


	return links

if __name__ == "__main__":
    x=main()
    return x;