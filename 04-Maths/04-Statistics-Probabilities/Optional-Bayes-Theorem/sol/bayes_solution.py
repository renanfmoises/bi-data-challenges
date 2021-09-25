# pylint: disable=missing-docstring

weather_data_example = ['Sunny', 'Overcast', 'Rainy', 'Sunny', 'Sunny', 'Overcast', 'Rainy', 'Rainy', 'Sunny',
'Rainy', 'Sunny', 'Overcast', 'Overcast', 'Rainy']

play_data_example = ['No', 'Yes', 'Yes', 'Yes', 'Yes', 'Yes', 'No', 'No', 'Yes', 'Yes', 'No', 'Yes', 'Yes', 'No']

def prior_probability(play, play_data):
    '''TO DO: return the probability that the event from the event_data occurs'''
    counter = 0
    for i in play_data:
        if i == play:
            counter += 1
    return float(counter/len(play_data))

def likelihood(weather, play, weather_data, play_data):
    '''TO DO: return P(weather|play)'''
    total = 0
    occurences = 0
    for i in range(len(play_data)):
        if play_data[i] == play:
            total += 1
            if weather_data[i] == weather:
                occurences += 1
    return float(occurences/total)

def posterior_probability(play, weather, weather_data, play_data):
    '''TO DO: return P(play|weather)
    '''
    p_play = prior_probability(play, play_data)
    p_weather = prior_probability(weather, weather_data)
    p_likelihood = likelihood(weather, play, weather_data, play_data)
    return p_play * p_likelihood / p_weather


# TEST
# posterior_probability('Yes','Sunny', weather_data_example, play_data_example)
