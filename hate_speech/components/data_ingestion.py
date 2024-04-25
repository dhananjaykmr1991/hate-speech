import os
import sys
from zipfile import ZipFile
from hate_speech.logger import logging
from hate_speech.exception import CustomException
from hate_speech.configuration.gcloud_syncer import GCloudSync 
from hate_speech.entity.config_entity import DataIngestionConfig
from hate_speech.entity.artifact_entity import DataIngestionArtifacts

class DataIngestion:
    def __init__(self, data_ingestion_config : DataIngestionConfig):
        self.data_ingestion_config = data_ingestion_config
        self.gcloud = GCloudSync() 