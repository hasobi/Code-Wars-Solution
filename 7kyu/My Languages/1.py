def my_languages(results):
    finalArray = []
    # a berupa list of list jadi iterasi harus berupa list biasa
    a = sorted(results.items(), key=lambda x: x[1], reverse=True)    
    for k in a:
        if (k[1]>=60):
            finalArray.append(k[0])
    return finalArray
