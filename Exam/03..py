def cookbook(*args):
    cuisines={}
    for recepies in args:

        if recepies[1] not in cuisines.keys():
            cuisines[recepies[1]]=1

        else:
            cuisines[recepies[1]]+=1

    args.sort(key=lambda x: x[1] )






print(cookbook(
    ("Spaghetti Bolognese", "Italian", ["spaghetti", "tomato sauce", "ground beef"]),
    ("Margherita Pizza", "Italian", ["pizza dough", "tomato sauce", "mozzarella"]),
    ("Tiramisu", "Italian", ["ladyfingers", "mascarpone", "coffee"]),
    ("Croissant", "French", ["flour", "butter", "yeast"]),
    ("Ratatouille", "French", ["eggplant", "zucchini", "tomatoes"])
))
