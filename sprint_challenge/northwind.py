import sqlite3

conn = sqlite3.connect("northwind_small.sqlite3")
curs = conn.cursor()

curs.execute("SELECT * FROM Product")

#What are the ten most expensive items (per unit price) in the database?
ten_most_expensive_products = """
    SELECT ProductName, UnitPrice
    FROM Product
    ORDER BY UnitPrice DESC
    LIMIT 10
    """
curs.execute(ten_most_expensive_products)
print("Ten most expensive products")
for row in curs:
    print(row)
print("\n")
# What is the average age of an employee at the time of their hiring? (Hint: a
# lot of arithmetic works with dates.)
avg_age_at_hiring = """
    SELECT AVG(HireDate - BirthDate)
    AS "HireAge"
    FROM Employee;
    """
print('Average hire age:', list(curs.execute(avg_age_at_hiring))[0][0])
print('\n')
# What are the ten most expensive items (per unit price) in the database *and* their suppliers?
expensive_items_and_suppliers = """
    SELECT ProductName, UnitPrice, CompanyName
    FROM Product
    LEFT JOIN Supplier
    ON Product.SupplierId = Supplier.Id
    ORDER BY UnitPrice DESC
    LIMIT 10
    """
curs.execute(expensive_items_and_suppliers)
print("Ten most expensive products and suppliers")
for row in curs:
    print(row)
print("\n")

# What is the largest category (by number of unique products in it)?
largest_category = """
    SELECT CategoryName, MAX(catcount)
    FROM
    (SELECT *, COUNT(CategoryId) as catcount
    FROM Product
    LEFT JOIN Category
    ON Product.CategoryId = Category.Id
    GROUP BY CategoryId)
    """
curs.execute(largest_category)
print("Largest category")
print(list(curs))

"""
OUTPUT FROM PYTHON REPL
python northwind.py
Ten most expensive products
('Côte de Blaye', 263.5)
('Thüringer Rostbratwurst', 123.79)
('Mishi Kobe Niku', 97)
("Sir Rodney's Marmalade", 81)
('Carnarvon Tigers', 62.5)
('Raclette Courdavault', 55)
('Manjimup Dried Apples', 53)
('Tarte au sucre', 49.3)
('Ipoh Coffee', 46)
('Rössle Sauerkraut', 45.6)


Average hire age: 37.22222222222222


Ten most expensive products and suppliers
('Côte de Blaye', 263.5, 'Aux joyeux ecclésiastiques')
('Thüringer Rostbratwurst', 123.79, 'Plutzer Lebensmittelgroßmärkte AG')
('Mishi Kobe Niku', 97, 'Tokyo Traders')
("Sir Rodney's Marmalade", 81, 'Specialty Biscuits, Ltd.')
('Carnarvon Tigers', 62.5, 'Pavlova, Ltd.')
('Raclette Courdavault', 55, 'Gai pâturage')
('Manjimup Dried Apples', 53, "G'day, Mate")
('Tarte au sucre', 49.3, "Forêts d'érables")
('Ipoh Coffee', 46, 'Leka Trading')
('Rössle Sauerkraut', 45.6, 'Plutzer Lebensmittelgroßmärkte AG')


Largest category
[('Confections', 13)]
"""