# AdditionalExercise3B.py
# Self-contained version for Exercise 2

CONTROL_NUM = 3   # Example: max(1, SEED_NUM)
FAVORITE_ARTIST = "ARTHUR NERY"

def compute_access_level(control, artist):
    return control * 3 * len(artist)

def validate_access(level, control):
    threshold = control * 5
    return level >= threshold, threshold

def audit_log(func):
    def wrapper(*args, **kwargs):
        print("Authorization Started")
        result = func(*args, **kwargs)
        print("Authorization Completed")
        return result
    return wrapper

@audit_log
def authorize():
    access_level = compute_access_level(CONTROL_NUM, FAVORITE_ARTIST)
    is_valid, threshold = validate_access(access_level, CONTROL_NUM)
    decision = "ACCESS GRANTED" if is_valid else "ACCESS DENIED"

    print("CONTROL_NUM Used:", CONTROL_NUM)
    print("FAVORITE_ARTIST Length:", len(FAVORITE_ARTIST))
    print("Computed Access Level:", access_level)
    print("Threshold Applied:", threshold)
    print("Final Authorization Decision:", decision)

# Run the authorization workflow
if __name__ == "__main__":
    authorize()
