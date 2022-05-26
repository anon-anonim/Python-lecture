entities = {}
for i in range(int(input())):
    user_input = input().split(' : ')
    name = user_input[0]
    if len(user_input) > 1:
        entities.setdefault(name, user_input[1].split(' '))
        continue
    entities.setdefault(name, [])

result = []
def is_child(child, target):
    if child == target:
        return 'Yes'
    parents = entities.get(child)
    for parent in parents:
        if parent == target:
            return 'Yes'
    for parent in parents:
        if is_child(parent, target) == 'Yes':
            return 'Yes'
    return 'No'

for i in range(int(input())):
    parent, child = input().split(' ')
    result.append(is_child(child, parent))

for answer in result:
    print(answer)