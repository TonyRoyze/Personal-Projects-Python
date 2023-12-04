
import numpy as np


def calculate_yaxis(matrix):

    ymean = np.mean(matrix, axis=0)
    yvar = np.var(matrix, axis=0)
    ystd = np.std(matrix, axis=0)
    ymax = np.max(matrix, axis=0)
    ymin = np.min(matrix, axis=0)
    ysum = np.sum(matrix, axis=0)

    return ymean, yvar, ystd, ymax, ymin, ysum


def calculate_xaxis(matrix):
    xmean = np.mean(matrix, axis=1)
    xvar = np.var(matrix, axis=1)
    xstd = np.std(matrix, axis=1)
    xmax = np.max(matrix, axis=1)
    xmin = np.min(matrix, axis=1)
    xsum = np.sum(matrix, axis=1)

    return xmean, xvar, xstd, xmax, xmin, xsum


def calculate_flat(flat_matrix):

    mean = np.mean(flat_matrix)
    var = np.var(flat_matrix)
    std = np.std(flat_matrix)
    max = np.max(flat_matrix)
    min = np.min(flat_matrix)
    sum = np.sum(flat_matrix)

    return mean, var, std, max, min, sum


def calculate(list):
    if len(list) < 9:
        return "List must contain nine numbers."

    flat_matrix = np.array(list)
    matrix = flat_matrix.reshape(3, 3)

    ymean, yvar, ystd, ymax, ymin, ysum = calculate_yaxis(matrix)
    xmean, xvar, xstd, xmax, xmin, xsum = calculate_xaxis(matrix)
    mean, var, std, max, min, sum = calculate_flat(flat_matrix)
    calculations = {
        'mean': [ymean.tolist(), xmean.tolist(), mean],
        'variance': [yvar.tolist(), xvar.tolist(), var],
        'standard deviation': [ystd.tolist(), xstd.tolist(), std],
        'max': [ymax.tolist(), xmax.tolist(), max],
        'min': [ymin.tolist(), xmin.tolist(), min],
        'sum': [ysum.tolist(), xsum.tolist(), sum]
    }

    return calculations




