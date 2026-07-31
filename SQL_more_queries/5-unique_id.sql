-- creates the table unique_id with id unique and defaulting to 1
CREATE TABLE IF NOT EXISTS unique_id (id INT UNIQUE DEFAULT 1, name VARCHAR(256));
