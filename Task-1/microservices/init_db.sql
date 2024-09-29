-- Create table
CREATE TABLE tasks (
    id SERIAL PRIMARY KEY,
    description VARCHAR(255) NOT NULL
);

-- Insert sample data
INSERT INTO tasks (description) VALUES ('Task 1');
INSERT INTO tasks (description) VALUES ('Task 2');
INSERT INTO tasks (description) VALUES ('Task 3');
