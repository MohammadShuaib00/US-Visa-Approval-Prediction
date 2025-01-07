import os
import sys
from usvisa.logger.logging import logging
from usvisa.exception.exception import usvisaException
from usvisa.pipeline.training_pipeline import TrainingPipeline


start = TrainingPipeline()
start.run_pipeline()