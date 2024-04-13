from hate_speech.logger import logging
from hate_speech.exception import CustomException
import sys
from hate_speech.configuration.gcloud_syncer import GCloudSync

obj = GCloudSync()
obj.sync_folder_from_gcloud("heat_speech0512","dataset.zip","download/dataset.zip")