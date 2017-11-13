email_domain = '@blah.com'

def get_email(word_list):
    # word_lilst - input parametr from two words
    # [:2] - return list with maximum two elements
    first_last_names_list = word_list[:2]
    if len(first_last_names_list) == 0:
        print('!!! Error: you need provide at list first name.')
        email_value = None
    else:
        # lower case for strings
        lower_case_list = [word.lower() for word in first_last_names_list]
        # attach words by dot(.)
        email_name = '.'.join(lower_case_list)
        # get email constructor
        email_value = '{}{}'.format(email_name, email_domain)
    return email_value

def main():
    input_words_str = raw_input('Please input your first and last name: ')
    # split() - create list with separate words
    input_words_list = input_words_str.split()
    # no spaces between characters
    sanitized_input_str = ' '.join(input_words_list)
    print ('Your input was: {}'.format(sanitized_input_str))
    # get get mail:
    email_value = get_email(input_words_list)
    if email_value is None:
        print('!!! Error: something went wrong')
    else:
        print('Your email: {}'.format(email_value))
    print ('Done!')


if __name__ == '__main__':
    main()
