#!/usr/bin/env python
# -*- coding: utf-8 -*-
import codecs
import re
import string
import csv
import pandas as pd
from pprint import pprint
from dateparser.search import search_dates
from collections import Counter
import datetime
import jaconv

# read the csv file
reader = codecs.open("original_japanese_internment_cards_data.csv", "r", "utf-8")

card_list = []
# structure the content and put all values in card_list
for row in list(reader):
    count = row.count('"')
    if count != 76:  # remove \" to organise the data analysis
        row = row.replace('\\\"', '')
    card_list.append(re.findall('(?:")([^"]*)(?:")', row))

# print value of a specific row number
i = 0
for content in card_list[6580]:  # row 4 [3]
    # print(str(i) + " " + content)
    i += 1


# check whether a column in a specific row number is empty
def is_empty(any_structure):
    if any_structure:
        # print('Structure is not empty.')
        return False
    else:
        # print('Structure is empty.')
        return True


# thirtyeight = thirtynine = forty = others = 0  # check how many rows are there in the csv file
# for content in card_list:
#     if len(content) == 38:
#         thirtyeight += 1
#     elif len(content) == 39:
#         thirtynine += 1
#     elif len(content) == 40:
#         forty += 1
#     else:
#         print(len(content))
#         others += 1

# # check whether a column in a specific row number is empty
# i = n = 0
# for content in card_list:
#     if is_empty(content[35]) is False:
#         print(i)
#         print(content[1])
#         print(content[35])
#         n += 1
#     i += 1

# remove column 35, because it is empty
for row in card_list:
    del row[35]  # 0 for column 1, 1 for column 2, etc.


# replace a string in the list
def replace_strings_in_list(mylist, dic):
    for a, b in dic.items():
        mylist = [w.replace(a, b) for w in mylist]
    return mylist


def digit_exists(s):
    return any(f.isdigit() for f in s)


phase_two_card_list = []
for item in card_list:
    d = {"ｎ/a": "", "(n/a)": "", "n/a": "", "\u3000": "", "\\n": " ", "■": "", "xxx": "", "--": ""}
    list = replace_strings_in_list(item, d)
    list.append('')
    list.append('male')
    for index, value in enumerate(list):
        value = value.lower()
        value = jaconv.z2h(value, kana=False, digit=True, ascii=True)
        if value.endswith(';'):
            value = value[:-1]
        if index == 1:
            value = re.sub("[(].*?[)]", "", value)
            value = ''.join(filter(lambda character: ord(character) < 0x3000, value))
            value = ''.join([i for i in value if not i.isdigit()])
            if ")" in value or "," in value:
                value = value.replace(")", "").replace(",", "")
            if " van. " in value:
                value = value.replace(" van. ", " van ")
            if " van t " in value:
                value = value.replace(" van t ", " van 't ")
            if " v d " in value or " v/d " in value or " v/d. " in value or " vd. " in value or " v.d " in value:
                value = value.replace(" v d ", " v.d. ").replace(" v/d ", " v.d. ").replace(" v/d. ", " v.d. ").replace(" vd. ", " v.d. ").replace(" v.d ", " v.d. ")
            if " int " in value or " in t " in value:
                value = value.replace(" int ", " in 't ").replace(" in t ", " in 't ")
            if " vander " in value or " van der. " in value or " van.der. " in value:
                value = value.replace(" vander ", " van der ").replace(" van der. ", " van der ").replace(" van.der. ", " van der ")
            if " v.den " in value or " van den. " in value or " van/den " in value:
                value = value.replace(" v.den ", " van den ").replace(" van den. ", " van den ").replace(" van/den ", " van den ")
            if " ter. " in value:
                value = value.replace(" ter. ", " ter ")
            if " de. " in value:
                value = value.replace(" de. ", " de ")
            if " de la. " in value:
                value = value.replace(" de la. ", " de la ")
            value = value.replace('-', ' ').replace('  ', ' ')
            list[index] = value
        if index == 2:
            value = re.sub("[(].*?[)]", "", value)
            value = ''.join(filter(lambda character: ord(character) < 0x3000, value))
            if "v d" in value or "v/d" in value:
                value = value.replace("v/d", "v.d.").replace("v d", "v.d.")
            value = value.replace(")", "").replace('-', ' ').replace('  ', ' ')
            list[index] = value
        if index == 3:
            value = re.sub("[(].*?[)]", "", value)
            value = ''.join(filter(lambda character: ord(character) < 0x3000, value))
            value = ''.join([i for i in value if not i.isdigit()])
            value = value.replace(")", "").replace(",", "").replace('-', ' ').replace('  ', ' ')
            list[index] = value
        if index == 4:
            if digit_exists(value):
                value = ""
            elif value == "(van)" or value == "van," or value == "van.":
                value = "van"
            elif value == "v d" or value == "v/d" or value == "v/d." or value == "v.d.," or value == "v.d," or value == "vd." or value == "v.d":
                value = "v.d."
            elif value == "van t":
                value = "van 't"
            elif value == "int" or value == "in t":
                value = "in 't"
            elif value == "vander" or value == "van der." or value == "van.der." or value == "van der,":
                value = "van der"
            elif value == "v.den" or value == "van den." or value == "van den," or value == "van/den":
                value = "van den"
            elif value == "t":
                value = "'t"
            elif value == "ter." or value == "ter,":
                value = "ter"
            elif value == "de." or value == "de,":
                value = "de"
            elif value == "d":
                value = "d'"
            elif value == "de la.":
                value = "de la"
            list[index] = value
        if index == 5:
            if value == "0000-00-00":
                value = ""
            if value.startswith("08"):
                value = value.replace("08", "18")
            value = value.replace('/', '-')
            list[index] = value
        if index == 6:
            value = ''.join(filter(lambda character: ord(character) < 0x3000, value))
            if "(dutch)" in value:
                value = value.replace("(dutch)", "")
            if "(, indonesia" in value:
                value = value.replace("(, indonesian)", "").replace("(, indonesia)", "")
            if "civ" in value:
                value = value.replace("; civ", "")
            if ":" in value:
                value = value.replace(":", "")
            if "( ; )" in value:
                value = value.replace("( ; )", "")
            if "(; )" in value:
                value = value.replace("(; )", "")
            if "( ;)" in value:
                value = value.replace("( ;)", "")
            if "(;)" in value:
                value = value.replace("(;)", "")
            if "(, )" in value:
                value = value.replace("(, )", "")
            if "()" in value:
                value = value.replace("()", "")
            if "(  )" in value:
                value = value.replace("(  )", "")
            if "( )" in value:
                value = value.replace("( )", "")
            if "()" in value:
                value = value.replace("()", "")
            if "  " in value:
                value = value.replace("  ", " ")
            value = value.rstrip()
            if "netherlands (indonesia)" in value or value == "dutch (indonesian)" or "netherlands (indonesian)" in value or value == "indonesia netherlands" or "netherlands, ind." in value or "ands ('indon" in value or "indonesia, netherlands" in value or "netherlands, indonesia" in value or value == "netherlands; indonesia":
                value = "netherlands, indonesia"
            if "netherlands, father mixed blood" in value:
                value = "netherlands, father mixed blood, mother indonesian"
            if value == "dutch, netherlands" or value == "dutch/netherlands" or value == "dutch." or value == "netherlands/ dutch" or value == "nederlands (nederander)" or value == "dutch" or value == "nederlander" or value == "netherland" or value == "netheralnds" or value == "netherlands (netherlands)" or value == "dutch (dutch)" or value == "nederlands" or value == "holland" or "blanda" in value or "indo-european" in value or "indo european" in value or "ind-european" in value or "netherlands (indonesian " in value:
                value = "netherlands"
            if value == "indonesia  (indonesia)" or value == "indonesia (indonesia)" or value == "indonesia (; indonesia)" or value == "indonesia ('indonesia)" or value == "indonesia (i)" or value == "indonesian" or "east asia" in value or value == "indonesia ( indonesia)":
                value = "indonesia"
            if value == "ambon, indonesia" or value == "ambon indonesia" or value == "ambon" or value == "ambonese, indonesia" or value == "ambon, indonesian" or "ambonese, indonesian" in value or value == "ambonees":
                value = "ambon (indonesia)"
            if value == "menado, indonesia" or value == "menado indonesia" or value == "menado" or value == "menado indonesian" or value == "menadonees" or value == "menado, indonesian" or "indonesia, menado" in value or value == "menado (menadonees)":
                value = "menado (indonesia)"
            if "ambon" in value and "netherlands" in value:
                value = "netherlands, ambon (indonesia)"
            if "menado" in value and "netherlands" in value:
                value = "netherlands, menado (indonesia)"
            if "ambon" in value and "indonesia" in value and value != "netherlands, ambon (indonesia)" and value != "ambon (indonesia)":
                value = "ambon (indonesia)"
            if "menado" in value and "indonesia" in value and value != "netherlands, menado (indonesia)" and value != "menado (indonesia)":
                value = "menado (indonesia)"
            if "mixed parentage" in value:
                value = "netherlands, mixed parentage"
            if value == "netherlands; indonesian mother":
                value = "netherlands, indonesian mother"
            if value == "netherlands, father and mother both mixed blood" or "netherlands parents are mixed bloods" in value:
                value = "netherlands, mixed blood parents"
            if "father mixed blood. mother indonesian" in value or "father is mixed-blood and mother is indonesian" in value:
                value = "netherlands, father mixed blood, mother indonesian"
            if "british" in value:
                if "netherlands" in value:
                    value = "netherlands, british"
                else:
                    value = "british"
            if "swiss" in value:
                value = "netherlands, swiss"
            if "mixed with javanese" in value:
                value = "netherlands, java (indonesia)"
            if "black father and black mother" in value:
                value = "netherlands, black parents"
            if value == "netherlands (mother mixed blood)":
                value = "netherlands, mother mixed blood"
            if "malay" in value:
                value = "java (indonesia), malaysia"
            if "india, africa" in value:
                value = "netherlands, india, africa"
            list[index] = value
        if index == 7:
            value = value.replace('(?)', '').replace('  ', ' ')
            value = value.strip()
            if value.startswith("(") and value.endswith(")"):
                value = value[1:]
                value = value[:-1]
            list[index] = value
        if index == 8 or index == 10:
            value = value.replace("  ", " ")
            list[index] = value
        if index == 9:
            if "forgotten" in value:
                value = ""
            value = value.replace("no.", "").replace("no ", "").replace("nr.", "").replace("n. ", "n.").replace("ni", "n.i.").replace("n.i. ", "n.i.").replace("st. ", "st.")
            list[index] = value
        if index == 11:
            if "no date" in value:
                value = ""
            if "date" in value:
                value = value.replace("  ", " ").replace("1942708", "1942/08")
                value = re.sub(r'.*;', '', value)
                value = value.replace("date of death: ", "").replace("date of death ", "").replace("17/07/29: ", "").replace("1942/06/023", "1942/06/23").replace("1942/04/17, 4:10", "1942/04/17").replace("2 august 1942", "1942/08/02").replace("11 june 1942", "1942/06/11").replace("01:00 on 24 july 1942", "1942/07/24").replace(" ", "")
                value = value.replace('/', '-')
                list[37] = value
                list[index] = ""
            else:
                value = value.replace(";0", "/0").replace(" ", "").replace(",", "/")
                if ";" in value and value.count(';') != 1:
                    if value.strip().endswith(";"):
                        value = value[:-1]
                    else:
                        value = "1942/03/08,1942/03/10"
                value = re.sub(r'.*;|:', '', value)
                value = re.sub("[^0-9|/|,]", '', value)
                if "17/" in value and "1942/" in value:
                    value = re.sub(r'.*1942', '1942', value)
                if len(value) != 10:
                    if value == "17" or value == "106401":
                        value = ""
                    if value == "42/03/09":
                        value = "1942/03/09"
                    if value == "1942/03/":
                        value = "1942/03/00"
                    value = value.replace("17/", "1942/").replace("18/", "1943/").replace("19/", "1944/").replace("/7/", "/07/").replace("/3/", "/03/").replace("1942/0308", "1942/03/08").replace("1942/03/8", "1942/03/08").replace("1942/03/1110", "1942/03/11,1942/03/10").replace("19420", "1942/0").replace("1944/0729", "1944/07/29").replace("1942/03/1111/03", "1942/03/11").replace("1942/03/1011", "1942/03/11,1942/03/10").replace("1942/03/9", "1942/03/09").replace("1942/4/22", "1942/04/22").replace("1942/0328", "1942/03/28").replace("1942/03/005", "1942/03/05").replace("1943/03/8", "1943/03/08").replace("1942/03/028", "1942/03/28").replace("1942/08/1503/08", "1942/08/15,1942/03/08").replace("1942/03/0805/08", "1942/03/08,1942/05/08").replace("1942/03/1908/15", "1942/03/19,1942/08/15").replace("1942/08/1503/18", "1942/08/15,1942/03/18").replace("1942/03/085", "1942/03/08,1942/03/05").replace("1942/08/1503/09", "1942/08/15,1942/03/09").replace("1943/08/0223", "1943/08/02,1943/08/23").replace("1944/077/29", "1944/07/29").replace("1942/0803/15", "1942/08/15,1942/03/15").replace("1942/093/08", "1942/09/08,1942/03/08").replace("1942/0403/03", "1942/04/03,1942/03/03").replace("1942/0/08", "1942/00/08").replace("1943/701/01", "1943/07/01,1943/01/01")
                    if len(value) == 20:
                        value = value[:10] + "," + value[10:]
                value = value.replace("0942/", "1942/").replace("09/03/1942", "1942/03/09").replace("01/04/1942", "1942/04/01").replace("08/03/1942", "1942/03/08").replace("29/07/1944", "1944/07/29").replace('/', '-')
                list[index] = value
        if index == 12:
            value = value.replace('  ', ' ')
            value = value.strip()
            if value.startswith("(") and value.endswith(")"):
                value = value[1:]
                value = value[:-1]
            list[index] = value
        if index == 13:
            value = value.replace('-・-', '').replace('unknown', '').replace('+', '').replace('  ', ' ').replace(';', ' ')
            list[index] = value
        if index == 14:
            value = value.replace('?', '').replace('  ', ' ').replace(':', '').replace('+', '')
            if "unknown" in value or "onbekend" in value:
                value = ""
            list[index] = value
        if index == 15:
            if re.match("^[() ]+$", value):
                value = ""
            value = value.strip()
            if value.startswith("(") and value.endswith(")"):
                value = value[1:]
                value = value[:-1]
            if value.endswith("/"):
                value = value[:-1]
            list[index] = value
        if index == 16:
            if re.match("^[() ]+$", value) or value == "2":
                value = ""
            value = value.strip()
            if value.startswith("(") and value.endswith(")"):
                value = value[1:]
                value = value[:-1]
            value = value.replace('  ', ' ').replace('([])', '').replace('?', '')
            if value.endswith(',') or value.endswith('.'):
                value = value[:-1]
            list[index] = value
        if index == 17:
            value = value.replace("pen; ", "pens.").replace("pen ", "pens.").replace("pen. ", "pens.").replace("pen.", "pens.").replace("pens. ", "pens.").replace("pens ", "pens.").replace("per ", "pers.").replace("per.", "pers.").replace("pesr.", "pers.").replace("pera ", "pers.").replace("pres ", "pers.").replace("pers. ", "pers.").replace("pers ", "pers.").replace("pers.:", "pers.").replace("pers; ", "pers.").replace("pers;", "pers.").replace("pers: ", "pers.").replace("pers:", "pers.").replace("pers/ ", "pers.").replace("---", "").replace("ーーー", "").replace("--", "").replace("ーー", "").replace("__", "").replace("p ", "p.").replace("p. ", "p.").replace("ｐ ", "p.").replace("pe ", "p.").replace("pes. ", "p.").replace("pes ", "p.").replace("prs ", "pers.").replace("per:", "pers.").replace("pen: ", "pens.").replace("rers; ", "pers.").replace(" - ", " ").replace("  ", " ")
            value = value.replace("p1", "p.1").replace("p2", "p.2").replace("p3", "p.3").replace("p4", "p.4").replace("p5", "p.5").replace("p6", "p.6").replace("p7", "p.7").replace("p8", "p.8").replace("p9", "p.9")
            value = value.replace("pens1", "pens.1").replace("pens2", "pens.2").replace("pens3", "pens.3").replace("pens4", "pens.4").replace(
                "pens5", "pens.5").replace("pens6", "pens.6").replace("pens7", "pens.7").replace("pens8", "pens.8").replace("pens9", "pens.9")
            value = value.replace("pers1", "pers1.1").replace("pers12", "pers1.2").replace("pers13", "pers1.3").replace("pers14", "pers1.4").replace(
                "pers15", "pers1.5").replace("pers16", "pers1.6").replace("pers17", "pers1.7").replace("pers18", "pers1.8").replace("pers19", "pers1.9")
            value = value.strip()
            if value == "na/" or value == "-":
                value = ""
            if value == "p－" or value == "p.-" or value == "ｐ" or value == "p-" or value == "p":
                value = "p."
            if value == "pen" or value == "pens.-":
                value = "pens."
            if value == "per-" or value == "per" or value == "pres" or value == "pers" or value == "pers-" or value == "pers.-" or value == "pers. -":
                value = "pers."
            list[index] = value
        if index == 18:
            if value.startswith("[") and value.endswith("]"):
                value = value[1:]
                value = value[:-1]
            value = re.sub(r'.*;|:', '', value)
            value = ''.join(filter(lambda character: ord(character) < 0x3000, value))
            value = value.replace('piow', 'pow').replace('  ', ' ').replace('p1', 'p 1').replace('/ ', '/').replace('18/', '1943/').replace('17/', '1942/').replace("/", "-").replace("camp, 1", "camp 1").replace("--", "")
            if value.strip().startswith("1"):
                if len(value) > 34:
                    value = value[18:]
                if len(value) == 34:
                    value = value[10:]
                if len(value) == 21:
                    value = value[11:]
            if value.endswith("-"):
                value = value + "00"
            list[index] = value
        if index == 19:
            if (value.startswith("[") and value.endswith("]")) or (value.startswith("(") and value.endswith(")")):
                value = value[1:]
                value = value[:-1]
            value = re.sub(r'.*;|:', '', value)
            value = ''.join(filter(lambda character: ord(character) < 0x3000, value))
            value = value.replace('piow', 'pow').replace('[]', '').replace('  ', ' ').replace('p1', 'p 1').replace(',', '').replace('thaipow', 'thai pow').replace('osakapow', 'osaka pow').replace('/ ', '/').replace('18/', '1943/').replace('17/', '1942/').replace("/", "-")
            value = value.strip()
            if value == "thai pow c":
                value = "thai pow camp"
            if value == "thai pow camp]":
                value = "thai pow camp"
            list[index] = value
        if index == 20 or index == 21 or index == 22:
            value = value.replace("  ", " ").replace("/", "-")
            if value.startswith("[") and value.endswith("]"):
                value = value[1:]
                value = value[:-1]
            value = re.sub(r'.*;|:', '', value)
            value = ''.join(filter(lambda character: ord(character) < 0x3000, value))
            list[index] = value
        if index == 23:
            if value.endswith(';') or value.endswith('-'):
                value = value[:-1]
            value = re.sub(r'.*;|:', '', value)
            value = ''.join(filter(lambda character: ord(character) < 0x3000, value))
            value = value.replace("/", "").replace("camp, ", "camp ").replace("pow, ", "pow ").replace("no,", "no.")
            value = re.sub(r'.*, m', 'm', value)
            value = re.sub(r'.*, j', 'j', value)
            value = value.replace("3,b", "3 b").replace("no.iii", "no.3").replace(" ii ", " no.2 ").replace("()", "")
            value = re.sub(r'.*i\(', '', value)
            value = re.sub(r'.*1 no|3 no|5 no|8 no|9 no|0 no', 'no', value)
            if value.strip().startswith('i'):
                value = re.sub(r'.*no', 'no', value)
                value = value.replace("i 6", "no.1 6").replace("i 1", "no.1 1")
            if value.strip().startswith('('):
                value = value.replace("(", "").replace(")", "")
            value = value.replace("camp )", "camp ").replace("camp)", "camp ").replace("  ", " ")
            if "no. b" in value:
                if "3015" in value or "5994" in value:
                    value = value.replace("no. b", "no.3 b")
            value = value.replace("no. ", "no.")
            list[index] = value
        if index == 24:
            value = re.sub(r'.*;|:', '', value)
            value = ''.join(filter(lambda character: ord(character) < 0x3000, value))
            value = value.replace("(", "").replace(")", "").replace("/", "").replace("camp, ", "camp ").replace("camp,", "camp ").replace("pow, ", "pow ").replace("no,", "no.").replace("  ", " ").replace("no. m", "m")
            value = re.sub(r'.*, ', '', value)
            if value.strip().startswith('i'):
                value = re.sub(r'.*no.', 'no.', value)
            if "no. b" in value:
                if "8111" in value or "8185" in value or "8251" in value or "12987" in value or "8101" in value:
                    value = value.replace("no. b", "no.4 b")
            value = value.replace("no. ", "no.")
            list[index] = value
        if index == 25:
            value = re.sub(r'.*;|:', '', value)
            value = ''.join(filter(lambda character: ord(character) < 0x3000, value))
            value = value.replace("(", "").replace(")", "").replace("）", "").replace("（", "").replace("/", "").replace("camp, ", "camp ").replace("no,", "no.").replace("no. ", "no.").replace("  ", " ")
            value = re.sub(r'.*, ', '', value)
            list[index] = value
        if index == 26:
            value = re.sub(r'.*;', '', value)
            value = ''.join(filter(lambda character: ord(character) < 0x3000, value))
            value = value.replace("(", "").replace(")", "").replace("）", "")
            list[index] = value
        if index == 27:
            value = re.sub(r'.*;', '', value)
            value = value.replace("/", "-")
            list[index] = value
        if index == 28:
            value = value.replace("  ", " ")
            if 'died' in value or 'deceased' in value:
                value_edit = value.replace(") ;", ");").replace("29 october 1932 ","29 october 1943 ").replace("in 2022 ","").replace("1942, ","1942. ").replace("1943, ","1943. ").replace("1944, ","1944. ").replace("1945, ","1945. ").replace(" 1942("," 1942 (").replace(" 1943("," 1943 (").replace(" 1944("," 1944 (").replace(" 1945("," 1945 (").replace(" 1942 "," 1942. ").replace(" 1943 "," 1943. ").replace(" 1944 "," 1944. ").replace(" 1945 "," 1945. ").replace(";",".").replace("died at 0500 on14 april","died at 05:00 on 14 april").replace("died at 1700 on 30","died at 17:00 on 30").replace("a.m."," ").replace("p.m."," ").replace(" no."," no ").replace(": died","; died").replace("pulmonary emphysema at 19:12.","pulmonary emphysema at 19:12").replace("  ", " ").replace(" 19 43 ", " 1943 ").replace("1942. died","1942 died").replace("1943. died","1943 died").replace("1944. died","1944 died").replace("1945. died","1945 died").replace("3 december 3, 1943","3 decemberz 1943").replace("31 my 1943","31 may 1943").replace("26 mary 1945","26 may 1945")
                if 'died' in value:
                    death_sentence = re.findall(r"([^.;]*?died[^.]*\.)", value_edit)
                    if str(death_sentence) == "[]":
                        value_edit = value_edit + "."
                        death_sentence = re.findall(r"([^.;]*?died[^.]*\.)", value_edit)
                elif 'deceased' in value:
                    death_sentence = re.findall(r"([^.;]*?deceased[^.]*\.)", value_edit)
                    if str(death_sentence) == "[]":
                        value_edit = value_edit + "."
                        death_sentence = re.findall(r"([^.;]*?deceased[^.]*\.)", value_edit)
                if len(death_sentence) == 1:
                    if "1942" in death_sentence[0] or "1943" in death_sentence[0] or "1944" in death_sentence[0] or "1945" in death_sentence[0]:
                        result = search_dates(str(death_sentence))
                elif len(death_sentence) > 1:
                    if "1942" in death_sentence[0] or "1943" in death_sentence[0] or "1944" in death_sentence[0] or "1945" in death_sentence[0] or "1985" in death_sentence[0]:
                        result = search_dates(str(death_sentence[0]))
                    elif "1942" in death_sentence[1] or "1943" in death_sentence[1] or "1944" in death_sentence[1] or "1945" in death_sentence[1]:
                        result = search_dates(str(death_sentence[1]))
                    else:
                        if len(death_sentence) > 2:
                            if "1942" in death_sentence[2] or "1943" in death_sentence[2] or "1944" in death_sentence[2] or "1945" in death_sentence[2]:
                                result = search_dates(str(death_sentence[2]))
                if result is not None:
                    r = False
                    if len(result) > 0:
                        r = all(elem[1].strftime('%Y-%m-%d') == result[0][1].strftime('%Y-%m-%d') for elem in result)
                    date = str(result[0][1].strftime('%Y-%m-%d'))
                    if date != str(datetime.date.today()) and date != "1900-01-01" and date[:4] != str(datetime.datetime.now().year):
                        if (len(result) == 1) or (len(result) > 1 and r):
                            if is_empty(list[37]):
                                list[37] = date
                            else:
                                list[37] = list[37] + ", " + date
            list[index] = value
        if index == 29:  # Check whether the person died
            if 'died' in value or 'deceased' in value or 'death' in value:
                value = value.replace("died.", "died;").replace("died on ", "died; ").replace("died on; ", "died; ").replace("deceased; ", "died; ").replace("death; ", "died; ").replace("died ;", "died;").replace("; (", ". (").replace("jlu", "july").replace("60october", "6 october")
                if ". (" not in value:
                    value = value.replace(" (", ". (")
                value = value.replace("died; recorded in the monthly report, october.", "died; 16 october 1942.recorded in the monthly report, october.")
                death_sentence = str(re.findall(r"([^.;]*?died[^.]*\.)", value))
                result = search_dates(death_sentence)
                if is_empty(list[37]):
                    list[37] = str(result[0][1].strftime('%Y-%m-%d'))
                else:
                    list[37] = list[37] + ", " + str(result[0][1].strftime('%Y-%m-%d'))
            else:
                if "december" in value:
                    if is_empty(list[37]):
                        list[37] = "1944-11-22"
                    else:
                        list[37] = list[37] + ", 1944-11-22"
            value = value.replace("  ", " ")
            list[index] = value
        if index == 30:  # Check whether the person died
            if value == "?" or value == "x" or value == "x; x" or value == "x x" or value == "ｘ" or value == "×" or value == "× ×" or value == "z.o.z." or value == "×; ×":
                value = ""
            if value.endswith(';') or value.endswith(','):
                value = value[:-1]
            if 'died' in value or 'deceased' in value:
                value = value.replace("died.", "died;").replace("; (", ". (").replace(", (died at)", "; (died at)")
                if ". (" not in value:
                    value = value.replace(" (", ". (")
                value_edit = value.replace("/43", "/1943").replace("/44", "/1944").replace(" 43/", " 1943/").replace(" 43 ", " 1943 ").replace(" 42", " 1942").replace("/19 ", "/1944 ").replace(" 17-", " 1942-").replace(" 20/7/13", " 1945/7/13").replace(" 5/6/1943 ", " 5 june 1943 ").replace(" 11/4/1943", " 11 april 1943").replace("3 died 24/11/1944", "died 24 november 1944").replace("4/5/1943", "4 may 1943").replace("16/6/1943", "16 june 1943").replace("1944 according", "1944. according").replace("july and died", "july and; died").replace("on board tofuku-maru", "").replace("on board of tofuku maru", "").replace("died prior to the establishment of an official pow camp,", "died on 7 august 1946 prior to the establishment of an official pow camp,")
                if 'died' in value:
                    if "died. (" in value_edit:
                        value_edit = value_edit.replace("died.", "died;")
                    death_sentence = str(re.findall(r"([^.;]*?died[^.]*\.)", value_edit))
                    if death_sentence == "[]":
                        value_edit = value_edit + "."
                        death_sentence = str(re.findall(r"([^.;]*?died[^.]*\.)", value_edit))
                elif 'deceased' in value:
                    death_sentence = str(re.findall(r"([^.;]*?deceased[^.]*\.)", value_edit))
                    if death_sentence == "[]":
                        value_edit = value_edit + "."
                        death_sentence = str(re.findall(r"([^.;]*?deceased[^.]*\.)", value_edit))
                result = search_dates(death_sentence)
                if result is not None:
                    date = str(result[0][1].strftime('%Y-%m-%d'))
                    if date != str(datetime.date.today()) and date != "1900-01-01" and date.startswith("1268") is False and "died before formal establishment of pow camp; 25" not in value and "2[5]3 april 1943" not in value and "no record" not in value:
                        date = date.replace(str(datetime.datetime.now().year), "0000")
                        if is_empty(list[37]):
                            list[37] = date
                        else:
                            list[37] = list[37] + ", " + date
            value = value.replace("  ", " ")
            list[index] = value
        if index == 31:  # get one or two or three digits of the serial number
            value = ''.join(filter(lambda character: ord(character) < 0x3000, value))
            value = re.sub(r'.*;|:', '', value)
            value = value.rstrip()
            value = re.sub(r',.*', '', value)
            value = value.lstrip()
            if 'number)' in list[index]:
                value = value.partition('number)')[2]
            elif 'number' in list[index]:
                value = value.partition('number')[2]
            elif 'numer' in list[index]:
                value = value.partition('numer')[2]
            elif 'seiribanngou' in list[index]:
                value = value.partition('seiribanngou')[2]
            elif 'siribango' in list[index]:
                value = value.partition('siribango')[2]
            value = re.sub("[^0-9]", '', value)
            if len(value) > 3:
                value = value[3:]
            list[index] = value
        if index == 32:  # remove japanese characters before the ; or :
            value = re.sub(r'.*;|:', '', value)
            value = value.rstrip()
            value = re.sub(r'.*所 N|所 \(N|所 n', 'n', value)
            value = value.rstrip()
            value = re.sub(r'ff.*', '', value)
            value = value.replace('分所', ' branch camp')
            list[index] = value
        if index == 33:  # remove translator's note at the beginning of the sentence
            if is_empty(list[index]) is False:
                if 's note) ' in value:
                    value = value.partition('s note) ')[2]
                elif 'r note)' in value:
                    value = value.partition('r note)')[2]
                elif 's note):' in value:
                    value = value.partition('s note):')[2]
                elif 's note);' in value:
                    value = value.partition('s note);')[2]
                elif 's note)' in value:
                    value = value.partition('s note)')[2]
                elif 's note）' in value:
                    value = value.partition('s note）')[2]
                elif 's note]' in value:
                    value = value.partition('s note]')[2]
                elif 's nor)' in value:
                    value = value.partition('s nor)')[2]
                elif 's nor' in value:
                    value = value.partition('s nor')[2]
                elif 's note ' in value:
                    value = value.partition('s note ')[2]
                elif 's note:' in value:
                    value = value.partition('s note:')[2]
                list[index] = value
        if value.isspace():  # if all characters in the string are whitespace characters
            list[index] = None
        if value.startswith(' ') or value.endswith(' '):  # leading and trailing whitespace are removed
            value = value.strip()
            list[index] = value
        value = re.sub(' +', ' ', value)
        list[index] = value.replace("  ", " ")
    # column 37
    death_date = list[37]
    single_date = None
    if ", " in death_date:
        single_date = death_date.split(", ")
    q = False
    if single_date is not None:
        if any("0000" in s for s in single_date):
            for item in single_date:
                if "0000" in item:
                    single_date.remove(item)
        q = all(elem == single_date[0] for elem in single_date)
    if q:
        death_date = single_date[0]
    list[37] = death_date
    list[38] = "male"
    phase_two_card_list.append(list)

headers = ["id", "full_name", "surname", "given_names", "infix", "date_of_birth",
           "nationality", "rank", "unit", "stamboeknr", "place_of_capture",
           "date_of_capture", "occupation", "fathers_name", "mothers_name",
           "place_of_origin", "destination_report", "remarks",
           "camp_and_transfer_date_one", "camp_and_transfer_date_two",
           "camp_and_transfer_date_three", "camp_and_transfer_date_four",
           "camp_and_transfer_date_five", "camp_branch_name_and_reg_no_one",
           "camp_branch_name_and_reg_no_two", "camp_branch_name_and_reg_no_three",
           "camp_branch_name_and_reg_no_four", "camp_branch_name_and_reg_no_five",
           "other_info_one", "other_info_two", "other_info_three", "serial_number",
           "center_top_red_letters", "translator_notes", "scan", "reference_one",
           "reference_two", "date_of_death", "gender"]
# write CSV using panda
my_df = pd.DataFrame(phase_two_card_list)
my_df.to_csv(
    r'C:\clean_japanese_internment_cards.csv',
    header=headers, index=False, encoding='utf_8_sig')
