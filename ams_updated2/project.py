import urllib.request
import os
import json

#must be on the same directory as the axie.txt file
url_genes = "https://api.axie.technology/getgenes"
url_axies = "https://api.axie.technology/getaxies"
axies = open("./axie.txt", "r")
axie_list = [x.strip() for x in axies.readlines()]

def check_save_to_list(mylist):
	dirlist = os.listdir()
	if "gene_list.json" not in dirlist:
		x = open("./genes_list.json", "w")
		x.write("[\n]")
		x.close()
		if "axies_list.json" not in dirlist:
			x = open("./axies_list.json", "w")
			x.write("[\n]")
			x.close()
	f1 = open("./genes_list.json")
	f2 = open("./axies_list.json")
	axie_gene_list_id = json.load(f1)
	axie_detail_list_id = json.load(f2)
	genes_id = [x['axieId'] for x in axie_gene_list_id]
	axies_id = [x['story_id'] for x in axie_detail_list_id]
	list1 = list(set(axie_list) - set(genes_id))
	list2 = list(set(axie_list) - set(axies_id))

	#check if passed list is already in the current list
	if len(list1) <= 0:
		pass
	else:
		list1 = ",".join(list1)
		genes = urllib.request.urlopen(f"{url_genes}/{list1}")
		data = json.loads(genes.read())
		axie_gene_list_id += data
		with open("./genes_list.json", "w") as outfile:
			json.dump(axie_gene_list_id, outfile)


	#check if passed list is already in the current list
	if len(list2) <= 0:
		pass
	else:
		list2 = ",".join(list2)
		axies = urllib.request.urlopen(f"{url_axies}/{list2}")
		data = json.loads(axies.read())
		axie_detail_list_id += data
		with open("./axies_list.json", "w") as outfile:
			json.dump(axie_detail_list_id, outfile)

	return {'genes': axie_gene_list_id, 'details': axie_detail_list_id}

x = check_save_to_list(axie_list)













