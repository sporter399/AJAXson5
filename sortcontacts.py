def sort_contacts(contacts):

        pre_list = list(contacts.keys())
        pre_list.sort()
        sorted_list = []

        for i in pre_list:
        
                tuple = (i,  contacts[i][0], contacts[i][1])
                sorted_list.append(tuple)

        return sorted_list

