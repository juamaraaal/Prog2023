class Consulta:
    def __init__ (self, nomedopaciente, nomedomédico, data, hora):
        self.np = nomedopaciente
        self.nm = nomedomédico
        self.data = data
        self.hora = hora
    def __str__(self):
        return "Paciente: " + self.np + "\n" + "Médico: " + self.nm + "\n" + "Horário: " + self.hora + "\n" + "Data: " + self.data
#criando pessoa
paciente = Consulta("Renata Vasconselos", "Ricardo de Oliveira", "23/09/2023", "13:30")
print(paciente)