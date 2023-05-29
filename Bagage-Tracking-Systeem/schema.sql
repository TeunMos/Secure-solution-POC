CREATE TABLE IF NOT EXISTS luggage (
    id varchar(255) NOT NULL,
    owner VARCHAR(255) NOT NULL,
    weight INT NOT NULL,

    check_in_time DATETIME,
    check_in_location VARCHAR(255),

    destination_gate VARCHAR(255),

    location VARCHAR(255),
    last_moved DATETIME DEFAULT CURRENT_DATE,

    PRIMARY KEY (id)

);



CREATE TABLE IF NOT EXISTS gates (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    location VARCHAR(255) NOT NULL
);

INSERT INTO gates (location)
    SELECT 'gate A' 
    UNION SELECT 'gate B' 
    UNION SELECT 'gate C'
    UNION SELECT 'gate D' 
    UNION SELECT 'gate E' 
    UNION SELECT 'gate F'
    WHERE NOT EXISTS (SELECT 1 FROM gates);






