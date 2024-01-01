import dremiosonar as dremio
import pandas as pd
import csv


# Get the connection object
dremioserver = 'ec2-3-84-218-11.compute-1.amazonaws.com'
flightport   = '32010'
username     = 'localadmin'
pat          = '6nnlXLCBSWy593ceX/4F4+w0geFTmkfnPtlndLAphTu/MAyPRlFI2Ku7GZrODg=='
flightjarpath = '/Users/kowshikdutta/mycode/flight/jar/flight-sql-jdbc-driver-10.0.0.jar'
dremioUrl = 'http://'+dremioserver + ':9047'
print(dremioUrl)

#cnxn = dremio.getConnection(dremioserver,flightport,username,pat,flightjarpath)

#all_pds_df = dremio.getPDS(cnxn)
#dremio.closeConnection(cnxn)

#all_pds_df.to_csv("all_pds.csv",index=False,quoting=csv.QUOTE_NONE)

auth_token = dremio.login(username,pat,dremioUrl)
print(auth_token)

exit(0)