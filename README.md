# Quiz
Hello Everyone.. I've made my first Git hub repository now. In this repository, I've created a python script that has 3 types of test - Tamilnadu vehicle number test, atomic number test, morse code test. It works like a quiz program and stores your scores, time taken to complete all these datas to the mysql database.

Tools Used :
 * Python 3.13.1
 * MySQL 8.0

mysql.connector is used to connect python and mysql. 

How to run :
  1. Download MySQL 8.0
  2. Download Python 3.13.1 (Python 3.7+)
  3. In cmd type "pip install mysql-connector-python"
  4. Paste the python code in your IDLE
  5. You need not do anything in MySQL, just run the python script and try accessing the program
  6. When you finish the test, your scores will be stored to the MySQL Database
  7. To check your stored datas in MySQL, go to MySQL and type the following commands;
      * USE Python_Test;
      * SELECT * FROM Vehicle_Number_Test;
      * SELECT * FROM Morse_Code_Test;
      * SELECT * FROM Atomic_Number_Test;
    
I know that this is very basic, just trying to upload something I've done. Definitely there will be more future updates. Keep Updated!
