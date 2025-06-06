categories = {
    "category_1": {
        "name":"category 1",
        "id":1,
        "description":"",
        "subcategories":[
            {
                "name":"subcategory 1",
                "description":"",
                "id":3,
                "subcategories":None
            },
            {
                "name":"subcategory 2",
                "description":"",
                "id":4,
                "subcategories":None
            }
        ]
    },
    "category_2": {
        "name":"category 2",
        "id":2,
        "description":"",
        "subcategories":[
            {
                "name":"subcategory 3",
                "description":"",
                "id":5,
                "subcategories":None
            },
            {
                "name": "subcategory 4",
                "description":"",
                "id":6,
                "subcategories":None
            }
        ]
    }
}

for id, info in categories.items():
    print(f"Categoría: {info['name']} (ID: {id})")

    subcategories = info.get("subcategories", [])
    if subcategories:
        for sub in subcategories:
            print(f"  └─ Subcategoría: {sub['name']} (ID: {sub['id']})")

