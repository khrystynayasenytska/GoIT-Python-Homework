import queue
import uuid
from collections import namedtuple
from datetime import datetime

# Create a named tuple to represent a service request
Request = namedtuple('Request', ['id', 'description', 'timestamp'])

# create a queue to hold service requests
request_queue = queue.Queue()


def generate_request():
    """Generates a new service request and adds it to the queue"""
    request_id = str(uuid.uuid4())[:8]  # unique short id
    description = f"Request for service #{request_id}"
    timestamp = datetime.now().strftime("%H:%M:%S")

    new_request = Request(id=request_id, description=description, timestamp=timestamp)
    request_queue.put(new_request)

    print("\n✓ New Request created:")
    print(f"  ID: {new_request.id}")
    print(f"  Description: {new_request.description}")
    print(f"  CreatedAt: {new_request.timestamp}")
    return new_request


def process_request():
    """processes the next service request in the queue"""
    if not request_queue.empty():
        request = request_queue.get()
        print("\n⚙ Request is in progress:")
        print(f"  ID: {request.id}")
        print(f"  Description: {request.description}")
        print(f"  CreatedAt: {request.timestamp}")
        print("✓ Request processed successfully and deleted from queue")
        return request
    else:
        print("\n⚠ queue is empty. No requests to process.")
        return None


def show_queue_status():
    """Displays the current status of the request queue"""
    size = request_queue.qsize()
    print("\n📊 Current status of the queue:")
    print(f"  Number of requests in the queue: {size}")
    if size == 0:
        print("  Queue is empty.")


# main function to simulate the service center request processing
def main():
    print("=" * 50)
    print("   Service Center Request Processing Simulation   ")
    print("=" * 50)

    # Simulate multiple cycles of request generation and processing
    for i in range(3):
        print(f"\n{'=' * 50}")
        print(f"Cycle {i + 1}")
        print('=' * 50)

        # generate new requests
        print("\n[Generating Requests]")
        generate_request()
        generate_request()

        # show current queue status
        show_queue_status()

        # process a request
        print("\n[Processing Request]")
        process_request()

        # show updated queue status
        show_queue_status()

    # remaining requests processing
    print(f"\n\n{'=' * 50}")
    print("   Processing Remaining Requests in Queue   ")
    print('=' * 50)

    while not request_queue.empty():
        process_request()

    show_queue_status()
    print("\n✓ All requests have been processed. Simulation complete.")


if __name__ == "__main__":
    main()
