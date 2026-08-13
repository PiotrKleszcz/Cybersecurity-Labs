// Fifth Ace Security Shield - popup.js
// Phishing detection and HTTPS security checker

const PHISHING_KEYWORDS = [
  'login', 'signin', 'account', 'verify', 'secure', 'update',
  'confirm', 'banking', 'paypal', 'amazon', 'microsoft', 'apple',
  'google', 'netflix', 'password', 'credential', 'wallet', 'crypto'
];

const SUSPICIOUS_TLDS = [
  '.tk', '.ml', '.ga', '.cf', '.gq', '.xyz', '.top', '.click',
  '.download', '.stream', '.bid', '.win', '.loan'
];

const TRUSTED_DOMAINS = [
  'google.com', 'microsoft.com', 'apple.com', 'amazon.com',
  'paypal.com', 'netflix.com', 'github.com', 'linkedin.com',
  'fifthace.net', 'gov.uk', 'bbc.co.uk'
];

function checkHttps(url) {
  return url.startsWith('https://');
}

function checkPhishingKeywords(url, hostname) {
  const urlLower = url.toLowerCase();
  const matches = PHISHING_KEYWORDS.filter(kw => urlLower.includes(kw));
  return matches;
}

function checkSuspiciousTLD(hostname) {
  return SUSPICIOUS_TLDS.some(tld => hostname.endsWith(tld));
}

function checkTrustedDomain(hostname) {
  return TRUSTED_DOMAINS.some(domain =>
    hostname === domain || hostname.endsWith('.' + domain)
  );
}

function checkUrlLength(url) {
  return url.length > 100;
}

function analyzeUrl(url) {
  let riskScore = 0;
  const results = {};

  try {
    const urlObj = new URL(url);
    const hostname = urlObj.hostname;

    // HTTPS check
    results.https = checkHttps(url);
    if (!results.https) riskScore += 30;

    // Phishing keywords
    results.phishingKeywords = checkPhishingKeywords(url, hostname);
    if (results.phishingKeywords.length > 0 && !checkTrustedDomain(hostname)) {
      riskScore += results.phishingKeywords.length * 10;
    }

    // Suspicious TLD
    results.suspiciousTLD = checkSuspiciousTLD(hostname);
    if (results.suspiciousTLD) riskScore += 40;

    // Trusted domain
    results.trustedDomain = checkTrustedDomain(hostname);
    if (results.trustedDomain) riskScore = Math.max(0, riskScore - 30);

    // URL length
    results.longUrl = checkUrlLength(url);
    if (results.longUrl) riskScore += 10;

    results.riskScore = Math.min(riskScore, 100);
    results.hostname = hostname;

  } catch (e) {
    results.error = true;
    results.riskScore = 50;
  }

  return results;
}

function updateUI(url, analysis) {
  document.getElementById('currentUrl').textContent = url;

  // HTTPS Check
  const httpsResult = document.getElementById('httpsResult');
  const httpsCheck = document.getElementById('httpsCheck');
  if (analysis.https) {
    httpsResult.textContent = 'SECURE';
    httpsResult.className = 'check-result pass';
    httpsCheck.querySelector('.check-icon').textContent = '✅';
  } else {
    httpsResult.textContent = 'INSECURE';
    httpsResult.className = 'check-result fail';
    httpsCheck.querySelector('.check-icon').textContent = '❌';
  }

  // Phishing Check
  const phishingResult = document.getElementById('phishingResult');
  const phishingCheck = document.getElementById('phishingCheck');
  if (analysis.phishingKeywords && analysis.phishingKeywords.length > 0 && !analysis.trustedDomain) {
    phishingResult.textContent = 'SUSPICIOUS';
    phishingResult.className = 'check-result fail';
    phishingCheck.querySelector('.check-icon').textContent = '⚠️';
  } else {
    phishingResult.textContent = 'CLEAN';
    phishingResult.className = 'check-result pass';
    phishingCheck.querySelector('.check-icon').textContent = '✅';
  }

  // Domain Check
  const domainResult = document.getElementById('domainResult');
  const domainCheck = document.getElementById('domainCheck');
  if (analysis.trustedDomain) {
    domainResult.textContent = 'TRUSTED';
    domainResult.className = 'check-result pass';
    domainCheck.querySelector('.check-icon').textContent = '✅';
  } else if (analysis.suspiciousTLD) {
    domainResult.textContent = 'SUSPICIOUS TLD';
    domainResult.className = 'check-result fail';
    domainCheck.querySelector('.check-icon').textContent = '❌';
  } else {
    domainResult.textContent = 'UNKNOWN';
    domainResult.className = 'check-result warn';
    domainCheck.querySelector('.check-icon').textContent = '⚠️';
  }

  // URL Safety Check
  const urlResult = document.getElementById('urlResult');
  const urlCheck = document.getElementById('urlCheck');
  if (analysis.longUrl) {
    urlResult.textContent = 'LONG URL';
    urlResult.className = 'check-result warn';
    urlCheck.querySelector('.check-icon').textContent = '⚠️';
  } else {
    urlResult.textContent = 'NORMAL';
    urlResult.className = 'check-result pass';
    urlCheck.querySelector('.check-icon').textContent = '✅';
  }

  // Overall Status
  const statusCard = document.getElementById('statusCard');
  const statusIcon = document.getElementById('statusIcon');
  const statusText = document.getElementById('statusText');

  if (analysis.riskScore >= 50) {
    statusCard.className = 'status-card danger';
    statusIcon.textContent = '🚨';
    statusText.textContent = `HIGH RISK (${analysis.riskScore}/100)`;
  } else if (analysis.riskScore >= 20) {
    statusCard.className = 'status-card warning';
    statusIcon.textContent = '⚠️';
    statusText.textContent = `MEDIUM RISK (${analysis.riskScore}/100)`;
  } else {
    statusCard.className = 'status-card safe';
    statusIcon.textContent = '✅';
    statusText.textContent = `SAFE (${analysis.riskScore}/100)`;
  }
}

// Main
document.addEventListener('DOMContentLoaded', () => {
  chrome.tabs.query({ active: true, currentWindow: true }, (tabs) => {
    if (tabs[0]) {
      const url = tabs[0].url;
      const analysis = analyzeUrl(url);
      updateUI(url, analysis);
    }
  });
});
