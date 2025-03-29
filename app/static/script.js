document.addEventListener("DOMContentLoaded", function () {
    const textarea = document.querySelector("textarea");
    const warning = document.getElementById("warning");
    const resultField = document.getElementById("result");
    const form = document.getElementById("sumForm");

    textarea.addEventListener("input", function () {
        const validInput = textarea.value.replace(/[^0-9,\n]/g, ''); // Remove invalid characters
        if (textarea.value !== validInput) {
            warning.textContent = "Only numbers, commas, and new lines are allowed.";
        } else {
            warning.textContent = "";
        }
        textarea.value = validInput; // Update the value with only allowed characters
    });

    form.addEventListener("submit", async function (event) {
        event.preventDefault();
        const formData = new FormData(form);
        const response = await fetch("/add", {
            method: "POST",
            body: formData,
        });
        const data = await response.json();
        resultField.textContent = `Sum: ${data.result}`;
    });
});
