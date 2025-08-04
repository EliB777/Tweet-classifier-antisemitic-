from dataAnalyzer import DataAnalyzer
from clean_data import Clean_data
from load_data import Load_data




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





if __name__ == "__main__":
    controller = Controller()
    controller.run()
