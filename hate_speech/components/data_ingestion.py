import os
import sys
from zipfile import ZipFile
from hate_speech.logger import logging
from hate_speech.exception import CustomException
from hate_speech.configuration import gcloud_syncer
from hate_speech.entity.config_entity import DataIngestionConfig

