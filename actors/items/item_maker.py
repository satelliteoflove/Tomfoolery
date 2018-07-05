def make_new_item():
    import yaml

    item = {}
    item['generic_name'] = input("Generic Item Name:")
    item['weight'] = input("Item weight:")
    item['equip_slot'] = input("What slot can it be equipped in?")
    item['break_chance'] = input("What is the chance of breaking on use?")

    for k,v in item.items():
        print(k + " = " + v)

