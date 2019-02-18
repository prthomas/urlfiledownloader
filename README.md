# urlfiledownloader

[![Build Status](https://travis-ci.org/prthomas/urlfiledownloader.svg?branch=master)](https://travis-ci.org/prthomas/urlfiledownloader)

## Setting up for unit-test with python
1. Create virtualenv  
    `python -m venv <env-name>`
1. Activate virtualenv  
    `source <env-name>/bin/activate`
1. Install python modules `pytest`, and other modules (`requests` is as needed in this use case)  
     `pip install -r requirements.txt`  
     or  
     `pip install requests`   
     `pip install pytest`
1. Implement test and code
1. Run tests or run individual test  
   `pytest`  
   or     
   `pytest <test-file-name>`
1. Deactivate virtualenv  
   `deactivate`

## Resources
1. Setup vim as a python [IDE](https://realpython.com/vim-and-python-a-match-made-in-heaven/)
1. Python venv [documentation](https://docs.python.org/3/library/venv.html#module-venv), and [primer](https://realpython.com/python-virtual-environments-a-primer/)
1. [pytest](https://docs.pytest.org/en/latest/) module
1. [unittest](https://docs.python.org/3/library/unittest.html) module
