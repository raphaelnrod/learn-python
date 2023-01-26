import random
import utils

FILE_PATH = "objects/forca/words/palavras.txt"


class Word:

    def __init__(self):
        self.__tip = self.__generate_tip().upper()
        self.__secret_word = self.__generate_word(self.__tip).upper()
        self.__progress = self.__generate_progress()

    @property
    def tip(self):
        return self.__tip

    @property
    def secret_word(self):
        return self.__secret_word

    @property
    def progress(self):
        return self.__progress

    @secret_word.setter
    def secret_word(self, value):
        self.__secret_word = value

    def update_progress(self, letter, index):
        self.__progress = utils.replacer(self.__progress, letter, index)

    def is_progress_done(self):
        return "_" not in self.__progress

    def __generate_progress(self):
        if self.__is_compound_word():
            progress = ''
            compost = self.__secret_word.split()
            idx = len(compost)
            for i in range(idx):
                progress += ''.ljust(len(compost[i])).replace(' ', '_')
                if i != idx:
                    progress += " "

            return progress
        else:
            return ''.ljust(len(self.__secret_word)).replace(' ', '_')

    def __is_compound_word(self):
        return len(self.__secret_word.split()) > 1

    def __generate_tip(self):
        return self.__shuffle_words(self.__open_file(FILE_PATH))[0]

    def __generate_word(self, tip):
        return self.__shuffle_words(self.__open_file(FILE_PATH.replace("palavras", tip.lower())))[0]

    @staticmethod
    def __shuffle_words(list):
        random.shuffle(list)
        return list

    @staticmethod
    def __open_file(path):
        words_files = open(path)
        files = words_files.read().splitlines()
        words_files.close()
        return files
