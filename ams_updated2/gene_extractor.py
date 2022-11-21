import json
import os
from mymodules import split_join
traits = open("./traits.json", "r")
parts = open("./parts.json", "r")
traits_json = json.load(traits)
parts_json = json.load(parts)
class_list = {"0000": "beast", "0001": "bug", "0010": "bird", "0011": "plant", "0100": "aquatic", "0101": "reptile",
			"1000": "mech", "1010": "dusk", "1001": "dawn"}
region_list = {"00000": 'global', "00001": 'japan'}
tags_list = {"00000": 'NoTag', "00001": 'Origin', "00010": 'Agamogenesis', "00011": 'Meo1', "00100": 'Meo2', "000000000000000": 'NoTag',
"000000000000001": 'Origin', "000000000000010": 'Meo1', "000000000000011": 'Meo2'}
part_type = {"11": "Mystic", "00": "Normal", "01": "XMas Gen 1"}

def hex_to_binary(hex_value):
	decimal = int(hex_value, 16)
	binary = bin(decimal)
	if len(binary[2:]) > 256:
		return binary[2:].zfill(512)
	return binary[2:].zfill(256)

def get_genes(hex_value):

	decimal = int(hex_value, 16)
	binary = bin(decimal)
	binary = binary[2:]

	if len(binary) > 256:
		binary = binary.zfill(512)
		axie_class_binary = binary[0:5]
		region_binary = binary[22:40]
		tag_binary = binary[40:55]
		frosty_mystic_binary = binary[55:61]
		body_skin_binary = binary[61:65]
		pattern_d_binary = binary[65:74]
		pattern_r1_binary = binary[74:83]
		pattern_r2_binary = binary[83:92]
		color_d_binary = binary[92:98]
		color_r1_binary = binary[98:104]
		color_r2_binary = binary[104:110]
		frosty_mystic_binary2 = binary[143:149]
		eyes_type_binary = binary[149:153]
		eyes_class_d_binary = binary[153:158]
		eyes_d_binary = binary[158:166]
		eyes_class_r1_binary = binary[166:171]
		eyes_r1_binary = binary[171:179]
		eyes_class_r2_binary = binary[179:184]
		eyes_r2_binary = binary[184:192]
		frosty_mystic_binary3 = binary[207:213]
		mouth_type_binary = binary[213:217]
		mouth_class_d_binary = binary[217:222]
		mouth_d_binary = binary[222:230]
		mouth_class_r1_binary = binary[230:235]
		mouth_r1_binary = binary[235:243]
		mouth_class_r2_binary = binary[243:248]
		mouth_r2_binary = binary[248:256]
		frosty_mystic_binary4 = binary[271:277]
		ears_type_binary = binary[277:281]
		ears_class_d_binary = binary[281:286]
		ears_d_binary = binary[286:294]
		ears_class_r1_binary = binary[294:299]
		ears_r1_binary = binary[299:307]
		ears_class_r2_binary = binary[307:312]
		ears_r2_binary = binary[312:320]
		frosty_mystic_binary5 = binary[335:341]
		horn_type_binary = binary[341:345]
		horn_class_d_binary = binary[345:350]
		horn_d_binary = binary[350:358]
		horn_class_r1_binary = binary[358:363]
		horn_r1_binary = binary[363:371]
		horn_class_r2_binary = binary[371:376]
		horn_r2_binary = binary[376:384]
		frosty_mystic_binary6 = binary[399:405]
		back_type_binary = binary[405:409]
		back_class_d_binary = binary[409:414]
		back_d_binary = binary[414:422]
		back_class_r1_binary = binary[422:427]
		back_r1_binary = binary[427:435]
		back_class_r2_binary = binary[435:440]
		back_r2_binary = binary[440:448]
		frosty_mystic_binary7 = binary[463:469]
		tail_type_binary = binary[469:473]
		tail_class_d_binary = binary[473:478]
		tail_d_binary = binary[478:486]
		tail_class_r1_binary = binary[486:491]
		tail_r1_binary = binary[491:499]
		tail_class_r2_binary = binary[499:504]
		tail_r2_binary = binary[504:512]


	else:
		binary = binary.zfill(256)

		axie_class_binary = binary[0:4]
		padding1_binary = binary[4:8]
		region_binary = binary[8:13]
		tag_binary = binary[13:18]
		body_skin_binary = binary[18:22]
		old_xmas_gen_binary = binary[22:34]
		pattern_d_binary = binary[34:40]
		pattern_r1_binary = binary[40:46]
		pattern_r2_binary = binary[46:52]
		color_d_binary = binary[52:56]
		color_r1_binary = binary[56:60]
		color_r2_binary = binary[60:64]
		eyes_type_binary = binary[64:66]
		eyes_class_d_binary = binary[66:70]
		eyes_d_binary = binary[70:76]
		eyes_class_r1_binary= binary[76:80]
		eyes_r1_binary = binary[80:86]
		eyes_class_r2_binary = binary[86:90]
		eyes_r2_binary = binary[90:96]
		mouth_type_binary = binary[96:98]
		mouth_class_d_binary = binary[98:102]
		mouth_d_binary = binary[102:108]
		mouth_class_r1_binary = binary[108:112]
		mouth_r1_binary = binary[112:118]
		mouth_class_r2_binary = binary[118:122]
		mouth_r2_binary = binary[122:128]
		ears_type_binary = binary[128:130]
		ears_class_d_binary = binary[130:134]
		ears_d_binary = binary[134:140]
		ears_class_r1_binary = binary[140:144]
		ears_r1_binary = binary[144:150]
		ears_class_r2_binary = binary[150:154]
		ears_r2_binary = binary[154:160]
		horn_type_binary = binary[160:162]
		horn_class_d_binary = binary[162:166]
		horn_d_binary = binary[166:172]
		horn_class_r1_binary = binary[172:176]
		horn_r1_binary = binary[176:182]
		horn_class_r2_binary = binary[182:186]
		horn_r2_binary = binary[186:192]
		back_type_binary = binary[192:194]
		back_class_d_binary = binary[194:198]
		back_d_binary = binary[198:204]
		back_class_r1_binary = binary[204:208]
		back_r1_binary = binary[208:214]
		back_class_r2_binary = binary[214:218]
		back_r2_binary = binary[218:224]
		tail_type_binary = binary[224:226]
		tail_class_d_binary= binary[226:230]
		tail_d_binary = binary[230:236]
		tail_class_r1_binary = binary[236:240]
		tail_r1_binary = binary[240:246]
		tail_class_r2_binary = binary[246:250]
		tail_r2_binary = binary[250:256]


	hex512 = len(binary) > 256
	if hex512:
		json_class = traits_json[class_list[axie_class_binary[-4:]]]
		axie_class = class_list[axie_class_binary[-4:]]
		region = region_list[region_binary[-5:]]
		tag = tags_list[tag_binary[-5:]]
	else:
		json_class = traits_json[class_list[axie_class_binary]]
		axie_class = class_list[axie_class_binary]
		region = region_list[region_binary]
		tag = tags_list[tag_binary]
	pattern = {"d": pattern_d_binary, "r1": pattern_r1_binary, "r2": pattern_r2_binary}
	color = {"d": color_d_binary, "r1": color_r1_binary, "r2": color_r2_binary}

	if hex512:
		eyes_class_d = class_list[eyes_class_d_binary[-4:]]
		eyes_d = traits_json[eyes_class_d]['eyes'][eyes_d_binary[-6:]]
		eyes_class_r1 = class_list[eyes_class_r1_binary[-4:]]
		eyes_r1 = traits_json[eyes_class_r1]['eyes'][eyes_r1_binary[-6:]]
		eyes_class_r2 = class_list[eyes_class_r2_binary[-4:]]
		eyes_r2 = traits_json[eyes_class_r2]['eyes'][eyes_r2_binary[-6:]]
	else:
		eyes_class_d = class_list[eyes_class_d_binary]
		eyes_d = traits_json[eyes_class_d]['eyes'][eyes_d_binary]
		eyes_class_r1 = class_list[eyes_class_r1_binary]
		eyes_r1 = traits_json[eyes_class_r1]['eyes'][eyes_r1_binary]
		eyes_class_r2 = class_list[eyes_class_r2_binary]
		eyes_r2 = traits_json[eyes_class_r2]['eyes'][eyes_r2_binary]

	eyes = {
		"d": eyes_d['global'],
		"r1": eyes_r1['global'],
		"r2": eyes_r2['global']
	}

	for k, v in eyes.items():
		part = "eyes"
		name = v.lower()
		splitted_name = v.split(" ")
		if len(splitted_name) > 1:
			name = "-".join([x.lower() for x in splitted_name])
		part_id = f"{part}-{name}"
		part_json = parts_json[part_id]
		eyes[k] = part_json

	if hex512:
		ears_class_d = class_list[ears_class_d_binary[-4:]]
		ears_d = traits_json[ears_class_d]['ears'][ears_d_binary[-6:]]
		ears_class_r1 = class_list[ears_class_r1_binary[-4:]]
		ears_r1 = traits_json[ears_class_r1]['ears'][ears_r1_binary[-6:]]
		ears_class_r2 = class_list[ears_class_r2_binary[-4:]]
		ears_r2 = traits_json[ears_class_r2]['ears'][ears_r2_binary[-6:]]
	else:
		ears_class_d = class_list[ears_class_d_binary]
		ears_d = traits_json[ears_class_d]['ears'][ears_d_binary]
		ears_class_r1 = class_list[ears_class_r1_binary]
		ears_r1 = traits_json[ears_class_r1]['ears'][ears_r1_binary]
		ears_class_r2 = class_list[ears_class_r2_binary]
		ears_r2 = traits_json[ears_class_r2]['ears'][ears_r2_binary]

	ears = {
		"d": ears_d['global'],
		"r1": ears_r1['global'],
		"r2": ears_r2['global']
	}

	for k, v in ears.items():
		part = "ears"
		name = v.lower()
		splitted_name = v.split(" ")
		if len(splitted_name) > 1:
			name = "-".join([x.lower() for x in splitted_name])
		part_id = f"{part}-{name}"
		part_json = parts_json[part_id]
		ears[k] = part_json

	if hex512:
		horn_class_d = class_list[horn_class_d_binary[-4:]]
		horn_d = traits_json[horn_class_d]['horn'][horn_d_binary[-6:]]
		horn_class_r1 = class_list[horn_class_r1_binary[-4:]]
		horn_r1 = traits_json[horn_class_r1]['horn'][horn_r1_binary[-6:]]
		horn_class_r2 = class_list[horn_class_r2_binary[-4:]]
		horn_r2 = traits_json[horn_class_r2]['horn'][horn_r2_binary[-6:]]
	else:
		horn_class_d = class_list[horn_class_d_binary]
		horn_d = traits_json[horn_class_d]['horn'][horn_d_binary]
		horn_class_r1 = class_list[horn_class_r1_binary]
		horn_r1 = traits_json[horn_class_r1]['horn'][horn_r1_binary]
		horn_class_r2 = class_list[horn_class_r2_binary]
		horn_r2 = traits_json[horn_class_r2]['horn'][horn_r2_binary]

	horn = {
		"d": horn_d['global'],
		"r1": horn_r1['global'],
		"r2": horn_r2['global']
	}

	for k, v in horn.items():
		part = "horn"
		name = v.lower()
		splitted_name = v.split(" ")
		if len(splitted_name) > 1:
			name = "-".join([x.lower() for x in splitted_name])
		part_id = f"{part}-{name}"
		part_json = parts_json[part_id]
		horn[k] = part_json


	if hex512:
		mouth_class_d = class_list[mouth_class_d_binary[-4:]]
		mouth_d = traits_json[mouth_class_d]['mouth'][mouth_d_binary[-6:]]
		mouth_class_r1 = class_list[mouth_class_r1_binary[-4:]]
		mouth_r1 = traits_json[mouth_class_r1]['mouth'][mouth_r1_binary[-6:]]
		mouth_class_r2 = class_list[mouth_class_r2_binary[-4:]]
		mouth_r2 = traits_json[mouth_class_r2]['mouth'][mouth_r2_binary[-6:]]
	else:
		mouth_class_d = class_list[mouth_class_d_binary]
		mouth_d = traits_json[mouth_class_d]['mouth'][mouth_d_binary]
		mouth_class_r1 = class_list[mouth_class_r1_binary]
		mouth_r1 = traits_json[mouth_class_r1]['mouth'][mouth_r1_binary]
		mouth_class_r2 = class_list[mouth_class_r2_binary]
		mouth_r2 = traits_json[mouth_class_r2]['mouth'][mouth_r2_binary]

	mouth = {
		"d": mouth_d['global'],
		"r1": mouth_r1['global'],
		"r2": mouth_r2['global']
	}

	for k, v in mouth.items():
		part = "mouth"
		name = v.lower()
		splitted_name = v.split(" ")
		if len(splitted_name) > 1:
			name = "-".join([x.lower() for x in splitted_name])
		part_id = f"{part}-{name}"
		part_json = parts_json[part_id]
		mouth[k] = part_json

	if hex512:
		back_class_d = class_list[back_class_d_binary[-4:]]
		back_d = traits_json[back_class_d]['back'][back_d_binary[-6:]]
		back_class_r1 = class_list[back_class_r1_binary[-4:]]
		back_r1 = traits_json[back_class_r1]['back'][back_r1_binary[-6:]]
		back_class_r2 = class_list[back_class_r2_binary[-4:]]
		back_r2 = traits_json[back_class_r2]['back'][back_r2_binary[-6:]]
	else:
		back_class_d = class_list[back_class_d_binary]
		back_d = traits_json[back_class_d]['back'][back_d_binary]
		back_class_r1 = class_list[back_class_r1_binary]
		back_r1 = traits_json[back_class_r1]['back'][back_r1_binary]
		back_class_r2 = class_list[back_class_r2_binary]
		back_r2 = traits_json[back_class_r2]['back'][back_r2_binary]

	back = {
		"d": back_d['global'],
		"r1": back_r1['global'],
		"r2": back_r2['global']
	}

	for k, v in back.items():
		part = "back"
		name = v.lower()
		splitted_name = v.split(" ")
		if len(splitted_name) > 1:
			name = "-".join([x.lower() for x in splitted_name])
		part_id = f"{part}-{name}"
		part_json = parts_json[part_id]
		back[k] = part_json



	if hex512:
		tail_class_d = class_list[tail_class_d_binary[-4:]]
		tail_d = traits_json[tail_class_d]['tail'][tail_d_binary[-6:]]
		tail_class_r1 = class_list[tail_class_r1_binary[-4:]]
		tail_r1 = traits_json[tail_class_r1]['tail'][tail_r1_binary[-6:]]
		tail_class_r2 = class_list[tail_class_r2_binary[-4:]]
		tail_r2 = traits_json[tail_class_r2]['tail'][tail_r2_binary[-6:]]
	else:
		tail_class_d = class_list[tail_class_d_binary]
		tail_d = traits_json[tail_class_d]['tail'][tail_d_binary]
		tail_class_r1 = class_list[tail_class_r1_binary]
		tail_r1 = traits_json[tail_class_r1]['tail'][tail_r1_binary]
		tail_class_r2 = class_list[tail_class_r2_binary]
		tail_r2 = traits_json[tail_class_r2]['tail'][tail_r2_binary]

	tail = {
		"d": tail_d['global'],
		"r1": tail_r1['global'],
		"r2": tail_r2['global']
	}

	for k, v in tail.items():
		part = "tail"
		name = v.lower()
		splitted_name = v.split(" ")
		if len(splitted_name) > 1:
			name = "-".join([x.lower() for x in splitted_name])
		part_id = f"{part}-{name}"
		part_json = parts_json[part_id]
		tail[k] = part_json


	data = {
		"cls": axie_class,
		"region": region,
		"tag": tag,
		'bodySkin': "",
		"pattern": pattern,
		"color": color,
		"eyes": eyes,
		"ears": ears,
		"horn": horn,
		"mouth": mouth,
		"back": back,
		"tail": tail
	}

	return data

def getPartGene256(binary, part):
	try:
		if "0b" in binary:
			x = f"0b{binary}"
			v = int(x, 2)
			binary = bin(v)
			binary = binary[2:]
	except ValueError:
		raise ValueError(f"Invalid binary value {binary}")
	search_part = part.title()
	body_parts = ["Mouth", "Horn", "Back", "Tail"]
	if search_part in body_parts:
		part_type_binary = binary[0:2]
		d_class_binary = binary[2:6]
		d_class = class_list[d_class_binary]
		d_binary = binary[6:12]
		d_trait = traits_json[d_class][search_part.lower()][d_binary]
		r1_class_binary = binary[12:16]
		r1_class = class_list[r1_class_binary]
		r1_binary = binary[16:22]
		r1_trait = traits_json[r1_class][search_part.lower()][r1_binary]
		r2_class_binary = binary[22:26]
		r2_class = class_list[r2_class_binary]
		r2_binary = binary[26:32]
		r2_trait = traits_json[r2_class][search_part.lower()][r2_binary]
		traits = {"d": d_trait['global'], "r1": r1_trait['global'], "r2": r2_trait['global']}
		for k, v in traits.items():
			part = search_part.lower()
			part_name = split_join(v.lower(), " ", "-")
			part_id = f"{part}-{part_name}"
			value_json = parts_json[part_id]
			traits[k] = value_json

		return traits


	else:
		raise IndexError(f"Part Not Found ({search_part})")

def getPartGene512(binary, part):
	try:
		if "0b" in binary:
			x = f"0b{binary}"
			v = int(x, 2)
			binary = bin(v)
			binary = binary[2:]
	except ValueError:
		raise ValueError(f"Invalid binary value {binary}")
	search_part = part.title()
	body_parts = ["Mouth", "Horn", "Back", "Tail"]
	if search_part in body_parts:
		part_type_binary = binary[0:4]
		d_class_binary = binary[4:9]
		d_class = class_list[d_class_binary[-4:]]
		d_binary = binary[9:17]
		d_trait = traits_json[d_class][search_part.lower()][d_binary[-6:]]
		r1_class_binary = binary[17:22]
		r1_class = class_list[r1_class_binary[-4:]]
		r1_binary = binary[22:30]
		r1_trait = traits_json[r1_class][search_part.lower()][r1_binary[-6:]]
		r2_class_binary = binary[30:35]
		r2_class = class_list[r2_class_binary[-4:]]
		r2_binary = binary[35:43]
		r2_trait = traits_json[r2_class][search_part.lower()][r2_binary[-6:]]
		traits = {"d": d_trait['global'], "r1": r1_trait['global'], "r2": r2_trait['global']}
		for k, v in traits.items():
			part = search_part.lower()
			part_name = split_join(v.lower(), " ", "-")
			part_id = f"{part}-{part_name}"
			value_json = parts_json[part_id]
			traits[k] = value_json

		return traits


	else:
		raise IndexError(f"Part Not Found ({search_part})")

gene512 = get_genes("0x280000000000010040412090830C0000000101942040440A00010190284082040001018C2061000A000101801021400400010180204080060001018418404008")
dec = int("0x280000000000010040412090830C0000000101942040440A00010190284082040001018C2061000A000101801021400400010180204080060001018418404008", 16)
binary = bin(dec)[2:].zfill(512)
tail_bin = binary[469:512]
print(getPartGene512(tail_bin, "tail"))

