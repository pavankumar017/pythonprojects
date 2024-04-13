def div(a, b):
    s = int(a)
    d = int(b)
    try:
        print(s/d)
    except  (Exception) as e:
        print(e)

    finally:
        print("close it ")

div('1', '1')