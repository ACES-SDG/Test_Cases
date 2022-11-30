capital_info = {
    "India": "New Delhi",
    "USA": "Washington DC",
    "UK": "London"
}
# rename key in dictionary
print(capital_info)

capital_info["United States of America"] = capital_info.pop("USA")
# display the dictionary
print(capital_info)