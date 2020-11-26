import sys
import xml.etree.ElementTree as ET
import xml.dom.minidom as MIN


def fix_law():
    law_xml = sys.argv[1]
    change_xml = sys.argv[2]
    apply_change(law_xml, change_xml)
    print('DONE')


def apply_change(law_xml, change_xml):
    tree = ET.parse(change_xml)
    change_root = tree.getroot()
    tree = ET.parse(law_xml)
    root = tree.getroot()

    if change_root.findall("new_title"):
        list(root)[0].text = change_root.find("new_title").text
        CHsections = (list(change_root[3]))
    else:
        CHsections = (list(change_root[2]))

    for i in range(len(CHsections)):
        CHsection = (list(CHsections[i]))
        number = CHsection[0].text

        if (len(CHsection) == 1):
            delete(law_xml, number, root)

        elif (len(CHsection) == 2):
            section = CHsection[1]
            father = CHsection[0].text
            add(law_xml, father, section, root)

        elif (len(CHsection) == 3):
            father = CHsection[1].text
            section = CHsection[2]
            exchange(law_xml, number, father, section, root)

        write_to_file(root, law_xml)


def add(law_xml, father, section, root):
    sections = (list(root))[1]
    print('Inserting law number', section[0].text, '...')
    count = 0
    for sec in root.findall("./sections/section"):
        count += 1
        if (sec.find("./number").text == father):
            print(count)
            sections.insert(count, section)


def exchange(law_xml, number, father, section, root):
    print('Exchanging section number', number, '...')
    delete(law_xml, number, root)
    add(law_xml, father, section, root)


def delete(law_xml, number, root):
    sections = (list(root[1]))
    for sec in root.findall("./sections/section"):
        if (sec.find("./number").text == str(number)):
            print('Deleting law number', number, '...')
            root.find("./sections").remove(sec)
            return
    print("ERROR: didn't find law number ", number)


def write_to_file(root, law_xml):
    res = MIN.parseString(ET.tostring(root)).toprettyxml()
    with open(law_xml, "w", 1, "utf-8") as f:
        f.write(res)


if __name__ == '__main__':
    fix_law()
