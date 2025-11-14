const POLL_INTERVAL = 5000;

// Check subdomain matches
const subdomain = window.location.host.split(".")[0];
const re = new RegExp("^[a-z0-9-]+-[a-f0-9]{16}$");
const parser = new DOMParser();

function errorHandler(e) {
  console.error("Error during challenge readiness check:", e);
  location.reload();
}

function checkChallengeReady() {
  const host = window.location.origin;
  fetch(host)
    .then(res => {
      if (res.status === 200) {
        // Parse response text
        res.text()
          .then(text => {
            // Check if 200 res has same title as this loading page
            try {
              const doc = parser.parseFromString(text, "text/html")
              if (doc.title !== document.title) {
                location.reload()
              }
            } catch (e) {
              errorHandler(e);
            }
          }).catch(e => errorHandler(e));
      } else { console.info("instance not ready"); }
    })
    .catch(e => errorHandler(e));
}

if (re.test(subdomain)) {
  document.getElementsByClassName("challenge-loading")[0].style.display =
    "block";
  setInterval(() => checkChallengeReady(), POLL_INTERVAL);
} else {
  document.getElementsByClassName("wrong-domain")[0].style.display =
    "block";
}

