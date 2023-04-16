


CREATE TABLE IF NOT EXISTS financial_data (
    -- id INT(11) NOT NULL AUTO_INCREMENT,
    symbol VARCHAR(255) NOT NULL,
    Date1 DATE,
    open_price FLOAT NOT NULL,
    close_price FLOAT NOT NULL,
    volume  BIGINT,
    PRIMARY KEY (symbol,Date1,open_price,close_price,volume)
);

