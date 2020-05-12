""" Compare xml """

from defusedxml.ElementTree import parse


def compareFiles(xml1, xml2, castTypes=True, numberTol=6):
	"""Compare two xml files

	Args:
		xml1 (string): file path for first xml file to compare
		xml2 (string): file path for the second xml file to compare
		castTypes (bool, optional): cast the xml attributes to python types.
		For instance, cast numbers to floats and compare. Defaults to True.
		numberTol (int): tolerance number of dp when comparing numbers/ floats.
		Defaults to 6

	Returns:
		bool: True/ False equality
	"""
	with open(xml1) as x1:
		xm1 = parse(x1).getroot()
	with open(xml2) as x2:
		xm2 = parse(x2).getroot()
	return compareXMLElements(xm1, xm2, castTypes, numberTol)


def compareAttrib(attrib1, attrib2, castTypes=True, numberTol=6):
	"""Compare two xml attributes

	Args:
		xml1 (xml.etree.ElementTree.Element.attrib): first xml attribute to compare
		xml2 (xml.etree.ElementTree.Element.attrib): the second xml attribute to compare
		castTypes (bool, optional): cast the xml attributes to python types.
		For instance, cast numbers to floats and compare. Defaults to True.
		numberTol (int): tolerance number of dp when comparing numbers/ floats.
		Defaults to 6

	Returns:
		bool: True/ False equality
	"""
	if castTypes:
		for attrib in (attrib1, attrib2):
			for key in attrib:
				# Attempt to convert to a number (float type)
				try:
					attrib[key] = round(float(attrib[key]), numberTol)
				except ValueError:
					pass
				# Attempt to convert from python bool and json bool
				if attrib[key] in ("True", "true"):
					attrib[key] = True
				if attrib[key] in ("False", "false"):
					attrib[key] = False
	return attrib1 == attrib2


def compareXMLElements(xml1, xml2, castTypes=True, numberTol=6):
	"""Compare two xml elements

	Args:
		xml1 (xml.etree.ElementTree.Element): first xml element to compare
		xml2 (xml.etree.ElementTree.Element): the second xml element to compare
		castTypes (bool, optional): cast the xml attributes to python types.
		For instance, cast numbers to floats and compare. Defaults to True.
		numberTol (int): tolerance number of dp when comparing numbers/ floats.
		Defaults to 6

	Returns:
		bool: True/ False equality
	"""
	if xml1.tag != xml2.tag:
		print(xml1.tag, xml2.tag)
		return False
	if xml1.text != xml2.text:
		print(xml1.text, xml2.text)
		return False
	if xml1.tail != xml2.tail:
		print(xml1.tail, xml2.tail)
		return False
	if not compareAttrib(xml1.attrib, xml2.attrib, castTypes, numberTol):
		print(xml1.attrib, xml2.attrib)
		return False
	if len(xml1) != len(xml2):
		print(len(xml1), len(xml2))
		return False
	return all(compareXMLElements(c1, c2) for c1, c2 in zip(xml1, xml2))
