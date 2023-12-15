CREATE EXTENSION IF NOT EXISTS "uuid-ossp";

CREATE TABLE IF NOT EXISTS categories (
    category_id UUID NOT NULL UNIQUE DEFAULT uuid_generate_v4() PRIMARY KEY,
    category_name VARCHAR(255) NOT NULL
);

CREATE TABLE IF NOT EXISTS users (
    user_id UUID NOT NULL UNIQUE DEFAULT uuid_generate_v4() PRIMARY KEY,
    username VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL,
    category_id UUID REFERENCES categories(category_id),
    ranking VARCHAR(1)
);

CREATE TABLE IF NOT EXISTS status (
    status_id UUID NOT NULL UNIQUE DEFAULT uuid_generate_v4() PRIMARY KEY,
    status_name VARCHAR(255) NOT NULL
);

CREATE TABLE IF NOT EXISTS tickets (
    ticket_id UUID NOT NULL UNIQUE DEFAULT uuid_generate_v4() PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    description TEXT NOT NULL,
    client_id UUID NOT NULL REFERENCES users(user_id),
    analyst_id UUID NOT NULL REFERENCES users(user_id),
    status_id UUID NOT NULL REFERENCES status(status_id),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    closed_by UUID REFERENCES users(user_id)
);

INSERT INTO categories (category_name) VALUES ('analyst'), ('client');
INSERT INTO status (status_name) VALUES ('pending'), ('review'), ('solved'), ('closed');
