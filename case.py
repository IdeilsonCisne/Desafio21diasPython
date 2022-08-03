class Switch:
  def case_1(self):
    print("Janeiro")
  def case_2(self):
    print("Fevereiro")
  def case_3(self):
    print("Março")
  def case_4(self):
    print("Abril")
  def case_5(self):
    print("Maio")
  def case_6(self):
    print("Junho")
  def case_7(self):
    print("Julho")
  def case_8(self):
    print("Agosto")
  def case_9(self):
    print("Setembro")
  def case_10(self):
    print("Outubro")
  def case_11(self):
    print("Novembro")
  def case_12(self):
    print("Dezembro")
  def case(self, cases):
    method = "case_" + str(cases)
    return getattr(self, method)()

print(f"O resultado foi:")
Switch().case(12)