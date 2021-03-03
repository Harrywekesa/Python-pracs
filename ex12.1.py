import ex12

sentence = "All good things come to those who wait"
words = ex12.break_words(sentence)
words

sorted_words = ex12.sort_words(words)
sorted_words

ex12.print_first_words(words)
ex12.print_last_words(words)

ex12.print_first_words(sorted_words)
ex12.print_last_words(sorted_words)
sorted_words

sorted_words = ex12.sort_sentence(sentence)
sorted_words

ex12.print_first_and_last(sorted_words)
ex12.print_first_and_last_sorted(sorted_words)