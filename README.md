# Project Overview

This project consists of producers and consumers that simulate the process of generating and processing messages in a streaming system. Below is a description of the key Python files in the project.

## Producers

### `basic_producer_dobler.py`

This producer generates random "buzz" messages in a continuous stream. The messages consist of a combination of adjectives, actions, and topics, such as "I just tried an app! It was funny." The producer writes these messages to a log file at regular intervals, which can be customized through the environment variable `MESSAGE_INTERVAL_SECONDS`. The messages are logged using the `logger` from the `utils` module.

**How it works**:
- Loads environment variables using `.venv`.
- Fetches the message interval from the environment or defaults to 3 seconds.
- Continuously generates and logs random buzz messages every few seconds.

### Example Usage:
source .venv/bin/activate
python3 -m consumers.basic_consumer_dobler
