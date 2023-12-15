post_ticket_query = 'INSERT INTO tickets (title, description, client_id, status_id) VALUES(%(title)s, %(description)s, %(user_id)s, %(status)s) RETURNING ticket_id'

get_tickets_client_query = "SELECT tickets.*, status.status_name AS status_name FROM tickets LEFT JOIN status ON status.status_id = tickets.status_id WHERE client_id = %s"

get_tickets_analyst_query = "SELECT tickets.*, status.status_name AS status_name FROM tickets LEFT JOIN status ON status.status_id = tickets.status_id WHERE analyst_id = %s OR analyst_id IS NULL"

get_ticket_query = "SELECT tickets.*, status.status_name AS status_name FROM tickets LEFT JOIN status ON status.status_id = tickets.status_id WHERE ticket_id = %s"

put_ticket_next_query = "UPDATE tickets SET status_id = %s WHERE ticket_id = %s"

put_ticket_finish_query = "UPDATE tickets SET status_id = %s, closed_by = %s WHERE ticket_id = %s;"

put_ticket_take_query = "UPDATE tickets SET status_id = %s, analyst_id = %s WHERE ticket_id = %s;"
