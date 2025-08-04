from dataAnalyzer import DataAnalyzer
from clean_data import Clean_data
from load_data import Load_data
# from writing_data import DataWriter
import pandas as pd


class Controller:

    def run(self):

        loader = Load_data("data/tweets_dataset.csv")
        data = loader.load_data()
        if data is None:
            print("error with loading")
            return

        cleaner = Clean_data(data)
        cleaner.basic_clean()

        analyzer = DataAnalyzer(data)
        results = analyzer.summary_analiza()
        # writer = DataWriter()
        # writer.cleaned_data_to_csv(cleaner.data, "results/tweets_dataset_cleaned.csv")
        # writer.analysis_results_to_json(results, "results/results.json")

        print("Pipeline completed successfully!")


if __name__ == "__main__":
    controller = Controller()
    controller.run()
