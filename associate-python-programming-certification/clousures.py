def greeter(prefix):
  other_name = prefix + "lala"
  def greet(name):
      print(f"{prefix} {name} {other_name}")
  return greet

hello = greeter("Hello,")
goodbye = greeter("Goodbye,")

hello("Kevin")
goodbye("Kyle")
