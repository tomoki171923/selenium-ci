# selenium-ci

## Application Architecture

```
root
 └ log  //log and screenshot files are located in this folder.
 └ mockdata  //mockdata files to test are located in this folder.
 └ src
    └ common  //common function code are located in this folder.
    └ scenario  //unittest code are located in this folder.
 └ case1_xxxx.py  //your test code
 └ case2_yyyy.py  //your test code
 └ case3_zzzz.py  //your test code
```

## Dependent Packages

```
brew cask install chromedriver
conda install selenium
conda install pillow
conda install termcolor
conda install pyyaml
```

## How to use

### 1. prepare test data

you need to prepare your test data in mockdata folder.
(reference. mockdata/case1_sample.yml)

### 2. code unittest

you need to code your unit test code in the root.
you can use functions of src/common/selenium.py
(reference. case1_sample.py)

### 3. execute Selinium Test

execute the following commond.
```
python3 ./case1_sample.py -v
```

### 4. check your log

check your test log in log folder.

the following is sample.
log/seleniumci_20200925_054618_case1_sample/case1_sample.log
```
******************* SELENIUM TEST START : 20200925_054618 *******************

test_case01 (__main__.case1_sample) ... ok
test_case02 (__main__.case1_sample) ... ok
test_case03 (__main__.case1_sample) ... ok
test_case04 (__main__.case1_sample) ... ok
test_case05 (__main__.case1_sample) ... ok
test_case06 (__main__.case1_sample) ... ok
test_case07 (__main__.case1_sample) ... ok
test_case08 (__main__.case1_sample) ... ok
test_case09 (__main__.case1_sample) ... ok
test_case10 (__main__.case1_sample) ... ok
test_case11 (__main__.case1_sample) ... ok
test_case12 (__main__.case1_sample) ... ok
test_case13 (__main__.case1_sample) ... ok
test_case14 (__main__.case1_sample) ... ok
test_case15 (__main__.case1_sample) ... ok
test_case16 (__main__.case1_sample) ... ok
test_case17 (__main__.case1_sample) ... ok
test_case18 (__main__.case1_sample) ... ok
test_case19 (__main__.case1_sample) ... ok
test_case20 (__main__.case1_sample) ... ok
test_case21 (__main__.case1_sample) ... ok
test_case22 (__main__.case1_sample) ... ok
test_case23 (__main__.case1_sample) ... ok
test_case24 (__main__.case1_sample) ... ok
test_case25 (__main__.case1_sample) ... ok
test_case26 (__main__.case1_sample) ... ok
test_case27 (__main__.case1_sample) ... ok
test_case28 (__main__.case1_sample) ... ok
test_case29 (__main__.case1_sample) ... ok
test_case30 (__main__.case1_sample) ... ok
test_case31 (__main__.case1_sample) ... ok

----------------------------------------------------------------------
Ran 31 tests in 471.687s

OK
```