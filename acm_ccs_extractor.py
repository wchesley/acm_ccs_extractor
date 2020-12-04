from bs4 import BeautifulSoup
import sys
json_file = open("acm_css_fixture.json", "w+")
html = open("ref.html", "r")
try:
    soup = BeautifulSoup(html, "html.parser")
    print("read the file")
    id = 1
    openbrace = "{"
    closebrace = "}"
    json_file.write("[")
    no_dups = []
    ccs = soup.find_all(href="javascript:void(0)")
    for item in ccs:
        if item.text not in no_dups:
            no_dups.append(item.text)
            print(f"CCS:{item.text} ID:{id}\n")
            json_file.write(
                f"\n{openbrace}\n\t\"model\":\"taggit.Tag\",\n\t\"pk\":{id},\n\t\"fields\":{openbrace}\n\t\t\"name\":\"{item.text}\",\n\t\t\"slug\":\"{item.text}\"\n\t{closebrace}\n{closebrace},")
            id += 1
except:
    print("Unexpected error:", sys.exc_info()[0])
    raise
json_file.write("]")
json_file.close()