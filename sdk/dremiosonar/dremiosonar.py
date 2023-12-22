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


import jaydebeapi
import pandas as pd


sql_allpds = "SELECT table_name AS PDSNAME, CONCAT(CONCAT('\"',\"CONTEXT\"),'\"') AS PDSPATH FROM (select table_name,source_name, REPLACE(DPATH,', ','\".\"') AS CONTEXT FROM (select \"tables\".table_name, ltrim(split_part(\"path\",',',1),'[') as source_name,SPLIT_PART(SPLIT_PART(\"tables\".path, '[', 2),']',1) AS DPATH from sys.\"tables\" where type = 'PHYSICAL_DATASET') TABLE_1) TABLE_2"


def getConnection(dremioServer,flightPort,username,password,flightjarpath):
    flightUrl = "jdbc:arrow-flight-sql://" + dremioServer + ":" + flightPort+ "/?useEncryption=false"
    cnxn = jaydebeapi.connect("org.apache.arrow.driver.jdbc.ArrowFlightJdbcDriver", flightUrl, [username, password], flightjarpath)
    return cnxn


def closeConnection(cnxn):
    cnxn.close()

def getPDS(cnxn):
    cursor = cnxn.cursor()
    cursor.execute(sql_allpds)
    result = cursor.fetchall()
    df = pd.DataFrame(result, columns=['PDSNAME','PDSPATH'])
    cursor.close()
    return df