# TESTER
class Tester:

    def __init__(self,inputs):
        print('tester working')
        self.inputs = inputs

    def test(self,to_match,possible_match):
        is_match = False
        #test null values
        if not is_match:
            is_match = self.test_null(to_match)
        #test remove
        if not is_match:
            is_match = self.test_remove(to_match,possible_match)
        #simple test
        if not is_match:
            is_match = self.simple_test(to_match,possible_match)
        #return
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

    #test null
    def test_null(self,to_match):
        is_null = False
        for n in self.inputs['nulos']:
            if to_match == n or to_match.startswith(n):
                is_null = True
                break
        if is_null:
            return '0'
        else:
            return False

    #test remove
    def test_remove(self,to_match,possible_match):
        most_remove = False
        possible_match_r = possible_match
        to_match_r = to_match
        for r in self.inputs['remover']:
            if r in to_match or r in possible_match:
                most_remove = True
                to_match_r = to_match_r.replace(r,"", 1)
                possible_match_r = possible_match_r.replace(r,"",1)

        if most_remove:
            return self.simple_test(to_match_r,possible_match_r)
        else:
            return False
            
    
