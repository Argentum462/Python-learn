import OrganisationOOOFate

dic = OrganisationOOOFate.OrganisationOOOFate.people_list()

for k in dic:
    if dic[k]['room'] >= 800 and dic[k]['room'] < 900:
        print(f"Name: {dic[k]['name']}, room: {dic[k]['room']}")

#    print(f'{k}: {dic[k]}')

