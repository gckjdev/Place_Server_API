'''
Created on 2011-5-16

= author: James
'''
import datetime

def date2str(datetime):
    datestring = datetime.strftime('%Y%m%d%H%M%S')
    return datestring;

def str2stddate(isostr):
    return date2str(datetime.datetime.strptime(isostr, '%Y-%m-%d %H:%M:%S.%f'))

def get_return_dict(return_code, data=None, message=None):
    return_dict = {ReturnConsts.CODE: return_code}
    if data:
        return_dict[ReturnConsts.DATA] = data
    if message:
        return_dict[ReturnConsts.MESSAGE] = message
    return return_dict

class MethodConsts():
    METHOD = "m"
    TEST = "test"
    ONLINESTATUS = "srpt"
    REGISTRATION = "reg"
    CREATEPOST = "cp"
    CREATEPLACE = "cpl"
    GETUSERPLACES = "gup"
    GETPLACEPOST = "gpp"

class ParamConsts():
    USERID = "uid"
    LOGINID = "lid"
    LOGINIDTYPE = "lty"
    USERTYPE = "uty"
    PASSWORD = "pwd"
    
    DEVICEID = "did"
    DEVICETYPE = "dty"
    DEVICEMODEL = "dm"
    DEVICEOS = "dos"
    DEVICETOKEN = "dto"
    NICKNAME = "nn"
    
    COUNTRYCODE = "cc"
    LANGUAGE = "lang"
    APPID = "app"
    
    RADIUS = "ra"
    POSTTYPE = "pt"
    NAME = "na"
    DESC = "de"
    AFTER_TIMESTAMP = "at"
    MAX_COUNT = "mc"
    
    TOTAL_VIEW = "tv"
    TOTAL_FORWARD = "tf"
    TOTAL_QUOTE = "tq"
    TOTAL_REPLY = "tr"
    CREATE_DATE = "cd"
    
    POSTID = "pi"
    IMAGE_URL = "iu"
    CONTENT_TYPE = "ct"
    TEXT_CONTENT = "t"
    USER_LATITUDE = "ula"
    USER_LONGITUDE = "ulo"
    SYNC_SNS = "ss"
    PLACEID = "pid" 
    
    CREATE_USERID = "cuid"
    
    STATUS = "s"
    
    TIMESTAMP = "ts"
    MAC = "mac"
    
    DATA = "dat"
    
    LONGTITUDE = "lo"
    LATITUDE = "lat"
    MESSAGETEXT = "t"
    
    VERSION = "v"

class ReturnConsts():
    MESSAGE = "msg"
    CODE = "ret"
    DATA = "dat"
    SUCCESS = 0
