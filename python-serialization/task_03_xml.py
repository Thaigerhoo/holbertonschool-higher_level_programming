#!/usr/bin/python3
import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """

    Serialize a dictionary to an XML file.

    Args:
        dictionary: The dictionary to serialize.
        filename: The file to save the XML to.

    """
    def add_items(parent, d):
        """

        Add dictionary items to the XML tree.

        Parameters:
            parent: The parent XML element.
            d: The dictionary to add to the XML tree.

        """
        for key, value in d.items():
            element = ET.SubElement(parent, key)
            if isinstance(value, dict):
                add_items(element, value)
            else:
                element.text = str(value)

    root = ET.Element("data")
    add_items(root, dictionary)
    tree = ET.ElementTree(root)
    tree.write(filename)


def deserialize_from_xml(filename):
    """

    Deserialize an XML file to a dictionary.

    Parameter:
        filename: Is the name of the XML file to read.

    Returns:
        dict: The deserialized dictionary.

    """
    def parse_element(element):
        """
        Convert XML element and its children to a dictionary.

        Parameter:
            element: The XML element to convert.

        Returns:
            dict: The converted dictionary.
        """
        parsed_dict = {}
        for child in element:
            if len(child) > 0:
                parsed_dict[child.tag] = parse_element(child)
            else:
                parsed_dict[child.tag] = child.text
        return parsed_dict

    tree = ET.parse(filename)
    root = tree.getroot()
    return parse_element(root)
