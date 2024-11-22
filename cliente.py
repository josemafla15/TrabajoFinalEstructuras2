class Cliente:
    def __init__(self, name, id_client, is_prioritary=False):
        self.name = name
        self.id_client = id_client
        self.is_prioritary = is_prioritary
        self.services = []

    def append_service(self, service):
        self.services.append(service)