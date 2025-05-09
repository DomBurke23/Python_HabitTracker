DROP TABLE IF EXISTS users;

CREATE TABLE users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE NOT NULL,
    password TEXT NOT NULL
);

-- Example user (remember to use secure password hashing in production!)
INSERT INTO users (username, password) VALUES ('testuser', 'password123');