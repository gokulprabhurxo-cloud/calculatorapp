from flask import Flask, render_template_string

app = Flask(__name__)

HTML = """
<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Modern Calculator</title>

<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet">

<style>
body {
    background: #0b1220;
}

.card {
    border: 0;
    background: rgba(255,255,255,0.06);
    backdrop-filter: blur(10px);
    box-shadow: 0 20px 60px rgba(0,0,0,0.35);
}

.display {
    height: 80px;
    font-size: 2rem;
    text-align: right;
    background: rgba(255,255,255,0.08);
    border: none;
    color: #fff;
    padding: 1rem;
    border-radius: 1rem;
}

.keypad {
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    gap: .8rem;
}

.btn-key {
    padding: 1rem;
    font-size: 1.2rem;
    font-weight: 600;
    border-radius: 1rem;
    border: none;
    background: rgba(255,255,255,0.08);
    color: #fff;
}

.btn-key:hover {
    background: rgba(255,255,255,0.15);
}

.btn-operator {
    background: rgba(13,110,253,0.25);
}

.btn-equal {
    background: rgba(40,167,69,0.35);
}

.btn-clear {
    background: rgba(220,53,69,0.35);
}
</style>
</head>

<body class="text-white">
<div class="container py-5">
<div class="row justify-content-center">
<div class="col-12 col-md-6">

<div class="text-center mb-4">
<h3>Modern Calculator</h3>
</div>

<div class="card p-4 rounded-4">

<input type="text" id="display" class="display mb-4" disabled>

<div class="keypad">

<button class="btn-key btn-clear" onclick="clearDisplay()">C</button>
<button class="btn-key" onclick="appendValue('(')">(</button>
<button class="btn-key" onclick="appendValue(')')">)</button>
<button class="btn-key btn-operator" onclick="appendValue('/')">÷</button>

<button class="btn-key" onclick="appendValue('7')">7</button>
<button class="btn-key" onclick="appendValue('8')">8</button>
<button class="btn-key" onclick="appendValue('9')">9</button>
<button class="btn-key btn-operator" onclick="appendValue('*')">×</button>

<button class="btn-key" onclick="appendValue('4')">4</button>
<button class="btn-key" onclick="appendValue('5')">5</button>
<button class="btn-key" onclick="appendValue('6')">6</button>
<button class="btn-key btn-operator" onclick="appendValue('-')">−</button>

<button class="btn-key" onclick="appendValue('1')">1</button>
<button class="btn-key" onclick="appendValue('2')">2</button>
<button class="btn-key" onclick="appendValue('3')">3</button>
<button class="btn-key btn-operator" onclick="appendValue('+')">+</button>

<button class="btn-key" style="grid-column: span 2;" onclick="appendValue('0')">0</button>
<button class="btn-key" onclick="appendValue('.')">.</button>
<button class="btn-key btn-equal" onclick="calculate()">=</button>

</div>
</div>
</div>
</div>
</div>

<script>
function appendValue(value) {
    document.getElementById("display").value += value;
}

function clearDisplay() {
    document.getElementById("display").value = "";
}

function calculate() {
    try {
        const result = eval(document.getElementById("display").value);
        document.getElementById("display").value = result;
    } catch {
        document.getElementById("display").value = "Error";
    }
}
</script>

</body>
</html>
"""

@app.route("/")
def home():
    return render_template_string(HTML)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
