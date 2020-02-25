# Weather comparison from two different sites

## General info
The main goal of project - to compare weather from two different sites (Sinoptik and Dark Sky) for three cites on next three days.
Main language - Python 2.7

## Technologies
* selenium;
* pytest;
* requests;

## Setup
To run this project:
1. Update or use default version(80.0.3987.106, must match with your version of Chrome) of chromedriver.exe in /drivers folder.
2. To run tests, go to project directory and run the commands:
```
$ pytest -rA tests/all_tests.py  #full result log
$ pytest -rA tests/all_tests.py --tb=short #shorter result log
$ pytest -rA tests/all_tests.py --tb=line #one line result log
```
2.1. To run tests and save the results of tests, run the command:
```
$ pytest -rA tests/all_tests.py > result_log/last_test_output.log
```
2.2 Go to directory with results report (/result_log/last_test_output.log) and open it in browser or text editor.