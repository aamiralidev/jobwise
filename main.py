from tasks.extractors.GreenHouseJobExtractor import GreenHouseJobExtractor
from tasks.extractors.LeverJobExtractor import LeverJobExtractor



if __name__ == "__main__":
    # extractor = GreenHouseJobExtractor('invisibletech')
    extractor = LeverJobExtractor('formstack')
    extractor.extract()