import xml.etree.ElementTree as ET
from xml.parsers import expat

name_space = r"{http://www.microsoft.com/GroupPolicy/Rsop}"


# check value in xml file
def check(path_file):
    tree = ET.parse(path_file)
    root = tree.getroot()

    for computer_result_tag in root:
        if "}ComputerResults" in computer_result_tag.tag:
            for extension_data_tag in computer_result_tag:
                if "}ExtensionData" in extension_data_tag.tag:
                    for extension_tag in extension_data_tag:
                        if "}Extension" in extension_tag.tag:
                            for account_tag in extension_tag:
                                if "}Account" in account_tag.tag:
                                    if account_tag[2].text == "MaximumPasswordAge":
                                        print(account_tag[3].text)
                                        break


def main():
    xml_path_file = r"E:\Codes\utm_fw\python_cis_benchmark\temp\gpo_apply.xml"
    check(xml_path_file)


# main func
if __name__ == "__main__":
    main()
