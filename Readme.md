# QA Technical Task for Richemot

## Exercise 1B

### Implementation details
The test cases are implemented using Robot Framework with Selenium. They can
be run using docker or directly by console.

The tests have been implemented using page objects for each web page of the
site and a service file where the keywords for the tests are implemented, that
are in the `resources`folder. The test cases are in `tests`folder on
file `tests.robot`.

### Run the test locally
In practice, it is easiest to install Robot Framework and SeleniumLibrary along 
with its dependencies using pip package manager. Once you have pip installed,
all you need to do is running this command:

`$ pip install -r requirements.txt`

To execute the test:

`$ python -m robot tests/tests.robot`
or
`$ robot tests`

In order to do this you should also need to have chromedriver installed on
the machine. (https://chromedriver.chromium.org/)



### Run the test using Docker

To build the docker image for testing:

`$ docker compose build`

To execute the tests:

`$ docker compose up --abort-on-container-exit`

### Read results
Once tests are executed for the first time a report, log and output files are created
,on project folder in case of running locally or in and `output` folder if using docker. 

The report (`output/report.html`) just have information about the test execution 
results.

The log (`output/log.html`) contains a detailed log of each step of the test
with the status of each one and screenshots of the last step or if something fails.

## Exercise 2
See Test Plan [here](TestPlan.md)