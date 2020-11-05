# EC601_project4
Jiaming Yu     
U72316560  
jiamingy@bu.edu  

## phase1
Unit Test for project 2: https://github.com/JimY233/EC601_project2  
Please read project4_phase1.pdf for details  

**Use Github Secrets to separate Twitter API keys from the code**  
Please go to Secrets under Settings and new secret  
json file for Google Cloud Language API can be saved with base64 encoded here.  

**Use os.getenv() to set keys for Twitter API in TwitterAPI.py**  

**Use pytest to do the unit test**  
The code is in test_case.py   
we can combine with Github Actions to find the errors in all the project2 code. And then by adding the unit test functions using pytest, we can test our code.  
Althought I have not solve the problem of separating key for Google Cloud Language API, I still add some unit test for NLPAPI.py with #  

**Use Github Actions**   
New a workflow and change the .yml file: added the keys for Twitter API as environment variables  
.yml file is under .github/workflows/python-app.yml  
Google Cloud Language API reference: https://github.com/actions-hub/gcloud but not working so far  
The process can be seen in the Actions. We updated the test_case.py and the code according to the result of Github Actions  
We can change our code due to the error found there.  
Finally it works successfyl with no error now.  

**UPDATED**
Successfully separate Google Cloud Language API from the script with others' help and thus run unit test for NLPAPI.py in test_case.py (reomove #)
