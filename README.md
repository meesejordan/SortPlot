# SortPlot

See Sorting algoritms work in real-time.

## Description

See sorting algorithms work in real-time with the help of the Python programming language, the Matplotlib plotting library and the NumPy numerical mathematics extension.

## Getting Started

### Dependencies

-   Python 3
-   matplotlib
-   numpy

### Installing

-   Download sortplot.py
-   Install numpy
-   Install matplotlib

### Executing program

```
usage: sortplot.py [-h] [-n N] [-alg ALG] [-s S]
```

-   options:
    -   -h, --help show this help message and exit
    -   -n N define the number of random integers.
        -   Default is 100
    -   -alg ALG define the sorting algorithm.
        -   Default is bubblesort.
        -   Options: - 'bbs': BubbleSort, 'qs': QuickSort, 'ss': SelectionSort, 'is': InsertionSort
    -   -s S define how fast the display is. Lower is faster.
        -   Default is 0.001.

## Help

To see help:

```
sortplot.py [-h]
```

Known issue:

-   Stopping the program while in execution:
    -   Simply exiting the matplotlib window will NOT stop execution and so the window must be opened again. Must use signals to stop execution of the program
        -   I.e., `CTRL+C` on windows machines

## Authors

Contributors names and contact info

[@JordanMeese](jordanmeese.tech)

## Version History

-   0.1
    -   Initial Release

## License

This project is licensed under the MIT License - see the LICENSE.md file for details

## Acknowledgments

Sorting Algorithms

-   [GeeksForGeeks](https://www.geeksforgeeks.org/sorting-algorithms/)
