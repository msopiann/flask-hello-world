from flask import Flask, Response
from flask_cors import CORS

app = Flask(__name__)

CORS(app)


@app.route("/")
def home():
    return "Hello, World!"


@app.route("/about")
def about():
    return "About"


@app.route("/description", methods=["GET"])
def get_description():
    html_content = """
    <p><strong>Shiba Inu</strong> adalah ras anjing kecil yang berasal dari <i>Jepang</i>, terkenal dengan penampilan yang mirip dengan serigala dan sifat yang ceria. Shiba Inu sepia adalah variasi warna yang menonjol dengan nuansa coklat kekuningan yang lembut.</p>
    <h2>Ciri-ciri Khusus Shiba Inu Sepia:</h2>
    <ul>
        <li><strong>Warna Bulu:</strong> Warna sepia yang khas, yaitu coklat kekuningan dengan nuansa hangat yang merata di seluruh tubuh.</li>
        <li><strong>Bentuk Tubuh:</strong> Postur tubuh yang tegap dan kompak dengan ekor yang melengkung ke atas.</li>
        <li><strong>Ekspresi Wajah:</strong> Mata kecil dan berbentuk segitiga, memberikan ekspresi yang tajam dan penuh perhatian.</li>
        <li><strong>Kepribadian:</strong> Cerdas, mandiri, dan penuh energi. Shiba Inu sepia juga dikenal dengan sifatnya yang setia dan perhatian terhadap pemiliknya.</li>
    </ul>
    """
    return Response(html_content, content_type="text/html")
