from time import perf_counter

def measure_seconds(predict_fn, image, repetitions=20):
    if repetitions < 1:
        raise ValueError("repetitions must be >= 1")
    predict_fn(image)  # warm-up
    start = perf_counter()
    for _ in range(repetitions):
        predict_fn(image)
    return (perf_counter() - start) / repetitions
