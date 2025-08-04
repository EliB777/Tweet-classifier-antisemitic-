import pandas as pd

class Clean_data:

    def __init__(self, data):
        self.text_column = 'Text'
        self.biased_column = 'Biased'
        self.data = data[['Text', 'Biased']].copy()
        # self.data = data['Text']
        # self.data = data['Biased']

    def remove_missing_labels(self):
        self.data = self.data.dropna(subset=[self.biased_column])

    def remove_symbols(self):
        symbols = "[!\"$%&()*+-./:;<=>?@[\]^_`{|}~\n]"
        self.data[self.text_column] = self.data[self.text_column].str.replace(symbols, "", regex=True)


    def converting_to_lowercas(self):
        self.data[self.text_column] = self.data[self.text_column].str.lower()

    def basic_clean(self):
        self.remove_missing_labels()
        self.remove_symbols()
        self.converting_to_lowercas()


