def run_algorithm(reference_string, frame_size):
    page_frame = []
    page_frame_order = []
    fault_track = ""

    print("Running LRU on", reference_string, "with frame size", frame_size)

    for page in reference_string:

        # If page already in page_frame, need to update the page_frame_order,
        # but no need to change the frame
        if page in page_frame:
            fault_track += " "

            print(page, "-", page_frame)

            page_frame_order.remove(page)
            page_frame_order.append(page)
            continue

        # Otherwise, need to remove the least recently used page
        if len(page_frame) >= frame_size:
            lru_page = page_frame_order.pop(0)
            page_frame.remove(lru_page)

        # Then need to update frame and frame_order
        page_frame.append(page)
        page_frame_order.append(page)
        fault_track += "X"

        print(page, "-", page_frame, end=" ")

        if fault_track[-1] == "X":
            print("X")

    fault_count = fault_track.count("X")

    print("LRU yields", fault_count, "page faults")
