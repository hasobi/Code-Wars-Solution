def my_languages(results):
    finalArray = []
    # a berupa list of list jadi iterasi harus berupa list biasa
    a = sorted(results.items(), key=lambda x: x[1], reverse=True)    
    
    print(type(a))


my_languages({"Hindi": 60, "Dutch": 93, "Greek": 71})