# Advanced Database Systems - Homework 2

Team members:

- Zheng Jiang, Net ID: zj688
- Shih-Yao Chou, Net ID: syc574

## Question 1

### Generate data

- Run `trade_gen.py` to generate data which will be stored in `trade.csv`.
- It takes me ~18min to generate 10,000,000 records on my laptop.

### Run the queries

- Make sure you have installed `q`, `sbt`, and `java`
- Get [aquery's jar](https://drive.google.com/file/d/0B9IR8VjNetPYbWRIX0x2SEdoUGc/view)
  and put it in the same directory (`q1/`)
- Translate AQuery to q code by running:
  ```bash
  java -jar aquery.jar -a 1 -c -o trade_query.q trade_query.a
  ```
  Or if you've [wrapped the call to java and added it to your path](https://github.com/josepablocam/aquery#installationbuilding):
  ```bash
  a2q -a 1 -c -o trade_query.q trade_query.a
  ```
  This will generate `trade_query.q`.
- Run the queries:
  `bash q trade_query.q`
  You will get the following output in kdb+:
  `` `trade `trade `query_a `query_b `query_c `query_d q) ``
  Results of the four queries are stored in tables `` `query_a ``,
  `` `query_b ``, `` `query_c ``, and `` `query_d ``, respectively.

  The prompt `q)` in the end means you are still in a q console session.

- Type the name of each table to show its content:

  ```
  q)query_a
  ...
  q)query_b
  ...
  q)query_c
  ...
  q)query_d
  ...
  ```

## Question 2

### The two rule of thumbs used here

1. Eliminate unnecessary DISTINCT method

2. Leverage Covering Indexes method  
   A covering index is a special case where the index itself contains the required data field(s) and can answer the required data.

### The two database systems used here

1. MySQL
2. KDB

### The two data distributions used here

1. Uniform distribution
2. Fractal distribution (we used the trades data generated from Question 1)

### The average time of the results

1. MySQL

|                        | Uniform Distribution | Fractal Distribution |
| ---------------------- | -------------------- | -------------------- |
| With Distinct          |                      |                      |
| Without Distinct       |                      |                      |
| With Covering Index    |                      |                      |
| Without Covering Index |                      |                      |

2. KDB

|                        | Uniform Distribution | Fractal Distribution |
| ---------------------- | -------------------- | -------------------- |
| With Distinct          |                      |                      |
| Without Distinct       |                      |                      |
| With Covering Index    |                      |                      |
| Without Covering Index |                      |                      |

The query codes we used were attached in the q2_query.a file.

### 1). Eliminate unnecessary DISTINCT method

The original query code used DISTINCT method as follows:

```
SELECT DISTINCT stocksymbol, time, quantity, price FROM trade;
```

&nbsp;
Firstly, we got the unique records with ***stock symbol, time, qunatity*** and ***price*** atrributes by using DISTINCT method. However, we noticed that it's unnecessary to have DISTINCT method since we've already selected the ***time*** attribute which always produces an unique value.

Thus, we can remove the unneeded DISTINCT method and still get the same results through below query:

```
SELECT stocksymbol, time, quantity, price FROM trade;
```

&nbsp;
From the result above, ... TO-DO (Analyze the averge time of two systems with two data distribution for this rule of thumb)

&nbsp;

### 2). Leverage Covering Indexes method

The way to create a covering index is as follows:

- MySQL:

```
CREATE INDEX price_stocksymbol ON trade (price, stocksymbol);
```

- KDB:

```
TO-DO
```

&nbsp;
We followed the instruction from book, and made an index on (price, stocksymbol) contains the required data field and eliminates the need to look up the record. It not only avoids accessing the table to evaluate the where clause, but avoids accessing the table completely if the database can find the selected columns in the index itself.

If the table has a multiple-column index, any leftmost prefix of the index can be used by the optimizer to look up rows. However, MySQL cannot use the index to perform lookups if the columns do not form a leftmost prefix of the index. Thus, we make ***price*** column in the leftmost prefix of the index (as the above SQL command) to make the below query effective:

```
SELECT price, stocksymbol FROM trade WHERE price > 400;
```

&nbsp;
From the result above, ... TO-DO (Analyze the averge time of two systems with two data distribution for this rule of thumb)

## Question 3

### Run the query

- Make sure the input data files are named `friends.csv` and `like.csv`
- Make sure you have installed `q`, `sbt`, and `java`
- Get [aquery's jar](https://drive.google.com/file/d/0B9IR8VjNetPYbWRIX0x2SEdoUGc/view)
  and put it in the same directory (`q3/`)
- Translate AQuery to q code by running:
  ```bash
  java -jar aquery.jar -a 1 -c -o q3_query.q q3_query.a
  ```
  Or if you've [wrapped the call to java and added it to your path](https://github.com/josepablocam/aquery#installationbuilding):
  ```bash
  a2q -a 1 -c -o q3_query.q q3_query.a
  ```
  This will generate `q3_query.q`.
- Run and time the queries:
  ```bash
  time q q3_query.q
  ```
- The output will go to `result.csv`.
- If you don't want to generate the output to a file, comment out the last few
  lines in `q3_query.a`.
