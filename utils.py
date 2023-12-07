# !/usr/bin/env python
# -*- coding: utf-8 -*-


"""
Classes & functions related to resources monitoring

Simple decorator designed to assess:
    - Running time
    - Max RAM usage
"""


# =========================================================================================================
# ================================ 0. MODULE

import numpy as np

from datetime import datetime
from dateutil.relativedelta import relativedelta

import tracemalloc
from functools import wraps


# =========================================================================================================
# ================================ 1. FUNCTIONS


def diff(t_a, t_b):
    t_diff = relativedelta(t_a, t_b)
    return f"{t_diff.microseconds}ms"

# diff(time_end, time_start)


# =========================================================================================================
# ================================ 2. DECORATORS


def decorator_maker(rep=1):
    def decorator(function):
        @wraps(function)
        def wrapper(*args, **kwargs):
            times = []
            memories = []

            for _ in range(rep):
                tracemalloc.start()
                time_start = datetime.now()
                
                # function_name = function.__name__
                result = function(*args, **kwargs)

                time_end = datetime.now()
                _, peak = tracemalloc.get_traced_memory()
                tracemalloc.stop()

                times.append(relativedelta(time_end, time_start).microseconds*1e-3 + relativedelta(time_end, time_start).seconds*1e3)
                memories.append(peak)

            # Formating time
            avg_time = np.mean(times)
            if avg_time < 1:
                avg_time_str = f'{round(avg_time*1e3)} µs'
            elif avg_time < 1e2:
                avg_time_str = f'{round(avg_time, 1)} ms'
            elif avg_time < 1e3:
                avg_time_str = f'{round(avg_time)} ms'
            elif avg_time < 1e4:
                avg_time_str = f'{round(avg_time/1e3, 1)} s'
            else:
                avg_time_str = f'{round(avg_time/1e3)} s'

            # Formating memory
            memory = memories[0] / 1024
            if memory < 1024:
                memory_str = f'{round(memory)} KB'
            else:
                memory_str = f'{round(memory / 1024)} MB'

            print(
                f"[{avg_time_str} / {memory_str}]"
            )

            return result

        return wrapper
    return decorator

monitor = decorator_maker(rep=10)