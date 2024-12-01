import random, os
from algorithms import fifo, lru, opt

FRAME_SIZES = [3, 4, 5, 6]


def generate_reference_strings():
    NUM_STRINGS = 50
    STRING_LENGTH = 30
    MAX_PAGE = 7

    FOLDER_NAME = "testing-data"
    FILE_NAME = "TestingData.txt"

    os.makedirs(FOLDER_NAME, exist_ok=True)
    full_path = os.path.join(FOLDER_NAME, FILE_NAME)

    with open(full_path, "w", encoding="utf-8") as file:
        for _ in range(NUM_STRINGS):
            reference_string = "".join(
                str(random.randint(0, MAX_PAGE)) for _ in range(STRING_LENGTH)
            )
            file.write(reference_string + "\n")


def testing_data_to_array():
    TESTING_DATA_PATH = "testing-data/"

    with open(TESTING_DATA_PATH + "TestingData.txt", "r", encoding="utf-8") as file:
        string_list = []

        for line in file.readlines():
            string_list.append(line.strip())

        return string_list


def run_fifo_tests():
    for reference_string in testing_data_to_array():
        for frame_size in FRAME_SIZES:
            fifo.run_algorithm(reference_string, frame_size)


def run_lru_tests():
    for reference_string in testing_data_to_array():
        for frame_size in FRAME_SIZES:
            lru.run_algorithm(reference_string, frame_size)


def run_opt_tests():
    for reference_string in testing_data_to_array():
        for frame_size in FRAME_SIZES:
            opt.run_algorithm(reference_string, frame_size)


def main():
    TEST_REFERENCE_STRING = "135732345051740"

    # Test to make sure algorithm works
    fifo.run_algorithm(TEST_REFERENCE_STRING, 5)
    lru.run_algorithm(TEST_REFERENCE_STRING, 5)
    opt.run_algorithm(TEST_REFERENCE_STRING, 5)

    # generate_reference_strings()

    # run_fifo_tests()
    # run_lru_tests()
    # run_opt_tests()


if __name__ == "__main__":
    main()
