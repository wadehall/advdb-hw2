# Advanced Database Systems - Homework 2
 
## Generate data
- Run `trade.py` to generate data which will be stored in `trade.csv`.
- It takes me ~18min to generate 10,000,000 records.

## Run query
- Make sure you have installed `q`, `sbt`, and `java`
- Get [aquery's jar](
https://drive.google.com/file/d/0B9IR8VjNetPYbWRIX0x2SEdoUGc/view)
and put it in the same directory
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