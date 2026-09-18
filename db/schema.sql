-- ============================================================
-- Base de TEST Ytasty Crousty
-- A remplacer par le script genere par Looping quand il sera pret.
-- PostgreSQL execute ce fichier a la premiere creation de la base.
-- ============================================================

CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    email TEXT NOT NULL UNIQUE,
    name TEXT NOT NULL
);

CREATE TABLE restaurants (
    id SERIAL PRIMARY KEY,
    name TEXT NOT NULL,
    address TEXT NOT NULL
);

CREATE TABLE products (
    id SERIAL PRIMARY KEY,
    restaurant_id INTEGER NOT NULL REFERENCES restaurants (id),
    name TEXT NOT NULL,
    price NUMERIC(6, 2) NOT NULL,
    available BOOLEAN NOT NULL DEFAULT TRUE
);

-- ------------------------------------------------------------
-- Donnees de test
-- ------------------------------------------------------------

INSERT INTO users (email, name) VALUES
    ('florian@example.com', 'Florian'),
    ('alice@example.com', 'Alice');

INSERT INTO restaurants (name, address) VALUES
    ('Chez Crousty', '12 rue du Poulet, Lyon'),
    ('Ytasty Pizza', '3 avenue de la Marguerite, Lyon');

INSERT INTO products (restaurant_id, name, price, available) VALUES
    (1, 'Poulet crousty', 9.90, TRUE),
    (1, 'Frites maison', 3.50, TRUE),
    (2, 'Pizza margherita', 11.00, TRUE),
    (2, 'Pizza 4 fromages', 13.50, FALSE);
