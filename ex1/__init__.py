def build_roles_tree(mapping):
    """
    :param mapping: маппинг ролей в категории
    :return: дерево ролей
    """
    categories = mapping["categories"]
    category_order_by_id = mapping["categoryIdsSorted"]
    roles = mapping["roles"]

    tree = {}
    mapped_categories = []
    for category_order_id in category_order_by_id:
        category_dict = {}
        category_dict["id"] = f"category-{category_order_id}"
        category_dict["text"] = categories[category_order_id]["name"]
        category_items = []
        for role_id in categories[category_order_id]["roleIds"]:
            role_dict = {}
            role_dict["id"] = roles[role_id]["id"]
            role_dict["text"] = roles[role_id]["name"]
            category_items.append(role_dict)
        mapped_categories.append(category_dict)
    tree["categories"] = mapped_categories
    return tree
