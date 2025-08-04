import pandas as pd

class DataAnalyzer:

    def count_teets_by_category(self, data):
        return data['Biased'].value_counts()

    def avg_len_by_category(self, data):
        data["average_length"] = data["Text"].apply(lambda x: len(str(x).split()))
        return

    def top_3_long_tweets(self, data):




    def top_10_words_common(self, data):\
        return

    def sum_of_words_in_uppercase_letter(self, data):
        return