def build_profile(first, last, **user_info):
    #start with empty dict to fill.
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    #if user wants to store more info.
    for key, value in user_info.items():
        profile[key] = value
    return profile

jon_profile = build_profile('Jon', 'Mast', age = 27, location = 'Coral Springs')
print(jon_profile)