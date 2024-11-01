class Aluno:
  def __init__(self, nome, matricula, curso = "", dataNascimento = ""):
    self.__nome = nome
    self.__matricula = matricula
    self.__curso = curso
    self.__dataNacimento = dataNascimento
  
  
  # Criar as propriedades para os atributos
  @property
  def nome(self):
    print(f"Nome: {self.__nome} ")
  
  @property
  def matricula(self):
      return f"Matrícula: {self.__matricula}"
      
  @property
  def curso(self):
      return f"Curso: {self.__curso}"
      
  @property
  def dataNascimento(self):
      return f"Data de nascimento: {self.__dataNacimento}"
      
  @nome.setter
  def nome(self, nome):
      self.__nome = nome
      
  @matricula.setter
  def matricula(self, matricula):
      self.__matricula = matricula
      
  @curso.setter
  def curso(self, curso):
      self.__curso = curso
      
  @dataNascimento.setter
  def dataNascimento(self, dataNascimento):
      self.__dataNacimento = dataNascimento
  
  def __str__(self) -> str:
     return f"Nome: {self.__nome} | Matrícula: {self.__matricula} | Curso: {self.__curso} | Data de Nascimento: {self.__dataNacimento}"  