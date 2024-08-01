CREATE TABLE Users (
    id INT PRIMARY KEY,
    name VARCHAR(100)
);


INSERT INTO Users (id, name) VALUES (1, 'Lionel Messi');


UPDATE Users
SET name = 'Cristiano Ronaldo'
WHERE id = 1;


DELETE FROM Users
WHERE id = 1;
