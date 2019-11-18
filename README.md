# Advanced Database Systems - Homework 2

## Question 1
### Generate data
- Run `trade_gen.py` to generate data which will be stored in `trade.csv`.
- It takes me ~18min to generate 10,000,000 records on my laptop.

### Run the queries
- Make sure you have installed `q`, `sbt`, and `java`
- Get [aquery's jar](
https://drive.google.com/file/d/0B9IR8VjNetPYbWRIX0x2SEdoUGc/view)
and put it in the same directory (`q1/`)
- Translate AQuery to q code by running:
    ```bash
    java -jar aquery.jar -a 1 -c -o trade_query.q trade_query.a
    ```
  Or if you've [wrapped the call to java and added it to your path](
  https://github.com/josepablocam/aquery#installationbuilding):
    ```bash
    a2q -a 1 -c -o trade_query.q trade_query.a
    ```
  This will generate `trade_query.q`.
- Run and time the queries:
    ```bash
    time q trade_query.q
    ```
- The outputs will go to `query_a.csv`, `query_b.csv`, `query_c.csv`,
  and `query_d.csv`.
  
## Question 3
### Run the query
- Make sure the input data files are named `friends.csv` and `like.csv`
- Make sure you have installed `q`, `sbt`, and `java`
- Get [aquery's jar](
https://drive.google.com/file/d/0B9IR8VjNetPYbWRIX0x2SEdoUGc/view)
and put it in the same directory (`q3/`)
- Translate AQuery to q code by running:
    ```bash
    java -jar aquery.jar -a 1 -c -o q3_query.q q3_query.a
    ```
  Or if you've [wrapped the call to java and added it to your path](
  https://github.com/josepablocam/aquery#installationbuilding):
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