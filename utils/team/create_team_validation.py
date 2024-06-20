# validation.py
def validate_integer(P):
    if P.isdigit() or P == "":
        return True
    return False

def validate_initial_level(P):
    if P.isdigit() and 0 <= int(P) <= 100:
        return True
    return False

def create_validation_commands(self):
    self.vcmd_integer = (self.master.register(validate_integer), '%P')
    self.vcmd_initial_level = (self.master.register(validate_initial_level), '%P')
