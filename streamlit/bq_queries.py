import pandas_gbq
import pandas as pd
import streamlit as st
from google.oauth2 import service_account

credentials = service_account.Credentials.from_service_account_info(
    {
        "type": st.secrets.type,
        "project_id": st.secrets.project_id,
        "private_key_id": st.secrets.private_key_id,
        "private_key": st.secrets.private_key,
        "client_email": st.secrets.client_email,
        "client_id": st.secrets.client_id,
        "auth_uri": st.secrets.auth_uri,
        "token_uri": st.secrets.token_uri,
        "auth_provider_x509_cert_url": st.secrets.auth_provider_x509_cert_url,
        "client_x509_cert_url": st.secrets.client_x509_cert_url
    },
)

def getFireData():
    query = """
    SELECT * 
    FROM `cloud-714.mack_fire.fire_speed`
    WHERE Date = (SELECT MAX(Date) FROM `cloud-714.mack_fire.fire_speed`)
    """
    data = pandas_gbq.read_gbq(query, credentials = credentials)
    return data

def getCountFires():
    query = """
    SELECT COUNT(*) AS count
    FROM `cloud-714.mack_fire.fire_speed`
    WHERE Date = (SELECT MAX(Date) FROM `cloud-714.mack_fire.fire_speed`)
    """
    return pandas_gbq.read_gbq(query, credentials = credentials)["count"][0]



