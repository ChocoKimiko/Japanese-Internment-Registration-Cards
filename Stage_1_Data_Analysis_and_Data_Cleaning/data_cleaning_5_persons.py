#!/usr/bin/env python
# -*- coding: utf-8 -*-
import codecs
import re
import string
import csv
import pandas as pd
from pprint import pprint
from dateparser.search import search_dates
import datetime

# read the csv file
reader = codecs.open("NT00425_Japanse_interneringskaarten.csv", "r", "utf-8")

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

# Phase 1 use the card number 4, 149, 958, 5236, 29525 (info)
first_phase = [3, 148, 957, 5235, 29524]
phase_one_card_list = []
for number in first_phase:
    i = 0
    for content in card_list[number]:
        # print(str(i) + " " + content)
        i += 1

# print(card_list[3])  # row 4
# print(card_list[148])  # row 149
# print(card_list[957])  # row 958
# print(card_list[5235])  # row 5236
# print(card_list[29524])  # row 29525


# replace a string in the list
def replace_all(mylist, dic):
    for a, b in dic.items():
        mylist = [w.replace(a, b) for w in mylist]
    return mylist


for item in first_phase:
    d = {"(n/a)": "", "n/a": "", "\u3000": "", "\\n": " "}
    list = replace_all(card_list[item], d)
    list.append('')
    for index, value in enumerate(list):
        if index == 1 or index == 2 or index == 3 or index == 6 or index == 7:
            if "-" in value:
                list[index] = value.replace('-', ' ')
            value = re.sub("[(].*?[)]", "", value)
            list[index] = value.rstrip()
        if index == 10 or index == 18 or index == 19 or index == 23 or \
                index == 24 or index == 25 or index == 31 or index == 32:
            value = re.sub(r'.*;', '', value)
            list[index] = value.rstrip()
        if index == 11:
            value = value.replace('/', '-')
            value = re.sub(r'.*;', '', value)
            list[index] = value.rstrip()
        if index == 12:
            value = ''.join(filter(lambda character: ord(character) < 0x3000, value))
            value = re.sub('[();]', '', value)
            list[index] = value
        if index == 28 or index == 29 or index == 30:  # Check whether the person died
            if 'died' in value.lower():
                death_sentence = str(re.findall(r"([^.;]*?died[^.]*\.)", value.lower()))
                result = search_dates(death_sentence)
                list[38] = str(result[0][1].strftime('%Y-%m-%d'))
        if value.isspace():  # if all characters in the string are whitespace characters
            list[index] = None
        if re.match(r'^\s', value):  # leading whitespace are removed
            list[index] = value.strip()
        value = re.sub(' +', ' ', value)
    phase_one_card_list.append(list)

pprint(phase_one_card_list)

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
           "center_top_red_letters", "translator_notes", "scan", "empty_column",
           "reference_one", "reference_two", "date_of_death"]
# write CSV using panda
my_df = pd.DataFrame(phase_one_card_list)
my_df.to_csv(
    r'C:\clean_5_persons.csv',
    header=headers, index=False, encoding='utf_8_sig')
