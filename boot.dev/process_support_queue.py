def process_support_queue(current_queue: list, new_customers: list, to_serve: int):
    working_queue = current_queue
    working_queue.extend(new_customers)
    served_customers = []
    while to_serve > 0 and len(working_queue) > 0:
        served_customers.append(working_queue.pop(0))
        to_serve -= 1
    return served_customers
