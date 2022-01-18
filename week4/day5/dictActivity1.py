# phonebook_dict = { 'Alice': '703-493-1834', 'Bob': '857-384-1234', 'Elizabeth': '484-584-2923' }

# # print(phonebook_dict["Elizabeth"])
# phonebook_dict["kareem"] = "938-489-1234"
# # print(phonebook_dict)
# del phonebook_dict["Alice"]
# # print(phonebook_dict)
# phonebook_dict["Bob"] = "968-345-2345"
# print(phonebook_dict)

ramit = { 
  'name': 'Ramit', 
  'email': 'ramit@gmail.com', 
  'interests': ['movies', 'tennis'], 
  
  'friends': 
    [ { 
      'name': 'Jasmine',       
      'email': 'jasmine@yahoo.com', 
      'interests': ['photography', 'tennis'] },
  
      { 
      'name': 'Jan', 
      'email': 'jan@hotmail.com', 
      'interests': ['movies', 'tv'] 
    } ] 
}

email = ramit['email']
# print(email)

interests = ramit["interests"][0]
# print(interests)

jasmineEmail = ramit["friends"][0]["email"] 
# print(jasmineEmail)

janInterest = ramit["friends"][1]["interests"][0]
# print(janInterest)





