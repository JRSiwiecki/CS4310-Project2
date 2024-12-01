def run_algorithm(reference_string, frame_size):
    page_frame = []
    fault_track = ""

    print(reference_string)

    for page in reference_string:

        if page in page_frame:
            fault_track += " "
            continue

        if len(page_frame) >= frame_size:
            page_frame.pop(0)

        page_frame.append(page)
        fault_track += "X"

    fault_count = 0
    for char in fault_track:
        if char == "X":
            fault_count += 1

    print(fault_track)
    print("FIFO yields", fault_count, "faults with frame size", frame_size)
