def error():
    try:
        li = [10,20,30,40,50]
        return li[8]
    except IndexError:
        return "Invalid Index"
