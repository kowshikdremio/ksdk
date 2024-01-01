#################################################################################
# This module provides functions to interact with Dremio Sonar. Find below a    #
# list of functions and their definitions                                       #
# Module Name       Description                                                 #
# getPDS            Returns a Pandas DataFrame having a list of all PDS with    #
#                   complete path                                               #    
#                                                                               #
#                                                                               #
#                                                                               #
# Note:                                                                         #
#                                                                               #
################################################################################


import json
import requests


headers = {'content-type':'application/json'}
dremioWebUrl = 'http://ec2-3-84-218-11.compute-1.amazonaws.com:9047'
api_timeout = 60
verifySsl = False

def login(username, password,dremioWebURL):
  # we login using the old api for now
  loginData = {'userName': username, 'password': password}
  response = requests.post(dremioWebURL + "/apiv2/login", headers=headers, data=json.dumps(loginData), verify=False)
  data = json.loads(response.text)
  # retrieve the login token
  token = data['token']
  print('Successfully completed login function....')
  return {'content-type':'application/json', 'Authorization':'_dremio{authToken}'.format(authToken=token)}

#username = 'localadmin'
#password = 'Kolkata@1'

#auth_token = login(username,password,dremioWebUrl)
#print(auth_token)