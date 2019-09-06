#!/usr/bin/python


def outlierCleaner(predictions, ages, net_worths):
    """
        Clean away the 10% of points that have the largest
        residual errors (difference between the prediction
        and the actual net worth).

        Return a list of tuples named cleaned_data where 
        each tuple is of the form (age, net_worth, error).
    """
    cleaned_data = []
    errors = [abs(a-b) for a,b in zip(predictions, net_worths)] 
    ages_net_worths_error = zip(ages, net_worths, errors)
    ages_net_worths_error = sorted(ages_net_worths_error, reverse=True,  key=lambda tup: (tup[2]))
    red=int(len(ages_net_worths_error)*.1)
    cleaned_data= ages_net_worths_error[red:]
    return cleaned_data

