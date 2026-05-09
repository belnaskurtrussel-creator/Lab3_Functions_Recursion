# media_engine.py

def monitor(func):
    def wrapper(*args, **kwargs):
        print("Processing Started")
        result = func(*args, **kwargs)
        print("Processing Completed")
        return result
    return wrapper

@monitor
def signal_shutdown(power):
    print(f"Signal strength: {power}")
    if power == 0:
        return 0
    return 1 + signal_shutdown(power - 1)

@monitor
def play_count_stream(limit):
    for n in range(limit):
        if n % 2 == 0:
            yield n ** 2
