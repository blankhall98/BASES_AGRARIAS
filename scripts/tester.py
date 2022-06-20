# TESTER
class Tester:

    def __init__(self):
        print('working')

    def test(self,to_match,possible_match):
        is_match = False
        if not is_match:
            is_match = self.simple_test(to_match,possible_match)
        return is_match

    
    #simple test
    def simple_test(self,to_match,possible_match):
        if to_match == possible_match:
            return possible_match
        elif to_match.strip() == possible_match.strip():
            return possible_match
        elif to_match.upper() == possible_match.upper():
            return possible_match
        elif to_match.lower() == possible_match.lower():
            return possible_match
        elif to_match.strip().upper() == possible_match.strip().upper():
            return possible_match
        elif to_match.strip().lower() == possible_match.strip().lower():
            return possible_match
        else:
            return False

    #
    
