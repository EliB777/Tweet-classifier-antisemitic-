import pandas as pd

class Load_data:
    def load_csv(self, file_path):
        data = pd.read_csv(file_path)
        data = pd.read_csv(self.file_path).astype(str)
        return data



