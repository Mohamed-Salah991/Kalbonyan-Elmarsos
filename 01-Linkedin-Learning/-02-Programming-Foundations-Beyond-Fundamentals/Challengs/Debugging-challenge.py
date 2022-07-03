def plant_recommendation(care):
    if care == 'low':  # if ->  ( == )  not (  = ) 
        print('aloe')
    elif care == 'medium':
        print('pothos')
    elif care == 'high':    # logical error (unexpected output ) => be careful about small things
        print('orchid')


plant_recommendation('low')  # write correct name of function
plant_recommendation('medium')
plant_recommendation('high')
