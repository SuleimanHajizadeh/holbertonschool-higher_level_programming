-- 4-first_table.sql
-- Bu skript current database-də first_table adlı cədvəli yaradır
-- Əgər cədvəl artıq varsa, heç bir xəta verməyəcək
CREATE TABLE IF NOT EXISTS first_table (
    id INT,
    name VARCHAR(256)
);
