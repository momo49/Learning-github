grand = None;
print ('Avant:', grand);
for itervar in [100, 1999, 200, 1999999, 90]:
    if grand is None or itervar > grand:
        grand = itervar;
        print('Louche:', itervar, grand);
        print ('Plus Grand est:', grand);