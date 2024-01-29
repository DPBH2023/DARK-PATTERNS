const endpoint = "http://127.0.0.1:5000/";
const descriptions = {
  "Sneaking": "Coerces users to act in ways that they would not normally act by obscuring information.",
  "Urgency": "Places deadlines on things to make them appear more desirable",
  "Misdirection": "Aims to deceptively incline a user towards one choice over the other.",
  "Social Proof": "Gives the perception that a given action or product has been approved by other people.",
  "Scarcity": "Tries to increase the value of something by making it appear to be limited in availability.",
  "Obstruction": "Tries to make an action more difficult so that a user is less likely to do that action.",
  "Forced Action": "Forces a user to complete extra, unrelated tasks to do something that should be simple.",
};

function scrape() {
  if (document.getElementById("darkdetect_count")) return;

  const elements = Array.from(document.querySelectorAll("body *"))
    .map(el => el.innerText.trim().replace(/\t/g, " "))
    .filter(text => text.length > 0);

  fetch(endpoint, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ tokens: elements }),
  })
  .then(resp => resp.json())
  .then(data => {
    data = JSON.parse(data.replace(/'/g, '"'));
    let dpCount = 0;

    elements.forEach((text, index) => {
      if (data.result[index] !== "Not Dark") {
        highlight(elements[index], data.result[index]);
        dpCount++;
      }
    });

    const darkDetectCount = document.createElement("div");
    darkDetectCount.id = "darkdetect_count";
    darkDetectCount.value = dpCount;
    darkDetectCount.style.opacity = 0;
    darkDetectCount.style.position = "fixed";
    document.body.appendChild(darkDetectCount);
    sendDarkPatterns(dpCount);
  })
  .catch(error => {
    console.error(error);
    alert("An error occurred while processing.");
  });
}

function highlight(element, type) {
  element.classList.add("darkdetect-highlight");
  
  const modalContent = document.createElement("div");
  modalContent.innerHTML = `<div class="modal-header"><h1>${type} Pattern</h1></div>
                            <div class="modal-content">${descriptions[type]}</div>`;
  element.appendChild(modalContent);
}

function sendDarkPatterns(number) {
  chrome.runtime.sendMessage({
    message: "update_current_count",
    count: number,
  });
}

chrome.runtime.onMessage.addListener(function (request, sender, sendResponse) {
  if (request.message === "analyze_site") {
    scrape();
  } else if (request.message === "popup_open") {
    const element = document.getElementById("darkdetect_count");
    if (element) sendDarkPatterns(element.value);
  }
});
