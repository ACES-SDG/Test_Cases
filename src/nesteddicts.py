# dict1  = {}
# 3 levels deep nested dictionary
dicth =    {
    "Dashboard 1": 
        {
            "sheet 1": 
                {
                    "water": 50,
                    "coffee": 18,
                },
            "sheet 2": 1.5,
        },
    "Dashboard 2": 
        {
            "sheet 3": 
                {
                    "water": 200,
                    "milk": 150,
                    "coffee": 24,
                },
            "sheet 4": 2.5,
        },
    "Dashboard 3": 
        {
            "sheet 3": 
                {
                    "water": 250,
                    "milk": 100,
                    "coffee": 24,
                },
            "sheet 4": 3.0,
        }
    }

# print(dicth["espresso"],'\n\n')
# dicth["espresso"].update({'ok':{'w':123}})
# print(dicth["espresso"])
# if dicth.__len__() == 0:
#     print('0')
# else:
#     print((dicth["cappuccino"].keys())  )
# x = tuple(dicth["Dashboard 3"].keys())
# print(type(x),x)

# print(dicth,'\n')

# # dicth["Dashboard 3"].update({'sheet 3':{'water':12,'milk':25}})

# dicth["Dashboard 3"].get('sheet 3').update({'water':12,'milk':25})        #.update({'sheet 3':{'water':12,'milk':25}})

# print(dicth,'\n')


# if dicth["Dashboard 2"].keys():
#     print('t')
# else:
#     print('f')

# print(dicth["Dashboard 3"]['sheet 3'].get('milk'))

# if 'milk_' in dicth["Dashboard 3"]['sheet 3'].keys():
#     print('ok')
# else:
#     print('no')
    
# print(dicth, ' before \n')
# if 'sheet 3' in dicth["Dashboard 3"].keys():
#     dicth['Dashboard 3']['rename_this'] = dicth["Dashboard 3"].pop('sheet 3')
#     print(dicth,'after')
    
# else:
#     print('not ok')


# print(dicth['Dashboard 3']['sheet 3'].get('water'))


# dicth['Dashboard 3']['sheet 3'].keys() = True
