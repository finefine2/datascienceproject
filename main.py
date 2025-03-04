from src.datascience import logger
from src.datascience.pipeline.data_ingestion_pipeline import DataIngestionTrainingPipeline
from src.datascience.pipeline.data_validation_pipeline import DataValidationTrainingPipeline
from src.datascience.pipeline.data_transformation_pipeline import DataTransformationTrainingPipeline
from src.datascience.pipeline.model_trainer_pipeline import ModelTrainerTrainingPipeline
from src.datascience.pipeline.model_evaluation_pipeline import ModelEvaluationTrainingPipeline

# STAGE_NAME = "Data Ingestion stage" 
# try: 
#     logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
#     data_ingestion = DataIngestionTrainingPipeline() 
#     data_ingestion.initiate_data_ingesetion()
#     logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx=========x")
        
# except Exception as e: 
#     logger.exception(e) 
#     raise e 

logger.info("Welcome to our custom logging data science")


STAGE_NAME = "Data validation stage"
try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    data_validation = DataValidationTrainingPipeline() 
    data_validation.initiate_data_validation()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx=========x")
        
except Exception as e: 
    logger.exception(e) 
    raise e 


STAGE_NAME = "Data transformation stage"
try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    data_transformation = DataTransformationTrainingPipeline() 
    data_transformation.initiate_data_transformation()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx=========x")
        
except Exception as e: 
    logger.exception(e) 
    raise e


STAGE_NAME = "Model Trainer Stage" 
try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    model_trainer = ModelTrainerTrainingPipeline() 
    model_trainer.initiate_model_training()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx=========x")
        
except Exception as e: 
    logger.exception(e) 
    raise e


STAGE_NAME = "Model Evaluation Stage" 
try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    model_ev = ModelEvaluationTrainingPipeline() 
    model_ev.initiate_model_evaluation()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx=========x")
        
except Exception as e: 
    logger.exception(e) 
    raise e