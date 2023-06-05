CREATE TABLE IF NOT EXISTS luggage (
    id varchar(255) NOT NULL,
    owner VARCHAR(255) NOT NULL,
    weight INT NOT NULL,

    check_in_time DATETIME,
    check_in_location VARCHAR(255),

    destination_gate VARCHAR(255),

    location VARCHAR(255),
    last_moved DATETIME DEFAULT CURRENT_TIMESTAMP,

    PRIMARY KEY (id)

);