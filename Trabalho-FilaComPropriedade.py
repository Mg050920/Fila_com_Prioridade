import os

def clean():
        os.system('cls')

class MaxHeap: 
    def __init__(self):
        self.heap=[0]
    
    def put(self, item):
        self.heap.append(item)
        self.__floatUp(len(self.heap) - 1)

    def get(self):
        if len(self.heap) > 2:
            self.__swap(1, len(self.heap) - 1)
            max = self.heap.pop()
            self.__bubbleDown(1)
        elif len(self.heap) == 2:
            max = self.heap.pop()
        else:
            max = False
        return max

    def peek(self):
        if self.heap[1]:
            return self.heap[1]
        return False

    def __swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    def __floatUp(self, index):
            parent = index//2
            if index <= 1:
                return
            elif self.heap[index] > self.heap[parent]:
                self.__swap(index, parent)
                self.__floatUp(parent)

    def __bubbleDown(self, index):
        left = index * 2
        right = index * 2 + 1
        maior = index
        if len(self.heap) > left and self.heap[maior] < self.heap[left]:
            maior = left
        if len(self.heap) > right and self.heap[maior] < self.heap[right]:
            maior = right

        if maior != index:
            self.__swap(index, maior)
            self.__bubbleDown(maior)

class Paciente:
    def __init__(self):
        clean()
        self.prioridade = ()
        self.listaPacientes = []
        self.contador = 999
        self.dadosPaciente = ()
        self.max_heap = MaxHeap()
        self.lista = []
        self.pacientes_chamados = []
   
    def adicionarPaciente(self, prioridade, nomeCompleto, tipoSanguineo, dataNascimento):
        self.prioridade = prioridade
        self.dadosPaciente = self.prioridade, self.contador, nomeCompleto, tipoSanguineo, dataNascimento
        self.listaPacientes.append(self.dadosPaciente)
        self.max_heap.put(self.prioridade)
        self.contador -= 1
        print("\nPaciente Adicionado Com Sucesso!\n\n")

    def mostrarProximoPaciente(self):
        if not self.listaPacientes:
            print("Ainda não possui um próximo Paciente!")
        else:
            i = 0
            self.elemento = self.max_heap.get()
            self.lista.append(self.elemento)
            while len(self.lista) > 0:    
                if self.listaPacientes[i][0] == self.lista[0]:
                        print(f"Próximo Paciente: {self.listaPacientes[i]}")
                        break  
                elif len(self.listaPacientes) == 1:
                        print(self.listaPacientes[0])
                        break
                else:
                        i += 1

    def chamarProximoPaciente(self):
        if not self.listaPacientes:
            print("Ainda não possui nenhum Paciente para chamar!")
        else:
            i = 0
            self.elemento = self.max_heap.get()
            self.lista.append(self.elemento)
            while len(self.lista) > 0:    
                if self.listaPacientes[i][0] == self.lista[0]:
                        print(f"Paciente Chamado: {self.listaPacientes[i]}")
                        self.pacientes_chamados.append(self.listaPacientes[i])
                        self.lista.pop(0)
                        self.listaPacientes[i], self.listaPacientes[0] = self.listaPacientes[0], self.listaPacientes[i]
                        self.listaPacientes.pop(0)
                        break
                else:
                        i += 1
        
    def mostrar5UltimosPacientes(self):
        if len(self.listaPacientes) < 5:
            print(f"Último(s) Paciente(s) Chamado(s): {self.pacientes_chamados}")
        else:
            print(f"Últimos 5 Pacientes Chamados: {self.pacientes_chamados[-5]}")


paciente = Paciente()

try:
    while True:  
        clean()  
        print("\n1- Adicionar Paciente.\n2- Chamar próximo Paciente.\n3- Mostrar próximo Paciente.\n4- Mostrar 5 últimos Pacientes chamados.\n5- Sair.")

        escolha = int(input("\n\nDigite uma opção: "))
        clean()

        if escolha == 1:
            nomeCompleto = str(input("\nInforme o nome completo do paciente: "))
            
            prioridade = int(input("Informe a prioridade: ")) 
            while prioridade < 1 or prioridade > 10:
                print("Prioridade Inválida!\n")
                prioridade = int(input("Informe a prioridade: "))
            
            tipoSanguineo = str(input("Informe o tipo sanguíneo do paciente: ")) 
            dataNascimento = str(input("Informe a data de nascimento do paciente: "))
            paciente.adicionarPaciente(prioridade, nomeCompleto, tipoSanguineo, dataNascimento)

        elif escolha == 2:
            paciente.chamarProximoPaciente()
            input()
        elif escolha == 3:
            paciente.mostrarProximoPaciente()
            input()
        elif escolha == 4:
            paciente.mostrar5UltimosPacientes()
            input()
        elif escolha == 5:

            break
        else:
            print("Opção inválida!\nEnter para voltar!")
            input()
except:
    print("Opção inválida!")