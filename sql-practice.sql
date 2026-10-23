DROP TABLE IF EXISTS books;
DROP TABLE IF EXISTS authors;

CREATE TABLE authors (
    id INT PRIMARY KEY,
    name TEXT NOT NULL
);

CREATE TABLE books (
    id INT PRIMARY KEY,
    title TEXT NOT NULL,
    year_published INT,
    author_id INT,
    FOREIGN KEY (author_id) REFERENCES authors(id)
);

INSERT INTO authors (id, name) VALUES
(1, 'George Orwell'),
(2, 'Rick Riordan'),
(3, 'J.K. Rowling');

INSERT INTO books (id, title, year_published, author_id) VALUES
(1, '1984', 1949, 1),
(2, 'The Lightning Thief', 2005, 2),
(3, 'Harry Potter and the Sorcerer''s Stone', 1997, 3);

SELECT * FROM books;

SELECT title, year_published FROM books
WHERE year_published > 2000;

UPDATE books
SET year_published = 2010
WHERE id = 2;

SELECT * FROM books;

--Delete 
DELETE FROM books WHERE id = 4;
SELECT * FROM books;

-- Join
SELECT books.title, books.year_published, authors.name
FROM books
JOIN authors ON books.author_id = authors.id;