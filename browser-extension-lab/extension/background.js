// Fifth Ace Security Shield - background.js
// Service worker for Manifest V3

chrome.runtime.onInstalled.addListener(() => {
  console.log('Fifth Ace Security Shield installed');
  chrome.storage.local.set({
    totalScans: 0,
    threatsDetected: 0
  });
});

chrome.tabs.onUpdated.addListener((tabId, changeInfo, tab) => {
  if (changeInfo.status === 'complete' && tab.url) {
    chrome.storage.local.get(['totalScans', 'threatsDetected'], (data) => {
      chrome.storage.local.set({
        totalScans: (data.totalScans || 0) + 1
      });
    });
  }
});
