import pandas
from pprint import pprint
import unittest
from unidecode import unidecode
df = pandas.read_csv(r'match_japanse_interneringskaarten_hub.csv')


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


class TestEvaluationMatch(unittest.TestCase):

    def test_evaluation_match(self):
        for item_to_test in new_list:
            try:
                self.assertEqual(unidecode(item_to_test[11].lower()), unidecode(item_to_test[32].lower()), "Unit Testing")
            except AssertionError as e:
                print(str(e))
                # raise


if __name__ == '__main__':
    unittest.main()
