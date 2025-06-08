#დაწერე ფუნქცია, რომელიც იღებს სიას და აბრუნებს მას შებრუნებულ მდგომარეობაში
def reverse_list(input_list):
    input_list.reverse()
    return input_list


print(reverse_list([1, 2, 3, 4, 5]))