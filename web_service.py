from flask import Flask, render_template, request, redirect

app = Flask(__name__)

# Mesajları geçici bir listede tutuyoruz (veritabanı yerine)
mesajlar = []

@app.route(&quot;/&quot;, methods=[&quot;GET&quot;, &quot;POST&quot;])
def index():
if request.method == &quot;POST&quot;:
isim = request.form.get(&quot;isim&quot;)
mesaj = request.form.get(&quot;mesaj&quot;)
if isim and mesaj:
mesajlar.append({&quot;isim&quot;: isim, &quot;mesaj&quot;: mesaj})
return redirect(&quot;/&quot;)

return render_template(&quot;index.html&quot;, mesajlar=mesajlar)

if __name__ == &quot;__main__&quot;:
app.run(host=&quot;0.0.0.0&quot;, port=5000)
