- In the Northwind database, what is the type of relationship between the `Employee` and `Territory` tables?

Employee and territory are two tables in a relational database connected by the employee territory table. Since one record of an employee relates to many records of a territory, the employee and territory tables have a one to many relationship.

- What is a situation where a document store (like MongoDB) is appropriate, and what is a situation where it is not appropriate?

An appropriate situation for NoSQL would be for large volumes of data, using cloud services, the data structure is changing, or the data structure is rapidly growing.

An inappropriate situation would be if ACID compliancy is important. ACID stands for Atomicity, Consistency, Isolation, and Durability. Also if the data structure has a consistent, unchanging structure then SQL would be better.


- What is "NewSQL", and what is it trying to achieve?

NewSQL is attempting to merge the benefits of SQL and NoSQL. This is being done by using traditional SQL querying along with ACID compliancy from SQL while also benefitting from the speed, storage power, and complexity that NoSQL has.