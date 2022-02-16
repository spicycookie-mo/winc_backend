from helpers import get_countries


""" Leave this untouched. Wincpy uses it to match this assignment with the
tests it runs. """
__winc_id__ = "c545bc87620d4ced81cbddb8a90b4a51"
__human_name__ = "for"


""" Write your functions here. """

# Exercise 1
## first option

def shortest_names(countries):
    countries.sort(key=len)
    short_countries = []
    for country in countries:
        if len(country) == len(countries[0]):
            short_countries.append(country)
        else:
            break
    return short_countries
                        
#Exercise 1
## second option 

# def shortest_names(countries):   
#     li = []
#     for country in countries:
#         li.append(len(country))
#     short_countries=[]
#     for country in countries:
#         if len(country) == min(li):
#             short_countries.append(country)
#     return short_countries

#Exercise 1   
## third option

# def shortest_names(countries):  
#     shortest_country_len = 0
#     shortest_countries_list = []
#     for country in countries:
#          if len(country) <= shortest_country_len or shortest_country_len == 0:
#              shortest_country_len = len(country)
#     for country in countries:
#          if len(country) == shortest_country_len:
#              shortest_countries_list.append(country)
#     return (shortest_countries_list)

#Exercise2

def most_vowels(countries):
    vowels_total = []
    top_vowels = []
    for country in countries:
        a = country.lower().count('a')
        e = country.lower().count('e')
        i = country.lower().count('i')
        o = country.lower().count('o')
        u = country.lower().count('u')
        sum = a + e + i + o + u
        vowels_total.append(sum)                       
    vowels_total_short_list = (list(set(vowels_total))) #set removes duplicates; needs casting back to list in order to index
    vowels_total_short_list.sort(reverse=True)
    # print (vowels_total_short_list)  
    for country in countries:
        a = country.lower().count('a')
        e = country.lower().count('e')
        i = country.lower().count('i')
        o = country.lower().count('o')
        u = country.lower().count('u')
        sum = a + e + i + o + u
        if sum == vowels_total_short_list[0]:
           top_vowels.append(country)
    for country in countries:
        a = country.lower().count('a')
        e = country.lower().count('e')
        i = country.lower().count('i')
        o = country.lower().count('o')
        u = country.lower().count('u')
        sum = a + e + i + o + u
        if sum == vowels_total_short_list[1]:
            top_vowels.append(country)
    for country in countries:
        a = country.lower().count('a')
        e = country.lower().count('e')
        i = country.lower().count('i')
        o = country.lower().count('o')
        u = country.lower().count('u')
        sum = a + e + i + o + u
        if sum == vowels_total_short_list[2]:
            top_vowels.append(country)
    return (top_vowels)

# Exercise 3

def alphabet_set(countries):
    alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    shortest_left = 0 
    selected_countries = []
    for country in countries:
        letters_country = []
        letters_country = list(country.lower())
        letters_left = []
        letters_left = list(set(alphabet).difference(set(letters_country)))
        num_letters_left = len(letters_left)
        #print (num_letters_left)
        if num_letters_left <= shortest_left or shortest_left == 0:
            shortest_left = num_letters_left
    for country in countries:
        letters_country = []
        letters_country = list(country.lower())
        letters_left = []
        letters_left = list(set(alphabet).difference(set(letters_country)))
        if len(letters_left) == shortest_left:
            selected_countries.append(country)
            for letter in letters_country:
                if letter in alphabet:
                    alphabet.remove(letter)
                    # print(alphabet)
            break
    for country in countries:
        letters_country = []
        letters_country = list(country.lower())
        letters_left = []
        letters_left = list(set(alphabet).difference(set(letters_country)))
        num_letters_left = len(letters_left)
        #print (num_letters_left)
        if num_letters_left <= shortest_left: 
            shortest_left = num_letters_left
    for country in countries:
        letters_country = []
        letters_country = list(country.lower())
        letters_left = []
        letters_left = list(set(alphabet).difference(set(letters_country)))
        if len(letters_left) == shortest_left:
            #print (country)
            selected_countries.append(country)
            #print(letters_country)
            for letter in letters_country:
                if letter in alphabet:
                    alphabet.remove(letter)
                    #print(alphabet)
            break
    for country in countries:
        letters_country = []
        letters_country = list(country.lower())
        letters_left = []
        letters_left = list(set(alphabet).difference(set(letters_country)))
        num_letters_left = len(letters_left)
        #print (num_letters_left)
        if num_letters_left <= shortest_left: 
            shortest_left = num_letters_left
    for country in countries:
        letters_country = []
        letters_country = list(country.lower())
        letters_left = []
        letters_left = list(set(alphabet).difference(set(letters_country)))
        if len(letters_left) == shortest_left:
            #print (country)
            selected_countries.append(country)
            #print(letters_country)
            for letter in letters_country:
                if letter in alphabet:
                    alphabet.remove(letter)
                    #print(alphabet)
            break
    for country in countries:
        letters_country = []
        letters_country = list(country.lower())
        letters_left = []
        letters_left = list(set(alphabet).difference(set(letters_country)))
        num_letters_left = len(letters_left)
        #print (num_letters_left)
        if num_letters_left <= shortest_left: 
            shortest_left = num_letters_left
    for country in countries:
        letters_country = []
        letters_country = list(country.lower())
        letters_left = []
        letters_left = list(set(alphabet).difference(set(letters_country)))
        if len(letters_left) == shortest_left:
            #print (country)
            selected_countries.append(country)
            #print(letters_country)
            for letter in letters_country:
                if letter in alphabet:
                    alphabet.remove(letter)
                    #print(alphabet)
            break
    for country in countries:
        letters_country = []
        letters_country = list(country.lower())
        letters_left = []
        letters_left = list(set(alphabet).difference(set(letters_country)))
        num_letters_left = len(letters_left)
        #print (num_letters_left)
        if num_letters_left <= shortest_left: 
            shortest_left = num_letters_left
    for country in countries:
        letters_country = []
        letters_country = list(country.lower())
        letters_left = []
        letters_left = list(set(alphabet).difference(set(letters_country)))
        if len(letters_left) == shortest_left:
            #print (country)
            selected_countries.append(country)
            #print(letters_country)
            for letter in letters_country:
                if letter in alphabet:
                    alphabet.remove(letter)
                    # print(alphabet)
            break
    for country in countries:
        letters_country = []
        letters_country = list(country.lower())
        letters_left = []
        letters_left = list(set(alphabet).difference(set(letters_country)))
        num_letters_left = len(letters_left)
        # print (num_letters_left)
        if num_letters_left <= shortest_left: 
            shortest_left = num_letters_left
    for country in countries:
        letters_country = []
        letters_country = list(country.lower())
        letters_left = []
        letters_left = list(set(alphabet).difference(set(letters_country)))
        if len(letters_left) == shortest_left:
            #print (country)
            selected_countries.append(country)
            #print(letters_country)
            for letter in letters_country:
                if letter in alphabet:
                    alphabet.remove(letter)
                    #print(alphabet)
            break
    return selected_countries
                  
        

 



# This block is only run if this file is the entrypoint; python main.py
# It is not run if it is imported as a module: `from main import *`
if __name__ == "__main__":
    countries = get_countries()

    """ Write the calls to your functions here. """

#1
print(shortest_names(countries))

# #2
print(most_vowels (countries))

#3 
print(alphabet_set(countries))
