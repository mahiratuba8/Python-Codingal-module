library={"name":"Mahira Khan", "age":[15], "grade":"10D"}
print(library)

library["Country"]="Sweden"
print(library)

library.pop("age")
print(library)

print("name:",library.get("name"))

library.clear()
print(library)