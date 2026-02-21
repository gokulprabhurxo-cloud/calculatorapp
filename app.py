from flask import Flask, request, render_template_string

app = Flask(__name__)

HTML = """
<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <title>Calculator</title>

    <!-- Bootstrap 5 -->
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet">

    <style>
      body { background: #0b1220; }
      .card {
        border: 0;
        background: rgba(255,255,255,0.06);
        backdrop-filter: blur(10px);
        box-shadow: 0 20px 60px rgba(0,0,0,0.35);
      }
      .text-muted-2 { color: rgba(255,255,255,0.65) !important; }
      .form-control, .form-select {
        background: rgba(255,255,255,0.08);
        border: 1px solid rgba(255,255,255,0.12);
        color: #000;
      }
      .form-control::placeholder { color: rgba(255,255,255,0.55); }
      .form-control:focus, .form-select:focus {
        box-shadow: 0 0 0 .25rem rgba(13,110,253,.25);
        border-color: rgba(13,110,253,.55);
      }
      .result-pill {
        background: rgba(13,110,253,0.18);
        border: 1px solid rgba(13,110,253,0.35);
        color: #eaf2ff;
      }
      .btn-primary { box-shadow: 0 12px 24px rgba(13,110,253,0.25); }
      .brand-dot { width: 10px; height: 10px; border-radius: 999px; background: #0d6efd; display:inline-block; }
    </style>
  </head>

  <body class="text-white">
    <div class="container py-5">
      <div class="row justify-content-center">
        <div class="col-12 col-md-8 col-lg-6">
          <div class="mb-4 text-center">
            <div class="mb-2">
              <span class="brand-dot me-2"></span>
              <span class="fw-semibold">Modern Calculator</span>
            </div>
            <div class="text-muted-2">Enter numbers, pick an operation, and hit calculate.</div>
          </div>

          <div class="card rounded-4 p-4">
            <form method="POST" class="row g-3">
              <div class="col-12 col-md-6">
                <label class="form-label text-muted-2">Number 1</label>
                <input class="form-control form-control-lg" name="num1" inputmode="decimal"
                       placeholder="e.g., 12.5" value="{{ num1 or '' }}" required>
              </div>

              <div class="col-12 col-md-6">
                <label class="form-label text-muted-2">Number 2</label>
                <input class="form-control form-control-lg" name="num2" inputmode="decimal"
                       placeholder="e.g., 3" value="{{ num2 or '' }}" required>
              </div>

              <div class="col-12">
                <label class="form-label text-muted-2">Operation</label>
                <select class="form-select form-select-lg" name="operation" required>
                  <option value="add" {{ 'selected' if operation=='add' else '' }}>Add (+)</option>
                  <option value="sub" {{ 'selected' if operation=='sub' else '' }}>Subtract (−)</option>
                  <option value="mul" {{ 'selected' if operation=='mul' else '' }}>Multiply (×)</option>
                  <option value="div" {{ 'selected' if operation=='div' else '' }}>Divide (÷)</option>
                </select>
              </div>

              <div class="col-12 d-grid">
                <button class="btn btn-primary btn-lg" type="submit">Calculate</button>
              </div>
            </form>

            {% if result is not none %}
              <div class="mt-4 p-3 rounded-4 result-pill">
                <div class="d-flex justify-content-between align-items-center">
                  <div class="fw-semibold">Result</div>
                  <div class="fs-4 fw-bold">{{ result }}</div>
                </div>
                {% if note %}
                  <div class="mt-2 text-muted-2">{{ note }}</div>
                {% endif %}
              </div>
            {% endif %}

            {% if error %}
              <div class="mt-4 alert alert-danger rounded-4 mb-0" role="alert">
                {{ error }}
              </div>
            {% endif %}
          </div>

          <div class="mt-3 text-center text-muted-2 small">
            Tip: press <span class="badge text-bg-light">Ctrl + C</span> in the terminal to stop the app.
          </div>
        </div>
      </div>
    </div>

    <!-- Bootstrap JS (optional) -->
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js"></script>
  </body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def home():
    result = None
    error = None
    note = None

    num1 = None
    num2 = None
    operation = "add"

    if request.method == "POST":
        try:
            num1 = request.form.get("num1", "").strip()
            num2 = request.form.get("num2", "").strip()
            operation = request.form.get("operation", "add")

            a = float(num1)
            b = float(num2)

            if operation == "add":
                result = a + b
            elif operation == "sub":
                result = a - b
            elif operation == "mul":
                result = a * b
            elif operation == "div":
                if b == 0:
                    result = "—"
                    note = "Cannot divide by zero."
                else:
                    result = a / b
            else:
                error = "Unknown operation selected."

            # Optional: pretty formatting for whole numbers
            if isinstance(result, (int, float)):
                if abs(result - round(result)) < 1e-12:
                    result = str(int(round(result)))
                else:
                    result = f"{result:.6g}"

        except ValueError:
            error = "Please enter valid numbers (example: 12, 3.5)."
        except Exception as e:
            error = f"Something went wrong: {e}"

    return render_template_string(
        HTML,
        result=result,
        error=error,
        note=note,
        num1=num1,
        num2=num2,
        operation=operation,
    )

if __name__ == "__main__":
        app.run(debug=True)

