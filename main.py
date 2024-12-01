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


def calculate_frame_fault_averages(page_fault_counts):
    frame_size_averages = []

    for frame_index in range(len(FRAME_SIZES)):
        frame_faults = [
            page_fault_counts[i][frame_index] for i in range(len(page_fault_counts))
        ]

        frame_size_averages.append(sum(frame_faults) / len(frame_faults))

    return frame_size_averages


def run_fifo_tests():
    page_fault_counts = []

    for reference_string in testing_data_to_array():
        current_frame_page_faults = []

        for frame_size in FRAME_SIZES:
            current_frame_page_faults.append(
                fifo.run_algorithm(reference_string, frame_size)
            )

        page_fault_counts.append(current_frame_page_faults)

    return calculate_frame_fault_averages(page_fault_counts)


def run_lru_tests():
    page_fault_counts = []

    for reference_string in testing_data_to_array():
        current_frame_page_faults = []

        for frame_size in FRAME_SIZES:
            current_frame_page_faults.append(
                lru.run_algorithm(reference_string, frame_size)
            )

        page_fault_counts.append(current_frame_page_faults)

    return calculate_frame_fault_averages(page_fault_counts)


def run_opt_tests():
    page_fault_counts = []

    for reference_string in testing_data_to_array():
        current_frame_page_faults = []

        for frame_size in FRAME_SIZES:
            current_frame_page_faults.append(
                opt.run_algorithm(reference_string, frame_size)
            )

        page_fault_counts.append(current_frame_page_faults)

    return calculate_frame_fault_averages(page_fault_counts)


def main():
    TEST_REFERENCE_STRING = "135732345051740"

    # Test to make sure algorithm works
    # fifo.run_algorithm(TEST_REFERENCE_STRING, 5)
    # lru.run_algorithm(TEST_REFERENCE_STRING, 5)
    # opt.run_algorithm(TEST_REFERENCE_STRING, 5)

    # generate_reference_strings()

    fifo_fault_averages = run_fifo_tests()
    lru_fault_averages = run_lru_tests()
    opt_fault_averages = run_opt_tests()

    print(fifo_fault_averages)
    print(lru_fault_averages)
    print(opt_fault_averages)


if __name__ == "__main__":
    main()
