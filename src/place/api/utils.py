'''
Created on 2011-5-16

= author: James
'''



class Constants(object):
    METHOD = "m"
    METHOD_TEST = "test"
    METHOD_ONLINESTATUS = "srpt"
    METHOD_REGISTRATION = "reg"
    METHOD_CREATEPOST = "cp"
    METHOD_CREATEPLACE = "cpl"
    
    # request parameters
    
    PARA_USERID = "uid"
    PARA_LOGINID = "lid"
    PARA_LOGINIDTYPE = "lty"
    PARA_USERTYPE = "uty"
    PARA_PASSWORD = "pwd"
    
    PARA_DEVICEID = "did"
    PARA_DEVICETYPE = "dty"
    PARA_DEVICEMODEL = "dm"
    PARA_DEVICEOS = "dos"
    PARA_DEVICETOKEN = "dto"
    
    PARA_COUNTRYCODE = "cc"
    PARA_LANGUAGE = "lang"
    PARA_APPID = "app"
    
    PARA_RADIUS = "ra"
    PARA_POSTTYPE = "pt"
    PARA_NAME = "na"
    PARA_DESC = "de"
    
    PARA_CONTENT_TYPE = "ct"
    PARA_TEXT_CONTENT = "t"
    PARA_USER_LATITUDE = "ula"
    PARA_USER_LONGITUDE = "ulo"
    PARA_SYNC_SNS = "ss"
    PARA_PLACEID = "pid" 
    
    PARA_STATUS = "s"
    
    PARA_TIMESTAMP = "ts"
    PARA_MAC = "mac"
    
    PARA_DATA = "dat"
    
    PARA_LONGTITUDE = "lo"
    PARA_LATITUDE = "lat"
    PARA_MESSAGETEXT = "t"
    
    # response parameters
    
    RET_MESSAGE = "msg"
    RET_CODE = "ret"
    RET_DATA = "dat"


