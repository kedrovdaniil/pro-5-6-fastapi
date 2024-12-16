import os

MODELS_DIR = os.getenv("MODELS_DIR", "models")
CPU_CORES = int(os.getenv("CPU_CORES", 2))
MAX_INFERENCE_MODELS = int(os.getenv("MAX_INFERENCE_MODELS", 2))