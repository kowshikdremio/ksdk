import dremiosonar as dremio
import pandas as pd
import csv


# Get the connection object
dremioserver = 'ec2-3-84-218-11.compute-1.amazonaws.com'
flightport   = '32010'
username     = '<User ID>'
pat          = '<PAT TAKOEN>'
dremioUrl = 'http://'+dremioserver + ':9047'
print(dremioUrl)

auth_token = dremio.login(username,pat,dremioUrl)
print(auth_token)

exit(0)