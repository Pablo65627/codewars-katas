
def multiTable(n: Int): String = {
	var i = 1
	var tabla = ""

	while i <= 10 do
	 tabla += s"$n = ${i * n}"
	 if i < 10 then
	   tabla += "\n"
	i += 1

tabla
}
