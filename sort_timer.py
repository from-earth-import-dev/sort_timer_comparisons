import time
import random as rand
from matplotlib import pyplot as plt
import functools

def sort_timer(func):
    @functools.wraps(func)
    def wrapper(*args):
        start_time = time.perf_counter()
        result = func(*args)
        ending_time = time.perf_counter()
        return ending_time - start_time
    return wrapper

@sort_timer
def bubble_sort(a_list):
  """
  Sorts a_list in ascending order
  """
  for pass_num in range(len(a_list) - 1):
    for index in range(len(a_list) - 1 - pass_num):
      if a_list[index] > a_list[index + 1]:
        temp = a_list[index]
        a_list[index] = a_list[index + 1]
        a_list[index + 1] = temp

@sort_timer
def insertion_sort(a_list):
  """
  Sorts a_list in ascending order
  """
  for index in range(1, len(a_list)):
    value = a_list[index]
    pos = index - 1
    while pos >= 0 and a_list[pos] > value:
      a_list[pos + 1] = a_list[pos]
      pos -= 1
    a_list[pos + 1] = value

def compare_sorts(bubble,insertion):
    """
    Iterate over lists of random integers of increasing size from 1000 to 10000
    Builds two lists of timing data for both the bubble sort and insertion sort
    Timing data from each algorithm is stored in separate lists
    Concludes with Matplotlib line chart showing the two algorithm's sorting times

    :param bubble: bubble_sort()
    :param insertion: insertion_sort()
    :return:
    """
    bubble_times = []
    insertion_times = []
    list_size = 1000

    while list_size <= 10000:
        bubble_list = [rand.randint(1,10000) for num in range(list_size)]
        insertion_list = list(bubble_list)
        bubble_times.append(bubble(bubble_list))
        insertion_times.append(insertion(insertion_list))
        list_size += 1000

    x_list_sizes = [val for val in range(1000,11000,1000)]
    plt.plot(x_list_sizes, bubble_times, 'ro--', linewidth=2, label='Bubble Sort')
    plt.plot(x_list_sizes, insertion_times, 'go--', linewidth=2, label='Insertion Sort')
    plt.xlabel('List Sizes')
    plt.ylabel('Sorting Time (Seconds)')
    plt.legend()
    plt.show()
    return

compare_sorts(bubble_sort,insertion_sort)


