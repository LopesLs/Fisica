def calcular_potencial(carga:float, distancia:float) -> float:
  """
   Calcula o potencial elétrico entre duas cargas.

    Args:
      carga (float): Valor da carga elétrica em Coulombs.
      distancia (float): Distância entre as cargas em metros.

    Returns:
      float: Valor do potencial elétrico em Volts.
  """
  
  K = 9e9
  Va = "{:.1e}".format(K * carga / distancia)
  return Va


def calcular_potencial_com_campo(carga: float, campo: float) -> float:
  """
   Calcula o potencial elétrico entre cargas levando em consideração o campo elétrico.

    Args:
      carga (float): Valor da carga elétrica em Coulombs.
      campo (float): Valor do campo elétrico em Newtons/Coulomb.
    
    Returns:
      float: Valor do potencial elétrico em Volts.
  """
  
  Va = "{:.1e}".format(campo * carga)
  return Va

def calcular_diferenca_potencial(potencial_inicial: float, potencial_final: float) -> str:
  """
   Calcula a diferença de potencial elétrico entre dois pontos.

    Args:
      potencial_inicial (float): Valor do potencial elétrico inicial em Volts.
      potencial_final (float): Valor do potencial elétrico final em Volts.
    
    Returns:
      float: Valor da diferença de potencial elétrico em Volts.
  """
  
  Vab = "{:.1e}".format(potencial_final - potencial_inicial)
  return Vab

def calcular_potencial_com_trabalho(trabalho: float, carga: float) -> float:
  """
   Calcula o potencial elétrico a partir do trabalho realizado sobre a carga.

    Args:
      trabalho (float): Valor do trabalho realizado em Joules.
      carga (float): Valor da carga elétrica em Coulombs.
    
    Returns:
      float: Valor do potencial elétrico em Volts.
  """

  Va = "{:.1e}".format(trabalho / carga)
  return Va

def calcular_energia_potencial(carga_geradora:float, carga_prova:float, distancia:float) -> float:
  """
   Calcula a energia potencial elétrica entre duas cargas.

    Args:
      carga_geradora (float): Valor da carga elétrica geradora em Coulombs.
      carga_prova (float): Valor da carga elétrica de prova em Coulombs.
      distancia (float): Distância entre as cargas em metros.

    Returns:
      float: Valor da energia potencial elétrica em Joules.
  """
  K = 9e9
  Epe = "{:.1e}".format(K * carga_geradora * carga_prova / distancia)
  return Epe

def calcular_trabalho(forca:float, distancia:float) -> float:
  """
   Calcula o trabalho realizado por uma força elétrica.

    Args:
      forca (float): Valor da força elétrica em Newtons.
      distancia (float): Distância percorrida pela carga em metros.
    
    Returns:
      float: Valor do trabalho realizado em Joules.
  """
  W = "{:.1e}".format(forca * distancia)
  return W
