__winc_id__ = "9920545368b24a06babf1b57cee44171"
__human_name__ = "refactoring"


""" the old code"""

# alice_name = "Alice Aliceville"
# alice_profession = "electrician"
# bob_name = "Bob Bobsville"
# bob_profession = "painter"
# craig_name = "Craig Craigsville"
# craig_profession = "plumber"

# alfred_name = "Alfred Alfredson"
# alfred_address = "Alfredslane 123"
# alfred_needs = ["painter", "plumber"]
# bert_name = "Bert Bertson"
# bert_address = "Bertslane 231"
# bert_needs = ["plumber"]
# candice_name = "Candice Candicedottir"
# candice_address = "Candicelane 312"
# candice_needs = ["electrician", "painter"]

# alfred_contracts = []
# for need in alfred_needs:
#     if need == alice_profession:
#         alfred_contracts.append(alice_name)
#     elif need == bob_profession:
#         alfred_contracts.append(bob_name)
#     elif need == craig_profession:
#         alfred_contracts.append(craig_name)

# bert_contracts = []
# for need in bert_needs:
#     if need == alice_profession:
#         bert_contracts.append(alice_name)
#     elif need == bob_profession:
#         bert_contracts.append(bob_name)
#     elif need == craig_profession:
#         bert_contracts.append(craig_name)

# candice_contracts = []
# for need in candice_needs:
#     if need == alice_profession:
#         candice_contracts.append(alice_name)
#     elif need == bob_profession:
#         candice_contracts.append(bob_name)
#     elif need == craig_profession:
#         candice_contracts.append(craig_name)

# print("Alfred's contracts:", alfred_contracts)
# print("Bert's contracts:", bert_contracts)
# print("Candice's contracts:", candice_contracts)

""""the new code"""


""""option 1: with list of instances"""

# class Homeowner:

#     def __init__(self,name, address, needs):
#         self.name = name
#         self.address = address
#         self.needs = needs

#     def contracts(self):
#         contracts = []
#         for need in self.needs:
#             if need == 'electrician':
#                 if electricians_list:
#                     price = electricians_list[0].price
#                     contracts.append(electricians_list[0].name)
#                     for i in range(len(electricians_list)):
#                         price_i = electricians_list[i].price
#                         if price_i <= price:
#                             contracts[-1] = electricians_list[i].name
#             if need == 'painter':
#                 if painters_list:
#                     price = painters_list[0].price
#                     contracts.append(painters_list[0].name)
#                     for i in range (len(painters_list)):
#                         price_i = painters_list[i].price
#                         if price_i <= price:
#                             contracts[-1] = painters_list[i].name
#             if need == 'plumber':
#                 if plumbers_list:
#                     price = plumbers_list[0].price
#                     contracts.append(plumbers_list[0].name)
#                     for i in range (len(plumbers_list)):
#                         price_i = plumbers_list[i].price
#                         if price_i <= price:
#                             contracts[-1] = plumbers_list[i].name 
#         return (f"{self.name[:self.name.find(' ')]}'s contracts:{contracts}")

# class Specialist:
#     def __init__(self,name,price):
#         self.name = name
#         self.price = price

# class Electrician(Specialist):
#     profession = 'electrician' 

# class Painter(Specialist):
#     profession = 'painter'

# class Plumber(Specialist):
#     profession = 'plumber'


# ## adding Specialists instances

# electricians_list=[]
# painters_list=[]
# plumbers_list=[]

# electricians_list.append(Electrician("Alice Aliceville", 50))
# electricians_list.append(Electrician("John Johnsville", 55))

# painters_list.append(Painter("Bob Bobsville", 60))
# painters_list.append(Painter("Tom Tomsville", 100))

# plumbers_list.append(Plumber("Craig Craigsville", 45))

# ## adding Homeowner instances
# alfred = Homeowner("Alfred Alfredson","Alfredslane 123",["painter", "plumber"])
# bert = Homeowner("Bert Bertson","Bertslane 231",["plumber"])
# candice = Homeowner("Candice Candicedottir","Candicelane 312",["electrician", "painter"])


# """test prints"""
# # print(candice.needs)
# # print(bert.address)
# # print(alfred.name)
# # print (electricians_list[0].name)
# # print(str(electricians_list[0].price))

# # print(alfred.contracts())
# # print(Homeowner.contracts(alfred))
# # print(bert.contracts())
# print(candice.contracts())


""""option2 - with staticmethods in child classes"""

# import gc


# class Homeowner:
#     def __init__(self,name, address, needs):
#         self.name = name
#         self.address = address
#         self.needs = needs

#     def contracts(self):
#         contracts = []
#         for need in self.needs:
#             if need == 'electrician':
#                 temp = min(Electrician.electricians_catalogue().values())
#                 contracts.append(list(Electrician.electricians_catalogue().keys())[list(Electrician.electricians_catalogue().values()).index(temp)])
#             elif need == 'painter':
#                 temp = min(Painter.painters_catalogue().values())
#                 contracts.append(list(Painter.painters_catalogue().keys())[list(Painter.painters_catalogue().values()).index(temp)])
#             elif need == 'plumber':
#                 temp = min(Plumber.plumbers_catalogue().values())
#                 contracts.append(list(Plumber.plumbers_catalogue().keys())[list(Plumber.plumbers_catalogue().values()).index(temp)])
#         return  (f"{self.name[:self.name.find(' ')]}'s contracts:{contracts}")


# class Specialist:
#     def __init__(self,name,price):
#         self.name = name
#         self.price = price

# class Electrician(Specialist):
#     profession = 'electrician' 

#     @staticmethod
#     def electricians_catalogue():
#         electricians = {}
#         for obj in gc.get_objects():
#             if isinstance(obj, Electrician):
#                 electricians[str(obj.name)] = obj.price
#         return electricians           

# class Painter(Specialist):
#     profession = 'painter'

#     @staticmethod
#     def painters_catalogue():
#         painters = {}
#         for obj in gc.get_objects():
#             if isinstance(obj, Painter):
#                 painters[str(obj.name)] = obj.price
#         return painters

# class Plumber(Specialist):
#     profession = 'plumber'

#     @staticmethod
#     def plumbers_catalogue():
#         plumbers = {}
#         for obj in gc.get_objects():
#             if isinstance(obj, Plumber):
#                 plumbers[str(obj.name)] = obj.price
#         return plumbers

""""option3 - with staticmethod in parent class and nested dict"""

import gc
import collections


class Homeowner:
    def __init__(self,name, address, needs):
        self.name = name
        self.address = address
        self.needs = needs

    def contracts(self):
        contracts = []
        for need in self.needs:
            lowest_price = min(Specialist.specialists_catalogue()[need].values())
            contracts.append(list(Specialist.specialists_catalogue()[need].keys())[list(Specialist.specialists_catalogue()[need].values()).index(lowest_price)])
        return (f"{self.name[:self.name.find(' ')]}'s contracts:{contracts}")


class Specialist:
    def __init__(self,name,price):
        self.name = name
        self.price = price

    @staticmethod
    def specialists_catalogue():
        specialists_catalogue = collections.defaultdict(dict)
        for obj in gc.get_objects():
            if isinstance(obj, Specialist):
                specialists_catalogue[obj.profession][str(obj.name)] = obj.price
        return specialists_catalogue
                  

class Electrician(Specialist):
    profession = 'electrician' 


class Painter(Specialist):
    profession = 'painter'


class Plumber(Specialist):
    profession = 'plumber'



## adding Specialists instances
alice = Electrician("Alice Aliceville", 50)
john = Electrician("John Johnsville", 50)
bob = Painter("Bob Bobsville", 60)
tom = Painter("Tom Tomsville", 100)
craig = Plumber("Craig Craigsville", 45)

## adding Homeowner instances
alfred = Homeowner("Alfred Alfredson","Alfredslane 123",["painter", "plumber"])
bert = Homeowner("Bert Bertson","Bertslane 231",["plumber"])
candice = Homeowner("Candice Candicedottir","Candicelane 312",["electrician", "painter"])


"""test prints"""

print(alfred.contracts())
print(Homeowner.contracts(alfred))
print(bert.contracts())
print(candice.contracts())
