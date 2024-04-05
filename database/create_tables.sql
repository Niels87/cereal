-- @block create tables
-- @conn local_mysql
-- @label Set up products table
CREATE TABLE IF NOT EXISTS cereal(
    ID          INT PRIMARY KEY AUTO_INCREMENT,
    name        VARCHAR(255) NOT NULL,
    mfr         CHAR,
    type        CHAR,
    calories    INT,
    protein     INT,
    fat         INT,
    sodium      INT,
    fiber       FLOAT,
    carbo       FLOAT,
    sugars      INT,
    potass      INT,
    vitamins    INT,
    shelf       INT,
    weight      FLOAT,
    cups        FLOAT,
    rating      VARCHAR(255)
);
