import logging
from usvisa.cloud_storage.aws_storage import SimpleStorageService
from usvisa.exception.exception import usvisaException
from usvisa.utils.model.estimator import USvisaModel
import sys
from pandas import DataFrame

# Set up logging
logging.basicConfig(level=logging.INFO)

class USvisaEstimator:
    """
    This class is used to save and retrieve us_visas model in s3 bucket and to do prediction
    """

    def __init__(self, bucket_name, model_path):
        """
        :param bucket_name: Name of your model bucket
        :param model_path: Location of your model in bucket
        """
        self.bucket_name = bucket_name
        self.s3 = SimpleStorageService()
        self.model_path = model_path
        self.loaded_model: USvisaModel = None
        logging.info(f"USvisaEstimator initialized with bucket: {self.bucket_name}, model path: {self.model_path}")

    def is_model_present(self, model_path):
        try:
            logging.info(f"Checking if model is present at path: {model_path}")
            return self.s3.s3_key_path_available(bucket_name=self.bucket_name, s3_key=model_path)
        except usvisaException as e:
            logging.error(f"Error checking if model is present: {e}")
            return False

    def load_model(self) -> USvisaModel:
        """
        Load the model from the model_path
        :return:
        """
        try:
            logging.info(f"Loading model from path: {self.model_path}")
            return self.s3.load_model(self.model_path, bucket_name=self.bucket_name)
        except Exception as e:
            logging.error(f"Error loading model from path: {self.model_path}, Error: {e}")
            raise usvisaException(e, sys)

    def save_model(self, from_file, remove: bool = False) -> None:
        """
        Save the model to the model_path
        :param from_file: Your local system model path
        :param remove: By default it is false that mean you will have your model locally available in your system folder
        :return:
        """
        try:
            logging.info(f"Saving model from {from_file} to S3 at path: {self.model_path}, remove local: {remove}")
            self.s3.upload_file(
                from_file,
                to_filename=self.model_path,
                bucket_name=self.bucket_name,
                remove=remove
            )
            logging.info(f"Model saved successfully to S3 at path: {self.model_path}")
        except Exception as e:
            logging.error(f"Error saving model: {e}")
            raise usvisaException(e, sys)

    def predict(self, dataframe: DataFrame):
        """
        :param dataframe:
        :return:
        """
        try:
            logging.info("Making prediction using the model.")
            if self.loaded_model is None:
                logging.info("Model is not loaded yet. Loading the model now.")
                self.loaded_model = self.load_model()
            predictions = self.loaded_model.predict(dataframe=dataframe)
            logging.info(f"Prediction completed. Number of predictions: {len(predictions)}")
            return predictions
        except Exception as e:
            logging.error(f"Error during prediction: {e}")
            raise usvisaException(e, sys)
