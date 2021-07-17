import base64
import os
from pathlib import Path

from cv2 import cv2
from flask import request, jsonify

import re
import datetime
import sys


#import mlapp.services.cust_records as custrec
#import mlapp.services.external_api_call as apicall
import mlapp.services.extract_information as extinfo
#import mlapp.services.img_pro_opencv as imgpropc
import mlapp.services.logs as logger
#import mlapp.services.nid_processing as nidproc

from mlapp import app

from PIL import Image, ImageEnhance
from PIL import Image

root_path = app.config.get("DIR_STATIC")

"""
developed by: Anika Nahar
"""
logger.error_logs("============START============")
@app.route('/test', methods=['GET'])
def test_anika():
    logger.error_logs("================test_anika")

    ext_info = extinfo.ExtractInfo()
    #result1 = ext_info.test()
    #testdata = 'আগামী ২ বছরের মধ্যে দেশের মোট জনসংখ্যাকে ছাড়িয়ে যাবে ফুড ব্লগারের সংখ্যা'
    result1 = ext_info.test()
    logger.error_logs(result1)
    return jsonify(status="OK", message="Successfully test", result=result1)


@app.route('/sampletrueset', methods=['GET'])
def SampleTrueSet():
    logger.error_logs("================SampleTrueSet")
    try:
        ext_info = extinfo.ExtractInfo()
        result1 = ext_info.SampleTrueSet()
        logger.error_logs(result1)
        if(result1 != None):
            
            return jsonify(status="OK", message="Successfully Got 1st 5 data", result=result1)
        else:
            return jsonify(status="FAILED", message="Failed to Get", result='N/A')
    except Exception as e:
        return jsonify(status="FAILED", message=str(e), result='N/A')

@app.route('/samplefakeset', methods=['GET'])
def SampleFakeSet():
    logger.error_logs("================SampleFakeSet")
    try:
        ext_info = extinfo.ExtractInfo()
        result1 = ext_info.SampleFakeSet()
        logger.error_logs(result1)
        if(result1 != None):
            return jsonify(status="OK", message="Successfully Got 1st 5 data", result=result1)
        else:
            return jsonify(status="FAILED", message="Failed to Get", result='N/A')
    except Exception as e:
        return jsonify(status="FAILED", message=str(e), result='N/A')

@app.route('/domainlist', methods=['GET'])
def totalUniqueDomains():
    logger.error_logs("================domainlist")
    try:
        ext_info = extinfo.ExtractInfo()
        result1 = ext_info.totalUniqueDomains()
        logger.error_logs(result1)
        if(result1 != None):
            return jsonify(status="OK", message="Successfully Got ", result=result1)
        else:
            return jsonify(status="FAILED", message="Failed to Get", result='N/A')
    except Exception as e:
        return jsonify(status="FAILED", message=str(e), result='N/A')

@app.route('/categorylist', methods=['GET'])
def totalUniqueCategory():
    logger.error_logs("================categorylist")
    try:
        ext_info = extinfo.ExtractInfo()
        result1 = ext_info.totalUniqueCategory()
        logger.error_logs(result1)
        if(result1 != None):
            return jsonify(status="OK", message="Successfully Got ", result=result1)
        else:
            return jsonify(status="FAILED", message="Failed to Get", result='N/A')
    except Exception as e:
        return jsonify(status="FAILED", message=str(e), result='N/A')

@app.route('/modelaccuracy', methods=['GET'])
def modelAccuracy():
    logger.error_logs("================modelaccuracy")
    try:
        ext_info = extinfo.ExtractInfo()
        result1 = ext_info.modelAccuracy()
        logger.error_logs(result1)
        if(result1 != None):
            return jsonify(status="OK", message="Successfully Got ", result=result1)
        else:
            return jsonify(status="FAILED", message="Failed to Get", result='N/A')
    except Exception as e:
        return jsonify(status="FAILED", message=str(e), result='N/A')

@app.route('/detectfakenews', methods=['POST'])
def detectFakeNews():
    logger.error_logs("================detectFakeNews")
    content = request.get_json()
    testdata = content['news']
    try:
        unicodetestdata = (testdata.encode(encoding='utf8'))
        logger.error_logs(unicodetestdata)
        
        ext_info = extinfo.ExtractInfo()
        
        result1 = ext_info.testSentence(testdata)
        logger.error_logs(result1)
        
        if(result1 != None):
            return jsonify(status="OK", message="Successfully Predicted", result=result1)
        else:
            return jsonify(status="FAILED", message="Failed to Predict", result='N/A')

    except Exception as e:
        return jsonify(status="FAILED", message=str(e), result='N/A')

@app.route('/detectfakenewsepoch', methods=['POST'])
def detectFakeNewsCustomEpoch():
    logger.error_logs("================detectfakenewsepoch")
    content = request.get_json()
    testdata = content['news']
    epoch = content['epoch']
    try:
        unicodetestdata = (testdata.encode(encoding='utf8'))
        logger.error_logs(unicodetestdata)
        
        ext_info = extinfo.ExtractInfo()
        
        result1 = ext_info.testSentence_customepoch(testdata, epoch)
        logger.error_logs(result1)
        
        if(result1 != None):
            return jsonify(status="OK", message="Successfully Predicted", result=result1)
        else:
            return jsonify(status="FAILED", message="Failed to Predict", result='N/A')

    except Exception as e:
        return jsonify(status="FAILED", message=str(e), result='N/A')



    logger.error_logs("/getblobphotos/"+cust_mob_no)
    try:
        ext_info = extinfo.ExtractInfo()
        blob_photos = ext_info.getBlobPhotos(cust_mob_no)
        if blob_photos is not None:
            return jsonify(status="OK", message="Successfully get blob photos", result=blob_photos)
        return jsonify(status="FAILED", message="Failed to get blob photos. Please, try again.", result=None)
    except Exception as e:
        return jsonify(status="FAILED", message="Failed to get blob photos. Please, try again.", result=None)