
def transform_to_upper(record: str) -> str:
    return record.upper()


def transform_to_lower(record: str) -> str:
    return record.lower()


def transform_remove_words(record: str) -> str:
    words = record.split()
    stop_words = ["a", "an", "and", "the", "or", "A", "AN", "AND", "THE", "OR"]
    remaining_words = [word for word in words if word not in stop_words]
    return " ".join(remaining_words)






