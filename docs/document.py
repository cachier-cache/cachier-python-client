with open('README-TEMPLATE.md') as f:
    lines = f.readlines()

variable_name = 'repo'
variable_value = next(
    (
        line.split(':')[-1].strip()
        for line in lines
        if line.startswith(f'[{variable_name}]')
    ),
    None,
)

ignore_line = f'[{variable_name}]: {variable_value}'

new_lines = []
for line in lines:
    if ignore_line in line:
        new_lines.pop()
        continue

    if f'[{variable_name}]' in line:
        line = line.replace(f'[{variable_name}]', variable_value)

    new_lines.append(line)

with open('../README.md', 'w') as f:
    for line in new_lines:
        f.write(line)
