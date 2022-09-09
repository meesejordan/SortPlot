import matplotlib.pyplot as plt
import numpy as np
import argparse
import time


def main():
    # Initialize argparser
    parser = argparse.ArgumentParser()

    # Add arguments
    parser.add_argument('-n', type=int, default=100,
                        help='define the number of random integers. Default is 100')
    parser.add_argument(
        '-alg', type=str, default='bbs', help='define the sorting algorithm. Default is bubblesort. Options: \'bbs\': BubbleSort, \'qs\': QuickSort,  \'ss\': SelectionSort, \'is\': InsertionSort')
    parser.add_argument('-s', type=float, default=0.001,
                        help='define how fast the display is. Default is 0.001. Lower is faster')

    # Get arguments
    args = parser.parse_args()
    nNum = args.n
    speed = args.s

    # Print usage
    parser.print_help()

    # create random list of elements
    lst = np.random.randint(1, 100, nNum)

    # create x axis, start, stop, step
    x = np.arange(0, nNum, 1)

    # get the count of random numbers
    n = len(lst)

    def bubblesort():
        for i in range(n):
            for j in range(0, n-i-1):
                time.sleep(speed)
                clrs = ['blue'] * n
                # COLOR CURRENT VALUE
                clrs[j] = 'red'
                g = len(clrs[n-i:])
                clrs[n-i:] = ['green'] * g
                plt.bar(x, lst, color=clrs)
                plt.title('Bubble Sort')
                plt.xlabel('index')
                plt.ylabel('number')
                plt.pause(speed)
                # plt.show()
                plt.clf()
                # actual swapping
                if lst[j] > lst[j+1]:
                    # COLOR SWAPPING MEMBER
                    clrs[j+1] = 'red'
                    temp = lst[j]
                    lst[j] = lst[j+1]
                    lst[j+1] = temp
                    g = len(clrs[n-i:])
                    clrs[n-i:] = ['green'] * g
                    # for when it refreshes
                    plt.bar(x, lst, color=clrs)
                    plt.title('Bubble Sort')
                    plt.xlabel('index')
                    plt.ylabel('number')
                    plt.pause(speed*2)
                    time.sleep(speed*2)
                    plt.clf()

    def quicksort(arr, low, high):
        if len(arr) == 1:
            return arr
        if low < high:
            pi = partition(arr, low, high)
            quicksort(arr, low, pi-1)
            quicksort(arr, pi+1, high)

    def partition(arr, low, high):
        i = (low-1)
        pivot = arr[high]
        clrs = ['blue'] * n

        # COLOR THE PIVOT
        clrs[high] = 'green'  # pivot
        # COLOR THE VALUE BEING CHECKED
        clrs[low] = 'red'

        plt.bar(x, lst, color=clrs)
        plt.title('Quick Sort')
        plt.xlabel('index')
        plt.ylabel('number')
        plt.pause(speed)
        plt.clf()

        for j in range(low, high):
            time.sleep(speed)
            if arr[j] <= pivot:
                i = i+1
                arr[i], arr[j] = arr[j], arr[i]
                clrs = ['blue'] * n
                # COLOR THE SWAP
                clrs[j] = 'red'
                clrs[i] = 'red'

                # COLOR THE PIVOT
                clrs[high] = 'green'
                plt.bar(x, lst, color=clrs)
                plt.title('Quick Sort')
                plt.xlabel('index')
                plt.ylabel('number')
                plt.pause(speed)
                time.sleep(speed)
                plt.clf()

        arr[i+1], arr[high] = arr[high], arr[i+1]
        clrs = ['blue'] * n
        # COLOR THE SWAP PIVOT
        clrs[high] = 'green'
        clrs[i+1] = 'green'
        plt.bar(x, lst, color=clrs)
        plt.title('Quick Sort')
        plt.xlabel('index')
        plt.ylabel('number')
        plt.pause(speed)
        plt.clf()
        return (i+1)

    def selectionSort():
        for i in range(n):
            time.sleep(speed)
            min = i
            for j in range(i+1, n):

                if lst[min] > lst[j]:
                    min = j
                    clrs = ['blue'] * n

                    # COLOR CURRENT VALUE
                    clrs[min] = 'red'

                    # COLOR THE SORTED ARRAY THUS FAR
                    if i > 0:
                        g = len(clrs[0:i-1])
                        clrs[0:i-1] = ['green'] * g
                    plt.bar(x, lst, color=clrs)
                    plt.title('Selection Sort')
                    plt.xlabel('index')
                    plt.ylabel('number')
                    plt.pause(0.01)
                    plt.clf()
            # COLOR THE SWAPPING OF THE PIVOT
            lst[i], lst[min] = lst[min], lst[i]
            clrs = ['blue'] * n
            clrs[i] = 'red'
            clrs[min] = 'red'
            # COLOR THE NEWLY SORTED PORTION
            if i > 0:
                g = len(clrs[0:i-1])
                clrs[0:i-1] = ['green'] * g
            plt.bar(x, lst, color=clrs)
            plt.title('Selection Sort')
            plt.xlabel('index')
            plt.ylabel('number')
            plt.pause(speed)
            time.sleep(speed)
            plt.clf()

    def insertionsort():
        for i in range(1, n):
            time.sleep(speed)
            curr = lst[i]
            j = i - 1
            while j >= 0 and curr < lst[j]:
                clrs = ['blue'] * n
                # COLOR THE CURRENT VALUES
                clrs[i] = 'red'  # curr
                clrs[j] = 'red'
                lst[j+1] = lst[j]

                plt.bar(x, lst, color=clrs)
                plt.title('Insertion Sort')
                plt.xlabel('index')
                plt.ylabel('number')
                plt.pause(speed)
                time.sleep(speed)
                plt.clf()
                j = j - 1

            lst[j+1] = curr
            clrs = ['blue'] * n
            # COLOR THE NEWLY PLACE VALUE
            clrs[j+1] = 'green'
            plt.bar(x, lst, color=clrs)
            plt.title('Insertion Sort')
            plt.xlabel('index')
            plt.ylabel('number')
            plt.pause(speed)
            time.sleep(speed)
            plt.clf()

    def insertionsortDriver():
        insertionsort()
        plt.bar(x, lst, color='green')
        plt.title('Insertion Sort')
        plt.xlabel('index')
        plt.ylabel('number')
        plt.show()

    def selectionsortDriver():
        selectionSort()
        plt.bar(x, lst, color='green')
        plt.title('Selection Sort')
        plt.xlabel('index')
        plt.ylabel('number')
        plt.show()

    def quicksortDriver():
        quicksort(lst, 0, n-1)
        plt.bar(x, lst, color='green')
        plt.title('Quick Sort')
        plt.xlabel('index')
        plt.ylabel('number')
        plt.show()

    def bubblesortDriver():
        bubblesort()
        plt.bar(x, lst, color='green')
        plt.title('Bubble Sort')
        plt.xlabel('index')
        plt.ylabel('number')
        plt.show()

    # MAP COMMAND LINE ARGS TO FUNCTIONS
    functionDict = {
        'bbs': bubblesortDriver,
        'qs': quicksortDriver,
        'ss': selectionsortDriver,
        'is': insertionsortDriver,
    }

    # CALL THE SELECTED SEARCH ALGORITHM
    functionDict[args.alg]()


main()
