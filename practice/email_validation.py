def valid_e(email):
    if "@" not in email or "." not in email or email.index('@') > email.index('.'):
        return False
    return True


print(valid_e('erik@mail.ru')) #True
print(valid_e('erik@mailru')) #False
print(valid_e('er.ik@mailru')) #False
print(valid_e('erikmail.ru')) #false




