def run_algorithm(reference_string, frame_size):
    page_frame = []
    fault_track = ""
    print("Running OPT on", reference_string, "with frame size", frame_size)

    for current_index, page in enumerate(reference_string):

        # If page is already in the frame, no page fault
        if page in page_frame:
            fault_track += " "
            print(page, "-", page_frame)
            continue

        fault_track += "X"

        # If the frame is not full, add the page
        if len(page_frame) < frame_size:
            page_frame.append(page)
            print(page, "-", page_frame, "X")
            continue

        # Frame is full, find the page to replace
        page_to_replace = None
        max_future_distance = -1

        for frame_page in page_frame:
            # Find the next occurrence of the frame page
            try:
                future_distance = reference_string[current_index + 1 :].index(
                    frame_page
                )
            except ValueError:
                # If the page is not found in future references, replace it
                page_to_replace = frame_page
                break

            # Update page to replace if this page will be used furthest in the future
            if future_distance > max_future_distance:
                max_future_distance = future_distance
                page_to_replace = frame_page

        # Replace the identified page
        page_frame[page_frame.index(page_to_replace)] = page
        print(page, "-", page_frame, "X")

    fault_count = fault_track.count("X")
    print("OPT yields", fault_count, "page faults")
