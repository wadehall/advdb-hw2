/* Use Distinct */
SELECT DISTINCT stocksymbol, time, quantity, price
FROM trade

/* Eliminate unneeded Distinct */
SELECT stocksymbol, time, quantity, price
FROM trade


/* Leveraging Covering Indexes */
SELECT stocksymbol
FROM trade
WHERE price > 100
