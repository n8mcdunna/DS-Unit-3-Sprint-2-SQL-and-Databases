
TOTAL_CHARACTERS = """
    SELECT COUNT(*)
    FROM charactercreator_character;
    """
TOTAL_MAGES = """
    SELECT COUNT(*) 
    FROM charactercreator_mage;
    """
TOTAL_THIEFS = """
    SELECT COUNT(*) 
    FROM charactercreator_thief;
    """
TOTAL_CLERICS = """
    SELECT COUNT(*) 
    FROM charactercreator_cleric;
    """
TOTAL_FIGHTERS = """
    SELECT COUNT(*) 
    FROM charactercreator_fighter;
    """  
TOTAL_ITEMS = """
    SELECT COUNT(*) 
    FROM armory_item;
    """
TOTAL_WEAPON_ITEMS = """
    SELECT COUNT(*)
    FROM armory_item i
    INNER JOIN armory_weapon w
    ON i.item_id = w.item_ptr_id;
    """
TOTAL_NON_WEAPON_ITEMS = """
    SELECT COUNT(item_id)
    FROM armory_item i
    LEFT JOIN armory_weapon w
    ON i.item_id = w.item_ptr_id
    WHERE w.item_ptr_id IS NULL;
    """
ITEMS_PER_FIRST_20_CHARACTERS = """
    SELECT character_id, COUNT(item_id) AS items
    FROM charactercreator_character_inventory 
    GROUP BY character_id
    LIMIT 20;
    """
WEAPONS_PER_FIRST_20_CHARACTERS = """
    SELECT character_id, COUNT(item_ptr_id) num_weapons
    FROM charactercreator_character_inventory c
    INNER JOIN armory_item AS ai
        ON ai.item_id = c.item_id
            INNER JOIN armory_weapon AS aw
            ON aw.item_ptr_id = ai.item_id
    GROUP BY character_id
    LIMIT 20;
    """
ITEMS_PER_CHARACTER_AVERAGE = """
    SELECT AVG(items)
    FROM 
    (SELECT *, COUNT(item_id) as items
    FROM charactercreator_character_inventory
    GROUP BY character_id);
    """
WEAPONS_PER_CHARACTER_AVERAGE = """
    SELECT AVG(num_weapons)
    FROM
    (SELECT character_id, COUNT(item_ptr_id) num_weapons
    FROM charactercreator_character_inventory c
    INNER JOIN armory_item AS ai
        ON ai.item_id = c.item_id
            INNER JOIN armory_weapon AS aw
            ON aw.item_ptr_id = ai.item_id
    GROUP BY character_id);
    """

RPG_QUERIES = {"TOTAL_CHARACTERS":TOTAL_CHARACTERS, 
            "TOTAL_MAGES":TOTAL_MAGES,
            "TOTAL_THIEFS":TOTAL_THIEFS,
            "TOTAL_CLERICS":TOTAL_CLERICS,
            "TOTAL_FIGHTERS":TOTAL_FIGHTERS,
            "TOTAL_ITEMS":TOTAL_ITEMS,
            "TOTAL_WEAPON_ITEMS":TOTAL_WEAPON_ITEMS,
            "TOTAL_NON_WEAPON_ITEMS":TOTAL_NON_WEAPON_ITEMS,
            "ITEMS_PER_FIRST_20_CHARACTERS":ITEMS_PER_FIRST_20_CHARACTERS,
            "WEAPONS_PER_FIRST_20_CHARACTERS":WEAPONS_PER_FIRST_20_CHARACTERS,
            "ITEMS_PER_CHARACTER_AVERAGE":ITEMS_PER_CHARACTER_AVERAGE,
            "WEAPONS_PER_CHARACTER_AVERAGE":WEAPONS_PER_CHARACTER_AVERAGE}
