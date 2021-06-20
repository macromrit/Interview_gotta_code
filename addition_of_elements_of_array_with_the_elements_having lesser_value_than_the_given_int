#stack over elements from an array that's lesser than or equal to a given value

#defining a function christined as figurer to make chores work right
def figurer(list_a: list=list(), max_value: int=0) -> int and list:

    #the variable to be returned 
    main_val = 0

    #list which contains the valid values
    sorted_list = list()
    excessive_list = list()
    
    #iterating through the list imparted by the user
    for i in list_a: 

        #checking via conditions to make stuffs work fine
        if (i < max_value) or (i == max_value):
    
            #implementing addition if the conditions make the cut
            main_val+=i
            
            #appending valid elements to the list we created 
            sorted_list.append(i)

        #else statement    
        else:

            #just skipping over as this step is not mandatory.. but made it to obcure clarity
            continue
    
    #puking out the data
    print('inserted list: {}'.format(list_a))
    print('the valid elements are: {}'.format(sorted_list))
    print('the total value is: {}'.format(main_val))
    return main_val, sorted_list
