import os
import logging as log

log.basicConfig(level=log.INFO) # Set the threshold to INFO

def double(input1: int) -> int:
    """
    It doubles a number
    
    :param input1: Description
    :type input1: int
    :return: Description
    :rtype: int
    """
    return input1*input1

if __name__ == "__main__":
    current_folder = os.listdir()
    #result = double(13)
    log.info(f"Current folder: {current_folder}")
