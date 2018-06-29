my_dictionary = [
    { 
  'name': 'Ramit', 
  'email': 'ramit@gmail.com', 
  'interests': ['movies', 'tennis'], 
  'friends': [ 
     { 
       'name': 'Jasmine', 
       'email': 'jasmine@yahoo.com', 
       'interests': ['photography', 'tennis']
     }, 
     { 
        'name': 'Jan', 
        'email': 'jan@hotmail.com', 
        'interests': ['movies', 'tv'] 
     } 
    ] 
}
]

print(my_dictionary[0]["email"])
print(my_dictionary[0]["interests"])
print(my_dictionary[0]["friends"][0]["email"])
print(my_dictionary[0]["friends"][1]["interests"][1])