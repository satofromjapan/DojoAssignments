my_dict = {
  "Speros": "(555) 555-5555",
  "Michael": "(999) 999-9999",
  "Jay": "(777) 777-7777"
}

def making_tuples(my_dict):
    list = []
    for key in my_dict:
        list.append((key, my_dict[key],))
    print list

making_tuples(my_dict)
