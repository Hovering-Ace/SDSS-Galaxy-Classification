document.getElementById("predictionForm").addEventListener("submit", async function(event) {
    event.preventDefault(); // Prevent default form submission

    // Collect form data
    const formData = new FormData(this);
    const data = Object.fromEntries(formData.entries());

    // Convert values to an array
    const inputData = Object.values(data).map(value => parseFloat(value));

    try {
        // Send data to backend
        const response = await fetch("/predict", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ features: inputData })
        });

        // Parse the JSON response
        const result = await response.json();

        // Show the result with an image
        let outputHTML = `<h3>Predicted Galaxy Type: ${result.prediction === 1 ? "Starburst Galaxy" : "Star-forming Galaxy"}</h3>`;
        outputHTML += `<img src="${result.image}" alt="Galaxy Image" width="300">`;

        document.getElementById("result").innerHTML = outputHTML;

    } catch (error) {
        console.error("Error:", error);
        document.getElementById("result").innerHTML = "<p style='color:red;'>Prediction failed. Try again.</p>";
    }
});
