import requests
import sys

def get_city_from_postal_code(postal_code):
    """
    :param postal_code: french postal code on five digits
    :returns City object
    Interrogate the INSEE database to find french cities with a given postal code
    """
    try:
        assert len(postal_code) == 5 and int(postal_code)
    except (ValueError, AssertionError) as e:
        return "Postal code looks wrong {0}".format(e)

    url = "http://public.opendatasoft.com/api/records/1.0/search?"
    params = {'dataset' : 'correspondance-code-insee-code-postal',
              'q' : 'postal_code={0}'.format(postal_code)}
    r = requests.get(url, params = params)
    records = r.json().get('records')
    if len(records) == 0 :
        return "No city found"
    elif len(records) == 1:
        return City(records[0]['fields'].get('nom_comm'), records[0]['fields'].get('insee_com'))
    else:
        cities_list = {}
        i = 0
        choice = ''
        for record in records:
            print i, record['fields'].get('nom_comm')
            cities_list[i] = City(record['fields'].get('nom_comm'), record['fields'].get('insee_com'))
            i += 1
        while choice not in cities_list.keys():
            choice = input("Which city ? ")
        return cities_list[choice]
    
def is_street(fantoir_entry):
    """
    :param fantoir_entry: a line from a FANTOIR file
    :returns True or False regarding the entry concerns a street or not
    """
    result = False
    if len(fantoir_entry[6:10].strip()) == 4:
        result = True
    return result

def is_city(fantoir_entry):
    """
    :param fantoir_entry: a line from a FANTOIR file
    :returns True if the entry is a street 
    """
    result = False
    if fantoir_entry[6:10].strip() == '' and fantoir_entry[10].strip() != '' :
        result = True
    return result

class City(object):
    def __init__(self, name, insee_code):
        self.insee_code = insee_code
        self.name = name
        self.street_list = []

    def __str__(self):
        return "{} {}".format(self.name, self.insee_code)

    def get_streets_from_city(self):
        """
        :param insee_code: the insee code from the city
        :returns list of streets
        """
        file = open("dpt/{}0.txt".format(self.insee_code[0:2]))
        for line in file.readlines():
            if is_street(line):
                if line[0:2] == self.insee_code[0:2] and line[3:6] == self.insee_code[2:]:
                    self.street_list.append({"type" : line[11:15],
                                             "name" : line[15:41].strip()})

    def look_for_street(self, street_name):
        """
        :param street_name: a string containing the name of a street
        :returns matching a street list
        """
        for street in self.street_list:
            if str(street_name) in street['name']:
                print street['type'], street['name']
        
if __name__ == '__main__':

    postal = sys.argv[1]

    city = get_city_from_postal_code(postal)
    print city.name
    city.get_streets_from_city()
    street_name = str(raw_input("What street are you looking for ? ")).upper()
    city.look_for_street(street_name)
