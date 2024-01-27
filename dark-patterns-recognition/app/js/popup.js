window.onload = function () {
  chrome.tabs.query({ currentWindow: true, active: true }, function (tabs) {
    chrome.tabs.sendMessage(tabs[0].id, { message: "popup_open" });
  });

  // Attach event handler to the first element with class "analyze-button"
  document.getElementsByClassName("analyze-button")[0].onclick = function () {
    chrome.tabs.query({ currentWindow: true, active: true }, function (tabs) {
      chrome.tabs.sendMessage(tabs[0].id, { message: "analyze_site" });
    });
  };

  // Attach event handlers to the first two elements with class "link"
  var linkElements = document.getElementsByClassName("link");
  for (var i = 0; i < Math.min(2, linkElements.length); i++) {
    linkElements[i].onclick = function () {
      chrome.tabs.create({
        url: this.getAttribute("href"),
      });
    };
  }
};

// Message listener
chrome.runtime.onMessage.addListener(function (request, sender, sendResponse) {
  if (request.message === "update_current_count") {
    document.getElementsByClassName("number")[0].textContent = request.count;
  }
});