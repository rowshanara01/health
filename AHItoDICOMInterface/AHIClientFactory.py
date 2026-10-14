"""
AHItoDICOM Module : This class contains the logic to create the AHI boto3 client.

SPDX-License-Identifier: Apache-2.0
"""
import boto3
import botocore
import tempfile
import logging
import os



class AHIClientFactory(object):


    def __init__(self) -> None:
        pass

    def __new__(self , aws_access_key : str = None , aws_secret_key : str = None , aws_session_token : str = None , aws_accendpoint_url : str = None):
        try:
            session = boto3.Session()
            # session._loader.search_paths.extend([tempfile.gettempdir()])
            aws_region = os.environ.get("DEFAULT_REGION")
            aws_access_key = os.environ.get("ACCESS_KEY_ID")
            aws_secret_key = os.environ.get("SECRET_ACCESS_KEY")
            aws_session_token = os.environ.get("SESSION_TOKEN")
            print(f"Aws region in AHIClientFactory : {aws_region}, access_key : {aws_access_key} , secret_key : {aws_secret_key} , session_token : {aws_session_token} , aws_region : {aws_region}")

            AHIclient = boto3.client('medical-imaging',  aws_access_key_id = aws_access_key , aws_secret_access_key = aws_secret_key , aws_session_token=aws_session_token , region_name=aws_region , endpoint_url=aws_accendpoint_url , config=botocore.config.Config(max_pool_connections=200)  ) 
            return AHIclient
        except Exception as AHIErr:
            logging.error(f"[AHIClientFactory] - {AHIErr}")
            return None 
