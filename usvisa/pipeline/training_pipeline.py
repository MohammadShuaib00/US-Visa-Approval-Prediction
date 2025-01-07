import os
import sys
from usvisa.logger.logging import logging
from usvisa.exception.exception import usvisaException
from usvisa.entity.entity_config import DataIngestionConfig
from usvisa.entity.artifact_config import DataIngestionArtifact
from usvisa.components.data_ingestion import DataIngestion

class TrainingPipeline:
    def __init__(self):
        try:
            self.data_ingestion_config = DataIngestionConfig()
        except Exception as e:
            raise usvisaException(e,sys)
        
    def start_data_ingestion(self) ->DataIngestionArtifact:
        try:
            logging.info("Entered the start_data_ingestion method of TrainPipeline class")
            logging.info("Getting the data from mongodb")
            data_ingestion = DataIngestion(data_ingestion_config=self.data_ingestion_config)
            data_ingestion_artifact = data_ingestion.intiate_data_ingestion()
            logging.info("Got the train_set and test_set from mongodb")
            logging.info(
                "Exited the start_data_ingestion method of TrainPipeline class"
            )
            return data_ingestion_artifact
        except Exception as e:
            raise usvisaException(e,sys)
        
    def run_pipeline(self) ->None:
        try:
            data_ingestion_artifact = self.start_data_ingestion()
        except Exception as e:
            raise usvisaException(e,sys)