spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]

def get_names(spicy_foods):
    pass
    """Return a list of names of all spicy foods."""
    return [food["name"] for food in spicy_foods]


def get_spiciest_foods(spicy_foods):
    pass
    """Return a list of foods with heat level greater than 5."""
    return [food for food in spicy_foods if food["heat_level"] > 5]


