CREATE TABLE messages (
  id SERIAL PRIMARY KEY,
  text TEXT NOT NULL
);

INSERT INTO messages (text) VALUES ('Hello from PostgreSQL inside Docker!');
