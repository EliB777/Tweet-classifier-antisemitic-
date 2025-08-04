import pandas as pd

class DataAnalyzer:

    def __init__(self, data):
        self.data = data
        self.text_column = 'Text'
        self.biased_column = 'Biased'
        # self.data = data['Text']
        # self.data = data['Biased']



    def count_teets_by_category(self):

        biased_counts = self.data[self.biased_column].value_counts()

        antisemitic = biased_counts.get(1, 0)
        non_antisemitic = biased_counts.get(0, 0)

        total_teets = len(self.data)
        no_category = total_teets - antisemitic - non_antisemitic

        result = {
            "antisemitic": antisemitic,
            "non_antisemitic": non_antisemitic,
            "total": total_teets,
            "no_category": no_category
        }

        return result




    def avg_len_by_category(self):

        self.data['word_count'] = self.data[self.text_column].apply(lambda x: len(x.split()))

        avg_by_category = self.data.groupby(self.biased_column)['word_count'].mean()

        avg_antisemitic = avg_by_category.get(1, 0)
        avg_non_antisemitic = avg_by_category.get(0, 0)

        avg = self.data['word_count'].mean()

        return {
            "antisemitic": avg_antisemitic,
            "non_antisemitic": avg_non_antisemitic,
            "total": avg
        }





    def top_3_long_tweets(self):

        self.data['count_char'] = self.data[self.text_column].apply(lambda x: len(x))

        antisemitic = self.data[self.data[self.biased_column] == 1].nlargest(3, 'count_char')[self.text_column].tolist()
        non_antisemitic = self.data[self.data[self.biased_column] == 0].nlargest(3, 'count_char')[
            self.text_column].tolist()

        return {
            "antisemitic": antisemitic,
            "non_antisemitic": non_antisemitic
        }



    def top_10_words_common(self):

        all_text = ' '.join(self.data[self.text_column])

        words = pd.Series(all_text.split())
        top_words_common = words.value_counts().head(10)

        return top_words_common.to_dict()



##################################################################################################################

    def sum_of_words_in_uppercase_letter(self):

        counts_uppercase = []

        for text in self.data[self.text_column]:
            if not isinstance(text, str):
                counts_uppercase.append(0)
            else:
                count = 0
                for word in text.split():
                    if word.isupper():
                        count += 1
                counts_uppercase.append(count)

        self.data['counts_uppercase'] = counts_uppercase

        groupby = self.data.groupby(self.biased_column)['counts_uppercase'].sum()
        antisemitic = groupby.get(1, 0)
        non_antisemitic = groupby.get(0, 0)
        total = self.data['counts_uppercase'].sum()

        return {
            "antisemitic": antisemitic,
            "non_antisemitic": non_antisemitic,
            "total": total
        }

    def summary_analiza(self):
        return {
            "total_tweets": self.count_teets_by_category(),
            "average_length": self.avg_len_by_category(),
            "longest_3_tweets": self.top_3_long_tweets(),
            "common_words": {
                "total": list(self.top_10_words_common().keys())
            },
            "uppercase_words": self.sum_of_words_in_uppercase_letter()
        }










