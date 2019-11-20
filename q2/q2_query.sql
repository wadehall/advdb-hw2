/* Use Distinct */
SELECT DISTINCT stocksymbol, time, quantity, price
FROM trade

/* Eliminate uneeded Distinct */
SELECT stocksymbol, time, quantity, price
FROM trade


/* Leveraging Covering Indexes */
SELECT price, stocksymbol
FROM trade
WHERE price > 400
