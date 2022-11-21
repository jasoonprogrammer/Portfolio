import requests
import os, json, datetime, time
import urllib.request
def hex_to_binary_256(hex_value):
	decimal = int(hex_value, 16)
	binary = bin(decimal)
	return binary[2:].zfill(256)

def hex_to_binary_512(hex_value):
	decimal = int(hex_value, 16)
	binary = bin(decimal)
	return binary[2:].zfill(512)

def split_join(value, split_char = " ", join_char = "-"):
	splitted = value.split(split_char)
	if len(splitted) > 1:
		splitted = join_char.join(splitted)
		return splitted
	else:
		return value

def text_to_list(text_file):
	my_list = text_file.split("\n")
	my_list = [x.strip() for x in my_list]
	return my_list

def market_json_query(classes = [], parts = [], speed = [], morale = [], skill = [], hp = [], pureness = []):
	#load market.json
	f = open("./market.json", "r")
	jsonx = json.load(f)[:-1]
	queries = {'classes': classes, 'parts': parts, 'speed': speed, 'morale': morale, 'skill': skill, 'hp': hp, 'pureness': pureness}
	#check all queries in market.json
	qs = [x['queries'] for x in jsonx]

	#check if data is more than 15mins old
	time_modified = os.path.getmtime("./market.json")
	dt = datetime.datetime.fromtimestamp(time_modified)
	time_delta = datetime.timedelta(minutes = 15)
	diff = datetime.datetime.now() - dt
	past_15 = diff > time_delta

	#check current query is in the query list
	if queries not in qs or past_15:
		data = start_marketquery(classes = classes, parts = parts, speed = speed, morale = morale, skill = skill, hp = hp, pureness = pureness)
		d = {'queries': queries, "data": data}
		jsonx.append(d)
		with open("./market.json", "w") as outfile:
			json.dump(jsonx, outfile)
		return data
	else:
		for x in jsonx:
			if queries == x['queries']:
				return x['data']


def marketquery(classes = [], parts = [], speed = [], morale = [], skill = [], hp = [], pureness = [], stages = 4):
	classes = [x.title() for x in classes]
	parts = [x for x in parts]
# data to be sent to api
	data ={
	"operationName": "GetAxieLatest",
	"variables": {
		"from": 0,
		"size": 30,
		"sort": "PriceAsc",
		"auctionType": "Sale",
		"criteria": {"classes": classes, "pureness": pureness, "parts": parts, "speed": speed, "morale": morale, "skill": skill, "hp": hp, "breedCount": [0, 0], 'stages': stages}
		},
		"query": "query GetAxieLatest($auctionType: AuctionType, $criteria: AxieSearchCriteria, $from: Int, $sort: SortBy, $size: Int, $owner: String) {\n  axies(auctionType: $auctionType, criteria: $criteria, from: $from, sort: $sort, size: $size, owner: $owner) {\n    total\n    results {\n      ...AxieRowData\n      __typename\n    }\n    __typename\n  }\n}\n\nfragment AxieRowData on Axie {\n  id\n  image\n  class\n  name\n  genes\n  owner\n  class\n  stage\n  title\n  breedCount\n  level\n  parts {\n    ...AxiePart\n    __typename\n  }\n  stats {\n    ...AxieStats\n    __typename\n  }\n  auction {\n    ...AxieAuction\n    __typename\n  }\n  __typename\n}\n\nfragment AxiePart on AxiePart {\n  id\n  name\n  class\n  type\n  specialGenes\n  stage\n  abilities {\n    ...AxieCardAbility\n    __typename\n  }\n  __typename\n}\n\nfragment AxieCardAbility on AxieCardAbility {\n  id\n  name\n  attack\n  defense\n  energy\n  description\n  backgroundUrl\n  effectIconUrl\n  __typename\n}\n\nfragment AxieStats on AxieStats {\n  hp\n  speed\n  skill\n  morale\n  __typename\n}\n\nfragment AxieAuction on Auction {\n  startingPrice\n  endingPrice\n  startingTimestamp\n  endingTimestamp\n  duration\n  timeLeft\n  currentPrice\n  currentPriceUSD\n  suggestedPrice\n  seller\n  listingIndex\n  state\n  __typename\n}\n"
		}
	return data

def start_marketquery(build = "No Build Name", classes = [], parts = [], speed = [], morale = [], skill = [], hp = [], pureness = []):
	API_ENDPOINT = "https://axieinfinity.com/graphql-server-v2/graphql"
	query_result = marketquery(classes = classes, parts = parts, speed = speed, morale = morale, skill = skill, hp = hp, pureness = pureness)
	response = requests.post(url = API_ENDPOINT, json = query_result)


	if response.status_code == 200:
		data = response.json()
		return data
	else:
		print(response)

def ownerquery(owner):
# data to be sent to api
	data ={
	"operationName": "GetAxieLatest",
	"variables": {
		"from": 0,
		"size": 100,
		"sort": "IdAsc",
		"auctionType": "All",
		"owner": owner
		},
		"query": "query GetAxieLatest($auctionType: AuctionType, $criteria: AxieSearchCriteria, $from: Int, $sort: SortBy, $size: Int, $owner: String) {\n  axies(auctionType: $auctionType, criteria: $criteria, from: $from, sort: $sort, size: $size, owner: $owner) {\n    total\n    results {\n      ...AxieRowData\n      __typename\n    }\n    __typename\n  }\n}\n\nfragment AxieRowData on Axie {\n  id\n  image\n  class\n  name\n  genes\n  owner\n  class\n  stage\n  title\n  breedCount\n  level\n  parts {\n    ...AxiePart\n    __typename\n  }\n  stats {\n    ...AxieStats\n    __typename\n  }\n  auction {\n    ...AxieAuction\n    __typename\n  }\n  __typename\n}\n\nfragment AxiePart on AxiePart {\n  id\n  name\n  class\n  type\n  specialGenes\n  stage\n  abilities {\n    ...AxieCardAbility\n    __typename\n  }\n  __typename\n}\n\nfragment AxieCardAbility on AxieCardAbility {\n  id\n  name\n  attack\n  defense\n  energy\n  description\n  backgroundUrl\n  effectIconUrl\n  __typename\n}\n\nfragment AxieStats on AxieStats {\n  hp\n  speed\n  skill\n  morale\n  __typename\n}\n\nfragment AxieAuction on Auction {\n  startingPrice\n  endingPrice\n  startingTimestamp\n  endingTimestamp\n  duration\n  timeLeft\n  currentPrice\n  currentPriceUSD\n  suggestedPrice\n  seller\n  listingIndex\n  state\n  __typename\n}\n"
		}
	return data

def start_ownerquery(owner):
	API_ENDPOINT = "https://axieinfinity.com/graphql-server-v2/graphql"
	query_result = ownerquery(owner)
	r = requests.post(url = API_ENDPOINT, json = query_result)

	if r.status_code == 200:
		data = r.json()
		total = data['data']['axies']['total']
		if total <= 0:
			return {}
		else:

			return data
	else:
		print(r)

def siblings(axie1, axie2):
	parents1 = [axie1['sireId'], axie1['matronId']]
	parents2 = [axie2['sireId'], axie2['matronId']]
	for parent in parents1:
		if parent in parents2:
			return True
	for parent in parents2:
		if parent in parents1:
			return True

	return False

def parents(axie1, axie2):
	parents1 = [axie1['sireId'], axie1['matronId']]
	parents2 = [axie2['sireId'], axie2['matronId']]
	if axie1['id'] in parents2:
		return True
	if axie2['id'] in parents1:
		return True

	return False
	
class Stat:

	@property
	def minimum(self):
		return self.minimum

	@minimum.setter
	def minimum(self, value):
		try:
			if isinstance(value, float):
				raise TypeError("Stat value must be an integer")
			else:
				return value
		except ValueError:
			raise TypeError("Stat value must be an integer")

	@property
	def range(self):
		return [self.minimum, self.maximum]
	
	

	def __init__(self, minimum, maximum = 61):
		self.minimum = minimum
		self.maximum = maximum


def index_query(index = 0, classes = [], stages = 4, speed = [], morale = [], skill = [], hp = [], parts = []):
	data = {
	  "operationName": "GetAxieLatest",
	  "variables": {
	    "from": index,
	    "size": 30,
	    "sort": "PriceAsc",
	    "auctionType": "Sale",
	    "criteria": {'stages': stages, "classes": classes, "skill": skill, "morale": morale, "hp": hp, "speed": speed, "parts": parts, "breedCount": [0, 0]}
	  },
	  "query": "query GetAxieLatest($auctionType: AuctionType, $criteria: AxieSearchCriteria, $from: Int, $sort: SortBy, $size: Int, $owner: String) {\n  axies(auctionType: $auctionType, criteria: $criteria, from: $from, sort: $sort, size: $size, owner: $owner) {\n    total\n    results {\n      ...AxieRowData\n      __typename\n    }\n    __typename\n  }\n}\n\nfragment AxieRowData on Axie {\n  id\n  image\n  class\n  name\n  genes\n  owner\n  class\n  stage\n  title\n  breedCount\n  level\n  parts {\n    ...AxiePart\n    __typename\n  }\n  stats {\n    ...AxieStats\n    __typename\n  }\n  auction {\n    ...AxieAuction\n    __typename\n  }\n  __typename\n}\n\nfragment AxiePart on AxiePart {\n  id\n  name\n  class\n  type\n  specialGenes\n  stage\n  abilities {\n    ...AxieCardAbility\n    __typename\n  }\n  __typename\n}\n\nfragment AxieCardAbility on AxieCardAbility {\n  id\n  name\n  attack\n  defense\n  energy\n  description\n  backgroundUrl\n  effectIconUrl\n  __typename\n}\n\nfragment AxieStats on AxieStats {\n  hp\n  speed\n  skill\n  morale\n  __typename\n}\n\nfragment AxieAuction on Auction {\n  startingPrice\n  endingPrice\n  startingTimestamp\n  endingTimestamp\n  duration\n  timeLeft\n  currentPrice\n  currentPriceUSD\n  suggestedPrice\n  seller\n  listingIndex\n  state\n  __typename\n}\n"
	}
	return data

def start_indexquery(build = "No Build Name", classes = [], parts = [], speed = [], morale = [], skill = [], hp = [], pureness = [], index = 0):
	while True:
		try:
			API_ENDPOINT = "https://axieinfinity.com/graphql-server-v2/graphql"
			query_result = index_query(classes = classes, stages = 4, index = index, speed = speed, morale = morale, skill = skill, hp = hp, parts = parts)
			r = requests.post(url = API_ENDPOINT, json = query_result)


			if r.status_code == 200:
				data = r.json()
				total = data['data']['axies']['total']
				if total <= 0:
					return {}
					break
				else:
					axies = data['data']['axies']
					return data
					break
			else:
				print(r)
				break
		except TypeError:
			time.sleep(1.5)

def request_data(url):
	response = urllib.request.urlopen(url)
	json_response = json.loads(response.read())
	return json_response

def convert_to_eth(val):
	return int(val) / (10**18)