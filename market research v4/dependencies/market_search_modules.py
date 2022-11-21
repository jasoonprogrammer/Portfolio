import json
import requests
def ownerquery(owner, index = 0, stages = 4):
# data to be sent to api
	data = {
	  "operationName": "GetAxieLatest",
	  "variables": {
	    "from": index,
	    "size": 100,
	    "sort": "IdAsc",
	    "auctionType": "All",
	    "owner": owner,
	    "criteria": {"stages": stages}
	  },
	  "query": "query GetAxieLatest($auctionType: AuctionType, $criteria: AxieSearchCriteria, $from: Int, $sort: SortBy, $size: Int, $owner: String) {\n  axies(auctionType: $auctionType, criteria: $criteria, from: $from, sort: $sort, size: $size, owner: $owner) {\n    total\n    results {\n      ...AxieRowData\n      __typename\n    }\n    __typename\n  }\n}\n\nfragment AxieRowData on Axie {\n  id\n  image\n  class\n  name\n  genes\n  matronId\n  sireId\n  owner\n  class\n  stage\n  title\n  breedCount\n  level\n  parts {\n    ...AxiePart\n    __typename\n  }\n  stats {\n    ...AxieStats\n    __typename\n  }\n  auction {\n    ...AxieAuction\n    __typename\n  }\n  __typename\n}\n\nfragment AxiePart on AxiePart {\n  id\n  name\n  class\n  type\n  specialGenes\n  stage\n  abilities {\n    ...AxieCardAbility\n    __typename\n  }\n  __typename\n}\n\nfragment AxieCardAbility on AxieCardAbility {\n  id\n  name\n  attack\n  defense\n  energy\n  description\n  backgroundUrl\n  effectIconUrl\n  __typename\n}\n\nfragment AxieStats on AxieStats {\n  hp\n  speed\n  skill\n  morale\n  __typename\n}\n\nfragment AxieAuction on Auction {\n  startingPrice\n  endingPrice\n  startingTimestamp\n  endingTimestamp\n  duration\n  timeLeft\n  currentPrice\n  currentPriceUSD\n  suggestedPrice\n  seller\n  listingIndex\n  state\n  __typename\n}\n"
	}
	return data

def start_ownerquery(owner, index = 0, stages = 4):
	API_ENDPOINT = "https://axieinfinity.com/graphql-server-v2/graphql"
	query_result = ownerquery(owner, index = index, stages = stages)
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

def marketquery(classes = [], parts = [], speed = [], morale = [], skill = [], hp = [], stages = 4, index = 0, size = 30):
# data to be sent to api
	data ={
	"operationName": "GetAxieLatest",
	"variables": {
		"from": index,
		"size": size,
		"sort": "PriceAsc",
		"auctionType": "Sale",
		"criteria": {"classes": classes, "parts": parts, "speed": speed, "morale": morale, "skill": skill, "hp": hp, "breedCount": [0, 0]}
		},
		"query": "query GetAxieLatest($auctionType: AuctionType, $criteria: AxieSearchCriteria, $from: Int, $sort: SortBy, $size: Int, $owner: String) {\n  axies(auctionType: $auctionType, criteria: $criteria, from: $from, sort: $sort, size: $size, owner: $owner) {\n    total\n    results {\n      ...AxieRowData\n      __typename\n    }\n    __typename\n  }\n}\n\nfragment AxieRowData on Axie {\n  id\n  image\n  class\n  name\n  genes\n  owner\n  class\n  stage\n  title\n  breedCount\n  level\n  parts {\n    ...AxiePart\n    __typename\n  }\n  stats {\n    ...AxieStats\n    __typename\n  }\n  auction {\n    ...AxieAuction\n    __typename\n  }\n  __typename\n}\n\nfragment AxiePart on AxiePart {\n  id\n  name\n  class\n  type\n  specialGenes\n  stage\n  abilities {\n    ...AxieCardAbility\n    __typename\n  }\n  __typename\n}\n\nfragment AxieCardAbility on AxieCardAbility {\n  id\n  name\n  attack\n  defense\n  energy\n  description\n  backgroundUrl\n  effectIconUrl\n  __typename\n}\n\nfragment AxieStats on AxieStats {\n  hp\n  speed\n  skill\n  morale\n  __typename\n}\n\nfragment AxieAuction on Auction {\n  startingPrice\n  endingPrice\n  startingTimestamp\n  endingTimestamp\n  duration\n  timeLeft\n  currentPrice\n  currentPriceUSD\n  suggestedPrice\n  seller\n  listingIndex\n  state\n  __typename\n}\n"
		}
	return data


def start_marketquery(build = "No Build Name", classes = [], parts = [], speed = [], morale = [], skill = [], hp = [], index = 0, size = 30):
	API_ENDPOINT = "https://axieinfinity.com/graphql-server-v2/graphql"
	query_result = marketquery(classes = classes, parts = parts, speed = speed, morale = morale, skill = skill, hp = hp, index = index, size = size)
	response = requests.post(url = API_ENDPOINT, json = query_result)


	if response.status_code == 200:
		data = response.json()
		return data
	else:
		print(response)


def latest_sold(index, size):
# data to be sent to api
	data = {
            "operationName": "GetRecentlyAxiesSold",
            "variables": {
                "from": index,
                "size": size
                },
            "query": "query GetRecentlyAxiesSold($from: Int, $size: Int) {\n  settledAuctions {\n    axies(from: $from, size: $size) {\n      total\n      results {\n     genes \n   ...AxieSettledBrief\n        transferHistory {\n          ...TransferHistoryInSettledAuction\n          __typename\n        }\n        __typename\n      }\n      __typename\n    }\n    __typename\n  }\n}\n\nfragment AxieSettledBrief on Axie {\n  id\n  name\n  image\n  class\n  breedCount\n  __typename\n}\n\nfragment TransferHistoryInSettledAuction on TransferRecords {\n  total\n  results {\n    ...TransferRecordInSettledAuction\n    __typename\n  }\n  __typename\n}\n\nfragment TransferRecordInSettledAuction on TransferRecord {\n  from\n  to\n  txHash\n  timestamp\n  withPrice\n  withPriceUsd\n  fromProfile {\n    name\n    __typename\n  }\n  toProfile {\n    name\n    __typename\n  }\n  __typename\n}\n"
	}
	return data

def start_soldquery(index, size):
	API_ENDPOINT = "https://axieinfinity.com/graphql-server-v2/graphql"
	query_result = latest_sold(index = index, size = size)
	response = requests.post(url = API_ENDPOINT, json = query_result)


	if response.status_code == 200:
		data = response.json()
		return data
	else:
		print(response)





def marketquery_2(classes = [], parts = [], speed = [], morale = [], skill = [], hp = [], breedCount = [0, 0], stages = 4, index = 0):
# data to be sent to api
	data ={
	"operationName": "GetAxieLatest",
	"variables": {
		"from": index,
		"size": 100,
		"sort": "PriceAsc",
		"auctionType": "Sale",
		"criteria": {"classes": classes, "parts": parts, "speed": speed, "morale": morale, "skill": skill, "hp": hp, "breedCount": breedCount}
		},
		"query": "query GetAxieLatest($auctionType: AuctionType, $criteria: AxieSearchCriteria, $from: Int, $sort: SortBy, $size: Int, $owner: String) {\n  axies(auctionType: $auctionType, criteria: $criteria, from: $from, sort: $sort, size: $size, owner: $owner) {\n    total\n    results {\n      ...AxieRowData\n      __typename\n    }\n    __typename\n  }\n}\n\nfragment AxieRowData on Axie {\n  id\n  image\n  class\n  name\n  genes\n  owner\n  class\n  stage\n  title\n  breedCount\n  level\n  parts {\n    ...AxiePart\n    __typename\n  }\n  stats {\n    ...AxieStats\n    __typename\n  }\n  auction {\n    ...AxieAuction\n    __typename\n  }\n  __typename\n}\n\nfragment AxiePart on AxiePart {\n  id\n  name\n  class\n  type\n  specialGenes\n  stage\n  abilities {\n    ...AxieCardAbility\n    __typename\n  }\n  __typename\n}\n\nfragment AxieCardAbility on AxieCardAbility {\n  id\n  name\n  attack\n  defense\n  energy\n  description\n  backgroundUrl\n  effectIconUrl\n  __typename\n}\n\nfragment AxieStats on AxieStats {\n  hp\n  speed\n  skill\n  morale\n  __typename\n}\n\nfragment AxieAuction on Auction {\n  startingPrice\n  endingPrice\n  startingTimestamp\n  endingTimestamp\n  duration\n  timeLeft\n  currentPrice\n  currentPriceUSD\n  suggestedPrice\n  seller\n  listingIndex\n  state\n  __typename\n}\n"
		}
	return data


def start_marketquery_2(build = "No Build Name", classes = [], parts = [], speed = [], morale = [], skill = [], hp = [], index = 0, breedCount = [0, 0]):
	API_ENDPOINT = "https://axieinfinity.com/graphql-server-v2/graphql"
	query_result = marketquery_2(classes = classes, parts = parts, speed = speed, morale = morale, skill = skill, hp = hp, index = index, breedCount = breedCount)
	response = requests.post(url = API_ENDPOINT, json = query_result)


	if response.status_code == 200:
		data = response.json()
		return data
	else:
		print(response)





#axie_details_ronin
def ownerquery_details(owner, index = 0):
# data to be sent to api
	data = {
	  "operationName": "GetAxieLatest",
	  "variables": {
	    "from": index,
	    "size": 100,
	    "sort": "IdAsc",
	    "auctionType": "All",
	    "owner": owner,
	  },
	  "query": "query GetAxieLatest($auctionType: AuctionType, $criteria: AxieSearchCriteria, $from: Int, $sort: SortBy, $size: Int, $owner: String) {\n  axies(auctionType: $auctionType, criteria: $criteria, from: $from, sort: $sort, size: $size, owner: $owner) {\n    total\n    results {\n      ...AxieRowData\n      __typename\n    }\n    __typename\n  }\n}\n\nfragment AxieRowData on Axie {\n  id\n  image\n  class\n  name\n  genes\n  birthDate\n  matronId\n  sireId\n  owner\n  class\n  stage\n  title\n  breedCount\n  level\n  parts {\n    ...AxiePart\n    __typename\n  }\n  stats {\n    ...AxieStats\n    __typename\n  }\n  auction {\n    ...AxieAuction\n    __typename\n  }\n  __typename\n}\n\nfragment AxiePart on AxiePart {\n  id\n  name\n  class\n  type\n  specialGenes\n  stage\n  abilities {\n    ...AxieCardAbility\n    __typename\n  }\n  __typename\n}\n\nfragment AxieCardAbility on AxieCardAbility {\n  id\n  name\n  attack\n  defense\n  energy\n  description\n  backgroundUrl\n  effectIconUrl\n  __typename\n}\n\nfragment AxieStats on AxieStats {\n  hp\n  speed\n  skill\n  morale\n  __typename\n}\n\nfragment AxieAuction on Auction {\n  startingPrice\n  endingPrice\n  startingTimestamp\n  endingTimestamp\n  duration\n  timeLeft\n  currentPrice\n  currentPriceUSD\n  suggestedPrice\n  seller\n  listingIndex\n  state\n  __typename\n}\n"
	}
	return data

def start_ownerquery_details(owner, index = 0):
	API_ENDPOINT = "https://axieinfinity.com/graphql-server-v2/graphql"
	query_result = ownerquery_details(owner, index = index)
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