from timeit import default_timer as timer

# cpu_time decorator
def cpu_time(func):
    def wrapper_cpu_time(*args, **kwargs):
        start = timer()
        value = func(*args, **kwargs)
        end = timer()
        print(f"Processing {func.__name__} for {end- start} seconds")

        return value
    return wrapper_cpu_time


@cpu_time
def pretty_fast():
    return sum([x for x in range(100_000)])


@cpu_time
def little_bit_slower():
    nums = []
    for i in range(1_000):
        for j in range(1_000):
            nums.append(i + j)

@cpu_time
def very_slow():
    nums = []
    for i in range(100):
        for j in range(1_000):
            for z in range(1_000):
            	nums.append(i + j + z)


if __name__ == '__main__':

    pretty_fast()
    little_bit_slower()
    very_slow()
