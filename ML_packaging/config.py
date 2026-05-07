class Config:

    # -------------------------
    # General Settings
    # -------------------------
    DEBUG = True
    LOG_LEVEL = "INFO"

    # -------------------------
    # Paths
    # -------------------------
    DATASET_PATH = "GCL.csv"
    MODEL_PATH = "knn_pipeline_model.pkl"

    # -------------------------
    # Data Parameters
    # -------------------------
    TEST_SIZE = 0.2
    RANDOM_STATE = 42
    STRATIFY = True   # important for classification

    # -------------------------
    # Feature Configuration
    # -------------------------
    N_FEATURES = 27
    LABEL_COLUMN_INDEX = 27

    # -------------------------
    # KNN Model Parameters
    # -------------------------
    N_NEIGHBORS = 5
    WEIGHTS = "uniform"   # or "distance"
    METRIC = "minkowski" # default distance metric
    P = 2                # Euclidean distance

    # -------------------------
    # Preprocessing
    # -------------------------
    USE_SCALER = True   # because KNN needs scaling

    # -------------------------
    # Utility Method
    # -------------------------
    @staticmethod
    def get_config():
        return {
            "debug": Config.DEBUG,
            "log_level": Config.LOG_LEVEL,
            "dataset_path": Config.DATASET_PATH,
            "model_path": Config.MODEL_PATH,
            "test_size": Config.TEST_SIZE,
            "random_state": Config.RANDOM_STATE,
            "stratify": Config.STRATIFY,
            "n_features": Config.N_FEATURES,
            "label_column_index": Config.LABEL_COLUMN_INDEX,
            "n_neighbors": Config.N_NEIGHBORS,
            "weights": Config.WEIGHTS,
            "metric": Config.METRIC,
            "p": Config.P,
            "use_scaler": Config.USE_SCALER
        }