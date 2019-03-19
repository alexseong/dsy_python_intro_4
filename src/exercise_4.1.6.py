lst = []
while True:
    s_num = input("Enter a number: ")
    if s_num.lower() == "done":
        if len(lst) > 0:
            print("Maximum:", max(lst))
            print("Minimum:", min(lst))
        break

    try:
        i_num = int(s_num)
        lst.append(i_num)
    except:
        print("Enter valid integer")
        continue
