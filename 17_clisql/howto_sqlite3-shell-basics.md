We were able to create insert into and view databases/tables through the command line prompt.

Breakthroughs:
- how to create tables
- inserting data into the tables
view by column


Steps to use SQL in the command-line prompt:
1. sqlite3 <filename> 
-> open sqlite shell
2. CREATE TABLE <tablename> (<columnName> <datatype>, ...)
-> create a table of the name
3. INSERT INTO <tablename> VALUES (name, column1_val, ..)
-> inserts a value set into the table (with all corresponding column fields)
4. .tables
-> shows all tables in directory
5. SELECT <columnName> FROM <tablename>
-> Displays all of the rows in <tablename> under the column <columnName>
6. .quit
-> closes the sqlite3 shell
