class Device:
    
    def __init__(self,item_type,weight,cpu,gpu,cost,owned_by):
        self.item_type = item_type
        self.weight = weight
        self.cpu = cpu
        self.gpu = gpu
        self.cost = cost
        self.owned_by = owned_by
        
    def get_owner(self):
        return self.owned_by
    
    def get_cost(self):
        return int(self.cost)
    
    def get_full_info(self):
        return f"ID: {self.item_id}, typ: {self.item_type}, waga: {self.weight} kg, " \
               f"cpu: {self.cpu}, gpu: {self.gpu}, cena: {self.cost}, właściciel: {self.owned_by}"
