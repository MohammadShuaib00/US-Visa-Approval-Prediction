import os
import sys
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from usvisa.logger.logging import logging
from usvisa.data_access.usvisa_data import USDataImport
from usvisa.exception.exception import usvisaException
from usvisa.entity.entity_config import DataIngestionConfig
from usvisa.entity.artifact_config import DataIngestionArtifact


class DataIngestion:
    def __init__(self,data_ingestion_config:DataIngestionConfig=DataIngestionConfig()):
        try:
            self.data_ingestion_config = data_ingestion_config
        except Exception as e:
            raise usvisaException(e,sys)
        
    def export_data_into_feature_store(self) -> pd.DataFrame:
        try:
            logging.info("Exporting the data from mongodb database")
            usvisa_data = USDataImport()
            dataframe = usvisa_data.export_collection_as_dataframe(collection_name=self.data_ingestion_config.collection_name)
            logging.info(f"Shape of dataframe: {dataframe.shape}")
            feature_store_file_path = self.data_ingestion_config.feature_store_file_path
            dir_name = os.path.dirname(feature_store_file_path)
            os.makedirs(dir_name,exist_ok=True)
            logging.info(f"Saving exported data into feature store file path: {feature_store_file_path}")
            dataframe.to_csv(feature_store_file_path,index=False,header=True)
            return dataframe
        except Exception as e:
            raise usvisaException(e,sys)
        
    def split_data_as_train_test(self,dataframe:pd.DataFrame) ->None:
        try:
            logging.info("Entered split_data_as_train_test method of Data_Ingestion class")
            train_set,test_set = train_test_split(dataframe,test_size= self.data_ingestion_config.train_test_split_ratio)
            logging.info("Performed train test split on the dataframe")
            logging.info(
                "Exited split_data_as_train_test method of Data_Ingestion class"
            )
            
            data_ingested_dir_path = self.data_ingestion_config.training_file_path
            dir_path = os.path.dirname(data_ingested_dir_path)
            os.makedirs(dir_path,exist_ok=True)
            logging.info(f"Exporting train and test file path.")
            train_set.to_csv(self.data_ingestion_config.training_file_path,index=False,header=True)
            test_set.to_csv(self.data_ingestion_config.testing_file_path,index=False,header=True)
            logging.info(f"Exported train and test file path.")
        except Exception as e:
            raise usvisaException(e,sys)
        
    def intiate_data_ingestion(self) -> DataIngestionArtifact:
        logging.info("Entered initiate_data_ingestion method of Data_Ingestion class")

        try:
            dataframe = self.export_data_into_feature_store()
            logging.info("Got the data from mongodb")
            self.split_data_as_train_test(dataframe=dataframe)
            logging.info("Performed train test split on the dataset")

            logging.info(
                "Exited initiate_data_ingestion method of Data_Ingestion class"
            )
            
            data_ingestion_artifact = DataIngestionArtifact(
                trained_file_path=self.data_ingestion_config.training_file_path,
                test_file_path=self.data_ingestion_config.testing_file_path
               
            )
            logging.info(f"Data ingestion artifact: {data_ingestion_artifact}")
            return data_ingestion_artifact
        except Exception as e:
            raise usvisaException(e,sys)
        