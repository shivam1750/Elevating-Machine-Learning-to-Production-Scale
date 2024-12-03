import os
import sys

import numpy as np
import dill
import yaml
from pandas import DataFrame

from us_visa.exception import USvisaException
from us_visa.logger import logging

def read_yaml_file(file_path: str) -> dict:
    """
    Reads a YAML file and returns its contents as a dictionary.
    
    :param file_path: Path to the YAML file.
    :return: Contents of the YAML file as a dictionary.
    """
    try:
        with open(file_path, "rb") as yaml_file:
            return yaml.safe_load(yaml_file)
    except Exception as e:
        raise USvisaException(e, sys) from e

def write_yaml_file(file_path: str, content: object, replace: bool = False) -> None:
    """
    Writes the given content to a YAML file. If 'replace' is True, it replaces the existing file.
    
    :param file_path: Path to the YAML file.
    :param content: Content to be written to the file.
    :param replace: Whether to replace the existing file.
    """
    try:
        if replace and os.path.exists(file_path):
            os.remove(file_path)
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        with open(file_path, "w") as file:
            yaml.dump(content, file)
    except Exception as e:
        raise USvisaException(e, sys) from e

def load_object(file_path: str) -> object:
    """
    Loads a serialized object from a file using dill.
    
    :param file_path: Path to the file containing the serialized object.
    :return: The deserialized object.
    """
    logging.info("Entered the load_object method of utils")
    try:
        with open(file_path, "rb") as file_obj:
            obj = dill.load(file_obj)
        logging.info("Exited the load_object method of utils")
        return obj
    except Exception as e:
        raise USvisaException(e, sys) from e

def save_numpy_array_data(file_path: str, array: np.array) -> None:
    """
    Saves a numpy array to a file.
    
    :param file_path: Path to the file where the array will be saved.
    :param array: Numpy array to save.
    """
    try:
        dir_path = os.path.dirname(file_path)
        os.makedirs(dir_path, exist_ok=True)
        with open(file_path, 'wb') as file_obj:
            np.save(file_obj, array)
    except Exception as e:
        raise USvisaException(e, sys) from e

def load_numpy_array_data(file_path: str) -> np.array:
    """
    Loads a numpy array from a file.
    
    :param file_path: Path to the file from which the array will be loaded.
    :return: The loaded numpy array.
    """
    try:
        with open(file_path, 'rb') as file_obj:
            return np.load(file_obj)
    except Exception as e:
        raise USvisaException(e, sys) from e

def save_object(file_path: str, obj: object) -> None:
    """
    Saves an object to a file using dill.
    
    :param file_path: Path to the file where the object will be saved.
    :param obj: Object to save.
    """
    logging.info("Entered the save_object method of utils")
    try:
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        with open(file_path, "wb") as file_obj:
            dill.dump(obj, file_obj)
        logging.info("Exited the save_object method of utils")
    except Exception as e:
        raise USvisaException(e, sys) from e

def drop_columns(df: DataFrame, cols: list) -> DataFrame:
    """
    Drops specified columns from a pandas DataFrame.
    
    :param df: Pandas DataFrame from which columns will be dropped.
    :param cols: List of columns to drop.
    :return: DataFrame with the specified columns dropped.
    """
    logging.info("Entered drop_columns method of utils")
    try:
        df = df.drop(columns=cols, axis=1)
        logging.info("Exited the drop_columns method of utils")
        return df
    except Exception as e:
        raise USvisaException(e, sys) from e
