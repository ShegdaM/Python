import xml.etree.cElementTree as ET

f = open('a.txt', 'r')
check = []


def func(item):
    count = 0
    for i in f.read().split():
        if i == item:
            count += 1
    return count


root = ET.Element("root")
words = ET.SubElement(root, "words")

i = 1
for item in f.read().split():
    if item in check:
        continue
    count = func(item)
    ET.SubElement(words, "word"+str(i), name=item).text = str(count)
    check.append(item)
    i += 1

tree = ET.ElementTree(root)
tree.write("c.xml")
