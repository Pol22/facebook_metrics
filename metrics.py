import csv
import pandas as pd
import numpy as np
from scipy.stats import mode


file_name = 'dataset_Facebook.csv'

array_for_converter = []

dict_functions = {'Min': np.min, 'Max': np.max, 'Median': np.median,
                  'Average': np.average}


def custom_print(str_func, input_dict, array):
    if str_func == 'Mode':
        print('Mode in all:', mode(array).mode[0],
              ', in Photo:', mode(input_dict['Photo']).mode[0],
              ', in Status:', mode(input_dict['Status']).mode[0],
              ', in Link:', mode(input_dict['Link']).mode[0],
              ', in Video:', mode(input_dict['Video']).mode[0])
    else:
        executable_func = dict_functions[str_func]
        print(str_func, 'in all:', executable_func(array),
              ', in Photo:', executable_func(input_dict['Photo']),
              ', in Status:', executable_func(input_dict['Status']),
              ', in Link:', executable_func(input_dict['Link']),
              ', in Video:', executable_func(input_dict['Video']))


def convert(input):
    try:
        array_for_converter.append(float(input))
        return float(input)
    except:
        # if value of missing returns average of past values
        return np.average(array_for_converter)


if __name__ == '__main__':
    data_matrix = list(map(lambda x: x.strip('\n').split(';'),
                           open(file_name, 'r').readlines()))
    metrics = data_matrix[0]
    data = pd.DataFrame.from_records(data_matrix[1:], columns=metrics)
    
    # can cycle for other metrics
    metric_number = 18
    metric = metrics[metric_number]
    metric_array = []
    dict_array_for_type = {}
    dict_array_for_type['Photo'] = []
    dict_array_for_type['Status'] = []
    dict_array_for_type['Link'] = []
    dict_array_for_type['Video'] = []

    for line in data.get_values():
        value = convert(line[metric_number])
        metric_array.append(value)
        dict_array_for_type[line[1]].append(value)
    array_for_converter.clear()

    print('Metric:', metric)

    custom_print('Min', dict_array_for_type, metric_array)
    custom_print('Max', dict_array_for_type, metric_array)
    custom_print('Median', dict_array_for_type, metric_array)
    custom_print('Average', dict_array_for_type, metric_array)
    custom_print('Mode', dict_array_for_type, metric_array)

    print('Most popular object is ', end='')
    # popular because have max interactions => max dispersion
    print(data[data[metric] == str(int(np.max(metric_array)))].index[0])
