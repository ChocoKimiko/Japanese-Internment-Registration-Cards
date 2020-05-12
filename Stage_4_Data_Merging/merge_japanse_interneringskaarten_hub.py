import pandas
import numpy as np
from pprint import pprint
df = pandas.read_csv(r'clean_all_data.csv')
df['initials'] = np.empty((len(df), 0)).tolist()
df['place_of_birth'] = np.empty((len(df), 0)).tolist()
df['place_of_death'] = np.empty((len(df), 0)).tolist()
df['nickname'] = np.empty((len(df), 0)).tolist()
df['image'] = np.empty((len(df), 0)).tolist()
df['extern_url'] = np.empty((len(df), 0)).tolist()

df2 = pandas.read_csv(r'clean_match.csv')

listOfDFRows = df.to_numpy().tolist()
listOfDFRows2 = df2.to_numpy().tolist()

# Remove nan, because it is empty
for item2 in listOfDFRows2:
    if str(item2[2]) == "nan":
        item2[2] = ""
    if str(item2[5]) == "nan":
        item2[5] = ""
    if str(item2[8]) == "nan":
        item2[8] = ""

for item in listOfDFRows:
    for i in range(39):
        if str(item[i]) == "nan":
            item[i] = ""

# Merge Japanse Interneringskaarten data with HUB data
for item1 in listOfDFRows:
    for item2 in listOfDFRows2:
        if item1[34] == item2[0]:
            # override date_of_birth & date_of_death
            item1[5] = item2[1]  # date_of_birth
            item1[37] = item2[3]  # date_of_death
            # add place_of_birth & place_of_death & initials & nickname &
            # image & extern_url (add gathena too)
            item1[39] = item2[7]  # initials
            item1[40] = item2[2]  # place_of_birth
            item1[41] = item2[4]  # place_of_death
            item1[42] = item2[8]  # nickname
            item1[43] = item2[5]  # image
            item1[44] = item2[6]  # extern_url
    if str(item1[44]) == "[]":
        item1[44] = "http://www.gahetna.nl/collectie/index/nt00425/" + \
                    str(item1[36])
    else:
        item1[44] = str(item1[44]) + ",http://www.gahetna.nl/" \
                                     "collectie/index/nt00425/" + str(item1[36])

# write CSV using panda
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
           "reference_two", "date_of_death", "gender", "initials", "place_of_birth",
           "place_of_death", "nickname", "image", "extern_url"]
my_df = pandas.DataFrame(listOfDFRows)
my_df.to_csv(
    r'C:\complete_data.csv',
    header=headers, index=False, encoding='utf_8_sig')
