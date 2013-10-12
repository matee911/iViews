# coding: utf-8
"""
Realny przykład wykorzystania wzorca
fabryki abstrakcyjnej wraz z implementacją
"""

from __future__ import print_function
import abc
import json
try:
    from lxml import etree as ET
except ImportError:
    from xml.etree import ElementTree as ET

ITEMS = [dict(id=i, name='obj %s' % i) for i in range(3)]


class Request(object):
    def __init__(self, accept):
        self.headers = {'Accept': accept}


class SerializerBase(object):
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def items_list(self, items):
        return

    @abc.abstractmethod
    def item_details(self, item):
        return


class XMLSerializer(SerializerBase):
    def items_list(self, items):
        root = ET.Element('items')
        root.extend(self._single_elem(item) for item in items)
        return ET.tostring(root)

    def item_details(self, item):
        root = ET.Element('item')
        id_elem = ET.SubElement(root, 'id')
        id_elem.text = item['id']
        name_elem = ET.SubElement(root, 'name')
        name_elem.text = item['name']
        return ET.tostring(root)

    def _single_elem(self, item):
        elem = ET.Element('item')
        elem.attrib['id'] = str(item['id'])
        return elem


class JSONSerializer(SerializerBase):
    def items_list(self, items):
        # Unfortunately generators aren't JSON serializable
        return json.dumps([dict(id=i['id']) for i in items])

    def item_details(self, item):
        return json.dumps(item)


class SerializerFactory(object):
    def __call__(self, request):
        if request.headers['Accept'] == 'application/xml':
            return XMLSerializer()
        elif request.headers['Accept'] == 'application/json':
            return JSONSerializer()

if __name__ == '__main__':
    print('Registered serializers:')
    map(lambda c: print("* %s" % c.__name__), SerializerBase.__subclasses__())
    print('='*20)

    factory = SerializerFactory()

    serializer = factory(Request('application/xml'))
    print("* Items list for application/xml")
    print(serializer.items_list(ITEMS))
    print("* Item details for application/xml")
    print(serializer.item_details(ITEMS[0]))

    print()
    serializer = factory(Request('application/json'))
    print("* Items list for application/json")
    print(serializer.items_list(ITEMS))
    print("* Item details for application/json")
    print(serializer.item_details(ITEMS[0]))
