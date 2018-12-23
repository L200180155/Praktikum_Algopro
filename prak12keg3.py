def volume(sisialas,tinggi) :
    sa = sisialas
    t = tinggi
    H =(sa ** 2 * t) / 3
    return V
sisialas = 5
tinggi = 8

print "<!DOCTYPE html>"
print
print """<html>
<head><title>WELCOME</title></head>
<body>"""
print """<table>
<tr>
    <th rowspan='8' width='100'> picture </th>
    <td><h3> Bangun Geometri <h3></td>
</tr>
<tr>
    <td>Nama Bangun</td>
    <td>:</td>
    <td>Piramid</td>
</tr>
<tr>
    <td>Dimensi (2D/3D)</td>
    <td>:</td>
    <td>3D</td>
</tr>
<tr>
    <td>Rumus Luas</td>
    <td>:</td>
    <td>(sa ** 2 * t) / 3</td>
</tr>
<tr>
    <td>Sisi Alas</td>
    <td>:</td>
    <td>{}</td>
</tr>
""".format(sisialas)
print """<tr>
    <td>Tinggi</td>
    <td>:</td>
    <td>{}</td>
</tr>
""".format(tinggi)
print """<tr>
    <td>Luas</td>
    <td>:</td>
    <td>{}</td>
</tr>
""".format(volume(sisialas,tinggi))
print"""
</table>"""

print"</body></html>"
