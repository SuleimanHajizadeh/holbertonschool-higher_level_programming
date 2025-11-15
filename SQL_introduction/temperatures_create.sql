-- Create temperatures table
CREATE TABLE IF NOT EXISTS temperatures (
    city VARCHAR(50),
    temp FLOAT
);

-- Insert sample data
INSERT INTO temperatures (city, temp) VALUES
('Tucson', 126.29),
('Pismo beach', 94.51),
('San Jose', 84.08),
('Phoenix', 83.70),
('Sonoma', 81.48),
('San Francisco', 72.55),
('Peoria', 65.41),
('Naperville', 57.31),
('Chicago', 42.00);
