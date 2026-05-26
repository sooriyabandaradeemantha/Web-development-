CREATE TABLE IF NOT EXISTS STUDS(
    ROLL_NUMBER TEXT PRIMARY KEY,
    NAME TEXT NOT NULL,
    ADDRESS TEXT,
    PHONE TEXT,
    AGE INTEGER
    );

INSERT INTO STUDS(ROLL_NUMBER,NAME,ADDRESS,PHONE,AGE)VALUES
('1','John','Kegalle','*******',17),
('2','Sujith','Colombo','*******',15),
('3','Ram','Delhi','*******',18),
('4','Ramesh','GallFace','*******',19),
('5','Trump','Kegalle','*******',20),
('6','Jack','Colombo','*******',22);

SELECT * FROM STUDS;

SELECT * FROM STUDS WHERE AGE=18 AND ADDRESS='Delhi';
SELECT * FROM STUDS WHERE NAME='Ram' AND AGE=18;
SELECT * FROM STUDS WHERE NAME='Ram' OR NAME='Sujith';
SELECT * FROM STUDS WHERE AGE=18 AND NAME='Ram' OR NAME='Ramesh';







