import json
import os
from mymodules import hex_to_binary_256, hex_to_binary_512, split_join
traits = json.load(open("./traits.json", "r"))
parts = json.load(open("./parts.json", "r"))

class_list = {"0000": "beast", "0001": "bug", "0010": "bird", "0011": "plant", "0100": "aquatic", "0101": "reptile",
			"1000": "mech", "1010": "dusk", "1001": "dawn"}

region_list = {"00000": 'global', "00001": 'japan'}

tags_list = {"00000": 'NoTag', "00001": 'Origin', "00010": 'Agamogenesis', "00011": 'Meo1', "00100": 'Meo2', "000000000000000": 'NoTag',
"000000000000001": 'Origin', "000000000000010": 'Meo1', "000000000000011": 'Meo2'}

part_type = {"0000": "Normal", "0001": "Mystic", "0011": "JP", "0101": "Xmas Gen 2"}

class Eyes:

	def __init__(self):
		self.name = "eyes"

class Ears:

	def __init__(self):
		self.name = "ears"

class Horn:

	def __init__(self):
		self.name = "horn"

class Mouth:

	def __init__(self):
		self.name = "mouth"

class Back:

	def __init__(self):
		self.name = "back"

class Tail:

	def __init__(self):
		self.name = "tail"


class Pattern256:

	def __init__(self, binary):
		self.binary = binary
		self.part = "pattern"
		self.d = self.binary[0:6]
		self.r1 = self.binary[6:12]
		self.r2 = self.binary[12:18]
		self.gene = {"d": self.d, "r1": self.r1, "r2": self.r2}

	def __str__(self):
		return f"{self.gene}"

class Color256:

	def __init__(self, binary):
		self.binary = binary
		self.part = "color"
		self.d = self.binary[0:4]
		self.r1 = self.binary[4:8]
		self.r2 = self.binary[8:12]
		self.gene = {"d": self.d, "r1": self.r1, "r2": self.r2}

	def __str__(self):
		return f"{self.gene}"

class Pattern512:

	def __init__(self, binary):
		self.binary = binary
		self.part = "pattern"
		self.d = self.binary[0:9]
		self.r1 = self.binary[9:18]
		self.r2 = self.binary[18:27]
		self.gene = {"d": self.d, "r1": self.r1, "r2": self.r2}

	def __str__(self):
		return f"{self.gene}"

class Color512:

	def __init__(self, binary):
		self.binary = binary
		self.part = "color"
		self.d = self.binary[0:6]
		self.r1 = self.binary[6:12]
		self.r2 = self.binary[12:18]
		self.gene = {"d": self.d, "r1": self.r1, "r2": self.r2}

	def __str__(self):
		return f"{self.gene}"


class Part256:

	def __init__(self, binary, part):
		self.binary = binary
		self.type = self.binary[:2]
		self.part = part.name
		self.dClassBin = self.binary[2:6]
		self.dBin = self.binary[6:12]
		self.r1ClassBin = self.binary[12:16]
		self.r1Bin = self.binary[16:22]
		self.r2ClassBin = self.binary[22:26]
		self.r2Bin = self.binary[26:32]
		self.dClass = class_list[self.dClassBin]
		self.r1Class = class_list[self.r1ClassBin]
		self.r2Class = class_list[self.r2ClassBin]
		self.dName = traits[self.dClass][self.part][self.dBin]['global'].lower()
		self.dId = self.part + "-" + split_join(self.dName, " ", "-")
		self.d = parts[self.dId]
		self.r1Name = traits[self.r1Class][self.part][self.r1Bin]['global'].lower()
		self.r1Id = self.part + "-" + split_join(self.r1Name, " ", "-")
		self.r1 = parts[self.r1Id]
		self.r2Name = traits[self.r2Class][self.part][self.r2Bin]['global'].lower()
		self.r2Id = self.part + "-" + split_join(self.r2Name, " ", "-")
		self.r2 = parts[self.r2Id]

		self.gene = {self.part: {"d": self.d, "r1": self.r1, "r2": self.r2}}

	def __str__(self):
		return f"{self.gene}"


class GeneBin256:

	def __init__(self, binary):
		self.binary = binary
		self.cls = self.binary[0:4]
		self.region = self.binary[8:13]
		self.tag = self.binary[13:18]
		self.bodySkin = self.binary[18:22]
		self.xmas = self.binary[22:34]
		self.pattern = self.binary[34:52]
		self.color = self.binary[52:64]
		self.eyes = self.binary[64:96]
		self.mouth = self.binary[96:128]
		self.ears = self.binary[128:160]
		self.horn = self.binary[160:192]
		self.back = self.binary[192:224]
		self.tail = self.binary[224:256]

class GetGenes256:

	@property
	def pureness(self):
		pureness = 0
		parts = [self.eyes.dClass, self.ears.dClass, self.mouth.dClass, self.horn.dClass, self.back.dClass, self.tail.dClass]
		for x in parts:
			if x == self.cls:
				pureness += 1
		return pureness

	@property
	def purity(self):
		purity = 100
		parts = [self.eyes.gene, self.ears.gene, self.horn.gene, self.mouth.gene, self.back.gene, self.tail.gene]
		for part in parts:
			for k, v in part.items():
				for a, b in v.items():
					if b['class'] != self.cls:
						if a == "d":
							deduction = 12.5
						elif a == "r1":
							deduction = 3
						elif a == "r2":
							deduction = 1
						purity -= deduction
		return purity
	

	@property
	def genes(self):
		genes = {
		"cls": self.cls, "region": self.region, "tag": tags_list[self.geneBin.tag],
		"pattern": self.pattern.gene, "color": self.color.gene, 
			"eyes": self.eyes.gene, "ears": self.ears.gene, "horn": self.horn.gene, "mouth": self.mouth.gene, "back": self.back.gene, "tail": self.tail.gene
			}
		return genes
	

	def __init__(self, hex_value):
		self.hex_value = hex_value
		self.binary = hex_to_binary_256(self.hex_value)
		self.geneBin = GeneBin256(self.binary)
		self.region = region_list[self.geneBin.region]
		self.cls = class_list[self.geneBin.cls]
		self.eyes = Part256(self.geneBin.eyes, Eyes())
		self.ears = Part256(self.geneBin.ears, Ears())
		self.horn = Part256(self.geneBin.horn, Horn())
		self.mouth = Part256(self.geneBin.mouth, Mouth())
		self.back = Part256(self.geneBin.back, Back())
		self.tail = Part256(self.geneBin.eyes, Tail())
		self.pattern = Pattern256(self.geneBin.pattern)
		self.color = Color256(self.geneBin.color)



	@property
	def hex_value(self):
		return self._hex_value
	
	@hex_value.setter
	def hex_value(self, value):
		if isinstance(value, int):
			raise TypeError("Hex Value Must Be String Format")
		if "0x" not in value:
			raise ValueError("Invalid Hex Value")
		self._hex_value = value

	def __str__(self):
		return f"{self.genes}"


class Part512:

	def __init__(self, binary, part):
		self.binary = binary
		self.type = self.binary[0:4]
		type_s = self.type[-2:]
		self.part = part.name
		self.dClassBin = self.binary[4:9]
		dClassBin_s = self.dClassBin[-4:]
		self.dBin = self.binary[9:17]
		dBin_s = self.dBin[-6:]
		self.r1ClassBin = self.binary[17:22]
		r1ClassBin_s = self.r1ClassBin[-4:]
		self.r1Bin = self.binary[22:30]
		r1Bin_s = self.r1Bin[-6:]
		self.r2ClassBin = self.binary[30:35]
		r2ClassBin_s = self.r2ClassBin[-4:]
		self.r2Bin = self.binary[35:43]
		r2Bin_s = self.r2Bin[-6:]
		# _s variables splices their corresponding variables to be able to get the correct binary value
		self.dClass = class_list[dClassBin_s]
		self.r1Class = class_list[r1ClassBin_s]
		self.r2Class = class_list[r2ClassBin_s]
		self.dName = traits[self.dClass][self.part][dBin_s]['global'].lower()
		self.dId = self.part + "-" + split_join(self.dName, " ", "-")
		self.d = parts[self.dId]
		self.r1Name = traits[self.r1Class][self.part][r1Bin_s]['global'].lower()
		self.r1Id = self.part + "-" + split_join(self.r1Name, " ", "-")
		self.r1 = parts[self.r1Id]
		self.r2Name = traits[self.r2Class][self.part][r2Bin_s]['global'].lower()
		self.r2Id = self.part + "-" + split_join(self.r2Name, " ", "-")
		self.r2 = parts[self.r2Id]
		self.gene = {self.part: {"d": self.d, "r1": self.r1, "r2": self.r2}}

	def __str__(self):
		return f"{self.gene}"

class GeneBin512:

	def __init__(self, binary):
		self.binary = binary
		self.cls = self.binary[0:5]
		self.region = self.binary[22:40]
		self.tag = self.binary[40:55]
		self.bodySkin = self.binary[61:65]
		self.pattern = self.binary[65:92]
		self.color = self.binary[92:110]
		self.eyes = self.binary[149:192]
		self.mouth = self.binary[213:256]
		self.ears = self.binary[277:320]
		self.horn = self.binary[341:384]
		self.back = self.binary[405:448]
		self.tail = self.binary[469:512]


class GetGenes512:
	@property
	def purity(self):
		purity = 100
		parts = [self.eyes.gene, self.ears.gene, self.horn.gene, self.mouth.gene, self.back.gene, self.tail.gene]
		for part in parts:
			for k, v in part.items():
				for a, b in v.items():
					if b['class'] != self.cls:
						if a == "d":
							deduction = 12.5
						elif a == "r1":
							deduction = 3
						elif a == "r2":
							deduction = 1
						purity -= deduction
		return purity

	@property
	def pureness(self):
		pureness = 0
		parts = [self.eyes.dClass, self.ears.dClass, self.mouth.dClass, self.horn.dClass, self.back.dClass, self.tail.dClass]
		for x in parts:
			if x == self.cls:
				pureness += 1
		return pureness
	

	def __init__(self, hex_value):
		self.hex_value = hex_value
		self.binary = hex_to_binary_512(self.hex_value)
		self.geneBin = GeneBin512(self.binary)
		self.region = region_list[self.geneBin.region[-5:]]
		self.cls = class_list[self.geneBin.cls[-4:]]
		self.eyes = Part512(self.geneBin.eyes, Eyes())
		self.ears = Part512(self.geneBin.ears, Ears())
		self.horn = Part512(self.geneBin.horn, Horn())
		self.mouth = Part512(self.geneBin.mouth, Mouth())
		self.back = Part512(self.geneBin.back, Back())
		self.tail = Part512(self.geneBin.eyes, Tail())
		self.pattern = Pattern512(self.geneBin.pattern)
		self.color = Color512(self.geneBin.color)

	@property
	def hex_value(self):
		return self._hex_value

	
	@hex_value.setter
	def hex_value(self, value):
		if isinstance(value, int):
			raise TypeError("Hex Value Must Be String Format")
		if "0x" not in value:
			raise ValueError("Invalid Hex Value")
		self._hex_value = value

	def __str__(self):
		return f"{self.genes}"

	@property
	def genes(self):
		genes = {
		"cls": self.cls, "region": self.region, "tag": tags_list[self.geneBin.tag],
		"pattern": self.pattern.gene, "color": self.color.gene, 
			"eyes": self.eyes.gene, "ears": self.ears.gene, "horn": self.horn.gene, "mouth": self.mouth.gene, "back": self.back.gene, "tail": self.tail.gene
			}
		return genes

def getPartGene256(binary, BodyClass):
	#BodyClasses are Tail(), Horn(), Mouth(), Eyes(), Ears() and Back()
	part = Part256(binary, BodyClass)
	return part

def getPartGene512(binary, BodyClass):
	#BodyClasses are Tail(), Horn(), Mouth(), Eyes(), Ears() and Back()
	part = Part512(binary, BodyClass)
	return part

