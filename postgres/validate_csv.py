import os
from os import listdir
from os.path import isfile, join
import pandas as pd

def validate_csv() -> bool:
    my_dir = r'data/'
    directory_path = os.listdir(my_dir)
    
    for filename in directory_path:
        path = os.path.join(my_dir, filename)
        if filename.endswith('.csv') and os.path.getsize(path) > 330:    
            if "value" and "id" in pd.read_csv(path).columns:
                continue
        else:
            return False
    
    return True

        