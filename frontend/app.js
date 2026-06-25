const API_ENDPOINT = "REPLACE_WITH_API_GATEWAY_URL";

const form = document.getElementById("feedbackForm");
const result = document.getElementById("result");

form.addEventListener("submit", async (event) => {
  event.preventDefault();

  const formData = new FormData(form);
  const payload = {
    name: formData.get("name"),
    email: formData.get("email"),
    rating: Number(formData.get("rating")),
    message: formData.get("message"),
    source: "s3-static-website"
  };

  if (API_ENDPOINT === "REPLACE_WITH_API_GATEWAY_URL") {
    result.textContent = "Update API_ENDPOINT in frontend/app.js with your API Gateway invoke URL.";
    return;
  }

  result.textContent = "Submitting feedback...";

  try {
    const response = await fetch(API_ENDPOINT, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(payload)
    });

    const data = await response.json();
    result.textContent = JSON.stringify(data, null, 2);

    if (response.ok) {
      form.reset();
    }
  } catch (error) {
    result.textContent = `Submission failed: ${error.message}`;
  }
});
