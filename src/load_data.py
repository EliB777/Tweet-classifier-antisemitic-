import pandas as pd

class load_data:
    def load_csv(self, file_path):
        data = pd.read_csv(file_path)
        return data



