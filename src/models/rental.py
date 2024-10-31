class Rental:
    def __init__(self, identifier, start_date, end_date, return_date, expected_end_date, additional_fee, penalty_percentage, total_amount):
        self.identifier = identifier 
        self.start_date = start_date
        self.end_date = end_date
        self.return_date = return_date
        self.expected_end_date = expected_end_date
        self.additional_fee = additional_fee
        self.penalty_percentage = penalty_percentage
        self.total_amount = total_amount