# Advanced Database Systems - Homework 2

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

### The two rules of thumbs

1. Eliminate unneeded DISTINCTs
2. Leveraging Covering Indexes

### The two database systems

1. MySQL
2. KDB

### The two data distributions

1. Uniform distribution
2. Fractal distribution (we used the trades data generated from problem 1)

### The average time of the results

1. MySQL

|             | Uniform | Fractal |
| ----------- | ------- | ------- |
| Distinct    |         |         |
| No Distinct |         |         |
| Covering    |         |         |
| No Covering |         |         |

2. KDB

|             | Uniform | Fractal |
| ----------- | ------- | ------- |
| Distinct    |         |         |
| No Distinct |         |         |
| Covering    |         |         |
| No Covering |         |         |

The query codes we used were attached in the q2_query.a file.

### 1). Eliminate unneeded DISTINCTs

TO-DO

### 2). Leveraging Covering Indexes

TO-DO

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
