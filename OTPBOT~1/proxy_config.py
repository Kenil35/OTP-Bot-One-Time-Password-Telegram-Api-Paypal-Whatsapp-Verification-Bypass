<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Dynamic Page Generator</title>
    <style>
        body {
            font-family: 'Arial', sans-serif;
            background-color: #f5f5f5;
            color: #333;
            margin: 0;
            padding: 0;
        }
        .container {
            max-width: 600px;
            margin: 20px auto;
            padding: 20px;
            background-color: #fff;
            border-radius: 8px;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
        }
    </style>
</head>
<body>

<div class="container">
    <h1 style="text-align: center;">Dynamic Page Generator</h1>
    
    <label for="pageContent">Enter your text:</label>
    <textarea id="pageContent" style="width: 100%; height: 100px;"></textarea>
    
    <button onclick="generatePage()">Generate Page</button>
</div>

<script>
    function generatePage() {
        var pageContent = document.getElementById('pageContent').value;
        
        // Open a new window with the generated content
        var newWindow = window.open();
        newWindow.document.write('<html><head><title>Generated Page</title></head><body>');
        newWindow.document.write('<div style="max-width: 600px; margin: 20px auto; padding: 20px; background-color: #fff; border-radius: 8px; box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);">');
        newWindow.document.write('<p>' + pageContent + '</p>');
        newWindow.document.write('</div></body></html>');
        newWindow.document.close();
    }
</script>

</body>
</html>
