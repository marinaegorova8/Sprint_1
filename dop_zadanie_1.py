def remove_duplicates(current_list, seen_list):
    unique_list = []
    for ticket in current_list:
        if ticket not in seen_list:
            unique_list.append(ticket)
            seen_list.append(ticket)
    return unique_list


def get_tickets_by_type(types, tickets):
    final_dict = {}
    seen_tickets = []
    
    for number in types:
        name_type = types[number]
        list_tickets = tickets[number]
        
        clean_tickets = remove_duplicates(list_tickets, seen_tickets)
        
        final_dict[name_type] = clean_tickets
        
    return final_dict