# @ parmm mfg manufacturer
# @ param model is the model of the car
# @ param **other: unlimited number of fields
def make_car(mfg, model, **other):
    """ stores information about the car in dictionary """
    my_dict = {"Manufacturer": mfg, "Model": model}
    for key, value in other.items():
        my_dict[key] = value
        
    return my_dict

def main():

    cars = make_car('subaru', 'outback', color='blue', tow_package=True) 

    print(cars)

if __name__ == "__main__":
    main()
    
