CREATE TABLE IF NOT EXISTS RESTU(
name TEXT,
neighborhood TEXT,
cuisine TEXT,
review REAL,
price TEXT,
health TEXT
);
INSERT INTO RESTU(name,neighborhood,cuisine,review,price,health)VALUES
    ('Peter','Broclyne','Steak',4.4,'$$$$','A'),
    ('Jogron','Midtown','Korean',3.5,'$$','A'),
    ('Pocha','Midtown','Pizza',4.0,'$$$','B'),
    ('Lighthouse','Queens','Chinese',3.9,'$','A'),
    ('Minca','Downtown','American',4.6,'$$$',''),
    ('Marea','ChinaTown','Chinese',3.0,'$$',''),
    ('Dirty Candy','UpTown','Italian',4.9,'$$$','B'),
    ('De Fara Pizza','Broclyne','Pizza',3.8,'$$','A'),
    ('Golden Unicorn','UpTown','Italian',3.8,'$$','A');

SELECT DISTINCT neighborhood FROM RESTU
SELECT DISTINCT cuisine FROM RESTU
SELECT * FROM RESTU WHERE cuisine = 'Chinese'
SELECT * FROM RESTU WHERE review > 4.0
SELECT * FROM RESTU WHERE cuisine = 'Italian' AND price IN ('$','$$','$$$','$$$$')
SELECT * FROM RESTU WHERE cuisine = 'Italian' AND price = '$'
SELECT * FROM RESTU WHERE name LIKE '%candy%'
SELECT * FROM RESTU WHERE neighborhood IN ('Midtown','UpTown','Downtown')
SELECT * FROM RESTU WHERE health IS NOT NULL














