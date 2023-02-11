
being_deleted = (input('Введите что будем удалять:\n ')).split()
proposal = str(input('Введите введите предложение:\n '))
split_str = proposal.split()
filtered_str = ' '.join((filter(lambda s: s not in being_deleted, split_str)))
print("Ваше предложение ->", filtered_str)
