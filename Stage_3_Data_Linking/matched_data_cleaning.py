import pandas
from pprint import pprint
df = pandas.read_csv(r'match_japanse_interneringskaarten_hub.csv')

# Delete rows with probability less than 55%
df_probability_insufficient = df[df['Probability'] < 0.55]
df = df.drop(df_probability_insufficient.index, axis=0)

# Delete columns that are not needed
del df['Rank']
del df['Probability']
del df['Column 1 (objID)']
del df['Column 1 (objType)']
del df['Column 1 birthEvent']
del df['Column 1 deathEvent']
del df['Column 1 http://purl.org/dc/elements/1.1/description']
del df['Column 1 http://schema.org/birthDate']
del df['Column 1 http://schema.org/birthPlace']
del df['Column 1 http://schema.org/deathDate']
del df['Column 1 http://schema.org/deathPlace']
del df['Column 1 http://schema.org/familyName']
del df['Column 1 http://schema.org/gender']
del df['Column 1 http://schema.org/givenName']
del df['Column 1 http://schema.org/jobTitle']
del df['Column 1 http://schema.org/name']
del df['Column 1 https://data.niod.nl/familyNamePrefix']
del df['Column 1 https://data.niod.nl/initials']
del df['Column 1 source']
del df['Column 2 (objID)']
del df['Column 2 (objType)']
del df['Column 2 birthEvent']
del df['Column 2 deathEvent']
del df['Column 2 http://purl.org/dc/elements/1.1/description']
del df['Column 2 http://purl.org/dc/elements/1.1/identifier']
del df['Column 2 http://purl.org/dc/elements/1.1/subject']
del df['Column 2 http://purl.org/dc/terms/source']
del df['Column 2 http://schema.org/familyName']
del df['Column 2 http://schema.org/gender']
del df['Column 2 http://schema.org/givenName']
del df['Column 2 http://schema.org/jobTitle']
del df['Column 2 http://schema.org/name']
del df['Column 2 https://data.niod.nl/familyNamePrefix']
del df['Column 2 https://data.niod.nl/oorlogslevensIdentifier']
del df['Column 2 https://data.niod.nl/preferredName']
del df['Column 2 source']


# replace a string in the list
def replace_strings_in_list(mylist, dic):
    for a, b in dic.items():
        mylist = [str(w).replace(a, b) for w in mylist]
    return mylist


# clean columns: col2birthPlace, col2deathPlace, col2image, col2url
listOfDFRows = df.to_numpy().tolist()
new_list = []

for item in listOfDFRows:
    d = {"\\n": "", '"': "", '[': "", ']': "", 'onbekend': "", '\/': "/"}
    new_list.append(replace_strings_in_list(item, d))

# write CSV using panda
headers = ["col1_url", "col2_birthDate", "col2_birthPlace", "col2_deathDate",
           "col2_deathPlace", "col2_image", "col2_url", "col2_initials",
           "col2_nickName"]
my_df = pandas.DataFrame(new_list)
my_df.to_csv(
    r'C:\clean_match.csv',
    header=headers, index=False, encoding='utf_8_sig')
