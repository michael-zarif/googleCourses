def full_emails(people):
    result = []
    for email, name in people:
        result.append(f'{name} <{email}>')

    return result

names_emails = [('john@example.com', 'John Doe'),
                ('peter@example.com', 'Peter Parker'),
                ('marina@example.com', 'Marina Alex')]
print(full_emails(names_emails))