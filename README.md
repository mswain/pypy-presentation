* Setup Pyenv https://github.com/pyenv/pyenv
* Install PyPy
```
pyenv install pypy2-5.7.1
```
* Install Python 2.7.13
```
pyenv install 2.7.13
```  
* Run demo w/ cpython
```
pyenv shell 2.7.13
python fibonacci.py 32
32 fibonacci number is: 2178309 found in 2.07093s
```

* Run demo w/ pypy
```
pyenv shell pypy2-5.7.1
python fibonacci.py 32
32 fibonacci number is: 2178309 found in 0.117313s
```
