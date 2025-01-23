# Takes two parameters, a string title, representing the title and a list that represents the menu options.
# The function starts calculating the length of the 'title', and frames it visually based of this information
# Finally, the function iterates over 'options' printing out and enumerating all elements in this list
def menu(title: str, options: list) -> None:
    tam = len(title) + 4
    print('=' * tam)
    print(f'{title:^{tam}}')
    print('=' * tam)

    for pos, string in enumerate(options):
        print(f'{pos + 1}- {string}', )








