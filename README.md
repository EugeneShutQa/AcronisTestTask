# AcronisFrameworkTestTask

# HOW TO RUN:
- Python 3.9
- Run:
```Pip install -r requirements.txt```
- Mark main directory as Root and run tests via ```Pytest``` command

# Bugs:
  - Sometimes DELETE method for pet deleting and POST method for pet update won’t return anything. Probably that is the server issue or API bug.
  - Sometimes Get requests return an error

# Framework folders:
- Common – folder for utils working with filesystem (configs load)
- Logger – logger included in all base modules to log every request or response, also it takes param ENGINE from config to mark log filenames.
- Utils – folder for additional functions like data generators.
- API – Place for base API methods.
- Tests – Forder for TestSuites.
- Resources – Place, where configs and datafiles are stored
- PageObjects:
-models – directory for any in requests folder 
-requests – directory for high-level methods which use test

