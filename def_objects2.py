 #Select Properties/Borders
    my_dict_Borders = dict()
    my_dict_Borders ['keyBrd1'] = ".//*[@id='bordersMenu']/option[1]"  # Form
    my_dict_Borders ['keyBrd2'] = ".//*[@id='bordersMenu']/option[2]"  # Section
    my_dict_Borders ['keyBrd3'] = ".//*[@id='bordersMenu']/option[3]"  # Instructions
    for key in my_dict_Borders:
        print key
   
    #Select Properties/Borders/Thickness
    my_dict_Thickness = dict()
    for i in xrange(4):
        my_dict_Thickness['keyThickness' + str(i+1)] = ".//*[@id='thickMenu']/select/option[" + str(i+1) + "]"
    for key in my_dict_Thickness:
        print key
