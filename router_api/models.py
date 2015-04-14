from django.db.models import *

class Router(Model):
    name = CharField(max_length=200)
    updated_at = DateTimeField()
    def __str__(self):
        return self.name

class Vpn(Model):
    router = ForeignKey(Router, related_name='vpns')
    name = CharField(max_length=200)
    import_target = CharField(max_length=52)
    route_target = CharField(max_length=52)
    num_routes = IntegerField(default=0)
    def __str__(self):
        return self.name

class Interface(Model):
    router = ForeignKey(Router, related_name='interfaces')
    name = CharField(max_length=52)
    description = CharField(max_length=200)
    input_bytes = IntegerField(default=0)
    output_bytes = IntegerField(default=0)
    discards = IntegerField(default=0)
    errors = IntegerField(default=0)
    def __str__(self):
        return self.name

class Cpu(Model):
    router = ForeignKey(Router, related_name='cpu')
    time = DateTimeField()
    utilization = IntegerField(default=0)
    def __str__(self):
        return "%s - %s" % (self.time, self.utilization)

class Memory(Model):
    router = ForeignKey(Router, related_name='memory')
    time = DateTimeField()
    utilization = IntegerField(default=0)
    def __str__(self):
        return "%s - %s" % (self.time, self.utilization)


