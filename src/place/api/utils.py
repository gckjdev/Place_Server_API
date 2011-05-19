'''
Created on 2011-5-16

= author: James
'''
from place.api import ReturnConsts
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
