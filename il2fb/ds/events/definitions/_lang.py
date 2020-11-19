class classproperty_readonly(property):
  def __get__(self, instance, owner=None):
    return super().__get__(owner)
