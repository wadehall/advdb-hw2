-- DROP TABLE IF EXISTS trade_fractal;
-- CREATE TABLE trade_fractal (stocksymbol INT, time INT, quantity INT, price INT);
--
-- LOAD DATA INFILE "trade_fractal.csv"
-- INTO TABLE trade_fractal
-- FIELDS TERMINATED BY ","
-- IGNORE 1 LINES;
--
-- DROP TABLE IF EXISTS trade_uniform;
-- CREATE TABLE trade_uniform (stocksymbol INT, time INT, quantity INT, price INT);
--
-- LOAD DATA INFILE "trade_uniform.csv"
-- INTO TABLE trade_uniform
-- FIELDS TERMINATED BY ","
-- IGNORE 1 LINES;

/* Distinct */
SELECT DISTINCT stocksymbol, time, quantity, price
FROM trade

/* No Distinct */
SELECT stocksymbol, time, quantity, price
FROM trade

/* Covering Index */
SELECT stocksymbol
FROM trade
WHERE price > 100
