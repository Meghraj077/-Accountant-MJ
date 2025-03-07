from flask import Flask, request, jsonify

app = Flask(__name__)

# Sample Tax Data
tax_rates = {
    "GST": 18,
    "Income Tax Slabs": {
        "0-250000": 0,
        "250001-500000": 5,
        "500001-1000000": 20,
        "1000001-above": 30
    }
}

@app.route('/')
def home():
    return "✅ Tax API Running..."

@app.route('/gst', methods=['GET'])
def calculate_gst():
    try:
        amount = float(request.args.get('amount', 0))
        gst = (amount * tax_rates["GST"]) / 100
        return jsonify({"GST": gst, "Total": amount + gst})
    except:
        return jsonify({"error": "Invalid Amount"}), 400

@app.route('/income_tax', methods=['GET'])
def calculate_income_tax():
    try:
        income = float(request.args.get('income', 0))
        tax = 0
        for bracket, rate in tax_rates["Income Tax Slabs"].items():
            low, high = bracket.split("-")
            low, high = int(low), int(high) if high != "above" else float("inf")
            if income > low:
                taxable = min(income, high) - low
                tax += (taxable * rate) / 100
        return jsonify({"Income Tax": tax, "Net Income": income - tax})
    except:
        return jsonify({"error": "Invalid Income"}), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
