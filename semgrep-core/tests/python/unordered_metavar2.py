#ERROR: match
class C:
    def a(self, default=[]):
        self.default = default
        
    def b(self, x):
        self.default.append(1)
        
    def some_other_function(self):
        return 5
        
#ERROR: match
class D:
    def b(self, x):
        self.default.append(1)
        
        
    def a(self, default=[]):
        self.default = default
        
    
    def some_other_function(self):
        return 5
        
#ERROR: match
class E:
    def a(self, default=[]):
        self.default = default
    
    def some_other_function(self):
        return 5
        
    def b(self, x):
        self.default.append(1)
