from flask import Flask, request, render_template_string

app = Flask(__name__)

# Single-file HTML template with embedded styling
HTML_TEMPLATE = ""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Text Utility App</title>
    <style>
        body { font-family: 'Segoe UI', Arial, sans-serif; background: #f4f6f9; color: #333; margin: 0; padding: 40px; }
        .container { max-width: 600px; background: white; margin: 0 auto; padding: 30px; border-radius: 8px; box-shadow: 0 4px 15px rgba(0,0,0,0.05); }
        h2 { color: #2c3e50; margin-top: 0; }
        textarea { width: 100%; height: 120px; padding: 10px; border: 1px solid #ddd; border-radius: 4px; box-sizing: border-box; resize: vertical; font-size: 15px; }
        .radio-group { margin: 15px 0; display: flex; gap: 15px; }
        .btn { background: #3498db; color: white; border: none; padding: 10px 20px; font-size: 16px; border-radius: 4px; cursor: pointer; transition: background 0.2s; }
        .btn:hover { background: #2980b9; }
        .result-box { margin-top: 25px; padding: 15px; background: #eef2f7; border-left: 5px solid #3498db; border-radius: 4px; }
        .meta { font-size: 13px; color: #7f8c8d; margin-top: 10px; }
    </style>
</head>
<body>

<div class="container">
    <h2>Text Analyzer Utility</h2>
    <form method="POST">
        <textarea name="text_input" placeholder="Type or paste your text here: " required>{{ original_text }}</textarea>
        
        <div class="radio-group">
            <label><input type="radio" name="operation" value="upper" {% if op == 'upper' or not op %}checked{% endif %}> UPPERCASE</label>
            <label><input type="radio" name="operation" value="lower" {% if op == 'lower' %}checked{% endif %}> lowercase</label>
            <label><input type="radio" name="operation" value="reverse" {% if op == 'reverse' %}checked{% endif %}> Reverse</label>
        </div>
        
        <button type="submit" class="btn">Process Text</button>
    </form>

    {% if result is not none %}
    <div class="result-box">
        <strong>Result:</strong>
        <p style="white-space: pre-wrap; margin: 5px 0 0 0;">{{ result }}</p>
        <div class="meta">
            <strong>Stats:</strong> {{ word_count }} words | {{ char_count }} characters
        </div>
    </div>
    {% endif %}
</div>

</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def home():
    result = None
    word_count = 0
    char_count = 0
    operation = "upper"
    text_input = ""

    if request.method == "POST":
        text_input = request.form.get("text_input", "")
        operation = request.form.get("operation", "upper")
        
        # Calculate text metrics
        word_count = len(text_input.split())
        char_count = len(text_input)

        # Process chosen action
        if operation == "upper":
            result = text_input.upper()
        elif operation == "lower":
            result = text_input.lower()
        elif operation == "reverse":
            result = text_input[::-1]

    return render_template_string(
        HTML_TEMPLATE, 
        result=result, 
        word_count=word_count, 
        char_count=char_count, 
        op=operation,
        original_text=text_input
    )

if __name__ == "__main__":
    app.run(debug=True)
