//class Pizza {
//
//}
class Foo{
  private val secret = 2
}
object Foo{
  //access the private class field 'secret'
  def double(foo: Foo) = foo.secret*2
}
