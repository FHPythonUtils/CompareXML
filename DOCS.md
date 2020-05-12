<a name=".comparexml"></a>
## comparexml

Compare xml

<a name=".comparexml.compareFiles"></a>
#### compareFiles

```python
compareFiles(xml1, xml2, castTypes=True, numberTol=6)
```

Compare two xml files

**Arguments**:

- `xml1` _string_ - file path for first xml file to compare
- `xml2` _string_ - file path for the second xml file to compare
- `castTypes` _bool, optional_ - cast the xml attributes to python types.
  For instance, cast numbers to floats and compare. Defaults to True.
- `numberTol` _int_ - tolerance number of dp when comparing numbers/ floats.
  Defaults to 6
  

**Returns**:

- `bool` - True/ False equality

<a name=".comparexml.compareAttrib"></a>
#### compareAttrib

```python
compareAttrib(attrib1, attrib2, castTypes=True, numberTol=6)
```

Compare two xml attributes

**Arguments**:

- `xml1` _xml.etree.ElementTree.Element.attrib_ - first xml attribute to compare
- `xml2` _xml.etree.ElementTree.Element.attrib_ - the second xml attribute to compare
- `castTypes` _bool, optional_ - cast the xml attributes to python types.
  For instance, cast numbers to floats and compare. Defaults to True.
- `numberTol` _int_ - tolerance number of dp when comparing numbers/ floats.
  Defaults to 6
  

**Returns**:

- `bool` - True/ False equality

<a name=".comparexml.compareXMLElements"></a>
#### compareXMLElements

```python
compareXMLElements(xml1, xml2, castTypes=True, numberTol=6)
```

Compare two xml elements

**Arguments**:

- `xml1` _xml.etree.ElementTree.Element_ - first xml element to compare
- `xml2` _xml.etree.ElementTree.Element_ - the second xml element to compare
- `castTypes` _bool, optional_ - cast the xml attributes to python types.
  For instance, cast numbers to floats and compare. Defaults to True.
- `numberTol` _int_ - tolerance number of dp when comparing numbers/ floats.
  Defaults to 6
  

**Returns**:

- `bool` - True/ False equality

<a name=".make"></a>
## make

Makefile for python. Run one of the following subcommands:

install: Poetry install
build: Building docs, requirements.txt, setup.py, poetry build

