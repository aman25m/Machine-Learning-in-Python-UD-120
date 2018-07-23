#!/usr/bin/python


def outlierCleaner(predictions, ages, net_worths):
    """
        Clean away the 10% of points that have the largest
        residual errors (difference between the prediction
        and the actual net worth).

        Return a list of tuples named cleaned_data where 
        each tuple is of the form (age, net_worth, error).
    """
    #print predictions
    cleaned_data = []

    ### your code goes here
    for i in range(len(ages)):
        cleaned_data.append((ages[i][0],net_worths[i][0], abs(predictions[i][0] - net_worths[i][0])))

    cleaned_data.sort(key=lambda x: x[2],reverse=True)
    #print cleaned_data
    return cleaned_data[9:]

