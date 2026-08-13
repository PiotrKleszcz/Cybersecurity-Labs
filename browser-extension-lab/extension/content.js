// Fifth Ace Security Shield - content.js
// Content script running on every page

const PHISHING_KEYWORDS = [
  'verify your account', 'confirm your identity', 'update your payment',
  'your account has been suspended', 'click here to restore',
  'enter your password', 'unusual activity detected'
];

function checkPageContent() {
  const bodyText = document.body.innerText.toLowerCase();
  const suspicious = PHISHING_KEYWORDS.filter(kw => bodyText.includes(kw.toLowerCase()));

  if (suspicious.length >= 2) {
    const banner = document.createElement('div');
    banner.style.cssText = `
      position: fixed;
      top: 0;
      left: 0;
      right: 0;
      background: #da3633;
      color: white;
      padding: 10px 16px;
      font-family: Arial, sans-serif;
      font-size: 14px;
      font-weight: bold;
      z-index: 999999;
      text-align: center;
    `;
    banner.textContent = '⚠️ Fifth Ace Security Shield: This page may be a phishing attempt. Proceed with caution!';
    document.body.prepend(banner);
  }
}

if (document.readyState === 'loading') {
  document.addEventListener('DOMContentLoaded', checkPageContent);
} else {
  checkPageContent();
}
