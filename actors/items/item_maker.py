import yaml

item = {}

def menu():

    print("Please select a trait to edit: \n\n 
    (1) General Item Traits\n
    (2) Wearable Item Traits\n
    (3) Weapon Item Traits\n
    (4) Usable Item Traits\n
    (5) Special Item Traits"
    choice = input()

def generic_traits():
    """Set generic item traits, such as weight or alignment, 
    :returns: TODO

    """
    print("Edit which trait?")
    print("(1) Generic Name\n
           (2) Weight\n
           (3) Specific Name\n
    item['generic_name'] = input("What is the generic name?")
    menu()k

def wearable_traits():
    """Set wearable item traits, such as equipment slot.
    :returns: TODO

    """
    pass

return item
